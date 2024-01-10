from flask import Flask, request, jsonify
import os
import stanza

os.makedirs(os.getenv("STANZA_RESOURCES_DIR", "/tmp/stanza_resources"), exist_ok=True)

nlp = stanza.Pipeline("en", processors="tokenize")

app = Flask(__name__)


@app.route("/")
def action_index():
    return "Hello, World!"


@app.route("/sentence_segmentation", methods=["POST"])
def action_sentences_segment():
    doc = nlp(request.get_json()["document"])
    return jsonify({"sentences": [sentence.text for sentence in doc.sentences]})
