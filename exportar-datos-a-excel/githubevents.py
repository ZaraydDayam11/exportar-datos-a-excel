
import requests
from bs4 import BeautifulSoup

class events:
    def __init__(self, url) -> None:
        self.url = url
    def obtenerEvents(self, url): 
        response = requests.get(url) #permite trabajar con los requerimientos y las respuestas que se le solicitan a
                                        #un servidor web a partir de la API (mec.q permiten a dos componentes soft.comunicarse entre sí mediante un conjunto de definiciones y protocolos
                                        # o del HTTP de la plataforma web

        if response.status_code == 200: #Después de recibir e interpretar un mensaje de solicitud, un servidor responde con 
                                        #un mensaje de respuesta HTTP. El mensaje de respuesta tiene un código de estado
            soup = BeautifulSoup(response.text, 'html.parser') #transforma el ht,l en objetos 
            lista= soup.find_all ("li", class_="py-3 py-lg-5 d-sm-flex") #li declara elementos de una lista donde class es unatributo global
            for noticia in lista: 
                t= noticia.find ("h3") 
                titulo= t.text.strip()
                print (titulo)
                
                p= noticia.find ("p",class_="mb-3") 
                parrafo= p.text.strip()
                print (parrafo)
                
                f= noticia.find ("p", class_= "color-fg-muted f5") 
                fecha= f.text.strip()
                print (fecha)
        else:
            print('Error al hacer la solicitud HTTP.')










