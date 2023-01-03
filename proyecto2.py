import cv2
import numpy as np
import math

#-----------------------------------------#
 # Se leen y se importan imagenes #
 #-----------------------------------------#
image = cv2.imread('vocales.png')
font = cv2.FONT_HERSHEY_SIMPLEX # se define la fuente

# Pasamos la imagen a escala de grises #

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold tipo THRESH_BINARY_INV
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
#TRESH: Conjunto de valores de umbral utilizados para cuantificar una imagen

# expandir (dilatar bordes)
kernel = np.ones((10, 1), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#cv2.dilate agrega una capa adicional de píxeles en una estructura
# revisa los contornos en el thresh
# contorno, jerarquia(exterior a interior) (imagen | modo | metodo)
ctrs, jer = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
# (copia de la imagen dilatada | devuelve los contornos exteriores|Comprime segmentos horizontales, verticales y diagonales y deja solo sus puntos finales.)
# se ordena el contorno
# Conjunto de puntos de entrada 2D
orden_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(orden_ctrs):
    # obtener el cuadro delimitador #
    x, y, w, h = cv2.boundingRect(ctr)
    # obteniendo la region de interes #
    roi = image[y:y + h, x:x + w]
    # mostrando la region de las letras
    #imagen |vertices| vertices opuestos| color | grosor 
    # #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    if w > 15 and h > 15:
        cv2.imwrite('vocalesfalse{}.png'.format(i), roi) #guardar

numpy_vertical = np.vstack((image))   
cc = 0
f1 = 70

for i, ctr in enumerate(orden_ctrs):
    imagen = cv2.imread('vocalesfalse{}.png'.format(i)) #leer las imagenes
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # se pasa a 1 channel
    moments = cv2.moments(imagen) #para asi leer los momentos
    humoments = cv2.HuMoments(moments) #se leen los momentos de hu
    print ('Momentos de Hu {}: '.format(i), humoments)
    if i==0:
        while cc<=6:
            #(arreglo, decimales) ,(posicion),fuente,tamaño letra,color,grosor
            cv2.putText(numpy_vertical,str(round(math.log(humoments[cc][0]),2)),(f1,122), font, .3,(0,255,0),1) #A
            cc=cc+1
            f1 = f1+70
        cc = 0
        f1 = 70
    elif i==1:
        while cc<=6:
            cv2.putText(numpy_vertical,str(round(math.log(humoments[cc][0]),2)),(f1,140), font, .3,(0,255,0),1) #E
            cc=cc+1
            f1 = f1+70
        cc = 0
        f1 = 70
    elif i==2:
        while cc<=6:
            cv2.putText(numpy_vertical,str(round(math.log(humoments[cc][0]),2)),(f1,156), font, .3,(0,255,0),1) #I
            cc=cc+1
            f1 = f1+70
        cc = 0
        f1 = 70
    elif i==3:
        while cc<=6:
            cv2.putText(numpy_vertical,str(round(math.log(humoments[cc][0]),2)),(f1,174), font, .3,(0,255,0),1) #O
            cc=cc+1
            f1 = f1+70
        cc = 0
        f1 = 70
    else:
        while cc<=6:
            cv2.putText(numpy_vertical,str(round(math.log(humoments[cc][0]),2)),(f1,190), font, .3,(0,255,0),1) #U
            cc=cc+1
            f1 = f1+70




        

