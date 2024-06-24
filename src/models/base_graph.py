from pydantic import BaseModel
from typing import Optional
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import TextAreaField, IntegerField, SelectField, validators

from src.constants import GRAPH_TYPES, ARROW_STYLES


class BaseGraph(BaseModel):
    text: str
    file: Optional[str]
    node_size: int
    font_size: int
    arrowsize: int
    arrowstyle: Optional[str]



def validate_text_file(form, field):
    if not field.data: 
        return
    
    file_path = field.data.filename

    if file_path.split(".")[1] != "txt":
        raise validators.ValidationError('Only .txt files are accepted')

class BaseGraphForm(FlaskForm):
    type = SelectField("Tipo de gráfico", coerce=str, choices=GRAPH_TYPES, default=GRAPH_TYPES[0])
    text = TextAreaField("Texto a graficar")
    file = FileField("O también puedes cargar archivo de texto", [validate_text_file])
    node_size = IntegerField("Tamaño del nodo (50 - 700)", default=None)
    font_size = IntegerField("Tamaño del texto del nodo (2 - 10)", default=None)
    arrowsize = IntegerField("Tamaño de las flechas  (2 - 10)", default=None)
    arrowstyle = SelectField("Estilo de la flechas", coerce=str, choices=ARROW_STYLES, default=ARROW_STYLES[0])