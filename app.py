from src import app
from src.routes.graph_text_routes import *
  
  
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 6000, debug = True)