from datetime import datetime

now = datetime.now()

# odev: strftime tarih ve saat format kisaltmalari
# yil-ay-gun-saat-dakika-saniye.jpg
file_name = now.strftime('%Y-%m')

with open(file_name + '.jpg', "w+") as f:
    f.write("deneme")

print(file_name)
print('done.')

