from text2graphapi.text2graphapi.src.Cooccurrence import Cooccurrence
from text2graphapi.text2graphapi.src.Heterogeneous import Heterogeneous
import nltk
nltk.download('omw-1.4')

class Text2GraphApiconnector:
    @staticmethod
    def get_test():
        corpus_docs = [
            {'id': 1, 'doc': "The sun was shining, making the river look bright and happy."},
            {'id': 2, 'doc': "Even with the rain, the sun came out a bit, making the wet river shine."}
        ]

        to_word_coocc_graph = Cooccurrence(graph_type = 'DiGraph', 
            language = 'en', 
            window_size = 3, output_format = 'adj_matrix')
        to_word_coocc_graph_transformed = to_word_coocc_graph.transform(corpus_docs)

        return to_word_coocc_graph_transformed

    @staticmethod
    def get_coocurrence_graph(graph_options: dict) -> Cooccurrence:
        coocurrence_graph = Cooccurrence(
            graph_type='DiGraph', 
            language=graph_options.get('language','sp'), 
            apply_prep=graph_options.get('apply_prep',True), 
            steps_preprocessing=graph_options.get('steps_preprocessing',[]),
            window_size=int(graph_options.get('window_size',20)),
            output_format='adj_matrix'
        )
        return coocurrence_graph

    @staticmethod
    def get_heterogeneus_graph(graph_options: dict) -> Heterogeneous:
        to_hetero_graph = Heterogeneous(
            graph_type = 'Graph', 
            language=graph_options.get('language','sp'), 
            apply_prep=graph_options.get('apply_prep',True), 
            steps_preprocessing=graph_options.get('steps_preprocessing',[]), 
            window_size=int(graph_options.get('window_size',20)),
            output_format = 'networkx'
        )
        return to_hetero_graph

    @staticmethod
    def get_transformed_text(coocurrence_graph:Cooccurrence, corpus_docs: list) -> list:
        coocurrence_graph_transformed = coocurrence_graph.transform(corpus_docs)

        return coocurrence_graph_transformed