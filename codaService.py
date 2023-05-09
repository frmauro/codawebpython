import requests


class CodaService:
     # init method or constructor
    def __init__(self, url, title, text):
        self.url = url
        self.title = title
        self.text = text

    def getColumnValue(columnValue):    
        headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
        uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows/'

        params = {
        'query': f'c-ILOZNEGduy:"{columnValue}"',
        }

        req = requests.get(uri, headers=headers, params=params)
        res = req.json()
        return res
    
    def createRow(self):
        headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
        uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows/'

        payload = {
            'rows': [
                {
                'cells': [
                    {'column': 'c-ILOZNEGduy', 'value': f'{self.url}'},
                    {'column': 'c-swYTqmkWLE', 'value': f'{self.title}'},
                ],
                },
            ],
            }

        req = requests.post(uri, headers=headers, json=payload)
        res = req.json()
        return res


    def update(self, rowid):
        headers = {'Authorization': 'Bearer 7a208aeb-ea98-414c-8e25-34d988f85892'}
        uri = f'https://coda.io/apis/v1/docs/pOe5ixBASv/tables/grid-wWfa52dKst/rows/{rowid}/'
        print("TEXTO: " + self.text)
        payload = {
        'row': {
            'cells': [
            {'column': 'c-swYTqmkWLE', 'value': f'{self.title}'},
            {'column': 'c-aHFCRMWW3E', 'value': f'{self.text}'},
            ],
        },
        }

        req = requests.put(uri, headers=headers, json=payload)
        #req.raise_for_status()
        res = req.json()
        return res    