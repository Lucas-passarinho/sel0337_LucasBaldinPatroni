#Importanto bibliotecas utilizadas
from picamera import PiCamera, Color
import requests
import json
import pprint
from time import sleep
from requests import get
from pprint import pprint

#Renomeando a PiCamera
camera = PiCamera()

#Teste da camera
camera.start_preview()
sleep(5)
camera.stop_preview()

#Mudando a resolução e taxa de quadros da camera
camera.resolution = (640, 640)
camera.framerate = 15
camera.start_preview()
sleep(5)
#Salvando uma imagem da camera
camera.capture('/home/sel/Documentos/Lab/max.jpg')
camera.stop_preview()

#Configurando o texto mostrado na captura de imagem
camera.start_preview()
camera.annotate_text_size = 100
camera.annotate_text = "Texto pedido. Numero USP: 11233626 e 11316524"
sleep(5)
#salvando a captura de imagem
camera.capture('/home/sel/Documentos/Lab/text.jpg')
camera.stop_preview()

#Salvando um vídeo
camera.start_preview()
camera.start_recording('/home/sel/Documentos/Lab/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

#Configurando o clima
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

weather = weather + str(966583)

#Salvando os dados retirados do apex.oracle
my_weather = get(weather).json()['items']
pprint(my_weather)
