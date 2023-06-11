"""
URL configuration
"""

from django.conf import settings
from django.urls import re_path

from edx_recommendations.api.course_recommendations import (
    CourseAboutPageRecommendationsView,
    LearnerDashboardRecommendationsView,
)
from edx_recommendations.api.cross_product_recommendations import (
    CrossProductRecommendationsView,
    ProductRecommendationsView,
)

app_name = "edx_recommendations"

urlpatterns = [
    re_path(
        rf"^course_about_page/amplitude/{settings.COURSE_ID_PATTERN}/$",
        CourseAboutPageRecommendationsView.as_view(),
        name="course_about_page_amplitude",
    ),
    re_path(
        rf"^course_about_page/cross_product/{settings.COURSE_ID_PATTERN}/$",
        CrossProductRecommendationsView.as_view(),
        name="course_about_page_cross_product",
    ),
    re_path(
        r"^learner_dashboard/amplitude/$",
        LearnerDashboardRecommendationsView.as_view(),
        name="learner_dashboard_amplitude",
    ),
    re_path(
        r"^learner_dashboard/amplitude/v2/$",
        ProductRecommendationsView.as_view(),
        name="learner_dashboard_amplitude_v2",
    ),
    re_path(
        rf"^learner_dashboard/cross_product/{settings.COURSE_ID_PATTERN}/$",
        ProductRecommendationsView.as_view(),
        name="learner_dashboard_cross_product",
    ),
]
