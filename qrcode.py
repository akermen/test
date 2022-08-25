import requests
from datetime import datetime
now = datetime.now()

# qr code okuma kodu buraya gelecek!

# qr code degeri bu degiskene yazilacak!
qrcode_opncv_ile_okunan = "opencv-qrcode-12345"

# qr code kaydet
r = requests.post(
    "http://127.0.0.1:5000/qrcodes",
    data={
        'code': qrcode_opncv_ile_okunan,
        'title': 'deneme3',
        'date': '%s' % now,
    })

print(r.text)

# qr code listesini iste
r = requests.get("http://127.0.0.1:5000/qrcodes")
print(r.text)
