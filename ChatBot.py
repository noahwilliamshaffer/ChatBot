import flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template('chat.html')