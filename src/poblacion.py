import csv 
from collections import namedtuple
from matplotlib import pyplot as plt  

RegistroPoblacion = namedtuple('RegistroPoblacion','pais, codigo, año, censo')
def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        poblaciones = [
            Registropoblacion(pais, codigo, int(año), int(censo))
            for pais, codigo, año, censo in lector
        ]
        return poblaciones

def calcula_paises(poblaciones):
    paises = set()
    for poblacion in poblaciones(RegistroPoblacion):
        paises.add(poblacion.pais)
    return sorted(paises)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    año_y_censo = []
    for poblacion in poblaciones(RegistroPoblacion):
        if pais == nombre_o_codigo or codigo == nombre_o_codigo:
            año_y_censo.append((poblacion.año,poblacion.censo))
    return año_y_censo

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    censo_por_año = []
    for poblacion in poblaciones(RegistroPoblacion):
        if poblacion.año == anyo and poblacion.pais in paises:
            censo_por_año.append((poblacion.pais, poblacion.censo))
    return censo_por_año

def muestra_evolucion_poblacion(poblaciones, pais_o_codigo):
    titulo = "Evolución población"
    lista_años = []
    lista_habitantes = []
    for poblacion in poblaciones(RegistroPoblacion):
        if poblacion.pais == pais_o_codigo or poblacion.codigo == pais_o_codigo:
            lista_años.append(int(poblacion.año))
            lista_habitantes.append(int(poblacion.censo))
        else:
            pass
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativas_paises_anyo(poblaciones, anyo, paises):
    titulo = "Comparativa países"
    lista_paises = []
    lista_habitantes = []
    for poblacion in poblaciones(RegistroPoblacion):
        if poblacion.año == anyo and poblacion.pais in paises:
            lista_paises.append(poblacion.pais)
            lista_habitantes.append(int(poblacion.censo))
        else:
            pass
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()          