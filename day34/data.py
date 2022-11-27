import requests as r

params = {
    'amount': 10,
    'type': 'boolean'
}

question_data = r.get(url='https://opentdb.com/api.php', params=params).json()['results']