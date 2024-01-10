from flask import Flask, request, jsonify
import stanza

nlp = stanza.Pipeline("en", processors="tokenize")

app = Flask(__name__)


@app.route("/")
def action_index():
    return "Hello, World!"


@app.route("/sentence_segmentation", methods=["POST"])
def action_sentences_segment():
    doc = nlp(request.get_json()["document"])
    return jsonify({"sentences": [sentence.text for sentence in doc.sentences]})
