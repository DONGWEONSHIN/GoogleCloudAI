## ChatBot 실행 및 사용 방법

### Chatbot 만들기

1. git에서 다운로드

```
git clone https://github.com/binary-hood/ChatBot.git
```

2. 가상환경 설정

```
conda create -n chatbot_venv phthon=3.9
```

3. 가상환경 접속

```
conda activate chatbot_venv
```

4. 필수 패키지 설치

```
pip install -r requirements.txt
```

5. 폴더로 이동

```
cd ChatBot
```

6. flask 실행

```
python app.py
```

### Gemini 로 모델 바꾸기

1. 참고 git 사이트
```
git clone https://github.com/GoogleCloudPlatform/generative-ai.git
```

2. 참고 자료
```
-> gemini/getting-started/intro_gemini_python.ipynb
```

3. google-cloud-aiplatform 패키지 설치
```
! pip3 install --upgrade --user google-cloud-aiplatform
```

4. gcloud 패키지 설치
```
https://cloud.google.com/sdk/docs/install?hl=ko
```

4.1. Pick cloud project to use: 

==> (현재 GCP 프로젝트 명 선택)

4.2. Do you want to configure a default Compute Region and Zone? (Y/n)? 

==> (Y)

4.3 Please enter numeric choice or text value (must exactly match list item):

==> ([7] us-central)

4.4 GCP 로그인
```
gcloud auth login
```

5. gcp project ID 확인 후 환경설정 하기
```
gcloud config set project {PROJECT_ID}
```

6. Vertex AI SDK - Install (Palm2)
```
!pip3 install google-cloud-aiplatform>=1.25 "shapely<2.0.0" --quiet
```


## 원본 출처
- https://github.com/binary-hood/ChatBot/tree/main





# ChatBot

## Installation & Setup

[Install Python] https://www.dataquest.io/blog/installing-python-on-mac/

[Install pip] https://phoenixnap.com/kb/install-pip-mac

If you have Python & pip installed then check their version in the terminal or command line tools

```
python3 --version
```

```
pip --version
```

## Installing Flask

In your terminal run the requirements.txt file using this pip

```
pip install -r requirements.txt
```


## Running ChatBot Application in Terminal

```
cd into your directory
```

```
python app.py
```



## What you will create

In this tutorial, I will guide you through the process of building a chatbot that can carry out conversations with users using natural language processing.

To start, we will be using Microsoft DialoGPT, a pre-trained language model that can generate human-like responses to given prompts. We will be integrating DialoGPT with Flask, a popular Python web framework, to create a web application that can communicate with users via a chat interface.

For the frontend of our application, we will be using HTML, CSS, and JavaScript to create a visually appealing and interactive chat interface. Additionally, we will be using jQuery to handle the HTTP requests that are made to the backend server.

Throughout the tutorial, I will provide step-by-step instructions on how to set up your development environment, install the necessary dependencies, and create the required files and code for the application. I will also explain how to train and fine-tune the DialoGPT model to improve the accuracy of its responses.

By the end of this tutorial, you will have a fully functional chatbot that can engage in conversations with users, and you will have gained valuable experience in using Microsoft DialoGPT, Flask, and web development technologies such as HTML, CSS, and JavaScript.

# ChatBot Link
The Chatbot is constructed using the Microsoft/DialoGPT-medium model.

```
https://huggingface.co/microsoft/DialoGPT-medium
```

# User-Html

```
var userHtml = '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' + user_input + '<span class="msg_time_send">'+ time + 
    '</span></div><div class="img_cont_msg"><img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg"></div></div>';
```

# Bot-HTML

```
var botHtml = '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' + bot_response + '<span class="msg_time">' + time + '</span></div></div>';
```
