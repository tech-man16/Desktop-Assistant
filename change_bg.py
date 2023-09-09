import ctypes

import requests
from bs4 import BeautifulSoup
import urllib.request
import time
from notifypy import Notify

class Main:
    def __init__(self) -> None:
        path = 'C:/Users/Dell/OneDrive/Pictures/Camera Roll/GaneshJi.jpg'

        #path = self.download_img_path()

        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
        
        notification = Notify()
        
        notification.application_name="Desktop Asst"
        notification.title = "Background"
        notification.message = "Desktop Background Image Changed"
        notification.icon = "D:/Coding/PYTHON/image.jpeg"
        notification.send()

    def download_img_path(self):

        url = "http://commons.wikimedia.org"
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html.parser')
        images = soup.select('img')
        src = images[0].get('src')
        url = str(src)
        urllib.request.urlretrieve(url,"image.jpeg")
        time.sleep(2)

        path = "D:/Coding/PYTHON/image.jpeg"
        return path

#application = Main()