from src.connectors.text_2_graph_api import Text2GraphApiconnector

class GraphTextService:
    @staticmethod
    def get_test():
        return Text2GraphApiconnector.get_test()