"""
Production settings for the edx_recommendations app.
"""


def plugin_settings(settings):
    """
    Settings for edx_recommendations app
    """
    settings.COURSE_ABOUT_PAGE_AMPLITUDE_MODEL_ID = settings.ENV_TOKENS.get(
        "COURSE_ABOUT_PAGE_AMPLITUDE_MODEL_ID"
    )
    settings.LEARNER_DASHBOARD_AMPLITUDE_MODEL_ID = settings.ENV_TOKENS.get(
        "LEARNER_DASHBOARD_AMPLITUDE_MODEL_ID"
    )
    settings.GENERAL_RECOMMENDATIONS = settings.ENV_TOKENS.get(
        "GENERAL_RECOMMENDATIONS", []
    )
