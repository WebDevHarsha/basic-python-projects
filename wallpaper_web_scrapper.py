import requests
from PIL import Image
from io import BytesIO
import random
from bs4 import BeautifulSoup

unsplash_url = "https://www.google.com/search?q=wallpaper+for+laptop&tbm=isch&ved=2ahUKEwiE4IyKqoaCAxXyXmwGHZsnAv4Q2-cCegQIABAA&oq=wallpaper+for+laptop&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6CggAEIoFELEDEEM6BwgAEIoFEEM6CQgAEBgQgAQQClDbBViZGWD4H2gBcAB4AIABugGIAdALkgEDNS44mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=71YzZcSsC_K9seMPm8-I8A8&bih=601&biw=1280"

response = requests.get(unsplash_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    random_image = random.choice(images)
    image_url = random_image['src']
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        image = Image.open(BytesIO(image_response.content))
        image.save("downloaded_wallpaper.jpg")
        print("Wallpaper downloaded successfully!")
    else:
        print("Failed to download the wallpaper. Status code:", image_response.status_code)
else:
    print("Failed to access Unsplash. Status code:", response.status_code)
