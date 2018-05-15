import json
import os

for filename in os.listdir('data/'):
    with open('data/{}'.format(filename)) as json_data:
        d = json.load(json_data)
        try:
            print(d['general-grade'][1][0]['value'])
        except IndexError:
            print('empty value')

# TO GET property current value = d['PROPERTY'][0]
# TO GET property full history = d['PROPERTY'][1][0] BUT NEEDS INDEX ERROR CHECK TO PASS
# TO GET property history value = d['PROPERTY'][1][0]['value'] BUT NEEDS INDEX ERROR CHECK TO PASS