from src.constants import GRAPH_OUTPUT_DIRECTORY, COOCURRENCE, HETEROGENEUS
from text2graphapi.text2graphapi.src.Cooccurrence import Cooccurrence
from src.models.plot_options import PlotOptions, NodeOptions, NodesLabelsOptions, EdgesOptions, EdgeLabelsOptions




class PlotManager:
    @staticmethod
    def generate_plot_image(graph: Cooccurrence, transformed_graph: dict, plot_options: dict, docname: str, graph_type: str) -> None:
        plot_settings = PlotManager._build_plot_options(transformed_graph, plot_options, graph_type)
        graph.plot_graph(transformed_graph["nx_graph"], f"{GRAPH_OUTPUT_DIRECTORY}{docname}.png", plot_settings.__dict__)
    
    @staticmethod
    def _build_plot_options(transformed_graph: dict, plot_options: dict, graph_type: str) -> PlotOptions:
        nodes_labels = {}

        for node in sorted(transformed_graph.get("nodes",[]), key=lambda tup: tup[0]):
            nodes_labels[node[0]] = f"{node[0]}\n<{node[1].get('pos_tag','')}>"
        
        nodes_colors = [degree[1] / 10 for degree in sorted(transformed_graph["nx_graph"].degree(), key=lambda tup: tup[0])]

        edge_prefix = "tfidf" if graph_type == HETEROGENEUS else "freq"
        edge_labels = dict([((nodes_labels[edge_from], nodes_labels[edge_to]), f"{edge_prefix}={frequency.get(edge_prefix)}") for edge_from, edge_to, frequency in transformed_graph.get("edges",[])])
        edge_colors = [0.1] * len(transformed_graph.get("edges",[]))

        if graph_type == COOCURRENCE:
            edge_colors = [int((edge_labels[(nodes_labels[edge_from], nodes_labels[edge_to])]).replace(f"{edge_prefix}=","")) / 10 for edge_from, edge_to in transformed_graph["nx_graph"].edges() if edge_labels[(nodes_labels[edge_from], nodes_labels[edge_to])]]

        node_options = NodeOptions(
            node_color=nodes_colors,
            node_size=plot_options.get("node_size", 200)
        )
        nodes_labels_options = NodesLabelsOptions(
            font_size=plot_options.get("font_size", 4)
        )
        edges_options = EdgesOptions(
            edge_color=edge_colors,
            arrows=plot_options.get("arrows"),
            arrowsize=plot_options.get("arrowsize"),
            arrowstyle=plot_options.get("arrowstyle"),
        )
        edge_labels_options = EdgeLabelsOptions(
            font_size=plot_options.get("font_size", 4)
        )

        return PlotOptions(
            nodes_labels=nodes_labels,
            edge_labels=edge_labels,
            nodes_options=node_options.__dict__,
            nodes_labels_options=nodes_labels_options.__dict__,
            edges_options=edges_options.__dict__,
            edges_labels_options=edge_labels_options.__dict__,
        )


