import json 
import requests 
from bs4 import BeautifulSoup

class TopicosModelo:
    def __init__(self, url) -> None:
        self.url = url
    def obtener_datos(url): 
        pagina = requests.get(url)
        bs = BeautifulSoup(pagina.content, "html.parser") 
        nombres = bs.find_all("p", class_="f3 lh-condensed mb-0 mt-1 Link--primary") 
        descripcion = bs.find_all("p", class_="f5 color-fg-muted text-center mb-0 mt-1")
        #p class="f5 color-fg-muted text-center mb-0 mt-1"
        topicos = [nombre.text.strip() for nombre in nombres] 
        print()
        resultado = [desc.text.strip() for desc in descripcion]
        return (resultado, topicos)

    
        

    

