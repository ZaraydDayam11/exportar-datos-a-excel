import requests
from bs4 import BeautifulSoup


class PerfilModelo:
    def __init__(self, url) -> None:
        self.url = url
       
           
    def obtenerInfoPerfil(self, url):  
        git='https://github.com/'
        urlCompleta=git+url
        # url = 'https://github.com/midudev'
        # url = 'https://github.com/phuocng'
        #url = 'https://github.com/hwchase17'
        respuesta = requests.get(urlCompleta)
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            perfil=[]
            repositorios = []
            readme=[]
           
            
            info_perfil = soup.find_all('div', class_='js-profile-editable-replace')
            for info in info_perfil:
                name = info.find('h1', class_='vcard-names')
                usuario = name.text.strip()
                des_perfil = info.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
                descripcion_perfil = des_perfil.text.strip()
                seguidores_perfil = info.find('span', class_='text-bold color-fg-default')
                seguidores = seguidores_perfil.text.strip()
                siguiendo_perfil = info.find('a', href=lambda href: href.endswith('=following'))
                siguiendo = siguiendo_perfil.span.text.strip()
                usuario = usuario.encode('utf-8', 'ignore').decode('utf-8')
                descripcion_perfil = descripcion_perfil.encode('utf-8', 'ignore').decode('utf-8')
         
                perfil.append({
                    'Usuario': usuario,
                    'Descripcion perfil': descripcion_perfil,
                    'Seguidores': seguidores,
                    'Siguiendo': siguiendo
                })
            
            ol = soup.find_all('ol')
            for repositorio in ol:
                for articulo in repositorio.find_all('li'):
                    repo = articulo.find('span', class_='repo')
                    repo_popular = repo.text.strip()
                    lenguaje_repo = articulo.find('span', class_='d-inline-block mr-3')
                    lenguaje = lenguaje_repo.text.strip() if lenguaje_repo else 'Sin lenguaje'
                    estrellas_repo = articulo.find('a', class_='pinned-item-meta Link--muted')
                    estrellas = estrellas_repo.text.strip() if estrellas_repo else '0'
                    forks_repo = articulo.find('a', href=lambda href: href.endswith('/forks'))
                    forks = forks_repo.text.strip() if forks_repo else '0'
                    descripcion_repo = articulo.find('p', class_='pinned-item-desc color-fg-muted text-small mt-2 mb-0')
                    descripcion = descripcion_repo.text.strip() if descripcion_repo else 'Sin descripción'

                    repo_popular = repo_popular.encode('utf-8', 'ignore').decode('utf-8')
                    lenguaje = lenguaje.encode('utf-8', 'ignore').decode('utf-8')
                    estrellas = estrellas.encode('utf-8', 'ignore').decode('utf-8')
                    forks = forks.encode('utf-8', 'ignore').decode('utf-8')
                    descripcion = descripcion.encode('utf-8', 'ignore').decode('utf-8')
                    
                    repositorios.append({
                    'Repositorios': repo_popular,
                    'Lenguaje de Programación': lenguaje,
                    'Estrellas': estrellas,
                    'Clonados': forks,
                    'Descripcion': descripcion,
                })

            cont = soup.find('h2', class_='f4 text-normal mb-2')
            contribuciones = cont.text.strip()
            palabras = contribuciones.split()  # divide el texto en palabras separadas
            numero_contribuciones = palabras[0]  # se extrae solo el numero con [0]
            
            
            contenido_readme = soup.find('article', class_='markdown-body entry-content container-lg f5')
            if contenido_readme:
                title = contenido_readme.find('a', class_='heading-link') 
                if title:  titulo = title.text.strip()
                else:  titulo = 'Título no encontrado'
                readme.append({
                    'titulo': titulo,
                })
                
                parrafos = contenido_readme.find_all('p')#buscar todos los parrafos en el readme
                for p in parrafos:
                    descripcion = p.text.strip() 
                    descripcion = descripcion.encode('utf-8', 'ignore').decode('utf-8')
                    
                    readme.append({
                        'Descripcion': descripcion,
                    })
          

            return perfil, numero_contribuciones, repositorios, readme
            

        else:
            print('Error al hacer la solicitud HTTP.')
        if respuesta.status_code == 404:
            print('Ese usuario no existe')
            

