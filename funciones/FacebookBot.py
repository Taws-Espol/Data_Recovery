from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import time
import threading
import json

lugar="driver/chromedriver"
url_publicaciones='https://www.facebook.com/'
email=''
contraseña=''

def leer_json():
    with open("xpaths_facebook.json") as mi_archivo:
        Dicc_xpaths=json.load(mi_archivo)
    return Dicc_xpaths

Dicc_xpaths=leer_json()

def verificarElemento(xpath,driver):
    try:
        driver.find_element(By.XPATH,xpath)
        return True
    except NoSuchElementException:
        return False

def verificarVisible(elemento):
    try:
        elemento.click()
        return True
    except ElementNotVisibleException:
        return False

def verificarReaccion(listaReacciones,reaccion):
    for reaccionString in listaReacciones:
        if reaccion in reaccionString:
            return reaccionString
    return "0"

def imprimir_publicaciones(pagina, cantidad_publicaciones):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(lugar,options=chrome_options)

    driver.get(url_publicaciones)
    emailElemento = driver.find_element(By.XPATH, Dicc_xpaths["email"])
    emailElemento.send_keys(email)
    passElemento = driver.find_element(By.XPATH, Dicc_xpaths["password"])
    passElemento.send_keys(contraseña)
    boton = driver.find_element(By.XPATH, Dicc_xpaths["boton_login"])
    boton.click()

    while not(verificarElemento(Dicc_xpaths["buscador"],driver)):
        time.sleep(10)

    buscar = driver.find_element(By.XPATH, Dicc_xpaths["buscador"])
    buscar.send_keys(pagina)

    lupa = driver.find_element(By.XPATH, Dicc_xpaths["lupa"])
    lupa.click()
    time.sleep(10)

    pagina_variable="'"+pagina+"'"
    pagina = driver.find_element(By.XPATH,".//*[@alt="+pagina_variable+"]")
    pagina.click()
    time.sleep(10)

    publicaciones = driver.find_element(By.XPATH,Dicc_xpaths["pagina_publicaciones"])
    publicaciones.click()
    time.sleep(10)

    publicacionesLista = driver.find_elements(By.XPATH, Dicc_xpaths["publicaciones_lista"])
    while(len(publicacionesLista)<cantidad_publicaciones):
        driver.execute_script("window.scrollBy(0,5000)","")
        time.sleep(10)
        publicacionesLista = driver.find_elements(By.XPATH, Dicc_xpaths["publicaciones_lista"])

    listaFinalPublicaciones=publicacionesLista[0:cantidad_publicaciones]

    driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

    f = open("Datos de las publicacones Facebook.tsv", "w", encoding="utf-8")

    time.sleep(10)
    for publicacion in listaFinalPublicaciones:
        contenido = publicacion.find_element(By.XPATH, Dicc_xpaths["contenido_publicacion"])
        escribir_contenido=str(contenido.text).replace("\t","").replace("\n","")
        f.write(escribir_contenido + "\t")
        if(verificarElemento(Dicc_xpaths["fecha_publicacion"],publicacion)):
            fechaLugar = publicacion.find_element(By.XPATH, Dicc_xpaths["fecha_publicacion"])
            fecha = fechaLugar.get_attribute("title")
        else:
            fecha="null"
        escribir_fecha=str(fecha).replace("\t","").replace("\n","")
        f.write(escribir_fecha+ "\t")
        botonReacciones=publicacion.find_element(By.XPATH, Dicc_xpaths["boton_reacciones"])
        botonReacciones.click()
        time.sleep(10)
        Reacciones=driver.find_elements(By.XPATH, Dicc_xpaths["reacciones"])
        listaReaccionesParaEscribir=[]
        for reaccion in Reacciones:
            Diferente=reaccion.get_attribute("aria-label")
            escribir_diferente=str(Diferente).replace("\t","").replace("\n","")
            listaReaccionesParaEscribir.append(escribir_diferente)

        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me gusta")+"\t")
        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me encanta") + "\t")
        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me importa") + "\t")
        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me divierte") + "\t")
        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me asombra") + "\t")
        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me entristece") + "\t")
        f.write(verificarReaccion(listaReaccionesParaEscribir, "Me enoja") + "\t")

        cerrar=driver.find_element(By.XPATH,Dicc_xpaths["boton_cerrar_reacciones"])
        cerrar.click()
        time.sleep(10)
        cantidadComentarios=publicacion.find_element(By.XPATH,Dicc_xpaths["cantidad_comentarios"])
        escribir_cantidad_comentarios=str(cantidadComentarios.text).replace("\t","").replace("\n","")
        f.write(escribir_cantidad_comentarios + "\n")

    f.close()

def imprimir_comentarios(url_comentario, tipo_comentarios):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(lugar, options=chrome_options)

    driver.get(url_comentario)

    ahoraNo = driver.find_element(By.XPATH, Dicc_xpaths["boton_ahora_no"])
    while not(verificarVisible(ahoraNo)):
        time.sleep(10)

    emailElemento = driver.find_element(By.XPATH, Dicc_xpaths["email"])
    emailElemento.send_keys(email)
    passElemento = driver.find_element(By.XPATH, Dicc_xpaths["password"])
    passElemento.send_keys(contraseña)
    boton = driver.find_element(By.XPATH, Dicc_xpaths["boton_login"])
    boton.click()
    time.sleep(30)

    if(tipo_comentarios!="Más relevantes"):
        abrirMenu=driver.find_element(By.XPATH, Dicc_xpaths["abrir_menu"])
        abrirMenu.click()
        time.sleep(10)
        listaDeTipos = driver.find_elements(By.XPATH, Dicc_xpaths["lista_tipos_comentarios"])
        for tipo in listaDeTipos:
            if str(tipo.text)==tipo_comentarios:
                tipo.click()
        time.sleep(10)

    while (verificarElemento(Dicc_xpaths["boton_ver_mas"], driver)):
        verMas=driver.find_element(By.XPATH, Dicc_xpaths["boton_ver_mas"])
        #SCROLLER_DE_COMENTARIOS
        driver.execute_script('document.getElementById("u_13_1").scrollTop+=5000')
        #FIN
        verMas.click()
        time.sleep(10)

    comentariosLista = driver.find_elements(By.XPATH, Dicc_xpaths["comentarios_lista"])

    f = open("Comentarios de la publicacion de Facebook.tsv", "w", encoding="utf-8")

    for comentario in comentariosLista:
        escribir_comentario=str(comentario.text).replace("\t","").replace("\n","")
        f.write(escribir_comentario + "\n")

    f.close()
