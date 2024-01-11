from flask import Flask, request, jsonify, abort
import os
import stanza

secret_key = os.getenv("SECRET_KEY", "")

nlp = stanza.Pipeline("en", processors="tokenize", download_method=None)

app = Flask(__name__)


def guard_secret_key():
    if request.args.get("secret_key", "") == secret_key:
        return
    if request.headers.get("X-Secret-Key", "") == secret_key:
        return
    abort(401)


@app.route("/")
def action_index():
    return "Hello, World!"


@app.route("/sentence_segmentation", methods=["POST"])
def action_sentences_segment():
    guard_secret_key()
    doc = nlp(request.get_json()["document"])
    return jsonify({"sentences": [sentence.text for sentence in doc.sentences]})
