from flask import Flask, jsonify
from datetime import datetime
import platform
import socket

app = Flask(__name__)

@app.route('/')
def home():

    hostname = socket.gethostname()
    os_name = platform.system()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <html>
    <head>
        <title>Lightweight DevOps Project</title>

        <style>
            body {{
                background-color: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }}

            .container {{
                background: #1e293b;
                width: 60%;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
            }}

            h1 {{
                color: #38bdf8;
            }}
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 Lightweight DevOps Project</h1>

            <p>Application Running Successfully ✅</p>

            <p><b>Hostname:</b> {hostname}</p>

            <p><b>Operating System:</b> {os_name}</p>

            <p><b>Current Time:</b> {current_time}</p>

        </div>

    </body>
    </html>
    """

    return html


@app.route('/health')
def health():
    return jsonify({
        "status": "running"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
