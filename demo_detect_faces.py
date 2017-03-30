from pprint import pprint

from aiception import detect_faces

# the secret token
token = "xxxxxxxxxxxxxxxxx"

# a group of kids
image_url = "http://cdn.www.ministry-to-children.com/wp-content/uploads/2013/08/group-of-children.jpg"

# the answer is a list of rectangles <x1, y1, x2, y2> that represent the faces
r = detect_faces(token, image_url)

pprint(r)
