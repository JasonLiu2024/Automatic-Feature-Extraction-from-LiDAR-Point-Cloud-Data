"""re-apply crestlines"""
import numpy as np
class crestline_mover:
    def __init__(self, mesh_3d_vertices, mesh_faces, 
                 mesh_3d_crestlines_vertices, crestline_edges, 
                 mesh_2d_vertices, color):
        self.mesh_3d_vertices = mesh_3d_vertices
        self.mesh_faces = mesh_faces
        self.mesh_3d_crestlines_vertices = mesh_3d_crestlines_vertices[:,0:3]
        self.mesh_2d_vertices = mesh_2d_vertices
        self.color = color
        self.crestline_edges = crestline_edges
        self.V = mesh_3d_vertices.shape[0]
        self.F = mesh_faces.shape[0]
        self.crestline_V = mesh_3d_crestlines_vertices.shape[0]
        self.crestline_E = crestline_edges.shape[0]
        self.mesh_2d_crestlines_vertices = self.Move_3D_vertices_to_2D() # want to find
    def collinear(self, a, b, c):
        # use matrix rank to determine colinearity (no work, needs exact equal)
        # Reference: https://stackoverflow.com/questions/9608148/python-script-to-determine-if-x-y-coordinates-are-colinear
        # -getting-some-e#:~:text=You%20can%20use%20the%20rank,i.e.%20any%20number%20of%20points).

        # added tolerance
        vector_ab = a - b
        vector_ac = a - c
        cross_product = np.cross(vector_ab, vector_ac)
        edge_length_ab = np.sqrt(vector_ab.dot(vector_ab))
        return np.sqrt(cross_product.dot(cross_product)) < edge_length_ab/500.0
    # v can be on line (a, b), (a, c), or (b, c)
    def FindVertexIndex(self, a, b, c, a_index, b_index, c_index, v):
        #print(f"checking colinearity of: {a, b} and {v}") 
        if(self.collinear(a, b, v)): 
            return a_index, b_index
        #print(f"checking colinearity of: {a, c} and {v}") 
        if(self.collinear(a, c, v)): 
            return a_index, c_index
        #print(f"checking colinearity of: {b, c} and {v}") 
        if(self.collinear(b, c, v)): 
            return b_index, c_index
        #print("no colinearity found!")
    # input: mesh vertices a and b; vertex v that lies on edge (a, b)
    # return alpha: from a to v on edge (a, b)
    def getAlpha(self, a, b, v):
        va = a - v
        ab = b - a
        va_length = np.sqrt(va.dot(va))
        ab_length = np.sqrt(ab.dot(ab))
        alpha = va_length / ab_length
        return alpha
    def LinearInterpolate(self):
        augmentation = np.zeros(shape=(self.crestline_V, 3))
        for e in range(self.crestline_E): # consider crestline edge (u, v)
            u_index, v_index, face_index = self.crestline_edges[e]
            #print(f"edge information: {u_index} {v_index} {face_index}")
            if(face_index != -1): # when face_index == -1, there's NO triangle associated w/ crestline edge
                face_vertex_a_index, face_vertex_b_index, face_vertex_c_index = self.mesh_faces[face_index]
                #print(f"checking face: {face_vertex_a_index} {face_vertex_b_index} {face_vertex_c_index}")
                # edge lies on triangle (a, b, c) <- these are MESH vertices
                a = self.mesh_3d_vertices[face_vertex_a_index]
                b = self.mesh_3d_vertices[face_vertex_b_index]
                c = self.mesh_3d_vertices[face_vertex_c_index]
                #print(f"which are: \n{a}, \n{b}, \n{c}")
                
                """for the two vertices in (u, v), do:""" # <- u, v are CRESTLINE vertices
                # u is on edge (u1, u2)
                u = self.mesh_3d_crestlines_vertices[u_index] # u can be on any of the 3 edges of the face
                #print(f"checking crestline vertex: {u} at index {u_index}")
                u1, u2 = self.FindVertexIndex(a, b, c, 
                                              face_vertex_a_index, 
                                              face_vertex_b_index, 
                                              face_vertex_c_index, u)
                alpha_u = self.getAlpha(a=self.mesh_3d_vertices[u1], 
                                        b=self.mesh_3d_vertices[u2], v=u)
                # for mesh vertex index@ u1, write down it's: (index) u2, alpha value
                augmentation[u_index][0] = u1
                augmentation[u_index][1] = u2
                augmentation[u_index][2] = alpha_u

                # v is on edge (v1, v2)
                v = self.mesh_3d_crestlines_vertices[v_index] # u can be on any of the 3 edges of the face
                v1, v2 = self.FindVertexIndex(a, b, c, 
                                              face_vertex_a_index, 
                                              face_vertex_b_index, 
                                              face_vertex_c_index, v)
                alpha_v = self.getAlpha(a=self.mesh_3d_vertices[v1], 
                                        b=self.mesh_3d_vertices[v2], v=v)
                # for mesh vertex index@ v1, write down its: (index) v2, alpha value
                augmentation[v_index][0] = v1
                augmentation[v_index][1] = v2
                augmentation[v_index][2] = alpha_v
        return augmentation
    # input: mesh vertices a, b
    # return: point v, which lies on edge (a, b)
    # assumption: alpha refers to: length of edge (v, a) / lendth of edge (b, a)
    def Recover(self, a, b, alpha):
        v = alpha * (b - a) + a
        return v
    def Move_3D_vertices_to_2D(self):
        augmentation = self.LinearInterpolate()
        crestline_V_2d = np.zeros(shape=(self.mesh_3d_crestlines_vertices.shape))
        for e in range(self.crestline_E): # for all mesh vertices:
            # use 3d crestline vertices + augmentation to find 2d creatline vertices
            u_index, v_index, face_index = self.crestline_edges[e]

            u1_index = augmentation[u_index][0].astype(int)
            u2_index = augmentation[u_index][1].astype(int)
            u_alpha = augmentation[u_index][2]
            u1 = self.mesh_2d_vertices[u1_index]
            u2 = self.mesh_2d_vertices[u2_index]
            u_2d = self.Recover(u1, u2, u_alpha)
            crestline_V_2d[u_index] = u_2d
            # print(f"processing point number {u_index + 1}, alpha: {u_alpha}, output: {u_2d}")
            # print(f"    this vertex lies on edge between {u1} and {u2}")

            v1_index = augmentation[v_index][0].astype(int)
            v2_index = augmentation[v_index][1].astype(int)
            v_alpha = augmentation[v_index][2]
            v1 = self.mesh_2d_vertices[v1_index]
            v2 = self.mesh_2d_vertices[v2_index]
            v_2d = self.Recover(v1, v2, v_alpha)
            crestline_V_2d[v_index] = v_2d 
            # print(f"processing point number {v_index + 1}, alpha: {v_alpha}, output: {v_2d}")
            # print(f"    this vertex lies on edge between {v1} and {v2}")
        return crestline_V_2d