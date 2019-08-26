import requests
from pprint import pprint
regions = ['fr', 'it']
with open('car1.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token b0a2454eeb5638d2da616cee18b1d26e79f5fef7'})
json_array=response.json()
print(json_array['results'][0]['plate'])
