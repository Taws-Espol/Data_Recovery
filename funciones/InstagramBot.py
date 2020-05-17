from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json
import threading

lugar="driver/chromedriver"
email='jgparraga99@gmail.com'
contraseña='testing4321'

def leer_json():
    with open("xpaths_instagram.json") as mi_archivo:
        Dicc_xpaths=json.load(mi_archivo)
    return Dicc_xpaths

Dicc_xpaths=leer_json()

def verificarElemento(xpath,driver):
    try:
        driver.find_element(By.XPATH,xpath)
        return True
    except NoSuchElementException:
        return False

def imprimir_informacion(url_ubicacion, cantidadDePublicaciones):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(lugar, options=chrome_options)
    driver.get(url_ubicacion)
    time.sleep(10)

    iniciar=driver.find_element(By.XPATH,Dicc_xpaths["inicio_sesion"])
    iniciar.click()
    time.sleep(10)

    correo=driver.find_element(By.XPATH, Dicc_xpaths["email"])
    correo.send_keys(email)
    contra=driver.find_element(By.XPATH, Dicc_xpaths["password"])
    contra.send_keys(contraseña)
    sesion=driver.find_element(By.XPATH, Dicc_xpaths["boton_iniciar"])
    sesion.click()
    time.sleep(10)

    listaPublicaciones=driver.find_elements(By.XPATH, Dicc_xpaths["publicaciones_lista"])
    publicacionInicial=listaPublicaciones[0]
    entrar=publicacionInicial.find_element(By.XPATH, Dicc_xpaths["entrar_primera_publicacion"])
    entrar.click()
    time.sleep(10)

    f = open("Datos de las publicaciones de la ubicacion seleccionada en Instagram.tsv", "w", encoding="utf-8")

    for numeroPublicacion in range(cantidadDePublicaciones):
        usuario=driver.find_element(By.XPATH, Dicc_xpaths["usuario_publicacion"])
        escribir_usuario=str(usuario.text).replace("\t","").replace("\n","")
        f.write(escribir_usuario+"\t")
        encabezado=driver.find_element(By.XPATH, Dicc_xpaths["encabezado_publicacion"])
        escribir_encabezado=str(encabezado.text).replace("\t","").replace("\n","")
        f.write(escribir_encabezado + "\t")
        fechaLugar=driver.find_element(By.XPATH, Dicc_xpaths["fecha_publicacion"])
        fecha=fechaLugar.get_attribute("title")
        escribir_fecha=str(fecha).replace("\t","").replace("\n","")
        f.write(escribir_fecha + "\t")
        listaImagenes=[]
        panelDeImagenes=driver.find_element(By.XPATH, Dicc_xpaths["panel_imagenes"])

        if(verificarElemento(Dicc_xpaths["video_presente_pantalla_publicacion"],panelDeImagenes)):
            video1=panelDeImagenes.find_element(By.XPATH,Dicc_xpaths["video_presente_pantalla_publicacion"])
            listaImagenes.append(video1.get_attribute("src"))
        else:
            imagen1=panelDeImagenes.find_element(By.XPATH, Dicc_xpaths["imagen_presente_pantalla_publicacion"])
            listaImagenes.append(imagen1.get_attribute("src"))

        while(verificarElemento(Dicc_xpaths["boton_seguir_imagenes_publicacion"],driver)):
            botonImagenesRestanes=driver.find_element(By.XPATH, Dicc_xpaths["boton_seguir_imagenes_publicacion"])
            botonImagenesRestanes.click()
            time.sleep(10)

            tupla_de_2_imagenes = panelDeImagenes.find_elements(By.XPATH, Dicc_xpaths["imagen_presente_pantalla_publicacion"])
            srcImagenes=[]
            if(len(tupla_de_2_imagenes)>0):
                for imag in tupla_de_2_imagenes:
                    srcImagenes.append(imag.get_attribute("src"))

            tupla_de_2_videos = panelDeImagenes.find_elements(By.XPATH,Dicc_xpaths["video_presente_pantalla_publicacion"])
            srcVideos=[]
            if(len(tupla_de_2_videos)>0):
                for vide in tupla_de_2_videos:
                    srcVideos.append((vide.get_attribute("src")))

            tupla_combinada=srcImagenes+srcVideos
            for elemento in tupla_combinada:
                if (elemento not in listaImagenes):
                    listaImagenes.append(elemento)

        for imgURL in listaImagenes:
            escribir_imgURL=str(imgURL).replace("\t","").replace("\n","")
            if (imgURL != listaImagenes[len(listaImagenes) - 1]):
                f.write(escribir_imgURL + " ")
            else:
                f.write(escribir_imgURL + "\n")
        botonPublicacionesSiguientes=driver.find_element(By.XPATH, Dicc_xpaths["boton_seguir_publicaciones_restantes"])
        botonPublicacionesSiguientes.click()
        time.sleep(10)

    f.close()