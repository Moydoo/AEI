from flask import Flask, jsonify, render_template
from text_extractor import get_all_text_info
import logging, math

logger = logging.getLogger("flaskAEI")
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
text_infos = {}
targets_map = {
    "Sprawca": tuple((["człowiek", "dziecko", "czytelnik", "dorosły"], 0.1)),
    "Zdarzenie": tuple((["czytać", "myślenie", "badanie"], 0.3)),
    "Narzędzie": tuple((["lektura", "słowo", "informacja", "mózg", "umysł"], 0.2)),
    "Obiekt": tuple((["bohater", "książka", "tekst"], 0.1)),
    "Cel": tuple((["wiedza", "czytanie", "umiejętność"], 0.3))
}


@app.route("/textInfos/<text_name>")
def single_text_info(text_name):
    return render_template("single_text.html", text_name = text_name, single_text_text=text_infos[text_name]['text'], single_text_accuracy=text_infos[text_name]['accuracy'], single_text_target=text_infos[text_name]['target_words'])

@app.route("/roles")
def roles():
    return render_template("roles.html")

@app.route("/scales")
def scales():
    return render_template("scales.html")

@app.route("/textInfos")
def all_texts_info():
    text_accuracies = {}
    for text, values in text_infos.items():
        text_accuracies[text] = values["accuracy"]
    sorted_text_accuracies = sorted(text_accuracies.items(), key=lambda x: x[1], reverse=True)
    return render_template("all_texts.html", infos=sorted_text_accuracies)


@app.route("/")
def default():
    return render_template("index.html")


if __name__ == "__main__":
    text_infos = get_all_text_info(targets_map)
    app.run(host="0.0.0.0", use_reloader=False, port=5022)
