Django plugin for learner recommendations
#########################################

Status
******


**Accepted**


Context
*******

The recommendations are currently part of the user journey on edX and are shown on multiple places such as the learner dashboard, course about pages and post-registration experience etc. Multiple teams within edX are contributing to the overall recommendations experience by generating recommendations using different technologies, namely Amplitude, Algolia, and in the future might expand to use another paid tool. 

It's also worth noting that recommendations are not integral to the core functionality of the platform. Therefore, it is possible to separate them from the core app. 

By creating a plugin, 
    - We avoid the risk of including organization (2u edX) specific code to the core app
    - We have the ability to incorporate paid technologies into core functionality without direct integration
    - This separation not only simplifies the codebase but also offers the opportunity to manage and update the recommendations and related technologies independently





.. This section describes the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts.

Decision
********

Given these considerations, we will be organizing recommendations code in this plugin that can be installed and utilized in edx-platform.



Consequences
************


- Teams within edX will have a centralized place to contribute and experiment functionality related to recommendations.
- The deployment of recommendations will continue to be dependent on the platform deployments
- In the future, we should evaluate the decision to make this an independent service instead of a plugin as it still contributes to the monolith edX platform service


Rejected Alternatives
*********************

**Add a Django app inside edx-platform repo**

The proposal to develop the recommendations app within edx-platform was declined due to the app's impact on the overall size of the edx-platform codebase, its reliance on 2u specific components and business logic, and the need for paid tools to make it work, making it less applicable to the openedX community