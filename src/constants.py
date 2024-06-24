ROOT_ABSOLUTE_PATH = "/home/diego/proyects/Text-To-Graph-Web-App"
GRAPH_OUTPUT_DIRECTORY = "src/static/outputs/graphs/"

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
GRAPH_TYPES = [
    (COOCURRENCE, "Coocurrencia"),
    (HETEROGENEUS, "Heterogenea")
]
NODE_CATEGORY_COLORS = {
    "NOUN": 1,
    "PROPN": 2,
    "VERB": 3,
    "X": 4,
    "ADJ": 5,
    "ADP": 6
}
