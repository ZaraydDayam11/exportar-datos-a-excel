import developer
import tendencias
import perfil
import githubevents
import topics
import contributions

def listarTendenciasMensuales():
    # link de pagina a scrapear
    url = 'https://github.com/trending?since=monthly&spoken_language_code=es'
    cantidad = int(input("\nIngrese número de repositorios a extraer(0 para extraer todos): "))
    # variable(con) donde llamamos al archivo(tendencias) donde tenemos la clase que necesitamos(TendenciasModelo) y le mandamos la url
    con = tendencias.TendenciasModelo(url, cantidad)
    # variable(lista) donde llamamos la variable anterior(con) y llamamos al metodo (obtenerTendencias) con la url
    lista = con.obtenerTendencias(url, cantidad)
    # recorremos los resultados que nos trajo con un for
    for t in lista:
        print(f'\nRepositorio: {t["Repositorio"]}')
        print(f'Desarrollador: {t["Desarrollador"]}')
        print(f'Descripción: {t["Descripción"]}')
        print(f'Lenguaje de Programación: {t["Lenguaje de Programación"]}')
        print(f'Estrellas: {t["Estrellas"]}' + ' ' *50 + f'Clonados: {t["Clonados"]}\n')
        print('-' * 100)


def listarTendenciasSemanales():
    url = 'https://github.com/trending?since=weekly&spoken_language_code=es'
    cantidad = int(input("\nIngrese número de repositorios a extraer(0 para extraer todos): "))
    con = tendencias.TendenciasModelo(url, cantidad)
    lista = con.obtenerTendencias(url, cantidad)
    for t in lista:
        print(f'\nRepositorio: {t["Repositorio"]}')
        print(f'Desarrollador: {t["Desarrollador"]}')
        print(f'Descripción: {t["Descripción"]}')
        print(f'Lenguaje de Programación: {t["Lenguaje de Programación"]}')
        print(f'Estrellas: {t["Estrellas"]}' + ' ' *50 + f'Clonados: {t["Clonados"]}\n')
        print('-' * 100)


def listarTendenciasDiarias():
    url = 'https://github.com/trending?since=daily&spoken_language_code=es'
    cantidad = int(input("\nIngrese número de repositorios a extraer(0 para extraer todos): "))
    con = tendencias.TendenciasModelo(url, cantidad)
    lista = con.obtenerTendencias(url, cantidad)
    for t in lista:
        print(f'\nRepositorio: {t["Repositorio"]}')
        print(f'Desarrollador: {t["Desarrollador"]}')
        print(f'Descripción: {t["Descripción"]}')
        print(f'Lenguaje de Programación: {t["Lenguaje de Programación"]}')
        print(f'Estrellas: {t["Estrellas"]}' + ' ' *50 + f'Clonados: {t["Clonados"]}\n')
        print('-' * 100)

#--------------------------------------------------------------------------------------------------------------------

def listarTendDeveloperMensuales():
        url= 'https://github.com/trending/developers?since=monthly'
        listaRepositorios = developer.TendenciasDeveloper(url)
        lista = listaRepositorios.obtenerTendDeveloper(url)
        for t in lista:
                print(f'\nNombre: {t["Nombre"]}')
                print(f'Desarrollador: {t["Desarrollador"]}')
                print(f'Título Repositorio: {t["Título Repositorio"]}')
                print(f'Descripción Repositorio: {t["Descripción Repositorio"]}')           

def listarTendDeveloperSemanales():
        url='https://github.com/trending/developers?since=weekly'
        listaRepositorios = developer.TendenciasDeveloper(url)
        lista = listaRepositorios.obtenerTendDeveloper(url)
        for t in lista:
                print(f'\nNombre: {t["Nombre"]}')
                print(f'Desarrollador: {t["Desarrollador"]}')
                print(f'Título Repositorio: {t["Título Repositorio"]}')
                print(f'Descripción Repositorio: {t["Descripción Repositorio"]}')  
            
def listarTendDeveloperDiarias():
        url='https://github.com/trending/developers?since=daily'
        listaRepositorios = developer.TendenciasDeveloper(url)
        lista = listaRepositorios.obtenerTendDeveloper(url)
        for t in lista:
                print(f'\nNombre: {t["Nombre"]}')
                print(f'Desarrollador: {t["Desarrollador"]}')
                print(f'Título Repositorio: {t["Título Repositorio"]}')
                print(f'Descripción Repositorio: {t["Descripción Repositorio"]}')  
            
#------------------------------------------------------------------------------------------------------------------------------------------------
def listarInformacionPerfil():
    url = input('\nIngrese nombre de usuario de perfil de GitHub: ')
    con = perfil.PerfilModelo(url)
    resultado= con.obtenerInfoPerfil(url)
    #dividimos la tupla(resultado) en las 3 variables por orden de return
    perfil_info, numero_contribuciones, repositorios_info, readme_info = resultado
    
     
    if readme_info:
        if 'titulo' in readme_info[0]:
            print(f'\n\nReadme:  {readme_info[0]["titulo"]}')
            for parrafo in readme_info[1:]:  # Se comienza desde el segundo elemento para no repetir el titulo
                print(parrafo["Descripcion"])
        # else:print('No se encontró un titulo\n')
    else:print('\n\nNo se encontró un README\n')
    
    print('-' * 100)
    for p in perfil_info:
        print(f'\nUsuario: {p["Usuario"]}')
        print(f'Descripcion: {p["Descripcion perfil"]}')
        print(f'Seguidores: {p["Seguidores"]}')
        print(f'Siguiendo: {p["Siguiendo"]}')
        print('')
        print('-' * 100)
    
    print(f'\nPopular repositories:')
    for repo in repositorios_info:
        print(f'\nRepositorio: {repo["Repositorios"]}')
        print(f'Lenguaje: {repo["Lenguaje de Programación"]}')
        print(f'Estrellas: {repo["Estrellas"]}')
        print(f'Clonados: {repo["Clonados"]}')
        print(f'Descripción: {repo["Descripcion"]}')
        
    
    print('-' * 100)    
    print(f'\nNúmero de Contribuciones: {numero_contribuciones}\n')
    
    
       
#----------------------------------------------------------------------------

def listarEvents():
        url='https://github.com/events'
        listaEventos = githubevents.events(url)
        listaEventos.obtenerEvents(url)
#----------------------------------------------------------------------------

def listarTopics():
        t=topics.TopicosModelo 
        lista=t.obtener_datos("https://github.com/topics/")
        print()
        resultado, topicos = lista
        for desc in resultado: print(desc)
        for topic in topicos: print(topic)
        
def listarContributions():
        nombre = input('\nIngrese nombre de usuario de perfil de GitHub: ')
        c=contributions.ContributionsModelo 
        print()
        cont = c.obtener_datos(nombre)
        if contributions:
            c.imprimir_info(cont)

            
