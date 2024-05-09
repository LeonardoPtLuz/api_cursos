import requests

headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

add_curso = {
    "titulo": "teste_post",
    "url": "http://testepost.com"
}

results_post = requests.post(url=url_cursos, headers=headers, data=add_curso)

#Teste endpoint:
assert results_post.status_code == 201

#Teste titulo POST:
assert results_post.json()['titulo'] == add_curso['titulo']