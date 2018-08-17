import requests
import tesserocr
from PIL import Image

session = requests.Session()

def download_and_check_image():
    image_url = 'http://www.hebeieb.com/admin/captcha.htm'
    response = session.get(image_url)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('code.png')
    image = image.convert('L')
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    captcha = tesserocr.image_to_text(image).strip()
    return captcha

def judge_captcha_is_num():
    while True:
        captcha = download_and_check_image()
        try:
            int(captcha)
            b = True
        except:
            b = False
        print(b)
        if b:
            return captcha

def login():
    url = 'http://www.hebeieb.com/admin/login.do'
    data = {
        'name':'biao800',
        'password':'xxxxxxx',
        'captcha':judge_captcha_is_num(),
    }
    response = session.post(url,data=data)
    if '/pubsev/index' in response.text:
        return response.request.headers['Cookie']
    else:
        return login()

def write_cookie():
    cookie = login()
    with open('hebei_cookie.txt', 'w') as f:        
        f.write(cookie)
        
if __name__ == '__main__':
    write_cookie()
