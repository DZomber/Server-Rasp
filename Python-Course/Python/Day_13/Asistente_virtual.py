import pyttsx3
import speech_recognition as sr
import pywhatkit
import  yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from pyttsx3 import engine

'''
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

'''

#escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    # alamcenar recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar!")

        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido = r.recognize_google(audio, language ='es-mx')
            # prueba de que pudo ingresar
            print("Dijiste "+pedido)
            #devolver pedido
            return pedido
        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print("no entendi.")

            #devolver error
            return  'sigo esperando'
        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("No hay servicio.")

            # devolver error
            return 'sigo esperando'
        #error inesperado
        except:

            # prueba de que no comprendio el audio
            print("algo salio mal")

            # devolver error
            return 'sigo esperando'

#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()
'''
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)

'''
# opciones de boz / idioma
def pedir_dia():
    #crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #crear una variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)
    #diccionario con nombre de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miercoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'
                  }
    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}, Diego')

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)

    #decir la hora
    hablar(hora)

def saludo_inicial():

    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour <6 and hora.hour >20:
        momento = 'Buenas noches'
    elif hora.hour >=6 and hora.hour <13:
        momento = 'Buenos Dias'
    else:
        momento = 'Buenas tardes'
    #decir el saludo
    hablar(f'Hola, {momento}, soy Karen, tu asistente personal. Porfavor dime en que te puedo ayudar?')

#funcion central del asistente
def pedir_cosas():
    #activar saludo
    saludo_inicial()
    #Variable de corte
    comenzar = True
    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if pedido == 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Con gusto, estoy abriendo Navegador')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'abrir spotify' in pedido:
            hablar('Con gusto, estoy abriendo spotify')
            webbrowser.open('https://open.spotify.com/intl-es#login')
        elif 'busca en internet' in pedido:
            hablar('Con gusto, estoy en eso')
            pedido = pedido.replace('Busca en internet ', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Con gusto, estoy reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar')
            break

pedir_cosas()