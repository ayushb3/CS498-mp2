from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def handle_request():
    if request.method == "POST":
        # Run stress_cpu.py in a separate process
        subprocess.Popen(["python3", "stress_cpu.py"])

        return jsonify({"message": "Stress CPU process initiated successfully."})

    elif request.method == "GET":
        # Get private IP address of the EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({"private_ip": private_ip})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
