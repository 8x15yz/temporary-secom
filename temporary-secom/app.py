## ecs secom proxy server -> "https://ecs-secom.bmap.kr"

from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins=[
    "https://ecs.bluemap.co.kr",
    "https://ecs-secom.bmap.kr",
    "http://localhost:8080",   # 추가
])

TARGET = "https://weather-api.bmap.kr"


@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def proxy(path):
    url = f"{TARGET}/{path}"
    resp = requests.request(
        method=request.method,
        url=url,
        params=request.args,
        headers={k: v for k, v in request.headers if k.lower() != "host"},
        data=request.get_data(),
    )
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get("Content-Type"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
