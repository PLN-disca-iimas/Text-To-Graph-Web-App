import uuid
from werkzeug.datastructures import FileStorage

from src import exception_handler
from src.constants import GRAPH_OUTPUT_DIRECTORY, COOCURRENCE, HETEROGENEUS
from src.connectors.text_2_graph_api import Text2GraphApiconnector
from src.managers.plot_manager import PlotManager
from src.managers.file_manager import FileManager




class GraphTextService:
    @staticmethod
    @exception_handler
    def get_test():
        return Text2GraphApiconnector.get_test()

    @staticmethod
    # @exception_handler
    def generate_graph(graph_data: dict, file: FileStorage) -> str:
        docname = GraphTextService._get_random_docname()
        graph = GraphTextService.get_graph_by_type(graph_data.get("model", ""), graph_data)

        if not graph:
            return ""

        if file:
            graph_data['text'] = GraphTextService.read_upload_text_file(file)

        transformed_text = Text2GraphApiconnector.get_transformed_text(graph, [{"id": 1, "doc": graph_data.get("text", "")}])
        PlotManager.generate_plot_image(graph, transformed_text[0], graph_data, docname, graph_data.get("model", ""))
        FileManager.write_file(str(transformed_text), f"{GRAPH_OUTPUT_DIRECTORY}{docname}.txt")
        FileManager.write_file(str(transformed_text[0].get("prep_text")), f"{GRAPH_OUTPUT_DIRECTORY}{docname}_.txt")

        return docname
    
    @staticmethod
    @exception_handler
    def get_original_text(docname: str) -> str:
        return FileManager.read_file(f"{GRAPH_OUTPUT_DIRECTORY}{docname}_.txt")

    @staticmethod
    @exception_handler
    def get_text_graph(docname: str) -> str:
        return FileManager.read_file(f"{GRAPH_OUTPUT_DIRECTORY}{docname}.txt")
    
    @staticmethod
    @exception_handler
    def _get_random_docname():
        return str(uuid.uuid4())
    
    @staticmethod
    @exception_handler
    def read_upload_text_file(file: FileStorage) -> str:
        if not file.filename:
            return ""
        
        return file.stream.read().decode("utf-8")
    
    @staticmethod
    @exception_handler
    def get_graph_by_type(graph_model: str, graph_data: dict):
        GRAPH_TYPES_FUNCTIONS = {
            COOCURRENCE: Text2GraphApiconnector.get_coocurrence_graph(graph_data),
            HETEROGENEUS: Text2GraphApiconnector.get_heterogeneus_graph(graph_data)
        }

        graph = GRAPH_TYPES_FUNCTIONS.get(graph_model)

        return graph