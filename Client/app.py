import json
import http.client

connection = http.client.HTTPConnection("localhost:5000")
objectPayload = json.dumps(
  {'ime': 'Stefan',
  'prezime': 'Nedeljkovic',
  'username': 'Nedeljko',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'Osnove programiranja', 'espb': 8},
     {'ime': 'AIOS', 'espb': 8},
     {'ime': 'PARIOS', 'espb': 6}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}

connection.request("POST", "/users", objectPayload, headers)
response = connection.getresponse()
dataDisplay = response.read()
print(dataDisplay.decode("utf-8"))