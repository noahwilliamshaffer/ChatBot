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

def get_chat_response(Text)
#lets chat 5 lines
for step in range(5):
    #encode the new user input, add the eos_token and return a tesor in pytorch
    new_user_input_ids = tokenizer.encode(input(">>user:")) + tokenizer.eos_token, return_tensor = 'pt')

    #append the new user iunput tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_ids], dim = -1) if step > 0 else new_new_user_input_ids

    #generated a response while limiting the total chat history to 1000 tokens
    chat_history_ids = model.generate(bot_input_ids, max_length = 1000, pad_token_id=tokenizer.eos_token_id)




