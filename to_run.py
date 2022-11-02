import requests
import json
import sys

test_data = {
    'test_data_first_name': 'Abc',
    'test_data_second_name': 'Zxc'
}

port = sys.argv[1]

r = requests.post('http://127.0.0.1:' + port, data=json.dumps(test_data))

print (r.json())