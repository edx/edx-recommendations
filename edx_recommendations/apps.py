"""
edx_recommendations Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginURLs, PluginSettings


class EdxRecommendationsConfig(AppConfig):
    """
    Configuration for the edx_recommendations Django application.
    """

    name = "edx_recommendations"

    plugin_app = {
        PluginURLs.CONFIG: {
            "lms.djangoapp": {
                PluginURLs.NAMESPACE: "edx_recommendations",
                PluginURLs.APP_NAME: "edx_recommendations",
                PluginURLs.REGEX: "api/edx_recommendations/",
                PluginURLs.RELATIVE_PATH: "api.urls",
            }
        },
        PluginSettings.CONFIG: {
            "lms.djangoapp": {
                "common": {
                    PluginSettings.RELATIVE_PATH: "settings.common",
                },
                "production": {
                    PluginSettings.RELATIVE_PATH: "settings.production",
                },
            }
        },
    }
