#Form Tutor Management System
import sys #this allows you to use the sys.exit command to quit/logout of the application
import textwrap
from textwrap import fill
import os
import time
def main():
    #Dimencionando a Tela de LOGIN
    os.system('mode con: cols=30 lines=15')
    #Capturando o largo da tela de Login
    ts = os.get_terminal_size()
    Tela_centro_Login=ts.columns-1
    #Teste para ver o tamanho do largo da tela de login
    print (Tela_centro_Login)
    time.sleep(1)
    #Iniciando o numero de tentativas para o Password
    Tentativas=0
    #Chama na função de Login
    login(Tela_centro_Login,Tentativas)

#FUNÇÃO QUE ACESSA NA PLATAFORMA DE LOGIN
def login(Tela_centro_Login,Tentativas):
    #NOME E SENHA PARA ACCESAR AO PROGRAMA
    username="AA"
    password="XX"
    #Redimencionando a Tela de LOGIN
    os.system('mode con: cols=30 lines=15')
    #Limpando a tela
    clear = lambda: os.system('cls')
    clear()
    #Incrementando o numero de tentativas para o acceso no sistema
    Tentativas=Tentativas+1
    #Disenhando o Formulario de Senha
    print ("\n\n\n")
    print ("        SENHA:".center(15))
    print ("")
    Text_Username="     USUARIO: ".center(10)
    Text_Password="     CONTRASENHA: ".center(10)
    answer1=input(Text_Username)
    answer2=input(Text_Password)
    #Validando o NOME E SENHA para acessar no Sistema
    if answer1==username and answer2==password:
        #Limpando a tela se esta correta o NOME E SENHA para dar Benvida!!!
        clear = lambda: os.system('cls')
        clear()
        #Escrevendo a BEMVINDA para o Acceso no sistema
        print ("\n\n\n")
        Text_benvinda="BENVINDO NO PROGRAMA"
        print ("")
        print(center_wrap(Text_benvinda, cwidth=Tela_centro_Login, width=37))
        #Capturando por dois segundo a Escrita de BENVINDA
        time.sleep(2)
        #Dimensionando a tela de MENU
        os.system('mode con: cols=70 lines=20')
        #Capturando o largo da tela de MENU
        ts = os.get_terminal_size()
        Tela_centro_Menu=ts.columns-1
        #Chama a Função de Menu
        menu(Tela_centro_Menu)
    else:
        if (Tentativas<3):
            #Chama na recurrencia da Função para escrever denovo o NOME E SENHA até 3 VEZES
            login(Tela_centro_Login,Tentativas)
        else:
            #Caso as tentativas acabaram
            print ('')
            print (center_wrap("CONTRASENHA INVALIDA!!!", cwidth=Tela_centro_Login, width=37))

#FUNÇÃO QUE ESCREVE AS LETRAS NO MEDIO DA TELA DIMENSIONADA
def center_wrap(text, cwidth=100, **kw):
    lines = textwrap.wrap(text, **kw)
    return "\n".join(line.center(cwidth) for line in lines)

#FUNÇÃO QUE ACESSA NA PLATAFORMA DE MENU
def menu(Tela_centro_Menu):
    Text_Menu="\n\
╔══════════════════════════════════╗\n\
║               Menu               ║\n\
╠══════════════════════════════════╣\n\
║ Opcoes:                          ║\n\
║     1) Atualizar Base de Dados   ║\n\
║     2) Elegir Estado             ║\n\
║     3) Mostrar Resultados        ║\n\
║     4) Guardar Resultados        ║\n\
║     5) Salir                     ║\n\
║                                  ║\n\
╠══════════════════════════════════╣\n\
║               DGD                ║\n\
╚══════════════════════════════════╝\n"
    print(center_wrap(Text_Menu, cwidth=Tela_centro_Menu, width=37))
    opcao = input("Ingresse uma Opcao: ")
    if opcao == "1":
        Atualizar_BD()
    elif opcao == "2":
        viewstudentdetails()
    elif opcao == "3":
        searchbyid()
    elif opcao=="4":
        producereports()
    elif opcao=="5":
        sys.exit
    else:
        clear = lambda: os.system('cls')
        clear()
        print("\n")
        print("Só selecionar as opções 1,2,3,4 or 5.".center(Tela_centro_Menu))
        print("Porfavor Ingrese de Novo:".center(Tela_centro_Menu))
        print("")
        menu(Tela_centro_Menu)

def Atualizar_BD():
    os.system('mode con: cols=75 lines=20')
    clear = lambda: os.system('cls')
    clear()
    print ('PROGRAMA 1')
    pass
    #Teacher will enter student details manually
    #These will be appended to the csv file

def viewstudentdetails():
    pass
#Teacher can press a button to view all students at a glance

def searchbyid():
    pass
    #Teacher can input an ID number and display the relevant student's details

def producereports():
    pass
    #Teacher can produce clever reports such as:
    #a) list of names of males and email addresses (to email a reminder about boys football club)
    #b) list of names of females in specific postcode (to remind them of a girls coding club in the area)
    #c) list of all names, birthdays and addresses (to send out birthday cards!)


#the program is initiated, so to speak, here
main()
