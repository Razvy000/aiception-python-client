from pprint import pprint

import requests

from aiception import artistic_image


# the secret token
token = "xxxxxxxxxxxxxxxxx"

# image of Morgan Freeman
image_url = "http://starsunfolded.1ygkv60km.netdna-cdn.com/wp-content/uploads/2016/06/Morgan-Freeman.jpg"

# style of Starry Night by Vincent van Gogh
style_url = "http://i.huffpost.com/gen/2299606/images/o-STARRY-NIGHT-facebook.jpg"

# patience ... it takes at least 55 seconds for the image to be ready
# redraw the image using the style
r = artistic_image(token, image_url, style_url)

pprint(r)


def download_image(image_url, image_name):
    res = requests.get(image_url, stream=True)

    if res.status_code == 200:
        with open(image_name, 'wb') as f:
            for chunk in res.iter_content(1024):
                f.write(chunk)


# a list of generated urls
urls = r['answer']['urls']

# extract each one individually
image_100 = next((i for i in urls if i['iteration'] == '100'), None)
image_200 = next((i for i in urls if i['iteration'] == '200'), None)
image_300 = next((i for i in urls if i['iteration'] == '300'), None)

# inspect
print('inspect the generated image at iteration no 300')
print(image_300)

image_urls = [image_100['image_url'], image_200['image_url'], image_300['image_url']]
image_names = ['a.png', 'b.png', 'c.png']

for url, name in zip(image_urls, image_names):
    print("downloading", url)
    download_image(url, name)
