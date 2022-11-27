import requests as r
import pandas

params = {
    'amount': 10,
    'type': 'boolean'
}

response = r.get(url='https://opentdb.com/api.php', params=params)
data = response.json()

df = pandas.read_json(data)


question_data = [  for (index, data_row) in df.
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium",
        "question": "The HTML5 standard was published in 2014.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
   
    
]
