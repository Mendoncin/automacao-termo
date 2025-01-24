import pyautogui
import cv2
import numpy as np
import unicodedata


url = 'https://term.ooo/'
pyautogui.PAUSE = 0.7

wordlist_path = "wordsList"

with open(wordlist_path, 'r', encoding='latin-1') as wordlist:
    palavras = []
    for linha in wordlist:
        palavras.append(linha.strip())

lista1 = list(set(palavras))

palpites = ['boiar', 'lutem', 'pando', 'vesgo', 'ficha']

pyautogui.press("win")
pyautogui.write("chrome")

pyautogui.PAUSE = 2.5

pyautogui.press("enter")

pyautogui.click(x=946, y=616)

pyautogui.hotkey('ctrl', 'shift', 'n')      #para testar

pyautogui.write(url)
pyautogui.press('enter')

pyautogui.click(x=946, y=616)

letras = []

for palpite in palpites:
    pyautogui.write(palpite)
    pyautogui.press('enter')
    for letra in palpite:
        letras.append(letra)


screenshot = pyautogui.screenshot(region=(769, 291, 380, 388))
screenshot.save('termo.png')

image = cv2.imread("termo.png")

coordenadas = []

x_inicial = 10
y_inicial = 65
incremento = 75

for linha in range(5): 
    for coluna in range(5):
        x = x_inicial + (coluna * incremento)
        y = y_inicial + (linha * incremento) 
        coordenadas.append([x, y])
contador = 0

for x, y in coordenadas:
    posicao_letra = (contador % 5)
    auxiliar = []
    b, g, r = image[y, x]
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = hsv_image[y, x]

    pixel_hsv = np.array([h, s, v])    
    if h == 171:
        for palavra in lista1:
            if not letras[contador] in palavra:
                auxiliar.append(palavra)
    elif h == 19:
        for palavra in lista1:
                if letras[contador] in palavra and palavra[posicao_letra] != letras[contador]:
                    auxiliar.append(palavra)
    elif h == 86:
        for palavra in lista1:
            if palavra[posicao_letra] == letras[contador]:
                auxiliar.append(palavra)
    contador +=1

    lista1 = []
    for palavra in auxiliar:
        lista1.append(palavra)

if len(lista1) == 1:
    pyautogui.write(lista1[0])
    pyautogui.press('enter')
else:
    print(lista1)


