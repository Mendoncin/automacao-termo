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

lista1 = []

for palavra in palavras:
    if len(palavra) == 5:
        palavra = unicodedata.normalize('NFKD', palavra)
        caracteres_sem_acento = []
        for char in palavra:
            if not unicodedata.combining(char):
                caracteres_sem_acento.append(char)
        palavra = ''.join(caracteres_sem_acento)
        lista1.append(palavra)



lista1 = list(set(lista1))

pyautogui.press("win")
pyautogui.write("chrome")

pyautogui.PAUSE = 2.5

pyautogui.press("enter")

pyautogui.click(x=946, y=616)

# pyautogui.hotkey('ctrl', 'shift', 'n')    para teste

pyautogui.write(url)
pyautogui.press('enter')

pyautogui.click(x=946, y=616)

pyautogui.write('boiar')
pyautogui.press('enter')
pyautogui.write('lutem')
pyautogui.press('enter')
pyautogui.write('pando')
pyautogui.press('enter')
pyautogui.write('vesgo')
pyautogui.press('enter')
pyautogui.write('ficha')
pyautogui.press('enter')


screenshot = pyautogui.screenshot(region=(769, 291, 380, 388))
screenshot.save('termo.png')

image = cv2.imread("termo.png")

coordenadas = [[11, 68], [84, 65], [212, 65], [241, 71], [317, 66], [8 ,140], [83 ,137], [160, 139], [237, 144], [316, 145], [10, 210], [83, 216], [164, 215], [237, 214], [313, 218], [10, 297], [83, 297], [164, 297], [237, 297], [313, 297], [10, 379], [83, 379], [164, 379], [237, 379], [313, 379]]

contador = 0
letras = ['b', 'o', 'i', 'a', 'r', 'l', 'u', 't', 'e', 'm', 'p', 'a', 'n', 'd', 'o', 'v', 'e', 's', 'g', 'o', 'f', 'i', 'c', 'h', 'a']

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


