import requests
import pandas as pd
import numpy as np

ACCESS_TOKEN = 'vf2H4OcPRXU7PzKKIFgkN3BUeoiGkrQEx6cg7lLqQUbECPUfEYwBrZos9X2y'

# query request
response = requests.get('https://zenodo.org/api/records',
                        params={'q': 'synthetic',
                        		'type': 'dataset',
                        		'access_right': 'open',
                        		#'keywords': ['machine learning'],
                        		'size': 2000,
                        		'access_token': ACCESS_TOKEN})
dict_data = response.json()

# create dataframe
lst = []
for hit in dict_data['hits']['hits']:

	doi = hit['doi']
	access_right = hit['metadata']['access_right']
	title = hit['metadata']['title']
	description = hit['metadata']['description']

	lst.append([doi, access_right, title])#, description])
df = pd.DataFrame.from_records(lst)

# save to file
df.columns = ['doi','access_right','title']#,'description']
df.to_csv('zenodo_open_synth_datasets.csv',index=None)