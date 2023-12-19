from flask import Flask, render_template, request, jsonify


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import vertexai

from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part,
)

# GCP 초기 설정
PROJECT_ID = "gcp-test-407507"  # os.environ.get('PROJECT_ID')  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}
# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

model = GenerativeModel("gemini-pro")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    prompt = request.form["msg"]

    chat = model.start_chat()

    # prompt = """My name is Ned. You are my personal assistant. My favorite movies are Lord of the Rings and Hobbit.

    # Suggest another movie I might like.
    # """

    responses = chat.send_message(prompt, stream=True)

    FullText = ""
    for response in responses:
        # print(response.text, end="")
        FullText += "{}".format(response.text)

    print(FullText)
    # return get_Chat_response(input)

    return FullText


# def get_Chat_response(text):
#     # Let's chat for 5 lines
#     for step in range(5):
#         # encode the new user input, add the eos_token and return a tensor in Pytorch
#         new_user_input_ids = tokenizer.encode(
#             str(text) + tokenizer.eos_token, return_tensors="pt"
#         )

#         # append the new user input tokens to the chat history
#         bot_input_ids = (
#             torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
#             if step > 0
#             else new_user_input_ids
#         )

#         # generated a response while limiting the total chat history to 1000 tokens,
#         chat_history_ids = model.generate(
#             bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
#         )

#         # pretty print last ouput tokens from bot
#         return tokenizer.decode(
#             chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
#         )


if __name__ == "__main__":
    app.run()
