"""
recommendations Django application initialization.
"""

from django.apps import AppConfig


class RecommendationsConfig(AppConfig):
    """
    Configuration for the recommendations Django application.
    """

    name = 'recommendations'
    verbose_name = "Learner Recommendations"

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'recommendations',
                'relative_path': 'urls',
            },
        },
    }
