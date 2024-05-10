import requests

organize = '-=-' * 65

headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

#CURSOS:
results_cursos = requests.get(url=url_cursos, headers=headers)

print(f"Cursos_Results: {organize}")
print(results_cursos.json())

#Teste endpoint:
assert results_cursos.status_code == 200

#AVALIAÇÕES:
results_avaliacoes = requests.get(url=url_avaliacoes, headers=headers)

print(f"Avaliações_Results: {organize}")
print(results_avaliacoes.json())

#Teste endpoint:
assert results_avaliacoes.status_code == 200