import logging
import os
from flask import Flask, render_template, url_for, request, redirect, flash

from email_validator import validate_email, EmailNotValidError
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

# Flask 클래스를 인스턴스화한다
app = Flask(__name__)

# SECRET_KEY를 추가한다
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

# 로그 레벨을 설정한다
app.logger.setLevel(logging.DEBUG)

# 리다이렉트를 중단하지 않도록 한다
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# Mail 클래스의 컨피그를 추가한다
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# DebugToolbarExtension에 애플리케이션을 세트한다
toolbar = DebugToolbarExtension(app)
# app.debug = True

# flask-mail 확장을 등록한다
mail = Mail(app)


# URL과 실행하는 함수를 매핑한다
# '127.0.0.1:5000/'
@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}"


# show_name 엔드포인트를 작성한다
@app.route("/name/<name>")
def show_name(name):
    # 변수를 템플릿 엔진에게 건넨다
    return render_template("index.html", name=name)


@app.route("/light_check/<command>", methods=["GET", "POST"])
def light_check(command):
    # 변수를 템플릿 엔진에게 건넨다
    return render_template("light_check.html", command=command)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/AK?page=1
    print(url_for("show_name", name="AK", page="1"))
    print(url_for("show_name", name=""))


with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    # 내용 보내기라면...
    if request.method == "POST":
        # 메일 보내기 구현
        # TODO

        # form 속성을 사용해서 폼의 값을 취득한다
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        print("username :", username)
        print("email :", email)
        print("description :", description)

        # 입력 체크
        is_valid = True

        if not username:
            flash("사용자명은 필수입니다")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다")
            is_valid = False

        # 이메일이 유효한지 체크
        try:
            # validate_email 함수가 실행되고 메일이
            # 유효하지 않으면 except로 이동한다.
            validate_email(email)
        except EmailNotValidError as e:
            flash("메일 주소의 형식으로 입력해 주세요")
            flash(str(e))
            is_valid = False
            print("EmailNotValidError :", str(e))

        if not description:
            flash("문의 내용은 필수입니다")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # 메일을 보낸다
        send_email(
            email,
            "문의 감사합니다.",
            "contact_mail",
            username=username,
            description=description,
        )
        # 문의 완료 엔드포인트로 리다이렉트한다
        flash("문의 내용은 메일로 송신했습니다. 문의해 주셔서 감사합니다.")

        # contact_complete 엔드포인트로 redirect한다.
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")


# 메일을 송신하는 함수
# 인수 : 누구에게, 제목, 내용
def send_email(to, subject, template, **kwargs):
    """메일을 송신하는 함수"""
    # 메일을 어떤 제목으로, 누구에게 보낼지 설정
    msg = Message(subject, recipients=[to])
    # 메일 내용을 txt로 생성
    msg.body = render_template(template + ".txt", **kwargs)
    # 메일 내용을 html로 생성
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)
