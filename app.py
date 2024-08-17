from flask import Flask, render_template, request, jsonify
from chatbot.chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    bot_response = bot.get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
