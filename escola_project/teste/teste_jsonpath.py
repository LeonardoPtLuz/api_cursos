import requests, jsonpath

organize = '-=-' * 65

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

print(f"Json_Results: {organize}")
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
print(resultados)

print(f"Json_Results_Position: {organize}")
primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeiro)

print(f"Json_Nome: {organize}")
nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)

print(f"Json_Nome: {organize}")
nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
print(nota)

print(f"Json_Nomes: {organize}")
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)

print(f"Json_Notas: {organize}")
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)