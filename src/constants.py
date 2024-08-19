GRAPH_OUTPUT_DIRECTORY = "src/static/outputs/graphs/"

GRAPH_TYPES = [
    ("Graph", "Graph"), 
    ("DiGraph", "DiGraph"), 
    ("MultiGraph", "MultiGraph"), 
    ("MultiDiGraph", "MultiDiGraph")
]
ARROW_STYLES = [
    ("-", "Curve"),
    ("->", "CurveB"),
    ("-[", "BracketB"),
    ("-|>", "CurveFilledB"),
    ("<-", "CurveA"),
    ("<->", "CurveAB"),
    ("<|-", "CurveFilledA"),
    ("<|-|>", "CurveFilledAB"),
    ("]-", "BracketA"),
    ("]-[", "BracketAB"),
    ("fancy", "Fancy"),
    ("simple", "Simple"),
    ("wedge", "Wedge"),
    ("|-|", "BarAB"),
]
COOCURRENCE = "Coocurrence"
HETEROGENEUS = "Heterogeneus"
GRAPH_MODELS = [
    (COOCURRENCE, "Coocurrencia"),
    (HETEROGENEUS, "Heterogenea")
]
AVAILABLE_LANGUAGES = [
    ("sp", "Español"),
    ("en", "English"),
    ("fr", "Francais")
]
AVAILABLE_PREPROCESSORS = [
    ("handle_blank_spaces", "Manejar espacios en blanco"),
    ("handle_non_ascii", "No ASCII"),
    ("handle_emoticons", "Manejar emoticons"),
    ("handle_html_tags", "Manejar etiquetas HTML"),
    ("handle_negations", "Manejar negaciones"),
    ("handle_contractions", "Manejar contracciones"),
    ("handle_stop_words", "Manejar palabras de pausa"),
    ("to_lowercase", "Texto a minúsculas"),
]
NODE_CATEGORY_COLORS = {
    "NOUN": 1,
    "PROPN": 2,
    "VERB": 3,
    "X": 4,
    "ADJ": 5,
    "ADP": 6,
    "SPACE": 7,
    "CCONJ": 8,
}
