# OS : Linux-5.15.0-91-generic-x86_64-with-glibc2.31
# Python : 3.9.18
# Flask : 3.0.0
# google-cloud-aiplatform : 1.38.1
# Created: Jan. 10. 2024
# Author: D.W. SHIN


import os

import vertexai
from markdown import markdown
from vertexai.language_models import ChatModel, InputOutputTextPair

from flask import Flask, jsonify, render_template, request

# Vertex AI parameter
PROJECT_ID = os.environ.get("PROJECT_ID")
LOCATION = os.environ.get("LOCATION")

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)


model = ChatModel.from_pretrained("chat-bison")

# chat_model = model.start_chat(
#     context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
#     examples=[
#         InputOutputTextPair(
#             input_text="How many moons does Mars have?",
#             output_text="The planet Mars has two moons, Phobos and Deimos.",
#         ),
#     ],
# )

chat_model = model.start_chat(
    context="You are a helpful assistant who is good at large language models.",
    examples=[
        InputOutputTextPair(
            input_text="Please list three representative keywords for what LLM can do.",
            output_text="Three representative keywords for what LLM can do are: Language Generation, Information Retrieval, Summarization",
        ),
    ],
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    query = request.form["msg"]

    parameters = {
        # "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0,
        "top_p": 1,
    }

    response = chat_model.send_message(
        query,
        **parameters,
    )

    print(chat_model.message_history)
    print(len(chat_model.message_history))

    return markdown(response.text, extensions=["extra"])


if __name__ == "__main__":
    app.run()
