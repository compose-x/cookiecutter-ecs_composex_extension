#  -*- coding: utf-8 -*-

"""Main module."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecs_composex.common.settings import ComposeXSettings
    from ecs_composex.mods_manager import XResourceModule, ModManager

from compose_x_common.compose_x_common import keyisset
from ecs_composex.common import build_template, add_parameters, LOG
from ecs_composex.common.stacks import ComposeXStack
from ecs_composex.compose.x_resources.helpers import (
    set_lookup_resources,
    set_new_resources,
    set_resources,
)
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}_template import process_new_resources
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.resource_class}}


class XStack(ComposeXStack):
    """
    Class to manage the stack for {{ cookiecutter.module_name }}
    """

    def __init__(
        self, title, settings: ComposeXSettings, module: XResourceModule, **kwargs
    ):
        set_resources(settings, {{ cookiecutter.resource_class}}, module)
        x_resources = settings.compose_content[module.res_key].values()
        lookup_resources = set_lookup_resources(x_resources)
        new_resources = set_new_resources(x_resources)
        if new_resources:
            stack_template = build_template(
                f"{module.res_key} - root stack",
            )
            super().__init__(title, stack_template, **kwargs)
            process_new_resources(new_resources, self)
        else:
            self.is_void = True
        if lookup_resources:
            if not keyisset(module.mapping_key, settings.mappings):
                settings.mappings[module.mapping_key] = {}
        for resource in settings.compose_content[module.res_key].values():
            resource.stack = self
