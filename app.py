from flask import Flask, jsonify, render_template
import uuid

app = Flask(__name__)

def get_mac_address():
    try:
        mac_address = hex(uuid.getnode()).replace("0x", "").zfill(12)
        formatted_mac = ":".join(mac_address[i:i+2] for i in range(0, len(mac_address), 2))
        return formatted_mac
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def home():
    return render_template('index.html')  # Load the frontend HTML page

@app.route('/get-mac-address', methods=['GET'])
def fetch_mac_address():
    mac_address = get_mac_address()
    return jsonify({"mac_address": mac_address})  # Send MAC address to the client

if __name__ == '__main__':
    app.run(debug=True)
