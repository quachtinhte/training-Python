import requests

def RequestData():
    req = requests.get("http://ktmt.github.io/blog/archives/")

    result = req.content.decode()

    with open('ktmt.github.io.html', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    RequestData()