from meta_names import name
import requests

def get_qid(comp_name):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': comp_name
    }
    responce = requests.get(url, params=params)
    data = responce.json()
    if data['search']:
        return data['search'][0]['id']
    else:
        return None

company_qids = {}

# names = ['google', 'apple', 'amazon']

for n in name:
    qid = get_qid(n)
    if qid:
        company_qids[n] = qid
    else:
        company_qids[n] = '0'

print(company_qids)