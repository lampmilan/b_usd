import bpy

# Get the active object
def test():
    obj = bpy.context.active_object

    if obj and obj.type == 'MESH':
        mesh = obj.data
        
        # Access vertices
        print("Vertices:")
        for vertex in mesh.vertices:
            print(f"Index: {vertex.index}, Co: {vertex.co}, Normal: {vertex.normal}")

        # Access faces
        print("\nFaces:")
        for poly in mesh.polygons:
            print(f"Index: {poly.index}, Vertices: {poly.vertices}")

        # Access materials
        print("\nMaterials:")
        materials = obj.data.materials
        for i, material in enumerate(materials):
            print(f"Material Index {i}: {material.name}")