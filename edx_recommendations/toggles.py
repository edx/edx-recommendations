"""
Toggles for learner recommendations.
"""
from edx_toggles.toggles import WaffleFlag

# Namespace for edx_recommendations waffle flags.
WAFFLE_FLAG_NAMESPACE = "edx_recommendations"


# Waffle flag to enable course about page recommendations.
# .. toggle_name: edx_recommendations.enable_course_about_page_recommendations
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Enable recommendations on course about page
# .. toggle_use_cases: temporary
# .. toggle_creation_date: 2023-01-30
# .. toggle_target_removal_date: None
# .. toggle_warning: None
# .. toggle_tickets: VAN-1259
ENABLE_COURSE_ABOUT_PAGE_RECOMMENDATIONS = WaffleFlag(
    f"{WAFFLE_FLAG_NAMESPACE}.enable_course_about_page_recommendations", __name__
)

# Waffle flag to enable to recommendation panel on learner dashboard
# .. toggle_name: edx_recommendations.enable_dashboard_recommendations
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to enable to recommendation panel on learner dashboard
# .. toggle_use_cases: temporary
# .. toggle_creation_date: 2023-03-24
# .. toggle_target_removal_date: None
# .. toggle_warning: None
# .. toggle_tickets: VAN-1310
ENABLE_DASHBOARD_RECOMMENDATIONS = WaffleFlag(
    f"{WAFFLE_FLAG_NAMESPACE}.enable_dashboard_recommendations", __name__
)

# Waffle flag to enable fallback recommendations.
# .. toggle_name: edx_recommendations.enable_fallback_recommendations
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Supports showing fallback recommendation in case of error on amplitude side.
#                        Currently, fallback recommendations are picked from settings.GENERAL_RECOMMENDATIONS.
# .. toggle_use_cases: opt_in
# .. toggle_creation_date: 2023-01-16
# .. toggle_target_removal_date: None
# .. toggle_warning: None
# .. toggle_tickets: VAN-1239
FALLBACK_RECOMMENDATIONS = WaffleFlag(
    f"{WAFFLE_FLAG_NAMESPACE}.enable_fallback_recommendations", __name__
)
