from flask import Flask, render_template, request, jsonify

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

#we are returning this response but we dont want to print it
    for step in range(5):
        #encode the new user input, add the eos_token and return a tesor in pytorch
        new_user_input_ids = tokenizer.encode(str(text)) + tokenizer.eos_token, return_tensor = 'pt')

        #append the new user iunput tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_ids], dim = -1) if step > 0 else new_user_input_ids

        #generated a response while limiting the total chat history to 1000 tokens
        chat_history_ids = model.generate(bot_input_ids, max_length = 1000, pad_token_id=tokenizer.eos_token_id)

        #pretty print last output tokens from bot
        return tokenizer.decode(chat_history_ids[:,bot_input_ids[-1]:][0],skip_special_tokens=True)

if __name__ == "__main__":
      app.run()




