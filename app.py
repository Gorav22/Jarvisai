from flask import Flask, render_template, jsonify, request
from Agent import run_conversation
from flask_ngrok import run_with_ngrok

app=Flask(__name__)
run_with_ngrok(app)

app = Flask(__name__)

@app.route("/process_message",methods=["POST"])
def process_message_func1():
    msg=request.json['message']
    print("we are getting",msg)
    resp=run_conversation(msg)
    return jsonify({"response":resp})



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()