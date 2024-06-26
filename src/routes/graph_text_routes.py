from flask import render_template, request, url_for, redirect, flash

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

    if len(request.form.get("text", "")) or request.files.getlist(form.file.name)[0]:
        docname = GraphTextService.generate_graph(
            {**request.form.to_dict(), **{"apply_prep": form.apply_prep.data, "steps_preprocessing": form.steps_preprocessing.data}}, 
            request.files.getlist(form.file.name)[0]
        )

        if not docname:
            return redirect(url_for("graph_form"))
        
        return redirect(url_for("graph_plot", docname=docname))

    else:
        flash("Por favor ingresa una entrada de texto", "warning")
    
    return redirect(url_for("graph_form"))

@app.route('/graph-plot/<docname>', methods=["GET"])
def graph_plot(docname):
    text_graph = GraphTextService.get_text_graph(docname)
    original_text = GraphTextService.get_original_text(docname)
    
    return render_template("graph_plot.html", **locals())