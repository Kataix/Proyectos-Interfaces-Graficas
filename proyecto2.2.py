import cv2
import numpy as np
import math
from PIL import Image
image = cv2.imread('figuras.png')
plantilla = cv2.imread('plantilla.png')
cambiar = 0
while cambiar <=1:
    # escala de grises #
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Threshold tipo THRESH_BINARY_INV . El pixel de destino se establece en cero si el pixel de origen correspondiente es mayor que el umbral y en valor maximo si el pixel de origen es menor que el umbral. 
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    #TRESH: Conjunto de valores de umbral utilizados para cuantificar una imagen 
    # expandir (dilatar bordes)
    kernel = np.ones((10, 1), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    #cv2.dilate agrega una capa adicional de píxeles en una estructura
    # revisa los contornos en el thresh
    # contorno, jerarquia(exterior a interior) (imagen | modo | metodo) #
    ctrs, jer = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # se ordena el contorno
    orden_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    if cambiar==0:
        # se crean los bounding box para la primera imagen #
        cc=0 # contador para enumerar las imagenes guardadas
        for i, ctr in enumerate(orden_ctrs):
            # se obtiene el cuadro delimitador
            x, y, w, h = cv2.boundingRect(ctr)
            # se obtiene la region de interes
            roi = image[y:y + h, x:x + w]
            if w > 15 and h > 15:
                if i==1 or i==9 or i==12 or i==14:
                    cv2.imwrite('trash/figura{}.png'.format(cc), roi)
                    cc=cc+1
        cambiar = cambiar+1
        image = cv2.imread('plantilla.png')
    else:
        # se crean los bounding box para la segunda imagen #
        for i, ctr in enumerate(orden_ctrs):
            # se obtiene el cuadro delimitador
            x, y, w, h = cv2.boundingRect(ctr)
            # se obtiene la region de interes
            roi = image[y:y + h, x:x + w]
            if w > 15 and h > 15:
                cv2.imwrite('trash/plantilla{}.png'.format(i), roi)
                cambiar = cambiar+1 # se cierra el ciclo while
cc = 0 #se sobreescribe el contador
while cc<4:
    if cc==0:#primera imagen (0)
        figura = Image.open('trash/figura{}.png'.format(cc)).rotate(-18)
    elif cc==1:#segunda imagen(1)
        figura = Image.open('trash/figura{}.png'.format(cc)).rotate(15)
    elif cc==2:#tercera imagen(2)
        figura = Image.open('trash/figura{}.png'.format(cc)).rotate(-15)
    else:#cuarta imagen (3)
        figura = Image.open('trash/figura{}.png'.format(cc)).rotate(15)
    fondo = Image.new('RGB', figura.size, (255, 255, 255))
    mascara = Image.open('trash/plantilla{}.png'.format(cc)).convert('L').resize(figura.size) #convert('L') convierte a escala de grises para guardar la luminancia
    im = Image.composite(fondo, figura, mascara)
    im.save('girada{}.png'.format(cc))
    cc= cc+1
