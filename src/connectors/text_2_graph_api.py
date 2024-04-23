from text2graphapi.text2graphapi.src.Cooccurrence import Cooccurrence
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