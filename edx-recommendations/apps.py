"""
edx-recommendations Django application initialization.
"""

from django.apps import AppConfig


class RecommendationsConfig(AppConfig):
    """
    Configuration for the edx-recommendations Django application.
    """

    name = 'edx-recommendations'
    verbose_name = "Learner Recommendations"

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'edx-recommendations',
                'relative_path': 'urls',
            },
        },
    }
