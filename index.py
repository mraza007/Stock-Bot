
import requests as r
import json


import os
import json
key = os.environ['API_KEY']


# app = Flask(__name__)


# @app.route('/add')
# def home():
data = r.get(f'https://api-v2.intrinio.com/companies/IBM/news?api_key={API_KEY}')
json_data = json.loads(data.text)
prettify = json_data['news'][2]['summary']
post =  r.post('http://text-processing.com/api/sentiment/',{'text':prettify})
post_data = json.loads(post.text)
print('POS: '+ str(post_data['probability']['pos']*100))
print('NEG: '+ str(post_data['probability']['neg']*100))





