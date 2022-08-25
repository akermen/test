from flask import jsonify
from flask import Flask
from flask import request

# __name__ : calistirilan modul adi
app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>qr code REST API</h3><p><a href='/qrcodes'>qrcodes list</a></p>"

# tum qr code listesi
# qrcodes = []
qrcodes = [
    {"code": "1234567890", "title": "Deneme", "date": "01.01.2022"}
]

@app.route("/qrcodes", methods=['GET'])
def rest_api_get_qrcodes():
    return jsonify(qrcodes)

@app.route("/qrcodes", methods=['POST'])
def rest_api_create_qrcodes():
    code = request.form.get('code')
    date = request.form.get('date')
    title = request.form.get('title')
    code = {"code": code, "title": title, "date": date}
    qrcodes.append(code)
    print(code)
    return " -- eklendi --"

@app.route("/qrcodes/<string:code>", methods=['GET'])
def rest_api_get_qrcode(code):
    for item in qrcodes:
        if item['code'] == code:
            found = item
            break
    if found:
        return jsonify(found)
    else:
        return "bulunamadi!"


if __name__ == '__main__':
    app.run(debug=True)
