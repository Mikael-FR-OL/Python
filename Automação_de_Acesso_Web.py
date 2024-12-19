import pyautogui

def youtube():
    pyautogui.PAUSE = 0.5
    pyautogui.press("win")
    pyautogui.write("Microsoft Edge")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    # x=534, y=62
    pyautogui.click(x=21439, y=212)
    pyautogui.click(x=512, y=280)
    pyautogui.sleep(3)
    pyautogui.click(x=206, y=156)
    pyautogui.sleep(1)
    pyautogui.click(x=637, y=167)

def desecsecurity():
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    pyautogui.write('Microsoft Edge')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.click(x=1439, y=212)
    pyautogui.click(x=390, y=58)
    pyautogui.write("https://desecsecurity.com/academy/login")
    pyautogui.press('enter')

def alura():
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    pyautogui.write('Microsoft Edge')
    pyautogui.press('enter')
    pyautogui.sleep(1)
    pyautogui.click(x=1439, y=212)
    pyautogui.click(x=390, y=58)
    pyautogui.write("https://cursos.alura.com.br/loginForm?urlAfterLogin=%5BaHR0cHM6Ly9jdXJzb3MuYWx1cmEuY29tLmJyL2Rhc2hib2FyZA%5D")
    pyautogui.press('enter')
    pyautogui.click(x=961, y=878)
    pyautogui.sleep(1)
    pyautogui.doubleClick(x=550, y=611)

def interface():
    print("[1] -> Youtube")
    print("[2] -> DesecSecurity")
    print("[3] -> Alura")

def verifica():
    interface()
    opcoes = {1: "Youtube", 2: "DesecSecurity", 3: "Alura"}
    entrada = input("Digite uma opção: ")

    try:
        escolha = int(entrada)

        if escolha in opcoes:
            if opcoes[escolha] == "Youtube":
                youtube()
            if opcoes[escolha] == "DesecSecurity":
                desecsecurity()
            if opcoes[escolha] == "Alura":
                alura()
        else:
            print("Opção inválida. Por favor, escolha uma das opções disponíveis.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente a uma das opções.")

verifica()
