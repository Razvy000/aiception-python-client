from pprint import pprint

from aiception import detect_object


# the secret token
token = "xxxxxxxxxxxxxxxxx"

# image of a squirrel
image_url = "https://s-media-cache-ak0.pinimg.com/736x/d6/e0/99/d6e099456899689e563f534e2cca476e.jpg"

# the answer is a list of <label, score> pairs
# the score is a confidence measure
r = detect_object(token, image_url)

pprint(r)

# extract a prediction
print('the first answer is:')
print('label: ' + r['answer'][0][0])
print('score: ' + str(r['answer'][0][1]))
