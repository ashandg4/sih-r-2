from flask import Flask, request, jsonify, render_template
import serial

app = Flask(__name__)

# Open serial connection to Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your port


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.json.get('command')
    if command:
        ser.write(command.encode())
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "No command provided"}), 400


if __name__ == '__main__':
    app.run(debug=True)
