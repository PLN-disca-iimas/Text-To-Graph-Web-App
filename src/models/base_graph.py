from pydantic import BaseModel
from typing import Optional
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import TextAreaField, IntegerField, SelectField, BooleanField, SelectMultipleField, validators

from src.constants import GRAPH_TYPES, ARROW_STYLES, AVAILABLE_LANGUAGES, AVAILABLE_PREPROCESSORS


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
    language = SelectField("Lenguaje", coerce=str, choices=AVAILABLE_LANGUAGES, default=AVAILABLE_LANGUAGES[0])
    window_size = IntegerField("Tamaño de la ventana", default=20)
    apply_prep = BooleanField("Aplicar Pre-procesamientos", default=True)
    steps_preprocessing = SelectMultipleField("Pre-procesamientos para aplicar (Mantén presionado ctrl/cmd para seleccionar mas de uno)", coerce=str, choices=AVAILABLE_PREPROCESSORS)
    node_size = IntegerField("Tamaño del nodo (50 - 700)", default=None)
    font_size = IntegerField("Tamaño del texto del nodo (2 - 10)", default=None)
    arrowsize = IntegerField("Tamaño de las flechas  (2 - 10)", default=None)
    arrowstyle = SelectField("Estilo de la flechas", coerce=str, choices=ARROW_STYLES, default=ARROW_STYLES[0])