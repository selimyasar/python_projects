import urllib.request

fliphtml5 = "https://online.fliphtml5.com/vnyxe/gegm"

for i in range(1,252):
    Links = f"{fliphtml5}/files/large/{i}.jpg"
    # print(Links)
    urllib.request.urlretrieve(Links)