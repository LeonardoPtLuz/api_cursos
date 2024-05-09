import requests

organize = '-=-' * 65

# #GET todas Avaliações:
# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# print(f"Status_Code: {organize}")
# print(avaliacoes.status_code)

# print(f"Json: {organize}")
# print(avaliacoes.json())

# print(f"Json_Count: {organize}")
# print(avaliacoes.json()['count'])

# print(f"Json_Results: {organize}")
# print(avaliacoes.json()['results'][0])

# print(f"Json_Next: {organize}")
# print(avaliacoes.json()['next'])



# #GET Avaliação específica:
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/3')

# print(f"Status_Code: {organize}")
# print(avaliacao.status_code)

# print(f"Json_Nome: {organize}")
# print(avaliacao.json()['nome'])



#GET Cursos:
headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos', headers=headers)

print(f"Status_Code: {organize}")
print(cursos.status_code)

print(f"Json: {organize}")
print(cursos.json())