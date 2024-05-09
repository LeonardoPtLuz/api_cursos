import requests

headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

update_curso = {
    "titulo": "Curso 3.1",
    "url": "http://curso3.1put.com"
}

results_put = requests.put(url=f'{url_cursos}3/', headers=headers, data=update_curso)

#Teste endpoint:
assert results_put.status_code == 200

#Teste titulo PUT:
assert results_put.json()['titulo'] == update_curso['titulo']

print(results_put.json())