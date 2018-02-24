#Python script to get word definitions from the Oxford Dictionary API and store them in a text file

import os
import requests as r
import json
from pprint import pprint

WORDS = ['forebrain','occipital','temporal lobes','gyrus','sulcus']

base_url = 'https://od-api.oxforddictionaries.com:443/api/v1/'
app_id = 'b62d6a70'
app_key = '0b65d2166229a7e856cb85f797d8bcb9'
function = 'entries'
language = 'en'

output = ''

for i in range(0,len(WORDS)):
	headers = {'app_id':app_id, 'app_key':app_key}
	url = base_url + function + '/' + language + '/' + WORDS[i].lower()
	#print(url)
	response = r.get(url, headers=headers)
	response_json = response.json()

	definition = response_json['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
	output = output + WORDS[i] + '\n' + definition + '\n\n'


filename = 'definitions.txt' 

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w'

f = open(filename,append_write)
f.write(output)
f.close()
	
