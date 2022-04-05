#  -*- coding: utf-8 -*-
"""
Pre-execution hooks
"""

import re
import sys


EXTENSION_REGEX = r"^x-[a-zA-Z0-9_]+$"
MODULE_REGEX = r'^[a-zA-Z0-9_]+$'
COMPOSE_MODULE_REGEX = r'^ecs_composex_[a-zA-Z0-9_]+$'

extension_name = '{{ cookiecutter.extension_name }}'
module_name = '{{ cookiecutter.module_name }}'
compose_module_name = '{{ cookiecutter.project_slug }}'

if not re.match(EXTENSION_REGEX, extension_name):
    print('ERROR: %s is not a valid extension name!' % extension_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

if extension_name.find(module_name) < 0:
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(COMPOSE_MODULE_REGEX, compose_module_name):
    print('ERROR: %s is not a valid Python module name!' % compose_module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)
