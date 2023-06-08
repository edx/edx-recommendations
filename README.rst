edx-recommendations
=============================

|pypi-badge| |license-badge| |Status|

A plugin for personalized recommendations

Please tag **@openedx/vanguards** on any PRs or issues.  Thanks!

Overview
---------

The ``edx-recommendations`` is a Django app that serves REST API endpoints for
getting personalized recommendations for learner. It used different sources
like Algolia and Amplitude for recommendations.

edx-recommendations is a plugin that runs under lms. It uses same configuration settings as defined in lms.
It can be used by installing in edx-platform.

How to install locally
--------------------------

1. | Clone this repo into ``../src/`` directory (relative to your "devstack" repo location). This will mount the directory
   | in a way that is accessible to the lms container.

2. From lms-shell, uninstall edx-recommendations and install your local copy. You can run the following command::

    pip uninstall edx-recommendations -y; pip install -e /edx/src/edx-recommendations


How to create a new release
---------------------------

1. | Checkout to a new branch and increment ``__version__`` by the smallest possible value located in ``edx-recommendations/__init__.py``.
   | This will allow edx-platform to pick up the new version.

2. Update the ``CHANGELOG.rst`` with the brief description of your changes.

2. | Once a branch has been merged, it is necessary to create a release on github, specifying the new version from
   | ``__version__`` set above. This will publish the release to PyPI.


.. Unit Testing
.. ------------
.. mock_apps folder: Since edx-recommendations depends on platform during actual runtime, for unit tests, we need to mock various
.. endpoints and calls. To this end, they are mocked in the mock_apps folder.

.. followed by::

..     $ cd /edx/src/edx-recommendations
..     virtualenv edx-recommendations-env
..     source edx-recommendations-env/bin/activate
..     make requirements
..     make test

.. This will run the unit tests and code coverage numbers

Testing
-------

edx-recommendations has an assortment of test cases and code quality
checks to catch potential problems during development.  To run them all in the
version of Python you chose for your virtualenv:

.. code-block:: bash

    $ make validate

To run just the unit tests:

.. code-block:: bash

    $ make test

To run just the unit tests and check diff coverage

.. code-block:: bash

    $ make diff_cover

To run just the code quality checks:

.. code-block:: bash

    $ make quality

To run the unit tests under every supported Python version and the code
quality checks:

.. code-block:: bash

    $ make test-all

To generate and open an HTML report of how much of the code is covered by
test cases:

.. code-block:: bash

    $ make coverage

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

.. |pypi-badge| image:: https://img.shields.io/pypi/v/edx-recommendations.svg
    :target: https://pypi.python.org/pypi/edx-ace/
    :alt: PyPI

.. |Status| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
