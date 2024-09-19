from flask import render_template, request, url_for, redirect, flash

from src import app
from src.services.graph_text_service import GraphTextService
from src.models.base_graph import BaseGraphForm

@app.route('/test/', methods=["GET"])
def test():
    """
    Route that returns the result of the 'get_test' method from the GraphTextService.

    Returns:
        str: The result of the 'get_test' method.
    """
    return str(GraphTextService.get_test())

@app.route('/', methods=["GET"])
def index():
    """
    Route that redirects to the 'graph_form' route.

    Returns:
        redirect: Redirects to the 'graph_form' route.
    """
    return redirect(url_for("graph_form"))

@app.route('/graph-form/', methods=["GET"])
def graph_form():
    """
    Route that renders the graph form template.

    Returns:
        render_template: The rendered template with the necessary variables.
    """
    form = BaseGraphForm(meta={"csrf": False})
    return render_template("graph_form.html", **locals())

@app.route('/generate-graph/', methods=["POST"])
def generate_graph():
    """
    Route that generates a graph based on the form data and file uploaded.

    Returns:
        redirect: Redirects to the 'graph_form' route if the graph generation fails, 
                  otherwise redirects to the 'graph_plot' route with the generated graph's document name.
    """
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
    """
    Route that renders the graph plot template and passes the necessary variables for displaying the graph.

    Args:
        docname (str): The name of the document.

    Returns:
        render_template: The rendered template with the necessary variables.
    """
    graph_code = GraphTextService.get_graph_code(docname)
    text_graph = GraphTextService.get_text_graph(docname)
    original_text = GraphTextService.get_original_text(docname)
    
    return render_template("graph_plot.html", **locals())