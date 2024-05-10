import requests

organize = '-=-' * 65

class TesteCursosPytest():
    headers = {'Authorization': 'Token 91aa3d2c81dd8ed1cc94a1855e70f65434576271'}
    url_cursos = 'http://localhost:8000/api/v2/cursos/'
    url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


    def curso_get(self):
        result = requests.get(url=self.url_cursos, headers=self.headers)
        assert result.status_code == 200

    
    def cursos_get(self):
        result = requests.get(url=f'{self.url_cursos}1/', headers=self.headers)
        assert result.status_code == 200

    
    def curso_post(self):
        add_curso = {
            "titulo": "",
            "url": ""
        }

        result = requests.post(url=self.url_cursos, headers=self.headers, data=add_curso)
        
        assert result.status_code == 201
        assert result.json()['titulo'] == add_curso['titulo']


    def curso_put(self):
        uptade_curso = {
            "titulo": "",
            "url": ""
        }

        result = requests.put(url=f'{self.url_cursos}1/', headers=self.url_cursos, data=uptade_curso)

        assert result.status_code == 200

    
    def curso_put_titulo(self):
        update_curso = {
            "titulo": "",
            "url": ""
        }

        result = requests.put(url=f'{self.url_cursos}1/', headers=self.headers, data=update_curso)
        
        assert result.json()['titulo'] == update_curso['titulo']


    def curso_delete(self):
        result = requests.delete(url=f'{self.url_cursos}1/', headers=self.headers)

        assert result.status_code == 204 and len(result.text) == 0