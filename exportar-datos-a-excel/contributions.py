import requests
from bs4 import BeautifulSoup

# Obtener datos y que reciba una URL
class ContributionsModelo:
    def obtener_datos(usuario):
        try:
            url = f"https://github.com/{usuario}"
            pagina = requests.get(url)
            pagina.raise_for_status()
            bs = BeautifulSoup(pagina.content, "html.parser")
            titulo = bs.find_all("span", class_="sr-only")
            return titulo
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos: {e}")
            return None

    # Mostrando info de contributions
    def imprimir_info(contributions):
        if contributions is not None and len(contributions) > 0:
            # Ordenando alfabéticamente
            contributions = sorted(contributions, key=lambda x: x.text)
            print(f"Información de contributions en la página:")
            for i, contribution in enumerate(contributions, start=1):
                print(f"{i}. Contribution: {contribution.text}")
            #print(f"Total de contributions encontradas: {len(contributions)}")ESTO NO ES CORRECTO
        else:
            print("No se encontraron contributions en la página.")


