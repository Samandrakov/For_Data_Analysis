# from meta_names import name
import pandas as pd
import requests
import threading


def get_qid(comp_name, timeout=15):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': comp_name
    }

    class RequestThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                response = requests.get(url, params=params, timeout=timeout)
                data = response.json()
                if data['search']:
                    self.result = data['search'][0]['id']
                else:
                    self.result = None
            except requests.exceptions.RequestException:
                self.result = None

    request_thread = RequestThread()
    request_thread.start()
    request_thread.join(timeout)

    if request_thread.is_alive():
        return None
    return request_thread.result


company_qids = {}
name = []

df = pd.read_csv("countries.csv")
for n in df['name']:
    name.append(n)


count = 0
for n in name:
    count += 1
    qid = get_qid(n)
    if qid:
        # print(f'Номер - {count})')
        print(f"{count};{n};{qid}")
        company_qids[n] = qid
    else:
        # print(f'Номер - {count} (нет QID)')
        print(f"{count};{n};{qid}")
        company_qids[n] = '0'


