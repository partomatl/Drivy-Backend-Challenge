import json
from datetime import datetime

with open('data.json') as data_file:
    data = json.load(data_file)

datetime_object = datetime.strptime('2017-12-8', '%Y-%m-%d')

print(datetime_object)