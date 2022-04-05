#  -*- coding: utf-8 -*-

"""Main module."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecs_composex.common.settings import ComposeXSettings
    from ecs_composex.mods_manager import XResourceModule, ModManager

from ecs_composex.common import build_template, add_parameters, LOG
from ecs_composex.common.stacks import ComposeXStack

from ecs_composex.compose.x_resources import XResource


class {{ cookiecutter.resource_class}}(XResource):
    """
    Class to represent the OpenSearch domain
    """

    def __init__(
        self, name, definition, module: XResourceModule, settings: ComposeXSettings
    ):

        super().__init__(
            name,
            definition,
            module,
            settings,
        )
