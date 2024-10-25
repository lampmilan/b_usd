from dataclasses import dataclass, field
import bpy
import bmesh
import bpy_types
from .data_utils import createn_new_abs_rep
from .modifiers import Modifier
from .bl_contexts import Modifiers

@dataclass
class Mesh:
    object_name: str = ""
    mesh_name: str = ""
    points: list[list[float]] = field(default_factory=list)
    normals: list[list[float]] = field(default_factory=list)
    face_vertex_counts: list[int] = field(default_factory=list)
    face_vertex_indices: list[int] = field(default_factory=list)
    uv_layer: list[list[float]] = field(default_factory=list)
    tex_coords: list[list[float]] = field(default_factory=list)



class Entity:
    @staticmethod
    def _extract_modifiers(object) -> list[Modifier]:
        mods: list[Modifier] = []
        if len(object.modifiers) == 0:
            return mods

        for modifier in object.modifiers:
            abs_mod = createn_new_abs_rep(modifier, Modifiers())
            mods.append(abs_mod)
        return mods


    @staticmethod
    def _extract_mesh_information(mesh_data, mesh_container: Mesh):
        bm = bmesh.new()
        bm.from_mesh(mesh_data)

        mesh_container.mesh_name = mesh_data.name
        mesh_container.points = [v.co for v in bm.verts]
        mesh_container.face_vertex_counts = [len(face.verts) for face in bm.faces]
        mesh_container.face_vertex_indices = [v.index for face in bm.faces for v in face.verts]
        mesh_container.normals = [face.normal for face in bm.faces]
        mesh_container.uv_layer = bm.loops.layers.uv.active
        mesh_container.tex_coords = [(loop[mesh_container.uv_layer].uv) for face in bm.faces for loop in face.loops] if mesh_container.uv_layer else []
        #sharp_face = [face.use_smooth for face in bm.faces]

        bm.free()
        return mesh_container


    def __init__(self, mesh_object: bpy_types.Object):
        self.mesh_info: Mesh = Mesh()
        
        self.mesh_info.object_name = mesh_object.name
        
        Entity._extract_mesh_information(mesh_object.data, self.mesh_info)
        self.modifiers: list[Modifier] = Entity._extract_modifiers(mesh_object)

        

        print(self.mesh_info)


    def get_mesh_data(self):
        """
        return a Mesh dataclass representation of the given Mesh Object
        """
        return self.mesh_info
