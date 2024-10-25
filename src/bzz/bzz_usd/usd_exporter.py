from pxr import Usd, UsdGeom, Gf,Sdf
from .py_to_usd_type import get_usd_type
from ..entity import Entity
from dataclasses import field, fields

def create_usd(mesh_data: Entity):
    # create a new stage

    stage = Usd.Stage.CreateNew(f"{mesh_data.mesh_info.object_name}.usd")
    # Add a comment to the stage
    stage.SetMetadata('comment', 'BZZ USD File')


    # Create a new prim at the root called /Loc1 and set its type to Locator
    # This is what your would call your things when you make them.
    mesh = stage.DefinePrim(f"/{mesh_data.mesh_info.mesh_name}", 'Mesh')
    # I'm going to add some attributes to my prim scale, name and position
    mesh.CreateAttribute('points', Sdf.ValueTypeNames.Point3d).Set(mesh_data.mesh_info.points)
    mesh.CreateAttribute('faceVertexCounts', Sdf.ValueTypeNames.IntArray).Set(mesh_data.mesh_info.face_vertex_counts)
    mesh.CreateAttribute('faceVertexIndices', Sdf.ValueTypeNames.IntArray).Set(mesh_data.mesh_info.face_vertex_indices)
    mesh.CreateAttribute('faceVertexIndices', Sdf.ValueTypeNames.IntArray).Set(mesh_data.mesh_info.face_vertex_indices)
    #locator.CreateAttribute("scale",Sdf.ValueTypeNames.Float ).Set(2.0)
    #locator.CreateAttribute("name",Sdf.ValueTypeNames.String ).Set("hello")
    #locator.CreateAttribute("position",Sdf.ValueTypeNames.Point3d ).Set((0,0,0))

    for modifier in mesh_data.modifiers:
        modifier_name = modifier.name.replace(".", "_")
        modifier_prim = stage.DefinePrim(f"/modifiers/{modifier_name}", 'Mesh')
        for field in fields(modifier):
            field_name = field.name
            my_value = getattr(modifier, field_name)  # Get the value of the field
            if my_value != None:
                modifier_prim.CreateAttribute(field_name, get_usd_type(my_value)).Set(my_value)  # Create attribute with the field name and value

        

    stage.Save()