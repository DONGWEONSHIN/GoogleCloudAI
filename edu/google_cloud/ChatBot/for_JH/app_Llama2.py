# OS : Linux-5.15.0-91-generic-x86_64-with-glibc2.31
# Python : 3.9.18
# Flask : 3.0.0
# ctransformers : 0.2.27
# Created: Jan. 15. 2024
# Author: D.W. SHIN


import os

from ctransformers import AutoModelForCausalLM
from markdown import markdown

from flask import Flask, jsonify, render_template, request

# local Llama2 7b model
llm = AutoModelForCausalLM.from_pretrained(
    "llama-2-7b-chat.Q2_K.gguf",
    model_type="llama",
)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    query = request.form["msg"]

    response = llm(query)

    return markdown(response, extensions=["extra"])


if __name__ == "__main__":
    app.run()
