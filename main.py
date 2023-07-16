from urllib.request import urlopen

if '__main__':
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
