from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
CORS(app)

KST = timezone(timedelta(hours=9))


@app.route("/api/secom/v1/ping")
def ping():
    now = datetime.now(KST).strftime("%Y%m%dT%H%M%S+0900")
    return jsonify(lastPrivateInteractionTime=now)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8767)
