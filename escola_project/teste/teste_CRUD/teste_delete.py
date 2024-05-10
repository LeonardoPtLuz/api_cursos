import requests

headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


results_delete = requests.delete(url=f'{url_cursos}3/', headers=headers)

#Teste endpoint:
assert results_delete.status_code == 204

assert len(results_delete.text) == 0