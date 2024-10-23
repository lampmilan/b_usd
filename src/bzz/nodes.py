from dataclasses import dataclass, fields
from typing import Any
import bpy
from .bl_data import BlBaseData


@dataclass(slots=True)
class Node(BlBaseData):
    """
    Base representation of a Blender node
    """
    name: str = ""
    label:str = ""
    position: list[float] = [0, 0]
    is_color: bool = False
    node_color: list[float] = [0.608, 0.608, 0.608]


