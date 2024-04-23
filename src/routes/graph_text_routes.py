from src import app
from src.services.graph_text_service import GraphTextService
  
@app.route('/')
def test():
    return str(GraphTextService.get_test())