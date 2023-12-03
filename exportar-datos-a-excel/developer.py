import requests
from bs4 import BeautifulSoup

class TendenciasDeveloper:
    def __init__(self,url,) -> None:   
        self.url = url
       
             
       
    def obtenerTendDeveloper(self,url):   
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            repositorios = []
            repositorio = soup.find_all('article', class_='Box-row d-flex')

            for articulo in repositorio:
                nombre = articulo.find('h1', class_='h3 lh-condensed')
                nombre_completo = nombre.text.strip()

                nombre_alias = articulo.find('p', class_='f4 text-normal mb-1')
                alias = nombre_alias.text.strip() if nombre_alias else 'Sin alias'

                nombre_repo = articulo.find('h1', class_='h4 lh-condensed')
                repo = nombre_repo.text.strip() if nombre_repo else ''
                
                breve_descrip=articulo.find('div', class_='f6 color-fg-muted mt-1') 
                #breve_descrip=articulo.find('div', class_='f6 colour-fg-muted mt-1')
                descrip= breve_descrip.text.strip() if breve_descrip else ''
                                
                nombre_completo=nombre_completo.encode("utf-8", "ignore").decode("utf-8")
                alias=alias.encode("utf-8", "ignore").decode("utf-8")
                repo=repo.encode("utf-8", "ignore").decode("utf-8")
                descrip=descrip.encode("utf-8", "ignore").decode("utf-8")
                
                repositorios.append({
                    'Nombre': nombre_completo,
                    'Desarrollador': alias,
                    'Título Repositorio': repo,
                    'Descripción Repositorio': descrip
                })
            
            return repositorios
        else:
            print('Error al hacer la solicitud HTTP.')
            
    