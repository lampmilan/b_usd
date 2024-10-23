from dataclasses import fields
from types import NoneType
from typing import Type
from enum import Enum
import bpy
from bzz.bl_data import BlBaseData
from .bl_contexts import ContainerFactory

class BlDataManager:
    def get_abs_rep(self, blender_container: bpy.types.Modifier, context: ContainerFactory,  modifier_index: int = None) -> BlBaseData:

        self.context = context
        self.blender_container = blender_container
        self.abstract_container: BlBaseData

        self._create_new_abs_rep(modifier_index)
        self._pack_abs_rep()

        return self.abstract_container


    def _create_new_abs_rep(self, modifier_index) -> None :

        self.abstract_container = self.context.get_bl_modifier(self.blender_container.type)

        if self.context.type == "Modifiers":
            self.abstract_container.index = modifier_index # If the context is MODIFIER then index is provided
        elif self.context.type == "Modifiers" and modifier_index == None:
            raise ValueError(f"Modifiers must need to provide index value.")

        for prop in dir(self.blender_container):
            if prop in [field.name for field in fields(self.abstract_container)]:
                value = getattr(self.blender_container, prop)
                self.abstract_container.set_attr(prop, value)


    def _pack_abs_rep(self) -> None:
        """
        Look's thought the default values of the object and remove values which are default.
        The method use a new instance of the same dataclass, becouse some field uses default_factory
        """
        original_state = self.context.get_bl_modifier(self.blender_container.type)

        for field in fields(self.abstract_container):
            current_value = getattr(self.abstract_container, field.name)
            original_value = getattr(original_state, field.name)
            if current_value == original_value:
                self.abstract_container.clear_attr(field.name)



def createn_new_abs_rep(blender_container: bpy.types.Modifier, context: ContainerFactory,  modifier_index: int = None) -> BlBaseData:
    container_processor = BlDataManager()
    container = container_processor.get_abs_rep(blender_container, context,  modifier_index)

    return container