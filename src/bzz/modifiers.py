from dataclasses import dataclass, fields, field
import bpy
import mathutils
from .bl_data import BlBaseData



@dataclass(slots=True)
class Modifier(BlBaseData):
    """
    Base representation of a Blender modifier
    """
    index: int = -1
    name: str = ""
    type: str = ""
    show_viewport: bool = True
    show_render: bool = True




@dataclass(slots=True)
class DataTransfer(Modifier):
    object: None = None
    data_types_edges: set = field(default_factory=set)
    data_types_loops: set = field(default_factory=set)
    data_types_polys: set = field(default_factory=set)
    data_types_verts: set = field(default_factory=set)
    edge_mapping: str = "NEAREST"
    invert_vertex_group: bool = False
    islands_precision: float = 0.0
    layers_uv_select_dst: str = "NAME"
    layers_uv_select_src: str = "ALL"
    layers_vcol_loop_select_dst: str = "NAME"
    layers_vcol_loop_select_src: str = "ALL"
    layers_vcol_vert_select_dst: str = "NAME"
    layers_vcol_vert_select_src: str = "ALL"
    layers_vgroup_select_dst: str = "NAME"
    layers_vgroup_select_src: str = "ALL"
    loop_mapping: str = "NEAREST_POLYNOR"
    max_distance: float = 1.0
    mix_factor: float = 1.0
    mix_mode: str = "REPLACE"
    poly_mapping: str = "NEAREST"
    use_apply_on_spline: bool = False
    use_edge_data: bool = False
    use_loop_data: bool = False
    use_max_distance: bool = False
    use_object_transform: bool = True
    use_poly_data: bool = False
    use_vert_data: bool = False
    vert_mapping: str = "NEAREST"
    vertex_group: str = ""


@dataclass(slots=True)
class DataMesh(Modifier):
    cache_format: str = "MDD"
    deform_mode: str = "OVERWRITE"
    eval_factor: float = 0.0
    eval_frame: float = 0.0
    eval_time: float = 0.0
    factor: float = 1.0
    filepath: str = ""
    flip_axis: set = field(default_factory=set)
    forward_axis: str = "POS_Y"
    frame_scale: float = 1.0
    frame_start: float = 0.0
    interpolation: str = "LINEAR"
    invert_vertex_group: bool = False
    play_mode: str = "SCENE"
    time_mode: str = "FRAME"
    type: str = "MESH_CACHE"
    up_axis: str = "POS_Z"
    use_apply_on_spline: bool = False
    vertex_group: str = ""


@dataclass(slots=True)
class MeshSequenceCache(Modifier):
    cache_file: None = None
    object_path: str = ""
    read_data: set = field(default_factory=lambda: {'VERT', 'COLOR', 'POLY', 'UV'})
    use_apply_on_spline: bool = False
    use_vertex_interpolation: bool = True
    velocity_scale: float = 1.0



@dataclass(slots=True)
class NormalEdit(Modifier):
    invert_vertex_group: bool = False
    mix_factor: float = 1.0
    mix_limit: float = 3.1415927410125732
    mix_mode: str = "COPY"
    mode: str = "RADIAL"
    no_polynors_fix: bool = False
    offset: mathutils.Vector = mathutils.Vector((0.0, 0.0, 0.0))
    target: bpy.types.Object = None
    use_apply_on_spline: bool = False
    use_direction_parallel: bool = False
    vertex_group: str = ""


@dataclass(slots=True)
class WeightedNormal(Modifier):
    invert_vertex_group: bool = False
    keep_sharp: bool = False
    mode: str = "FACE_AREA"
    thresh: float = 0.009999999776482582
    use_apply_on_spline: bool = False
    use_face_influence: bool = False
    vertex_group: str = ""
    weight: int = 50


@dataclass(slots=True)
class UvProject(Modifier):
    aspect_x: float = 1.0
    aspect_y: float = 1.0
    is_active: bool = True
    projector_count: int = 1
    scale_x: float = 1.0
    scale_y: float = 1.0
    use_apply_on_spline: bool = False
    uv_layer: str = ""


@dataclass(slots=True)
class UvWarp(Modifier):
    bone_from: str = ""
    bone_to: str = ""
    center: bpy.props.FloatVectorProperty = (0.0, 0.0, 0.0)
    invert_vertex_group: bool = False
    object_from: bpy.types.Object = None
    object_to: bpy.types.Object = None
    offset: bpy.props.FloatVectorProperty = (0.0, 0.0, 0.0)
    rotation: float = 0.0
    scale: bpy.props.FloatVectorProperty = (0.0, 0.0, 0.0)
    use_apply_on_spline: bool = False
    uv_layer: str = ""
    vertex_group: str = ""



@dataclass(slots=True)
class VertexWeightEdit(Modifier):
    default_weight: float = 0.0
    falloff_type: str = "LINEAR"
    invert_falloff: bool = False
    invert_mask_vertex_group: bool = False
    mask_constant: float = 1.0
    mask_tex_map_bone: str = ""
    mask_tex_map_object: None = None
    mask_tex_mapping: str = "LOCAL"
    mask_tex_use_channel: str = "INT"
    mask_tex_uv_layer: str = ""
    mask_texture: None = None
    mask_vertex_group: str = ""
    normalize: bool = False
    remove_threshold: float = 0.009999999776482582
    use_add: bool = False
    use_apply_on_spline: bool = False
    use_remove: bool = False
    vertex_group: str = ""


@dataclass(slots=True)
class VertexWeightMix(Modifier):
    default_weight_a: float = 0.0
    default_weight_b: float = 0.0
    invert_mask_vertex_group: bool = False
    invert_vertex_group_a: bool = False
    invert_vertex_group_b: bool = False
    mask_constant: float = 1.0
    mask_tex_map_bone: str = ""
    mask_tex_map_object: None = None
    mask_tex_mapping: str = "LOCAL"
    mask_tex_use_channel: str = "INT"
    mask_tex_uv_layer: str = ""
    mask_texture: None = None
    mask_vertex_group: str = ""
    mix_mode: str = "SET"
    mix_set: str = "AND"
    normalize: bool = False
    use_apply_on_spline: bool = False
    vertex_group_a: str = ""
    vertex_group_b: str = ""


@dataclass(slots=True)
class VertexWeightProximity(Modifier):
    falloff_type: str = "LINEAR"
    invert_falloff: bool = False
    invert_mask_vertex_group: bool = False
    mask_constant: float = 1.0
    mask_tex_map_bone: str = ""
    mask_tex_map_object: None = None
    mask_tex_mapping: str = "LOCAL"
    mask_tex_use_channel: str = "INT"
    mask_tex_uv_layer: str = ""
    mask_texture: None = None
    mask_vertex_group: str = ""
    max_dist: float = 1.0
    min_dist: float = 0.0
    normalize: bool = False
    proximity_geometry: set = field(default_factory=lambda: {'VERTEX'})
    proximity_mode: str = "OBJECT"
    target: None = None
    use_apply_on_spline: bool = False
    vertex_group: str = ""


@dataclass(slots=True)
class Array(Modifier):
    constant_offset_displace: mathutils.Vector = mathutils.Vector((1.0000, 0.0000, 0.0000))
    count: int = 2
    curve: None = None
    end_cap: None = None
    fit_length: float = 0.0
    fit_type: str = "FIXED_COUNT"
    is_active: bool = True
    is_override_data: bool = False
    merge_threshold: float = 0.009999999776482582
    offset_object: None = None
    offset_u: float = 0.0
    offset_v: float = 0.0
    relative_offset_displace: mathutils.Vector = mathutils.Vector((1.0000, 0.0000, 0.0000))
    start_cap: None = None
    use_apply_on_spline: bool = False
    use_constant_offset: bool = False
    use_merge_vertices: bool = False
    use_merge_vertices_cap: bool = False


@dataclass(slots=True)
class Bevel(Modifier):
    face_strength_mode: str = "FSTR_NONE"
    harden_normals: bool = False
    invert_vertex_group: bool = False
    limit_method: str = "ANGLE"
    loop_slide: bool = True
    mark_seam: bool = False
    mark_sharp: bool = False
    material: int = -1
    miter_inner: str = "MITER_SHARP"
    miter_outer: str = "MITER_SHARP"
    offset_type: str = "OFFSET"
    profile: float = 0.5
    profile_type: str = "SUPERELLIPSE"
    segments: int = 1
    spread: float = 0.10000000149011612
    use_apply_on_spline: bool = False
    use_clamp_overlap: bool = True
    vertex_group: str = ""
    vmesh_method: str = "ADJ"
    width: float = 0.10000000149011612
    width_pct: float = 0.10000000149011612


@dataclass(slots=True)
class Boolean(Modifier):
    double_threshold: float = 9.999999974752427e-07
    object: None = None
    operand_type: str = "OBJECT"
    operation: str = "DIFFERENCE"
    solver: str = "EXACT"
    use_apply_on_spline: bool = False
    use_hole_tolerant: bool = False
    use_self: bool = False


@dataclass(slots=True)
class Build(Modifier):
    frame_duration: float = 100.0
    frame_start: float = 1.0
    seed: int = 0
    use_apply_on_spline: bool = False
    use_random_order: bool = False
    use_reverse: bool = False


@dataclass(slots=True)
class Decimate(Modifier):
    decimate_type: str = "COLLAPSE"
    delimit: set = field(default_factory=set)
    face_count: int = 0
    invert_vertex_group: bool = False
    iterations: int = 0
    ratio: float = 1.0
    symmetry_axis: str = "X"
    type: str = "DECIMATE"
    use_apply_on_spline: bool = False
    use_collapse_triangulate: bool = False
    use_dissolve_boundaries: bool = False
    use_symmetry: bool = False
    vertex_group: str = ""
    vertex_group_factor: float = 1.0


@dataclass(slots=True)
class EdgeSplit(Modifier):
    split_angle: float = 0.5235987901687622
    type: str = "EDGE_SPLIT"
    use_apply_on_spline: bool = False
    use_edge_angle: bool = True
    use_edge_sharp: bool = True

@dataclass(slots=True)
class Nodes(Modifier):
    node_group: None = None
    use_apply_on_spline: bool = False


@dataclass(slots=True)
class Smooth(Modifier):
    factor: float = 0.5
    repeat: int = 1
    vertex_group: str = ""


@dataclass(slots=True)
class Skin(Modifier):
    branch_smoothing: float = 0.0
    use_smooth_shade: bool = False



