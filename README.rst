edx-recommendations
=============================

|license-badge|

Support for learner recommendations. This adds API for fetching the recommendations from different sources like Algolia and Amplitude.

Overview
---------

edx-recommendations is a plugin that runs under lms. It uses the configuration settings defined in lms as well.
In order to use, the library must be installed into edx-platform. The purpose of this plugin is to fetch the recommendations from different sources.

Using with Docker Devstack
--------------------------
Prerequisite: Have your Open edX https://github.com/openedx/devstack properly installed.
Note: When you see "from inside the lms" below, it means that you've run ``make lms-shell`` from your devstack directory
and are on a command prompt inside the LMS container.

1. | Clone this repo into ``../src/`` directory (relative to your "devstack" repo location). This will mount the directory
   | in a way that is accessible to the lms container.

2. From inside the lms, uninstall bulk-grades and reinstall your local copy. You can just copy the following line::

    pip uninstall edx-recommendations -y; pip install -e /edx/src/edx-recommendations

   Or, you can run the following make command::

    make install-local

3. Now, get your edx-recommendations development environment set up::

    cd /edx/src/edx-recommendations
    virtualenv edx-recommendations-env
    source edx-recommendations-env/bin/activate
    make requirements

Making Code Changes
-------------------

1. | After checking out a new branch, increment ``__version__`` by the smallest possible value located in ``edx-recommendations/__init__.py``.
   | This will allow edx-platform to pick up the new version.

2. | Once a branch has been merged, it is necessary to make a release on github, specifying the new version from
   | ``__version__`` set above.

3. In order for platform to use the newest version of edx-recommendations, it is necessary to run the::

    $ make upgrade

from docker shell of edx-platform. This will increment the version of edx-bulk-grades to the correct one.

4. Once the code from step 3 is merged, this will trigger deployment of the correct versions of edx platform and bulk-grades.

Unit Testing
------------
mock_apps folder: Since edx-recommendations depends on platform during actual runtime, for unit tests, we need to mock various
endpoints and calls. To this end, they are mocked in the mock_apps folder.

Since edx-recommendations runs under platform, it is necessary to connect to platform docker::

    $ make lms-shell

followed by::

    $ cd /edx/src/edx-recommendations
    make test

This will run the unit tests and code coverage numbers

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/openedx/.github/blob/master/CONTRIBUTING.md>`_ for details.

The pull request description template should be automatically applied if you are creating a pull request from GitHub. Otherwise you
can find it at `PULL_REQUEST_TEMPLATE.md <https://github.com/openedx/edx-recommendations/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_.

The issue report template should be automatically applied if you are creating an issue on GitHub as well. Otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/openedx/edx-recommendations/blob/master/.github/ISSUE_TEMPLATE.md>`_.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |license-badge| image:: https://img.shields.io/github/license/edx/edx-recommendations.svg
    :target: https://github.com/openedx/edx-recommendations/blob/master/LICENSE.txt
    :alt: License
