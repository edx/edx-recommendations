"""
APIs to get cross product recommendations.
"""

import logging
from django.conf import settings
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.auth.session.authentication import (
    SessionAuthenticationAllowInactiveUser,
)
from edx_rest_framework_extensions.permissions import NotJwtRestrictedApplication
from ipware.ip import get_client_ip
from opaque_keys.edx.keys import CourseKey
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from openedx.core.djangoapps.catalog.utils import get_course_data
from openedx.core.djangoapps.geoinfo.api import country_code_from_ip

from edx_recommendations.api.serializers import (
    CrossProductAndAmplitudeRecommendationsSerializer,
    CrossProductRecommendationsSerializer,
    AmplitudeRecommendationsSerializer,
)
from edx_recommendations.api.utils import (
    _has_country_restrictions,
    get_amplitude_course_recommendations,
    filter_recommended_courses,
    get_cross_product_recommendations,
    get_active_course_run,
)

log = logging.getLogger(__name__)


class CrossProductRecommendationsView(APIView):
    """
    **Example Request**

    GET api/edx_recommendations//cross_product/{course_id}/
    """

    def _empty_response(self):
        return Response({"courses": []}, status=200)

    def get(self, request, course_id):
        """
        Returns cross product recommendation courses
        """
        course_locator = CourseKey.from_string(course_id)
        course_key = f"{course_locator.org}+{course_locator.course}"

        associated_course_keys = get_cross_product_recommendations(course_key)

        if not associated_course_keys:
            return self._empty_response()

        fields = [
            "key",
            "uuid",
            "title",
            "owners",
            "image",
            "url_slug",
            "course_type",
            "course_runs",
            "location_restriction",
            "advertised_course_run_uuid",
        ]
        course_data = [get_course_data(key, fields) for key in associated_course_keys]
        filtered_courses = [course for course in course_data if course and course.get("course_runs")]

        ip_address = get_client_ip(request)[0]
        user_country_code = country_code_from_ip(ip_address).upper()

        unrestricted_courses = []

        for course in filtered_courses:
            if _has_country_restrictions(course, user_country_code):
                continue

            active_course_run = get_active_course_run(course)
            if active_course_run:
                course.update({"active_course_run": active_course_run})
                unrestricted_courses.append(course)

        if not unrestricted_courses:
            return self._empty_response()

        return Response(
            CrossProductRecommendationsSerializer(
                {"courses": unrestricted_courses}
            ).data,
            status=200,
        )


class ProductRecommendationsView(APIView):
    """
    **Example Request**

    GET api/edx_recommendations/learner_dashboard/amplitude/v2/
    GET api/edx_recommendations/learner_dashboard/cross_product/{course_id}/
    """

    authentication_classes = (
        JwtAuthentication,
        SessionAuthenticationAllowInactiveUser,
    )
    permission_classes = (IsAuthenticated, NotJwtRestrictedApplication)

    fields = [
        "title",
        "owners",
        "image",
        "url_slug",
        "course_type",
        "course_runs",
        "location_restriction",
    ]

    def _get_amplitude_recommendations(self, user, user_country_code):
        """
        Helper for getting amplitude recommendations
        """

        fallback_recommendations = settings.GENERAL_RECOMMENDATIONS[0:4]

        try:
            _, _, course_keys = get_amplitude_course_recommendations(
                user.id, settings.LEARNER_DASHBOARD_AMPLITUDE_MODEL_ID
            )
        except Exception as ex:  # pylint: disable=broad-except
            log.warning(f"Cannot get recommendations from Amplitude: {ex}")
            return fallback_recommendations

        if not course_keys:
            return fallback_recommendations

        filtered_courses = filter_recommended_courses(
            user,
            course_keys,
            recommendation_count=4,
            user_country_code=user_country_code,
            course_fields=self.fields,
        )

        return filtered_courses if len(filtered_courses) > 0 else fallback_recommendations

    def _get_cross_product_recommendations(self, course_key, user_country_code):
        """
        Helper for getting cross product recommendations
        """

        associated_course_keys = get_cross_product_recommendations(course_key)

        if not associated_course_keys:
            return []

        course_data = [get_course_data(key, self.fields) for key in associated_course_keys]
        filtered_cross_product_courses = []

        for course in course_data:
            if (
                course
                and course.get("course_runs", [])
                and not _has_country_restrictions(course, user_country_code)
            ):
                filtered_cross_product_courses.append(course)

        return filtered_cross_product_courses

    def _cross_product_recommendations_response(self, course_key, user, user_country_code):
        """
        Helper for collecting and forming a response for
        cross product and Amplitude recommendations
        """
        amplitude_recommendations = self._get_amplitude_recommendations(user, user_country_code)
        cross_product_recommendations = self._get_cross_product_recommendations(course_key, user_country_code)

        return Response(
            CrossProductAndAmplitudeRecommendationsSerializer(
                {
                    "crossProductCourses": cross_product_recommendations,
                    "amplitudeCourses": amplitude_recommendations,
                }
            ).data,
            status=200,
        )

    def _amplitude_recommendations_response(self, user, user_country_code):
        """
        Helper for collecting and forming a response for Amplitude recommendations only
        """
        amplitude_recommendations = self._get_amplitude_recommendations(user, user_country_code)

        return Response(
            AmplitudeRecommendationsSerializer(
                {"amplitudeCourses": amplitude_recommendations}
            ).data,
            status=200,
        )

    def get(self, request, course_id=None):
        """
        Returns cross product and Amplitude recommendation courses if a course id is included,
        otherwise, returns only Amplitude recommendations
        """

        ip_address = get_client_ip(request)[0]
        user_country_code = country_code_from_ip(ip_address).upper()

        if course_id:
            course_locator = CourseKey.from_string(course_id)
            course_key = f'{course_locator.org}+{course_locator.course}'
            return self._cross_product_recommendations_response(course_key, request.user, user_country_code)

        return self._amplitude_recommendations_response(request.user, user_country_code)
