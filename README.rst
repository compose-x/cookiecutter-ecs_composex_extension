#############################################
ECS Compose-X Modules cookiecutter
#############################################

--------------------------------------------------------------------------------------------------------------
Create all the necessary layout for new ECS Compose-X modules extensions.
--------------------------------------------------------------------------------------------------------------

From version 0.18 of ECS Compose-X you can now create your own extensions to import into your compose files.
These extensions, used as extension-fields in the compose syntax, will allow you to implement functions to link
up to your ECS services or other AWS Resources defined in the template.

To be functional, your module will have to be a python path that ECS Compose-X can import as it initializes itself.

How to use
============

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate
    pip install pip -U
    pip install cookiecutter

    git clone https://github.com/compose-x/cookiecutter-ecs_composex_extension.git
    cookiecutter cookiecutter-ecs_composex_extension


