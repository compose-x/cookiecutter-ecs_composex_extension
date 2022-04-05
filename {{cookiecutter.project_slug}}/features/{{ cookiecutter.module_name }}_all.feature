# {{ cookiecutter.module_name }}
Feature: {{ cookiecutter.project_slug }} - All compute modes

    Background: I run in Fargate only
        Given With docker-compose.yaml
        And With compute_modes/all_modes.yaml

    @create
    Scenario Outline: Render docker-compose with new {{ cookiecutter.module_name }} resources
        Given With <override_file>
        And I use defined files as input to define execution settings
        Then I render all files to verify execution

        Examples:
            | override_file                  |
            | create_lookup/services.yaml    |
            | create_lookup/no_services.yaml |

    @lookup
    Scenario Outline: Render docker-compose with new {{ cookiecutter.module_name }} resources
        Given With <override_file>
        And I use defined files as input to define execution settings
        Then I render all files to verify execution

        Examples:
            | override_file                  |
            | create_lookup/services.yaml    |
            | create_lookup/no_services.yaml |

    @create_lookup
    Scenario Outline: Render docker-compose with new {{ cookiecutter.module_name }} resources
        Given With <override_file>
        And I use defined files as input to define execution settings
        Then I render all files to verify execution

        Examples:
            | override_file                  |
            | create_lookup/services.yaml    |
            | create_lookup/no_services.yaml |
