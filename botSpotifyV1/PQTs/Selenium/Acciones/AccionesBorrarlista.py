# -*- coding: utf-8 -*-

import random
import time

import pyautogui
from PQTs.Selenium.Base import BaseAcciones
from PQTs.Utilizar import urlSpotifysinginUS
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import os
from PQTs.Paths import pathImg


class Acciones(BaseAcciones):
    def ingresarSpotify(self):
        try:
            self.ir(urlSpotifysinginUS)
            self.sleep(2)
            return True
        except:
            self.salir()
            return False


    def loginSpotify(self,cuenta,password):
        try:
            xpathInputEmail = (By.ID,"login-username")
            xpathInputPassword = (By.ID,"login-password")        
            xpathBotonLogin= (By.ID,"login-button")
            

            visibleInputEmail = self.explicitWaitElementoVisibility(15,xpathInputEmail)
            if visibleInputEmail:
                self.escribir(xpathInputEmail,cuenta)
                
                visibleInputPassword = self.explicitWaitElementoVisibility(15,xpathInputPassword)
                if visibleInputPassword:
                    self.escribir(xpathInputPassword,password)
                    visibleBotonLogin = self.explicitWaitElementoVisibility(15,xpathBotonLogin)
                    if visibleBotonLogin:
                        self.click(xpathBotonLogin)
                        self.explicitWaitElementoInvisibility(11,xpathBotonLogin)

                    else:
                        print(f"visibleBotonLogin {xpathBotonLogin}")
                        return False
                else:
                    print(f"visibleInputPassword {visibleInputPassword}")
                    return False
            else:
                print(f"visibleInputEmail {visibleInputEmail}")
                return False
        except:
            #self.refreshweb()
            time.sleep(2)
            return False
    
    def borrarlista(self):
        try: 

            time.sleep(3)                            
            xpathlistas = (By.XPATH, "//li[@class='whXv9jYuEgS1DPTmPCe_' and @data-testid='rootlist-item']")
            xpathtrespuntos=  (By.XPATH, "//button[@aria-haspopup='menu' and @class='T0anrkk_QA4IAQL29get']")
            xpathtdelete=  (By.XPATH, "//span[contains(text(),'Delete')]")
            
            Visiblelistareproduccion = self.explicitWaitElementoVisibility(15,xpathlistas)

            if Visiblelistareproduccion:
                print ("visible lista de canciones")
                listacancio= self.findElements(xpathlistas)
                print (listacancio)
                
                for elem in listacancio:
                    elem.click()

                    Visibletrespuntos = self.explicitWaitElementoVisibility(15,xpathtrespuntos)
                    if Visibletrespuntos:
                        self.click(xpathtrespuntos)
                        Visibledelete = self.explicitWaitElementoVisibility(15,xpathtdelete)
                        if Visibledelete:
                            self.click(xpathtdelete)
                            time.sleep(3)
                            pyautogui.press('enter')
            time.sleep(10)                            
            print ("Saliendo ....")
            self.salir()

        except Exception as e:
            print(e)

    def enviardatos(self,email):
        remitente = 'mayfeljonas1229@gmail.com'
        destinatarios = ['azuresilkmain@gmail.com']
        asunto = f'LISTA BORRADA: {email}'
        cuerpo = f"{str(datetime.datetime.now().strftime('%H-%M-%S'))} {email}"
        ruta_adjunto = (os.path.join(pathImg,f"{email}.png"))
        nombre_adjunto = f'{email}.png'

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(ruta_adjunto, 'rb')
        
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Ciframos la conexión
        sesion_smtp.starttls()

        # Iniciamos sesión en el servidor
        sesion_smtp.login('azuresilk02@gmail.com','iyuwppjjgfshypht')

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()


    def enviardatoslogfail(self,email,passw):
        remitente = 'mayfeljonas1229@gmail.com'
        destinatarios = ['azuresilkmain@gmail.com']
        asunto = f'ERROR LOGING: {email} {passw}'
        cuerpo = f"{str(datetime.datetime.now().strftime('%H-%M-%S'))} Error loging acount para pasar a pais US"
        ruta_adjunto = (os.path.join(pathImg,f"{email}.png"))
        nombre_adjunto = f'{email}.png'

        # Creamos el objeto mensaje
        mensaje = MIMEMultipart()
        
        # Establecemos los atributos del mensaje
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        
        # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        # Abrimos el archivo que vamos a adjuntar
        archivo_adjunto = open(ruta_adjunto, 'rb')
        
        # Creamos un objeto MIME base
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        # Y le cargamos el archivo adjunto
        adjunto_MIME.set_payload((archivo_adjunto).read())
        # Codificamos el objeto en BASE64
        encoders.encode_base64(adjunto_MIME)
        # Agregamos una cabecera al objeto
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        # Y finalmente lo agregamos al mensaje
        mensaje.attach(adjunto_MIME)
        
        # Creamos la conexión con el servidor
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Ciframos la conexión
        sesion_smtp.starttls()

        # Iniciamos sesión en el servidor
        sesion_smtp.login('azuresilk02@gmail.com','iyuwppjjgfshypht')

        # Convertimos el objeto mensaje a texto
        texto = mensaje.as_string()

        # Enviamos el mensaje
        sesion_smtp.sendmail(remitente, destinatarios, texto)

        # Cerramos la conexión
        sesion_smtp.quit()