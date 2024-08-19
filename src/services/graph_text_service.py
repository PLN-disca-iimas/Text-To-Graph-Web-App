import uuid
from werkzeug.datastructures import FileStorage

from src import exception_handler
from src.constants import GRAPH_OUTPUT_DIRECTORY, COOCCURRENCE, HETEROGENEUS, CODE_TEMPLATE_DIRECTORY
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
        graph_code = GraphTextService.generate_graph_code(graph_data)
        FileManager.write_file(graph_code, f"{GRAPH_OUTPUT_DIRECTORY}{docname}.py")

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
    def get_graph_code(docname: str) -> str:
        return FileManager.read_file(f"{GRAPH_OUTPUT_DIRECTORY}{docname}.py")
    
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
            COOCCURRENCE: Text2GraphApiconnector.get_coocurrence_graph(graph_data),
            HETEROGENEUS: Text2GraphApiconnector.get_heterogeneus_graph(graph_data)
        }
        graph = GRAPH_TYPES_FUNCTIONS.get(graph_model)

        return graph
    
    @staticmethod
    def generate_graph_code(graph_data: dict) -> str:
        code_template = FileManager.read_file(CODE_TEMPLATE_DIRECTORY)

        return code_template\
            .replace("&text&", graph_data['text'])\
            .replace("&model&", graph_data['model'])\
            .replace("&graph_type&", graph_data['graph_type'])\
            .replace("&language&", graph_data['language'])\
            .replace("&window_size&", graph_data['window_size'])\
            .replace("&apply_prep&", str(len(graph_data.get('steps_preprocessing',[])) > 0))\
            .replace("&steps_preprocessing&", str(graph_data['steps_preprocessing']))\
            .replace("&output_format&", graph_data['output_format'])
            