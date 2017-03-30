from pprint import pprint

from aiception import face_age


# the secret token
token = "xxxxxxxxxxxxxxxxx"

# image of young Taylor Swift
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Taylor_Swift_GMA_2012.jpg/330px-Taylor_Swift_GMA_2012.jpg"

# the answer is the approximate age of the face in the image
# image should contain 1 face and it should be centered
r = face_age(token, image_url)

pprint(r)
