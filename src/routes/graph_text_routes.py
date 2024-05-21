from flask import render_template, request, url_for, redirect

from src import app
from src.services.graph_text_service import GraphTextService
from src.models.base_graph import BaseGraphForm
  
@app.route('/test/', methods=["GET"])
def test():
    return str(GraphTextService.get_test())
  
@app.route('/', methods=["GET"])
def index():
    return redirect(url_for("graph_form"))
  
@app.route('/graph-form/', methods=["GET"])
def graph_form():
    form = BaseGraphForm(meta={"csrf": False})
    return render_template("graph_form.html", **locals())

@app.route('/generate-graph/', methods=["POST"])
def generate_graph():
    form = BaseGraphForm(meta={"csrf": False})

    if form.validate_on_submit():
        docname = GraphTextService.generate_graph(request.form.to_dict(), request.files.getlist(form.file.name)[0])

        if not docname:
            return redirect(url_for("graph_form"))
        
        return redirect(url_for("graph_plot", docname=docname))

    else:
        print(form.__dict__)
    
    return "ko"

@app.route('/graph-plot/<docname>', methods=["GET"])
def graph_plot(docname):
    original_text = GraphTextService.get_original_text(docname)
    
    return render_template("graph_plot.html", **locals())