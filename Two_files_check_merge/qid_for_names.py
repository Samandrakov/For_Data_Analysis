from meta_names import name
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

# name = ['google', 'apple', 'amazon']
count = 0
for n in name:
    count += 1
    qid = get_qid(n)
    if qid:
        print(f"{count}, {qid}")
        company_qids[n] = qid
    else:
        print(f"{count}, {qid}")
        company_qids[n] = '0'

print(company_qids)
