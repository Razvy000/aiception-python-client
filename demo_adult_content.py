from pprint import pprint

from aiception import adult_content


# the secret token
token = "xxxxxxxxxxxxxxxxx"

# swimsuit
image_url = "http://i.telegraph.co.uk/multimedia/archive/01007/Borat-mankini_1007719a.jpg"

# not safe for work score between 0 (safe) and 1 (unsafe)
r = adult_content(token, image_url)

pprint(r)
