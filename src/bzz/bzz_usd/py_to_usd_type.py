from enum import Enum
from typing import Any
from pxr import Sdf

class InvalidAttributeType(Exception):
    "Raise when an attribute is not defined in the PyToUsd Enum"
    pass

class PyToUsd(Enum):
    BOOL = Sdf.ValueTypeNames.Bool
    FLOAT = Sdf.ValueTypeNames.Float
    STR =  Sdf.ValueTypeNames.String



def get_usd_type(var: Any):
    """
    Get the SDF.ValueTypeNames type of a attribute type.
    """
    var_type: str

    if type(var) in (list, tuple, set):
        base_type = type(var).__name__.upper()
        child_type = type(var[0]).__name__.upper()
        var_type = f"{base_type}.{child_type}"
    else:
        var_type = type(var).__name__.upper()

    try:
        return PyToUsd[var_type].value
    except KeyError:
        raise(InvalidAttributeType)
