from pydantic import BaseModel
from typing import Optional





class NodeOptions(BaseModel):
    node_color: Optional[list] = []
    node_size: Optional[int] = 300

class NodesLabelsOptions(BaseModel):
    font_size: int

class EdgesOptions(BaseModel):
    edge_color: list
    arrows: Optional[bool] = True
    arrowsize: Optional[int] = 3
    arrowstyle: Optional[str] = "->"
    connectionstyle: str = f"arc3,rad=0.1"

class EdgeLabelsOptions(BaseModel):
    font_size: Optional[int] = 2

class PlotOptions(BaseModel):
    nodes_labels: dict
    edge_labels: dict
    nodes_options: Optional[dict]
    nodes_labels_options: Optional[dict]
    edges_options: Optional[dict]
    edges_labels_options: Optional[dict]
