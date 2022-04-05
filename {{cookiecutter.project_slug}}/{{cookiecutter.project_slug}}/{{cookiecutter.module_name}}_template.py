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


def process_new_resources(new_resources, stack: ComposeXStack) -> None:
    """

    :param new_resources:
    :param stack:
    :return:
    """

