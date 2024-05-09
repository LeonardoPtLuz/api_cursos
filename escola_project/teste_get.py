import requests

organize = '-=-' * 65

headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

results = requests.get(url=url_cursos, headers=headers)

print(f"Json_Results: {organize}")
print(results.json())

#Teste endpoint:
assert results.status_code == 200

# assert results.json()['count'] == 2

# assert results.json()['results'][0]['titulo'] == ''