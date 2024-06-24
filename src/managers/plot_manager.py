from src.constants import GRAPH_OUTPUT_DIRECTORY, COOCURRENCE, HETEROGENEUS, NODE_CATEGORY_COLORS
from text2graphapi.text2graphapi.src.Cooccurrence import Cooccurrence
from src.models.plot_options import PlotOptions, NodeOptions, NodesLabelsOptions, EdgesOptions, EdgeLabelsOptions




class PlotManager:
    @staticmethod
    def generate_plot_image(graph: Cooccurrence, transformed_graph: dict, plot_options: dict, docname: str, graph_type: str) -> None:
        plot_settings = PlotManager._build_plot_options(transformed_graph, plot_options, graph_type)
        graph.plot_graph(transformed_graph["nx_graph"], f"{GRAPH_OUTPUT_DIRECTORY}{docname}.png", plot_settings.__dict__)
    
    @staticmethod
    def _build_plot_options(transformed_graph: dict, plot_options: dict, graph_type: str) -> PlotOptions:
        PlotManager.clean_nodes(transformed_graph)
        nodes_labels = {}
        nodes_colors = {}

        for node, pos_tag in transformed_graph["nodes"]:
            nodes_labels[node] = f"{node}\n<{pos_tag.get('pos_tag','')}>"
            nodes_colors[node] = NODE_CATEGORY_COLORS.get(pos_tag.get("pos_tag"), 9)
        
        nodes_size = int(plot_options["node_size"]) if plot_options.get("node_size") else PlotManager._get_node_size_by_nodes(transformed_graph["nodes"])
        edge_prefix = "tfidf" if graph_type == HETEROGENEUS else "freq"
        edge_labels = dict([((nodes_labels[edge_from], nodes_labels[edge_to]), f"{edge_prefix}={frequency.get(edge_prefix)}") for edge_from, edge_to, frequency in transformed_graph.get("edges",[])])
        edge_colors = [0] * len(transformed_graph.get("edges",[]))

        if graph_type == COOCURRENCE:
            edge_colors = [int((edge_labels[(nodes_labels[edge_from], nodes_labels[edge_to])]).replace(f"{edge_prefix}=","")) / 10 for edge_from, edge_to in transformed_graph["nx_graph"].edges() if edge_labels[(nodes_labels[edge_from], nodes_labels[edge_to])]]

        node_options = NodeOptions(
            node_color=list(nodes_colors.values()),
            node_size=nodes_size
        )
        nodes_labels_options = NodesLabelsOptions(
            font_size=PlotManager._get_font_size_by_node_size(nodes_size)
        )
        edges_options = EdgesOptions(
            edge_color=edge_colors,
            arrowsize=int(plot_options["arrowsize"]) if plot_options.get("arrowsize") else PlotManager._get_font_size_by_node_size(nodes_size),
            arrowstyle=plot_options.get("arrowstyle"),
        )
        edge_labels_options = EdgeLabelsOptions(
            font_size=int(plot_options["font_size"]) if plot_options.get("font_size") else PlotManager._get_font_size_by_node_size(nodes_size)
        )

        return PlotOptions(
            nodes_labels=nodes_labels,
            edge_labels=edge_labels,
            nodes_options=node_options.__dict__,
            nodes_labels_options=nodes_labels_options.__dict__,
            edges_options=edges_options.__dict__,
            edges_labels_options=edge_labels_options.__dict__,
        )
    
    @staticmethod
    def _get_node_size_by_nodes(nodes: list) -> int:
        node_size = int(7000 / len(nodes))

        if node_size < 50:
            return 50

        if node_size > 700:
            return 700

        return node_size
    
    @staticmethod
    def _get_font_size_by_node_size(node_size) -> int:
        font_size = int(node_size / 70)

        if font_size < 2:
            return 2

        if font_size > 10:
            return 10

        return font_size
    
    @staticmethod
    def clean_nodes(transformed_graph: dict) -> None:
        sorted_nodes = sorted(transformed_graph.get("nodes",[]), key=lambda tup: tup[0])
        assigned_nodes = []
        transformed_graph["nodes"] = []

        for node in sorted_nodes:
            if node[0] not in assigned_nodes:
                transformed_graph["nodes"].append(node)
                assigned_nodes.append(node[0])


