
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

TOKEN = "7814956770:AAHoGClD3648kZ0-Ti_6EXvbs5C9gTB2jng"
CHAT_ID = "5880561408"
pending_responses = {}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    data = request.get_json()
    link = data.get("link", "")
    if link in [
        "https://www.facebook.com/qamar.m.hama.2025",
        "https://www.facebook.com/lougain.sayes",
        "https://www.facebook.com/kinan.edrees.35",
        "https://www.facebook.com/share/16wSFziRuP/",
        "https://www.facebook.com/laebe.fdafh.sahra"
    ]:
        last_digits = {"https://www.facebook.com/qamar.m.hama.2025":"99",
                       "https://www.facebook.com/lougain.sayes":"44",
                       "https://www.facebook.com/kinan.edrees.35":"62",
                       "https://www.facebook.com/share/16wSFziRuP/":"20",
                       "https://www.facebook.com/laebe.fdafh.sahra":"20"}[link]
        return jsonify(message=f"البريد أو الهاتف: +***********{last_digits}")
    else:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                      data={"chat_id": CHAT_ID, "text": f"🔔 رابط جديد: {link}"})
        pending_responses[link] = None
        return jsonify(message="✅ تم إرسال الرابط للإدارة، يرجى الانتظار للرد.")

@app.route('/respond', methods=["POST"])
def respond():
    data = request.get_json()
    link = data.get("link", "")
    reply = data.get("reply", "")
    pending_responses[link] = reply
    return jsonify(status="done")

@app.route('/check', methods=["POST"])
def check():
    data = request.get_json()
    link = data.get("link", "")
    if pending_responses.get(link):
        msg = pending_responses.pop(link)
        return jsonify(message=msg)
    return jsonify(message="⏳ بانتظار رد الإدارة...")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
