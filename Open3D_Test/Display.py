"""Display utility"""
import numpy as np
class Colors:
    def __init__(self) -> None:
        self.PURPLE = np.array([1.0, 0.1, 1.0]) # purple
        self.TURQUOISE = np.array([0.1, 1.0, 0.1]) # turquoise
        self.BLUE = np.array([0.1, 0.1, 1.0]) # blue
        self.GREEN = np.array([0.1, 1.0, 0.1]) # green
        self.YELLOW = np.array([1.0, 1.0, 0.1]) # yellow
        self.RED = np.array([1.0, 0.1, 0.1]) # red
        self.BLACK = np.array([0, 0, 0]) # black
        self.GREY = np.array([0.8, 0.8, 0.8]) # grey

def mesh_lines(vertices, faces, plot, color):
    plot.add_lines(vertices[faces[:, 0]], 
                    vertices[faces[:, 1]], 
                    shading={"line_color": color})
    plot.add_lines(vertices[faces[:, 0]], 
                    vertices[faces[:, 2]], 
                    shading={"line_color": color})
    plot.add_lines(vertices[faces[:, 1]], 
                    vertices[faces[:, 2]], 
                    shading={"line_color": color})