from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "📦 Parcel Status API running"

@app.route("/status")
def status():
    # Тут потім додамо реальний парсинг
    return jsonify({
        "status1": "W drodze do Wroclawia",
        "status2": "Doręczona odbiorcy"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
