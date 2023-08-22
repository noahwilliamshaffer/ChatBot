import flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template('chat.html')

@app.route("get", methods = ["GET","POST"]
def chat():
    msg = request.form("msg")
    input = msg
    return get_chat_response(input)


    
