from flask import Flask, request, jsonify
import telebot

app = Flask(__name__)
TOKEN = "7814956770:AAHoGClD3648kZ0-Ti_6EXvbs5C9gTB2jng"
bot = telebot.TeleBot(TOKEN)
ADMIN_ID = 5880561408

responses = {}

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if str(message.chat.id) == str(ADMIN_ID):
        parts = message.text.split(':',1)
        if len(parts) == 2:
            link_id, reply = parts
            responses[link_id.strip()] = reply.strip()
            bot.send_message(ADMIN_ID, f"✔ الرد تم تخزينه للربط: {link_id.strip()}")

bot.polling(non_stop=True, timeout=60)

@app.route('/send_link', methods=['POST'])
def send_link():
    data = request.get_json()
    link = data.get('link')
    link_id = str(hash(link))[-6:] 
    bot.send_message(ADMIN_ID, f"🔗 رابط جديد:
{link}
ID: {link_id}")
    for _ in range(10):
        if link_id in responses:
            reply = responses.pop(link_id)
            return jsonify({"reply": reply})
    return jsonify({"reply": "❗ لم يصل رد الإدارة بعد. الرجاء إعادة المحاولة لاحقاً."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)