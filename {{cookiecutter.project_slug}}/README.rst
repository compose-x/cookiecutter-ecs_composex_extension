{% for _ in cookiecutter.module_name %}#{% endfor %}
{{ cookiecutter.module_name }}
{% for _ in cookiecutter.module_name %}#{% endfor %}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}


Use with ECS Compose-X
========================

Install
-----------

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate
    pip install .

Use
-----

.. code-block:: yaml

    services:
      frontend:
        image: nginx

    {{ cookiecutter.extension_name }}:
      Properties: {}
      Lookup: {}
      Settings: {}
      Services: {}

