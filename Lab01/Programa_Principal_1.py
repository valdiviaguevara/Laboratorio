from functools import partial
from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import shutil
import pandas as pd
#Librerias para Graficar
from string import ascii_letters
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
#from pandastable import Table,TableModel
master=Tk()
def main(master):
	app_janela_Conect_BD=janela_Conect_BD.Inicializando()
	master.mainloop()
#================================================================================================================
#=========================CLASSE CONECCION=======================================================================
#================================================================================================================
class janela_Conect_BD:
	def bt_Conectar_Click(txt_Servidor,txt_Base_Dados):
		if (txt_Servidor.get()=="servidor" and txt_Base_Dados.get()=="bd_dgd"):
			master.destroy()
			master_janela_Login=Tk()
			app_janela_Login=janela_Login.Inicializando(master_janela_Login)
			master_janela_Login.mainloop()
			print (txt_Servidor.get())
			print (txt_Base_Dados.get())
		else:
			messagebox.showwarning("ALERTA PERIGO!!","Dados Incorretos!!")
	def bt_Sair_Click():
		if (messagebox.askyesno("SAIR!!","Verdaderamente quer sair?")):
			messagebox.showinfo("Informação","Volte Sempre!")
			master.quit()
	def Inicializando():
		master.title("CONECTAR_BASE_DADOS SQL")
		master["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master.geometry("330x120+400+250")
		#Insertando os Labels Servidor
		lb_Servidor=Label(master,text="Servidor SQL :",bg="light goldenrod")
		lb_Servidor.place(x=50,y=10)
		#Insertando as caixas de Textos Servidor
		txt_Servidor=Entry(master)
		txt_Servidor.place(x=140,y=10)
		#Insertando os Labels Base de Dados
		lb_Base_Dados=Label(master,text="Base de Dados:",bg="light goldenrod")
		lb_Base_Dados.place(x=50,y=40)
		#Insertando as caixas de Textos Base de Dados
		txt_Base_Dados=Entry(master)
		txt_Base_Dados.place(x=140,y=40)
		#Instertando os BOtoes
		bt_Conectar=Button(master,width=9,text="Conectar")
		bt_Conectar["command"]=partial(janela_Conect_BD.bt_Conectar_Click,txt_Servidor,txt_Base_Dados)
		bt_Conectar.place(x=50,y=80)
		bt_Sair=Button(master,width=8,text="Sair",command=janela_Conect_BD.bt_Sair_Click)
		bt_Sair.place(x=200,y=80)
#================================================================================================================
#=========================CLASSE LOGIN===========================================================================
#================================================================================================================
class janela_Login:
	def bt_Entrar_Click(txt_Usuario,txt_Senha,master_janela_Login):
		if (txt_Usuario.get()=="juan" and txt_Senha.get()=="an"):
			master_janela_Login.destroy()
			master_janela_Modelos=Tk()
			app_janela_Modelos=janela_Modelos.Inicializando(master_janela_Modelos)
			master_janela_Modelos.mainloop()
			print (txt_Usuario.get())
			print (txt_Senha.get())
		else:
			messagebox.showwarning("ALERTA PERIGO!!","Dados Incorretos!!")
	def Inicializando(master_janela_Login):
		master_janela_Login.title("LOGIN")
		master_janela_Login["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master_janela_Login.geometry("270x110+400+250")
		#Insertando os Labels Servidor
		lb_Usuario=Label(master_janela_Login,text="USUARIO:",bg="light goldenrod")
		lb_Usuario.place(x=20,y=10)
		#Insertando as caixas de Textos Servidor
		txt_Usuario=Entry(master_janela_Login)
		txt_Usuario.place(x=110,y=10)
		#Insertando os Labels Base de Dados
		lb_Senha=Label(master_janela_Login,text="SENHA  :",bg="light goldenrod")
		lb_Senha.place(x=20,y=40)
		#Insertando as caixas de Textos Base de Dados
		txt_Senha=Entry(master_janela_Login)
		txt_Senha.place(x=110,y=40)
		#Instertando os BOtoes
		bt_Entrar=Button(master_janela_Login,width=9,text="Entrar")
		bt_Entrar["command"]=partial(janela_Login.bt_Entrar_Click,txt_Usuario,txt_Senha,master_janela_Login)
		bt_Entrar.place(x=100,y=75)
#================================================================================================================
#=========================CLASSE MENUS MODELOS===================================================================
#================================================================================================================
class janela_Modelos:
	#================================================================================================================
	#================================================================================================================
	#Funcao para chamar pelo menu no Projeto Agricola
	def bt_Projeto_Treinamento_Agricola_mn_Click():
		#Projeto_Escolhido="Agricola"
		master_janela_APP_MODELO_TREINAMENTO=Tk()
		app_janela_Plataforma_SQL=janela_APP_MODELO_TREINAMENTO.Inicializando(master_janela_APP_MODELO_TREINAMENTO)
		master_janela_APP_MODELO_TREINAMENTO.mainloop()
		print("Entrou no projeto Agricola")
	#Funcao para chamar pelo menu no Projeto Pecuario
	def bt_Projeto_Treinamento_Pecuario_mn_Click():
		#Projeto_Escolhido="Pecuario"
		master_janela_APP_MODELO_TREINAMENTO=Tk()
		app_janela_Plataforma_SQL=janela_APP_MODELO_TREINAMENTO.Inicializando(master_janela_APP_MODELO_TREINAMENTO)
		master_janela_APP_MODELO_TREINAMENTO.mainloop()
		print("Entrou no projeto Pecuario")
	#Funcao para chamar pelo boton e combobox nos Projetos
	def bt_Entrar_Projeto_cmb_Click(cmb_Projectos):
		if (cmb_Projectos.get()=="Agricola"):
			Projeto_Escolhido="Agricola"
			master_janela_APP_MODELO_TREINAMENTO=Tk()
			app_janela_APP_MODELO_TREINAMENTO=janela_APP_MODELO_TREINAMENTO.Inicializando(master_janela_APP_MODELO_TREINAMENTO)
			master_janela_APP_MODELO_TREINAMENTO.mainloop()
			print("Entrou no "+ cmb_Projectos.get())
		if (cmb_Projectos.get()=="Pecuario"):
			Projeto_Escolhido="Pecuario"
			master_janela_APP_MODELO_TREINAMENTO=Tk()
			app_janela_APP_MODELO_TREINAMENTO=janela_APP_MODELO_TREINAMENTO.Inicializando(master_janela_APP_MODELO_TREINAMENTO)
			master_janela_APP_MODELO_TREINAMENTO.mainloop()
			print("Entrou no "+ cmb_Projectos.get())
	#================================================================================================================
	#================================================================================================================
		#Funcao para chamar pelo menu no Projeto Agricola
	def bt_SQL_SERVER_Agricola_mn_Click():
		Projeto_Escolhido="Agricola"
		master_janela_Plataforma_SQL=Tk()
		app_janela_Plataforma_SQL=janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido)
		master_janela_Plataforma_SQL.mainloop()
		print("Entrou no projeto Agricola")
	#Funcao para chamar pelo menu no Projeto Pecuario
	def bt_SQL_SERVER_Pecuario_mn_Click():
		Projeto_Escolhido="Pecuario"
		master_janela_Plataforma_SQL=Tk()
		app_janela_Plataforma_SQL=janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido)
		master_janela_Plataforma_SQL.mainloop()
		print("Entrou no projeto Pecuario")
	#Funcao para chamar pelo boton e combobox na Plataforma de SQL
	def bt_Entrar_SQL_SERVER_cmb_Click(cmb_Projectos):
		if (cmb_Projectos.get()=="Agricola"):
			Projeto_Escolhido="Agricola"
			master_janela_Plataforma_SQL=Tk()
			app_janela_Plataforma_SQL=janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido)
			master_janela_Plataforma_SQL.mainloop()
			print("Entrou no "+ cmb_Projectos.get())
		if (cmb_Projectos.get()=="Pecuario"):
			Projeto_Escolhido="Pecuario"
			master_janela_Plataforma_SQL=Tk()
			app_janela_Plataforma_SQL=janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido)
			master_janela_Plataforma_SQL.mainloop()
			print("Entrou no "+ cmb_Projectos.get())
	#================================================================================================================
	#================================================================================================================
	#Funcao para chamar pelo menu na plataforma Entregavel Agricola
	def bt_Entregavel_Agricola_mn_Click():
		master_janela_APP_MODELO_RECORRENTE=Tk()
		app_janela_APP_MODELO_RECORRENTE=janela_APP_MODELO_RECORRENTE.Inicializando(master_janela_APP_MODELO_RECORRENTE)
		master_janela_APP_MODELO_RECORRENTE.mainloop()
	#Funcao para chamar pelo menu na plataforma Entregavel Pecuario
	def bt_Entregave_Pecuario_mn_Click():
		master_janela_APP_MODELO_RECORRENTE=Tk()
		app_janela_APP_MODELO_RECORRENTE=janela_APP_MODELO_RECORRENTE.Inicializando(master_janela_APP_MODELO_RECORRENTE)
		master_janela_APP_MODELO_RECORRENTE.mainloop()
	#Funcao para chamar pelo boton e combobox na Plataforma Projeto Entregavel
	def bt_Entrar_Projeto_Entregavel_cmb_Click(cmb_Projectos_Entregavel):
		if (cmb_Projectos_Entregavel.get()=="Agricola"):
			Projeto_Escolhido="Agricola"
			master_janela_APP_MODELO_RECORRENTE=Tk()
			app_janela_APP_MODELO_RECORRENTE=janela_APP_MODELO_RECORRENTE.Inicializando(master_janela_APP_MODELO_RECORRENTE)
			master_janela_APP_MODELO_RECORRENTE.mainloop()
			print("Entrou no "+ cmb_Projectos_Entregavel.get())
		if (cmb_Projectos_Entregavel.get()=="Pecuario"):
			Projeto_Escolhido="Pecuario"
			master_janela_APP_MODELO_RECORRENTE=Tk()
			app_janela_APP_MODELO_RECORRENTE=janela_APP_MODELO_RECORRENTE.Inicializando(master_janela_APP_MODELO_RECORRENTE)
			master_janela_APP_MODELO_RECORRENTE.mainloop()
			print("Entrou no "+ cmb_Projectos_Entregavel.get())
	#================================================================================================================
	#================================================================================================================
	#Funcao para chamar pelo menu no Monitoramento Agricola
	def bt_Monitoramento_Treino_Agricola_mn_Click():
		Projeto_Escolhido="Agricola"
		master_janela_APP_MONITORAMENTO_TREINO=Tk()
		app_janela_APP_MONITORAMENTO_TREINO=janela_APP_MONITORAMENTO_TREINO.Inicializando(master_janela_APP_MONITORAMENTO_TREINO,Projeto_Escolhido)
		master_janela_APP_MONITORAMENTO_TREINO.mainloop()
		print("Entrou no Monitoramento Agricola")
	#Funcao para chamar pelo menu no Monitoramento Pecuario
	def bt_Monitoramento_Treino_Pecuario_mn_Click():
		Projeto_Escolhido="Pecuario"
		master_janela_APP_MONITORAMENTO_TREINO=Tk()
		app_janela_APP_MONITORAMENTO_TREINO=janela_APP_MONITORAMENTO_TREINO.Inicializando(master_janela_APP_MONITORAMENTO_TREINO,Projeto_Escolhido)
		master_janela_APP_MONITORAMENTO_TREINO.mainloop()
		print("Entrou no Monitoramento Pecuario")
	#Funcao para chamar pelo boton e combobox no Monitoramento do Treino
	def bt_Entrar_Monitoramento_Treino_cmb_Click(cmb_Projectos_Monitoramento):
		if (cmb_Projectos_Monitoramento.get()=="Agricola"):
			master_janela_APP_MONITORAMENTO_TREINO=Tk()
			app_janela_APP_MONITORAMENTO_TREINO=janela_APP_MONITORAMENTO_TREINO.Inicializando(master_janela_APP_MONITORAMENTO_TREINO,cmb_Projectos_Monitoramento.get())
			master_janela_APP_MONITORAMENTO_TREINO.mainloop()
			print("Entrou no "+ cmb_Projectos_Entregavel.get())
		if (cmb_Projectos_Monitoramento.get()=="Pecuario"):
			master_janela_APP_MONITORAMENTO_TREINO=Tk()
			app_janela_APP_MONITORAMENTO_TREINO=janela_APP_MONITORAMENTO_TREINO.Inicializando(master_janela_APP_MONITORAMENTO_TREINO,cmb_Projectos_Monitoramento.get())
			master_janela_APP_MONITORAMENTO_TREINO.mainloop()
			print("Entrou no "+ cmb_Projectos_Entregavel.get())
	#================================================================================================================
	#================================================================================================================
	#Funcao para chamar pelo menu no Monitoramento Agricola
	def bt_Monitoramento_Entregavel_Agricola_mn_Click():
		#Projeto_Escolhido="Agricola"
		#master_janela_APP_MONITORAMENTO_TREINO=Tk()
		#app_janela_APP_MONITORAMENTO_TREINO=janela_APP_MONITORAMENTO_TREINO.Inicializando(master_janela_APP_MONITORAMENTO_TREINO,Projeto_Escolhido)
		#master_janela_APP_MONITORAMENTO_TREINO.mainloop()
		print("Entrou no Monitoramento Entregavel Agricola")
	#Funcao para chamar pelo menu no Monitoramento Pecuario
	def bt_Monitoramento_Entregavel_Pecuario_mn_Click():
		#Projeto_Escolhido="Pecuario"
		#master_janela_APP_MONITORAMENTO_TREINO=Tk()
		#app_janela_APP_MONITORAMENTO_TREINO=janela_APP_MONITORAMENTO_TREINO.Inicializando(master_janela_APP_MONITORAMENTO_TREINO,Projeto_Escolhido)
		#master_janela_APP_MONITORAMENTO_TREINO.mainloop()
		print("Entrou no Monitoramento Entregavel Pecuario")
	#Funcao para chamar pelo boton e combobox no Monitoramento do Entregavel
	def bt_Entrar_Monitoramento_Entregavel_cmb_Click(cmb_Projectos_Monitoramento):
		if (cmb_Projectos_Monitoramento.get()=="Agricola"):
			Projeto_Escolhido="Agricola"
			print("Entrou no "+ cmb_Projectos_Monitoramento.get())
		if (cmb_Projectos_Monitoramento.get()=="Pecuario"):
			Projeto_Escolhido="Pecuario"
			print("Entrou no "+ cmb_Projectos_Monitoramento.get())
	def bt_Sair_Click():
		if (messagebox.askyesno("SAIR!!","Verdaderamente quer sair?")):
			messagebox.showinfo("Informação","Volte Sempre!")
			master_janela_Modelos.quit()
	def Inicializando(master_janela_Modelos):
		master_janela_Modelos.title("LISTA DE MODELOS")
		master_janela_Modelos["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master_janela_Modelos.geometry("350x300+400+250")
		#Insertndo um frame para os menus
		#frm_Menu=Frame(master_janela_Modelos)
		#frm_Menu.pack()
		#Insertando a lista de Menus
		mn_Menu=Menu(master_janela_Modelos)
		#Sub Menus Pojetos
		mn_Sub_Menu_Projetos=Menu(mn_Menu)
		mn_Menu.add_cascade(label="Treinar Modelo",menu=mn_Sub_Menu_Projetos)
		mn_Sub_Menu_Projetos.add_command(label="Plataforma SQL SERVER Agricola",command=janela_Modelos.bt_SQL_SERVER_Agricola_mn_Click)
		mn_Sub_Menu_Projetos.add_command(label="Plataforma SQL SERVER Pecuario",command=janela_Modelos.bt_SQL_SERVER_Pecuario_mn_Click)
		mn_Sub_Menu_Projetos.add_separator()
		mn_Sub_Menu_Projetos.add_command(label="Plataforma Treinamento Agricola",command=janela_Modelos.bt_Projeto_Treinamento_Agricola_mn_Click)
		mn_Sub_Menu_Projetos.add_command(label="Plataforma Treinamento Pecuario",command=janela_Modelos.bt_Projeto_Treinamento_Pecuario_mn_Click)
		mn_Sub_Menu_Projetos.add_separator()
		mn_Sub_Menu_Projetos.add_command(label="Sair",command=janela_Modelos.bt_Sair_Click)
		#Sub Menu Entregavel
		mn_Entregavel=Menu(mn_Menu)
		mn_Entregavel.add_command(label="Plataforma Entregavel Agricola",command=janela_Modelos.bt_Entregavel_Agricola_mn_Click)
		mn_Entregavel.add_command(label="Plataforma Entregavel Pecuario",command=janela_Modelos.bt_Entregave_Pecuario_mn_Click)
		mn_Menu.add_cascade(label="Executar Modelo",menu=mn_Entregavel)
		#Sub Menu Monitoramento
		mn_Monitoramento=Menu(mn_Menu)
		mn_Monitoramento.add_command(label="Treino Agricola",command=janela_Modelos.bt_Monitoramento_Treino_Agricola_mn_Click)
		mn_Monitoramento.add_command(label="Treino Pecuario",command=janela_Modelos.bt_Monitoramento_Treino_Pecuario_mn_Click)
		mn_Monitoramento.add_separator()
		mn_Monitoramento.add_command(label="Entregavel Agricola",command=janela_Modelos.bt_Monitoramento_Entregavel_Agricola_mn_Click)
		mn_Monitoramento.add_command(label="Entregavel Pecuario",command=janela_Modelos.bt_Monitoramento_Entregavel_Pecuario_mn_Click)
		mn_Menu.add_cascade(label="Monitoramento",menu=mn_Monitoramento)
		master_janela_Modelos.config(menu=mn_Menu)
		#Insertando o label para o contexto inicial 	
		lb_Text_Inicial=Label(master_janela_Modelos,text="\n'Escolhe uma das opções para processar \n PROJETOS ou MONITORAMENTO'\n",bg="light goldenrod")
		lb_Text_Inicial.pack(side=TOP)
		#Insertando os tabs para os Projetos  e Monitoramento
		tb=ttk.Notebook(master_janela_Modelos)
		#Tab Projeto
		pagina_Treinamento=ttk.Frame(tb)
		tb.add(pagina_Treinamento,text="Treinar Modelo")
		tb.pack(expand=YES,fill=X)
		#Insertando o label para o contexto inicial 
		lb_Text_Inicial=Label(pagina_Treinamento,text="Escolher Projeto: ",bg="light goldenrod")
		lb_Text_Inicial.place(x=30,y=10)
		#Instar o Combobox para escolher o Projeto
		cmb_Projectos=ttk.Combobox(pagina_Treinamento,width=15)
		cmb_Projectos['values']=("Agricola","Pecuario")
		cmb_Projectos.place(x=50,y=40)
		cmb_Projectos.current(0)
		#Instertando o botao para entrar aos projetos para rodar SQL_SERVER
		bt_SQL_SERVER=Button(pagina_Treinamento,width=13,text="Plataforma \nSQL SERVER")
		bt_SQL_SERVER["command"]=partial(janela_Modelos.bt_Entrar_SQL_SERVER_cmb_Click,cmb_Projectos)
		bt_SQL_SERVER.place(x=180,y=40)
		#Instertando o botao para entrar aos projetos para seu Treinanmento
		bt_Entrar_treino=Button(pagina_Treinamento,width=13,text="Plataforma \nTreinamento")
		bt_Entrar_treino["command"]=partial(janela_Modelos.bt_Entrar_Projeto_cmb_Click,cmb_Projectos)
		bt_Entrar_treino.place(x=180,y=90)
		#Tab Entregavel
		pagina_Entregavel=ttk.Frame(tb)
		tb.add(pagina_Entregavel,text="Executar Modelo")
		tb.pack(expand=1,fill='both')
		#Insertando o label para o contexto inicial 
		lb_Text_Inicial=Label(pagina_Entregavel,text="Escolher Projeto:",bg="light goldenrod")
		lb_Text_Inicial.place(x=30,y=10)
		#Instar o Combobox para escolher os projetos para o Entregavel
		cmb_Projectos_Entregavel=ttk.Combobox(pagina_Entregavel,width=15)
		cmb_Projectos_Entregavel['values']=("Agricola","Pecuario")
		cmb_Projectos_Entregavel.place(x=50,y=40)
		cmb_Projectos_Entregavel.current(0)
		#Instertando o botao  Entregavel
		bt_Entrar_Modelo=Button(pagina_Entregavel,width=13,text="Plataforma \nEntregavel")
		bt_Entrar_Modelo["command"]=partial(janela_Modelos.bt_Entrar_Projeto_Entregavel_cmb_Click,cmb_Projectos_Entregavel)
		bt_Entrar_Modelo.place(x=180,y=40)
		#Tab Monitoramento
		pagina_Monitoramento=ttk.Frame(tb)
		tb.add(pagina_Monitoramento,text="Monitoramento")
		tb.pack(expand=1,fill='both')
		#Insertando o label para o contexto inicial 
		lb_Text_Inicial=Label(pagina_Monitoramento,text="Escolher Projeto:",bg="light goldenrod")
		lb_Text_Inicial.place(x=30,y=10)
		#Instar o Combobox para escolher os projetos para o Monitoramento
		cmb_Projectos_Monitoramento=ttk.Combobox(pagina_Monitoramento,width=15)
		cmb_Projectos_Monitoramento['values']=("Agricola","Pecuario")
		cmb_Projectos_Monitoramento.place(x=50,y=40)
		cmb_Projectos_Monitoramento.current(0)
		#Instertando o botao para entrar aos monitoramentos do Treino
		bt_Entrar_Monitoramento_Treino=Button(pagina_Monitoramento,width=33,text="Plataforma Monitoramento Treino")
		bt_Entrar_Monitoramento_Treino["command"]=partial(janela_Modelos.bt_Entrar_Monitoramento_Treino_cmb_Click,cmb_Projectos_Monitoramento)
		bt_Entrar_Monitoramento_Treino.place(x=50,y=80)
		#Instertando o botao para entrar aos monitoramentos dos Entregaveis
		bt_Entrar_Monitoramento_Entregavel=Button(pagina_Monitoramento,width=33,text="Plataforma Monitoramento Entregavel")
		bt_Entrar_Monitoramento_Entregavel["command"]=partial(janela_Modelos.bt_Entrar_Monitoramento_Entregavel_cmb_Click,cmb_Projectos_Monitoramento)
		bt_Entrar_Monitoramento_Entregavel.place(x=50,y=120)
		#Instertando o botao para Sair do Program
		bt_Sair=Button(master_janela_Modelos,width=9,text="Sair")
		bt_Sair["command"]=partial(janela_Modelos.bt_Sair_Click)
		bt_Sair.pack(side=BOTTOM)
#================================================================================================================
#=========================CLASSE PLATAFORMA SQL===========================================================================
#================================================================================================================
class janela_Plataforma_SQL:
	def bt_Executar_Script_SQL_Click(txt_Projeto):
		print ("AQUI VEM O CODIGO FEITO EM SQL-SERVER")
	def bt_Mostrar_Tabela_Click(txt_Projeto):
		pass
	def bt_Exportar_Base_Click(txt_Projeto):
		print ("Exportando Base Dados....")
	def bt_Cerrar_Janela_Click(txt_Projeto,master_janela_Plataforma_SQL):
		if (messagebox.askyesno("Cerrar!!","Quere cerrar?")):
			master_janela_Plataforma_SQL.destroy()
	def Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido):
		master_janela_Plataforma_SQL.title("PLATAFORMA SQL SERVER "+Projeto_Escolhido.upper())
		master_janela_Plataforma_SQL["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master_janela_Plataforma_SQL.geometry("870x650+40+20")
		#Insertando os Labels com a descripcao
		lb_descripcao=Label(master_janela_Plataforma_SQL,text="\n'Este front permite rodar o script SQL Server \n Assim como tambem exporta a base tratada no formato .csv'\n:",bg="light goldenrod")
		lb_descripcao.place(x=120,y=10)
		#Insertando botao de Excutar Script SQL
		bt_Executar_Script=Button(master_janela_Plataforma_SQL,width=23,text="Executar Script SQL")
		bt_Executar_Script["command"]=partial(janela_Plataforma_SQL.bt_Executar_Script_SQL_Click,Projeto_Escolhido)
		bt_Executar_Script.place(x=120,y=80)
		#Insertando botao de Excutar Script SQL
		bt_Mostrar_Tabela=Button(master_janela_Plataforma_SQL,width=21,text="Mostrar Informação")
		bt_Mostrar_Tabela["command"]=partial(janela_Plataforma_SQL.bt_Mostrar_Tabela_Click,Projeto_Escolhido)
		bt_Mostrar_Tabela.place(x=580,y=80)
		#
		#
		#
		#Insertando botao de Exportar Base
		bt_Exportar_Base=Button(master_janela_Plataforma_SQL,width=15,text="Exportar Base")
		bt_Exportar_Base["command"]=partial(janela_Plataforma_SQL.bt_Exportar_Base_Click,Projeto_Escolhido)
		bt_Exportar_Base.place(x=140,y=600)
		#Insertando botao de Cerrar
		bt_Cerrar=Button(master_janela_Plataforma_SQL,width=9,text="Cerrar")
		bt_Cerrar["command"]=partial(janela_Plataforma_SQL.bt_Cerrar_Janela_Click,Projeto_Escolhido,master_janela_Plataforma_SQL)
		bt_Cerrar.place(x=600,y=600)
#================================================================================================================
#=========================CLASSE APP MODELO TREINAMENTO===========================================================================
#================================================================================================================
class janela_APP_MODELO_TREINAMENTO:

	def bt_Importar_Base_Click(txt_Base_Dados_Import):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		path_Arquivo = askopenfilename() # show an "Open" dialog box and return the path to the selected file
		nome_Arquivo=path_Arquivo.split("/")[-1:][0]
		txt_Base_Dados_Import.values=nome_Arquivo
		txt_Base_Dados_Import.insert(0,nome_Arquivo)
		txt_Base_Dados_Import.configure(state='disabled')
		#Teletransportar o Arquivo a nossa pasta especifica
		shutil.copy(path_Arquivo,'Base_Dados/')
		messagebox.showinfo("Importado", "Arquivo Importado!!")
	def bt_Mostrar_Tabela_Click(cmb_Projeto,txt_Base_Dados_Import,master_janela_APP_MODELO_TREINAMENTO):
		print("Base_Dados/"+txt_Base_Dados_Import.get())
		df_BD_Total=pd.read_csv("Base_Dados/"+txt_Base_Dados_Import.get())
		df_BD_Total_Amostra=df_BD_Total.head(10)
		Frame_Mostrar_Tabela=Frame(master_janela_APP_MODELO_TREINAMENTO)
		Frame_Mostrar_Tabela.place(x=120,y=170)
		Tabela_Mostrar=Table(Frame_Mostrar_Tabela,dataframe=df_BD_Total_Amostra,showtoolbar=True,showstatusbar=True,width=10,height=50)
	def bt_Executar_Modelo_Click(txt_Projeto):
		print ("Script do Modelo")
	def bt_Exportar_Base_Click(txt_Projeto):
		print ("Exportando Base Dados....")
	def bt_Guardar_Base_Click(txt_Projeto):
		print ("Exportando Base Dados....")
	def bt_Limpar_Bases_Antigas_mn_Click(txt_Projeto):
		pass
	def bt_Cerrar_Janela_Click(master_janela_APP_MODELO_TREINAMENTO):
		if (messagebox.askyesno("Cerrar!!","Quere cerrar?")):
			master_janela_APP_MODELO_TREINAMENTO.destroy()
	def Inicializando(master_janela_APP_MODELO_TREINAMENTO):
		master_janela_APP_MODELO_TREINAMENTO.title("APP MODELO TREINAMENTO")
		master_janela_APP_MODELO_TREINAMENTO["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master_janela_APP_MODELO_TREINAMENTO.geometry("780x700+0+0")
		#Insertando os Menus
		mn_Menu=Menu(master_janela_APP_MODELO_TREINAMENTO)
		#Sub Menus Pojetos
		mn_Sub_Menu_Ajuda=Menu(mn_Menu)
		mn_Menu.add_cascade(label="Ajuda",menu=mn_Sub_Menu_Ajuda)
		mn_Sub_Menu_Ajuda.add_command(label="Limpar",command=janela_APP_MODELO_TREINAMENTO.bt_Limpar_Bases_Antigas_mn_Click)
		mn_Sub_Menu_Ajuda.add_separator()
		master_janela_APP_MODELO_TREINAMENTO.config(menu=mn_Menu)
		#Insertando os Labels com a descripcao
		lb_descripcao_App=Label(master_janela_APP_MODELO_TREINAMENTO,text="App de treinamentos dos respeitovos projetos\n 'AGRONEGOCIO'",bg="light goldenrod")
		lb_descripcao_App.place(x=240,y=10)
		#Insertando os Labels com a descripcao da escolha do Projeto
		lb_Escolher_Projeto=Label(master_janela_APP_MODELO_TREINAMENTO,text="Escolhe tipo do projeto: ",bg="light goldenrod")
		lb_Escolher_Projeto.place(x=120,y=70)
		#Instar o Combobox para escolher o Projeto para rodar o Modelo
		cmb_Projectos=ttk.Combobox(master_janela_APP_MODELO_TREINAMENTO,width=15)
		cmb_Projectos['values']=("Agricola","Pecuario")
		cmb_Projectos.place(x=255,y=70)
		cmb_Projectos.current(0)
		#Insertando os Labels com a descripcao
		lb_descripcao_impotar=Label(master_janela_APP_MODELO_TREINAMENTO,text="Importar Base de Dados: ",bg="light goldenrod")
		lb_descripcao_impotar.place(x=120,y=105)
		#Insertando as caixas de Textos para importar base dados
		txt_Base_Dados_Import=Entry(master_janela_APP_MODELO_TREINAMENTO,width=40)
		txt_Base_Dados_Import.place(x=255,y=105)
		#Insertando botao de Importar Base de Dados
		bt_Importar_Dados=Button(master_janela_APP_MODELO_TREINAMENTO,width=9,text="Importar")
		bt_Importar_Dados["command"]=partial(janela_APP_MODELO_TREINAMENTO.bt_Importar_Base_Click,txt_Base_Dados_Import)
		bt_Importar_Dados.place(x=510,y=105)
		#Insertando botao de Excutar Script SQL
		bt_Mostrar_Tabela=Button(master_janela_APP_MODELO_TREINAMENTO,width=17,text="Mostrar Informação")
		bt_Mostrar_Tabela["command"]=partial(janela_APP_MODELO_TREINAMENTO.bt_Mostrar_Tabela_Click,cmb_Projectos.current(0),txt_Base_Dados_Import,master_janela_APP_MODELO_TREINAMENTO)
		bt_Mostrar_Tabela.place(x=120,y=140)
		#
		#
		#
		#Insertando botao de Exportar Base Treino
		bt_Executar_Modelo=Button(master_janela_APP_MODELO_TREINAMENTO,width=15,text="Executar Modelo")
		bt_Executar_Modelo["command"]=partial(janela_APP_MODELO_TREINAMENTO.bt_Executar_Modelo_Click,cmb_Projectos.current(0),txt_Base_Dados_Import,master_janela_APP_MODELO_TREINAMENTO)
		bt_Executar_Modelo.place(x=140,y=380)
		#Insertando botao de Guardar Base Treino
		bt_Guardar_Base=Button(master_janela_APP_MODELO_TREINAMENTO,width=20,text="Guardar Base de Treino")
		bt_Guardar_Base["command"]=partial(janela_APP_MODELO_TREINAMENTO.bt_Guardar_Base_Click,cmb_Projectos.current(0))
		bt_Guardar_Base.place(x=140,y=640)
		#Insertando botao de Exportar Base Treino
		bt_Exportar_Base=Button(master_janela_APP_MODELO_TREINAMENTO,width=20,text="Exportar Base de Treino")
		bt_Exportar_Base["command"]=partial(janela_APP_MODELO_TREINAMENTO.bt_Exportar_Base_Click,cmb_Projectos.current(0))
		bt_Exportar_Base.place(x=325,y=640)

		#Insertando botao de Cerrar
		bt_Cerrar=Button(master_janela_APP_MODELO_TREINAMENTO,width=9,text="Cerrar")
		bt_Cerrar["command"]=partial(janela_APP_MODELO_TREINAMENTO.bt_Cerrar_Janela_Click,master_janela_APP_MODELO_TREINAMENTO)
		bt_Cerrar.place(x=510,y=640)
#================================================================================================================
#=========================CLASSE APP MODELO RECORRENTE===========================================================================
#================================================================================================================
class janela_APP_MODELO_RECORRENTE:

	def bt_Importar_Base_Click(txt_Base_Dados_Import):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		path_Arquivo = askopenfilename() # show an "Open" dialog box and return the path to the selected file
		nome_Arquivo=path_Arquivo.split("/")[-1:][0]
		txt_Base_Dados_Import.values=nome_Arquivo
		txt_Base_Dados_Import.insert(0,nome_Arquivo)
		txt_Base_Dados_Import.configure(state='disabled')
		#Teletransportar o Arquivo a nossa pasta especifica
		shutil.copy(path_Arquivo,'Base_Dados/')
		messagebox.showinfo("Importado", "Arquivo Importado!!")
	def bt_Mostrar_Tabela_Click(cmb_Projeto,txt_Base_Dados_Import,master_janela_APP_MODELO_RECORRENTE):
		print("Base_Dados/"+txt_Base_Dados_Import.get())
		df_BD_Total=pd.read_csv("Base_Dados/"+txt_Base_Dados_Import.get())
		df_BD_Total_Amostra=df_BD_Total.head(10)
		Frame_Mostrar_Tabela=Frame(master_janela_APP_MODELO_RECORRENTE)
		Frame_Mostrar_Tabela.place(x=120,y=170)
		Tabela_Mostrar=Table(Frame_Mostrar_Tabela,dataframe=df_BD_Total_Amostra,showtoolbar=True,showstatusbar=True,width=10,height=50)
	def bt_Executar_Modelo_Click(txt_Projeto):
		print ("Script do Modelo")
	def bt_Exportar_Base_Click(txt_Projeto):
		print ("Exportando Base Dados....")
	def bt_Guardar_Base_Click(txt_Projeto):
		print ("Exportando Base Dados....")
	def bt_Limpar_Bases_Antigas_mn_Click(txt_Projeto):
		pass
	def bt_Cerrar_Janela_Click(master_janela_APP_MODELO_RECORRENTE):
		if (messagebox.askyesno("Cerrar!!","Quere cerrar?")):
			master_janela_APP_MODELO_RECORRENTE.destroy()
	def Inicializando(master_janela_APP_MODELO_RECORRENTE):
		master_janela_APP_MODELO_RECORRENTE.title("APP MODELO RECORRENTE")
		master_janela_APP_MODELO_RECORRENTE["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master_janela_APP_MODELO_RECORRENTE.geometry("780x700+0+0")
		#Insertando os Menus
		mn_Menu=Menu(master_janela_APP_MODELO_RECORRENTE)
		#Sub Menus Pojetos
		mn_Sub_Menu_Ajuda=Menu(mn_Menu)
		mn_Menu.add_cascade(label="Ajuda",menu=mn_Sub_Menu_Ajuda)
		mn_Sub_Menu_Ajuda.add_command(label="Limpar",command=janela_APP_MODELO_RECORRENTE.bt_Limpar_Bases_Antigas_mn_Click)
		mn_Sub_Menu_Ajuda.add_separator()
		master_janela_APP_MODELO_RECORRENTE.config(menu=mn_Menu)
		#Insertando os Labels com a descripcao
		lb_descripcao_App=Label(master_janela_APP_MODELO_RECORRENTE,text="App Recorrente dos respeitovos projetos\n 'AGRONEGOCIO'",bg="light goldenrod")
		lb_descripcao_App.place(x=240,y=10)
		#Insertando os Labels com a descripcao da escolha do Projeto
		lb_Escolher_Projeto=Label(master_janela_APP_MODELO_RECORRENTE,text="Escolhe tipo do projeto: ",bg="light goldenrod")
		lb_Escolher_Projeto.place(x=120,y=70)
		#Instar o Combobox para escolher o Projeto para rodar o Modelo
		cmb_Projectos=ttk.Combobox(master_janela_APP_MODELO_RECORRENTE,width=15)
		cmb_Projectos['values']=("Agricola","Pecuario")
		cmb_Projectos.place(x=255,y=70)
		cmb_Projectos.current(0)
		#Insertando os Labels com a descripcao
		lb_descripcao_impotar=Label(master_janela_APP_MODELO_RECORRENTE,text="Importar Base de Dados: ",bg="light goldenrod")
		lb_descripcao_impotar.place(x=120,y=105)
		#Insertando as caixas de Textos para importar base dados
		txt_Base_Dados_Import=Entry(master_janela_APP_MODELO_RECORRENTE,width=40)
		txt_Base_Dados_Import.place(x=255,y=105)
		#Insertando botao de Importar Base de Dados
		bt_Importar_Dados=Button(master_janela_APP_MODELO_RECORRENTE,width=9,text="Importar")
		bt_Importar_Dados["command"]=partial(janela_APP_MODELO_RECORRENTE.bt_Importar_Base_Click,txt_Base_Dados_Import)
		bt_Importar_Dados.place(x=510,y=105)
		#Insertando botao de Excutar Script SQL
		bt_Mostrar_Tabela=Button(master_janela_APP_MODELO_RECORRENTE,width=17,text="Mostrar Informação")
		bt_Mostrar_Tabela["command"]=partial(janela_APP_MODELO_RECORRENTE.bt_Mostrar_Tabela_Click,cmb_Projectos.current(0),txt_Base_Dados_Import,master_janela_APP_MODELO_RECORRENTE)
		bt_Mostrar_Tabela.place(x=120,y=140)
		#
		#
		#
		#Insertando botao de Exportar Base Treino
		bt_Executar_Modelo=Button(master_janela_APP_MODELO_RECORRENTE,width=15,text="Executar Modelo")
		bt_Executar_Modelo["command"]=partial(janela_APP_MODELO_RECORRENTE.bt_Executar_Modelo_Click,cmb_Projectos.current(0),txt_Base_Dados_Import,master_janela_APP_MODELO_RECORRENTE)
		bt_Executar_Modelo.place(x=140,y=380)
		#Insertando botao de Guardar Base Treino
		bt_Guardar_Base=Button(master_janela_APP_MODELO_RECORRENTE,width=20,text="Guardar Base de Treino")
		bt_Guardar_Base["command"]=partial(janela_APP_MODELO_RECORRENTE.bt_Guardar_Base_Click,cmb_Projectos.current(0))
		bt_Guardar_Base.place(x=140,y=640)
		#Insertando botao de Exportar Base Treino
		bt_Exportar_Base=Button(master_janela_APP_MODELO_RECORRENTE,width=20,text="Exportar Base de Treino")
		bt_Exportar_Base["command"]=partial(janela_APP_MODELO_RECORRENTE.bt_Exportar_Base_Click,cmb_Projectos.current(0))
		bt_Exportar_Base.place(x=325,y=640)

		#Insertando botao de Cerrar
		bt_Cerrar=Button(master_janela_APP_MODELO_RECORRENTE,width=9,text="Cerrar")
		bt_Cerrar["command"]=partial(janela_APP_MODELO_RECORRENTE.bt_Cerrar_Janela_Click,master_janela_APP_MODELO_RECORRENTE)
		bt_Cerrar.place(x=510,y=640)
#================================================================================================================
#=========================CLASSE APP MONITORAMENTO TREINO===========================================================================
#================================================================================================================
class janela_APP_MONITORAMENTO_TREINO:
	def Grafica_Curva_Roc():
		sns.set(style="white")
		rs=np.random.RandomState(9)
		d=pd.DataFrame(data=rs.normal(size=(10,10)),columns=list(ascii_letters[42:]))
		# Compute the correlation matrix
		corr = d.corr()
		# Generate a mask for the upper triangle
		mask = np.zeros_like(corr, dtype=np.bool)
		mask[np.triu_indices_from(mask)] = True
		# Set up the matplotlib figure
		f, ax = plt.subplots(figsize=(3, 3))
		# Generate a custom diverging colormap
		cmap = sns.diverging_palette(220, 10, as_cmap=True)
		# Draw the heatmap with the mask and correct aspect ratio
		sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,square=True, linewidths=.5, cbar_kws={"shrink": .5})
		return f
	def bt_Ver_Resultados_Historicos_cmb_Click(pagina_Resultados,df_Base_Historico_Treinamento):
		Frame_Mostrar_Tabela=Frame(pagina_Resultados)
		Frame_Mostrar_Tabela.place(x=420,y=170)
		Tabela_Mostrar=Table(Frame_Mostrar_Tabela,dataframe=df_Base_Historico_Treinamento,showtoolbar=True,showstatusbar=True,width=10,height=50)
		Tabela_Mostrar.show()
	def bt_Ver_Ultimo_Resultado_cmb_Click(txt_Acuracia,txt_Qtd_Registros,txt_Log_Reg,df_Base_Historico_Treinamento):
		#Escrevendo o Texto da Acuaracia
		txt_Acuracia.configure(state='normal')
		txt_Acuracia.insert(0,str(df_Base_Historico_Treinamento.Acuracia.tail(1).values[0])+"%")
		txt_Acuracia.configure(state='disabled')
		#Escrevendo o Texto da Quantidade
		txt_Qtd_Registros.configure(state='normal')
		txt_Qtd_Registros.insert(0,str(df_Base_Historico_Treinamento.Qtd_Registros.tail(1).values[0])+"%")
		txt_Qtd_Registros.configure(state='disabled')
		#Escrevendo o Texto de Log_Reg
		txt_Log_Reg.configure(state='normal')
		txt_Log_Reg.insert(0,str(df_Base_Historico_Treinamento.Log_Reg.tail(1).values[0])+"%")
		txt_Log_Reg.configure(state='disabled')
	def bt_Exportar_Base_Click(txt_Projeto):
		print ("Exportando Base Dados....")
	def bt_Limpar_Bases_Antigas_mn_Click(txt_Projeto):
		pass
	def bt_Cerrar_Janela_Click(master_janela_APP_MONITORAMENTO_TREINO):
		if (messagebox.askyesno("Cerrar!!","Quere cerrar?")):
			master_janela_APP_MONITORAMENTO_TREINO.destroy()
	#========================================================================================================
	#                                      Botones para Graficar RESULTADOS
	#========================================================================================================
	def bt_Grafico_Curva_Roc_Click(pagina_Resultados,Grafica_Curva_Roc):
		fig = Grafica_Curva_Roc()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=20)
		print (str(Grafica_Curva_Roc))
	def bt_Grafico_Distribuicao_Click(pagina_Resultados,Grafica_Distribuicao):
		fig = Grafica_Distribuicao()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=20)
		print (str(Grafica_Curva_Roc))
	def bt_Grafico_Matriz_Confuncao_Click(pagina_Resultados,Grafica_Matriz_Confucao):
		fig = Grafica_Matriz_Confucao()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=20)
		print (str(Grafica_Curva_Roc))
	#========================================================================================================
	#                                      Botones para Graficar COMPORTAMENTO DAS VARIAVEIS
	#========================================================================================================
	def bt_Grafico_Matriz_Correlacao_CLick(pagina_Resultados,Grafica_Distribuicao):
		fig = Grafica_Distribuicao()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=80)
		print (str(Grafica_Curva_Roc))
	def bt_Grafico_Variaveis_Importantes_Click(pagina_Resultados,Grafica_Matriz_Confucao):
		fig = Grafica_Matriz_Confucao()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=80)
		print (str(Grafica_Curva_Roc))
	def bt_Grafico_Especial_1_Click(pagina_Resultados,Grafica_Distribuicao):
		fig = Grafica_Distribuicao()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=80)
		print (str(Grafica_Curva_Roc))
	def bt_Grafico_Especial_2_Click(pagina_Resultados,Grafica_Matriz_Confucao):
		fig = Grafica_Matriz_Confucao()
		canvas = FigureCanvasTkAgg(fig, master=pagina_Resultados)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=RIGHT,padx=80)
		print (str(Grafica_Curva_Roc))
	def Inicializando(master_janela_APP_MONITORAMENTO_TREINO,Projeto_Escolhido):
		#Lendo a base de dados doshitoricos Guardados
		path_Historico_Treino="Resultados/Historico_Treinamento_"+Projeto_Escolhido+".csv"
		if Projeto_Escolhido=="Agricola":
			df_Base_Historico_Treinamento=pd.read_csv(path_Historico_Treino,sep=",",encoding="latin1")
		elif Projeto_Escolhido=="Pecuario":
			df_Base_Historico_Treinamento=pd.read_csv(path_Historico_Treino,sep=",",encoding="latin1")
		print (Projeto_Escolhido)
		#================================================================================================
		master_janela_APP_MONITORAMENTO_TREINO.title("APP MONITORAMENTO TREINO "+Projeto_Escolhido.upper())
		master_janela_APP_MONITORAMENTO_TREINO["bg"]="light goldenrod"
		#LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
		master_janela_APP_MONITORAMENTO_TREINO.geometry("980x680+0+0")
		#Insertando os Menus
		mn_Menu=Menu(master_janela_APP_MONITORAMENTO_TREINO)
		#Sub Menus Pojetos
		mn_Sub_Menu_Ajuda=Menu(mn_Menu)
		mn_Menu.add_cascade(label="Ajuda",menu=mn_Sub_Menu_Ajuda)
		mn_Sub_Menu_Ajuda.add_command(label="Limpar",command=janela_APP_MONITORAMENTO_TREINO.bt_Limpar_Bases_Antigas_mn_Click)
		mn_Sub_Menu_Ajuda.add_separator()
		master_janela_APP_MONITORAMENTO_TREINO.config(menu=mn_Menu)
		#Insertando os Labels com a descripcao
		lb_descripcao_App=Label(master_janela_APP_MONITORAMENTO_TREINO,text="App de treinamentos dos respeitovos projetos\n 'AGRONEGOCIO'",bg="light goldenrod")
		lb_descripcao_App.place(x=240,y=10)
		#Insertando os tabs para os Resultados  e Variaves
		tb=ttk.Notebook(master_janela_APP_MONITORAMENTO_TREINO)
		#Tab Resultados
		pagina_Resultados=ttk.Frame(tb)
		tb.add(pagina_Resultados,text="Resultados")
		tb.pack(expand=YES,fill=X)
		#==========================================================================================================
		#											MOSTRANDO OS RESULTADOS
		#==========================================================================================================
		#Insertando os Labels Quantidade de treino
		lb_Qtd_Treino=Label(pagina_Resultados,text="# Registros: ",bg="light goldenrod")
		lb_Qtd_Treino.place(x=10,y=100)
		#Insertando as caixas de Textos mostra numero de propensos
		txt_Qtd_Treino=Entry(pagina_Resultados,width=7)
		txt_Qtd_Treino.place(x=80,y=100)
		txt_Qtd_Treino.configure(state='disabled')
		#Insertando os Labels Acuracia
		lb_valor_Acuracia=Label(pagina_Resultados,text="% Acuracia: ",bg="light goldenrod")
		lb_valor_Acuracia.place(x=10,y=130)
		#Insertando as caixas de Textos mostra a Acuracia
		txt_valor_Acuracia=Entry(pagina_Resultados,width=7)
		txt_valor_Acuracia.place(x=80,y=130)
		txt_valor_Acuracia.configure(state='disabled')
		#Insertando os Labels Log_Reg
		lb_valor_Log_Reg=Label(pagina_Resultados,text="% Log_Reg: ",bg="light goldenrod")
		lb_valor_Log_Reg.place(x=10,y=160)
		#Insertando as caixas de Textos mostra a Acuracia
		txt_valor_Log_Reg=Entry(pagina_Resultados,width=7)
		txt_valor_Log_Reg.place(x=80,y=160)
		txt_valor_Log_Reg.configure(state='disabled')

		#Instertando o botao para mostrar oultimo resultado feito
		bt_Ultimo_Resultado=Button(pagina_Resultados,width=15,text="Ultimo Resultado")
		bt_Ultimo_Resultado["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Ver_Ultimo_Resultado_cmb_Click,txt_valor_Acuracia,txt_Qtd_Treino,txt_valor_Log_Reg,df_Base_Historico_Treinamento)
		bt_Ultimo_Resultado.place(x=20,y=10)
		#Insertando Separador
		lb_separador=Label(pagina_Resultados,text="_____________________________|",bg="light goldenrod")
		lb_separador.place(x=10,y=180)
		#==========================================================================================================
		#											Mostrando Dados Historicos
		#==========================================================================================================
		#Instertando o botao para mostrar historico dosresultados
		bt_Resultados_Historicos=Button(pagina_Resultados,width=20,text="Historico dos Resultados")
		bt_Resultados_Historicos["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Ver_Resultados_Historicos_cmb_Click,pagina_Resultados,df_Base_Historico_Treinamento)
		bt_Resultados_Historicos.place(x=420,y=10)
		#==========================================================================================================
		#											Mostrando os Graficos dos Resultados
		#==========================================================================================================
		#Conteiners dos Graficos
		Frame_Conteiner_Graficos=Frame(pagina_Resultados)
		Frame_Conteiner_Graficos.pack(side=BOTTOM,pady=50)
		#Lendo Base de Dados para os Graficos
		#Insertando labels para descriver a Seção
		lb_Graficos_Modelos=Label(Frame_Conteiner_Graficos,text="Nesta Seção Graficamos os ultimos resultados da ultima face do Treinamento",bg="light goldenrod")
		lb_Graficos_Modelos.pack(side=TOP,pady=20)
		#Instertando o botao para mostrar o Grafico da curva Roc
		bt_Grafico_Curva_Roc=Button(pagina_Resultados,width=20,text="Curva Roc")
		bt_Grafico_Curva_Roc["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Curva_Roc_Click,Frame_Conteiner_Graficos,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Curva_Roc.place(x=30,y=220)
		#Instertando o botao para mostrar o Grafico da Distribuicao}
		bt_Grafico_Distribuicao=Button(pagina_Resultados,width=20,text="Distribuição Normal")
		bt_Grafico_Distribuicao["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Distribuicao_Click,Frame_Conteiner_Graficos,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Distribuicao.place(x=380,y=220)
		#Instertando o botao para mostrar o Grafico da Matriz de Confucao
		bt_Grafico_Matriz_Confuncao=Button(pagina_Resultados,width=20,text="Matriz de Confução")
		bt_Grafico_Matriz_Confuncao["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Matriz_Confuncao_Click,Frame_Conteiner_Graficos,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Matriz_Confuncao.place(x=740,y=220)
		#Instertando o botao de Encerramento
		bt_Cerrar=Button(master_janela_APP_MONITORAMENTO_TREINO,width=9,text="Cerrar")
		bt_Cerrar["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Cerrar_Janela_Click,master_janela_APP_MONITORAMENTO_TREINO)
		bt_Cerrar.place(x=510,y=640)
		#Tab Entregavel
		pagina_Entregavel=ttk.Frame(tb)
		tb.add(pagina_Entregavel,text="Variaveis e Coeficientes")
		#tb.pack(expand=YES,fill=X)
		tb.pack(expand=1,fill='both')
		#==========================================================================================================
		#											Mostrando os Graficos dos Resultados
		#==========================================================================================================
		#Conteiners dos Graficos
		Frame_Conteiner_Graficos_Variaveis=Frame(pagina_Entregavel)
		Frame_Conteiner_Graficos_Variaveis.pack(side=TOP,pady=10)
		#Lendo Base de Dados para os Graficos
		#Insertando labels para descriver a Seção
		lb_Graficos_Variaveis=Label(Frame_Conteiner_Graficos_Variaveis,text="Nesta Seção Graficamos o comportamento das variaveis Utilizados para sua respetivas calibração",bg="light goldenrod")
		lb_Graficos_Variaveis.pack(side=TOP,pady=10)
		#Instertando o botao para mostrar o Grafico da curva Roc
		bt_Grafico_Matriz_Correlacao=Button(pagina_Entregavel,width=20,text="Matriz de Correlação")
		bt_Grafico_Matriz_Correlacao["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Matriz_Correlacao_CLick,Frame_Conteiner_Graficos_Variaveis,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Matriz_Correlacao.place(x=200,y=40)
		#Instertando o botao para mostrar o Grafico da Distribuicao}
		bt_Grafico_Variaveis_Importantes=Button(pagina_Entregavel,width=20,text="Variaveis Importantes")
		bt_Grafico_Variaveis_Importantes["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Variaveis_Importantes_Click,Frame_Conteiner_Graficos_Variaveis,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Variaveis_Importantes.place(x=630,y=40)
		#=====================================================================================================================================
		#SEGUNDA LINHA DE GRAFICOS
		#=====================================================================================================================================
		#Conteiners dos Graficos
		Frame_Conteiner_Graficos_Variaveis=Frame(pagina_Entregavel)
		Frame_Conteiner_Graficos_Variaveis.pack(side=BOTTOM)
		#Lendo Base de Dados para os Graficos
		#Instertando o botao para mostrar o Grafico da curva Roc
		bt_Grafico_Especial_1=Button(pagina_Entregavel,width=20,text="Grafico Especial 1")
		bt_Grafico_Especial_1["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Especial_1_Click,Frame_Conteiner_Graficos_Variaveis,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Especial_1.place(x=200,y=320)
		#Instertando o botao para mostrar o Grafico da Distribuicao}
		bt_Grafico_Especial_2=Button(pagina_Entregavel,width=20,text="Grafico Especial 2")
		bt_Grafico_Especial_2["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Especial_2_Click,Frame_Conteiner_Graficos_Variaveis,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		bt_Grafico_Especial_2.place(x=630,y=320)
		##Instertando o botao para mostrar o Grafico da Matriz de Confucao
		#bt_Grafico_Matriz_Confuncao=Button(pagina_Entregavel,width=20,text="Matriz de Confução")
		#bt_Grafico_Matriz_Confuncao["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Grafico_Matriz_Confuncao_Click,Frame_Conteiner_Graficos_Variaveis,janela_APP_MONITORAMENTO_TREINO.Grafica_Curva_Roc)
		#bt_Grafico_Matriz_Confuncao.place(x=740,y=220)
		#Instertando o botao de Encerramento
		bt_Cerrar=Button(master_janela_APP_MONITORAMENTO_TREINO,width=9,text="Cerrar")
		bt_Cerrar["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Cerrar_Janela_Click,master_janela_APP_MONITORAMENTO_TREINO)
		bt_Cerrar.place(x=510,y=640)







		##Insertando o label para o contexto inicial 
		#lb_Text_Inicial=Label(pagina_Resultados,text="Escolher Projeto: ",bg="light goldenrod")
		#lb_Text_Inicial.place(x=30,y=10)
		##Instertando o botao para entrar aos Resultados para seu Treinanmento
#		#bt_Entrar_treino=Button(pagina_Treinamento,width=13,text="Plataforma \nTreinamento")
		#bt_Entrar_treino["command"]=partial(janela_Modelos.bt_Entrar_Projeto_cmb_Click,cmb_Projectos)
		#bt_Entrar_treino.place(x=180,y=90)
		##Tab Entregavel
		#pagina_Entregavel=ttk.Frame(tb)
		#tb.add(pagina_Entregavel,text="Executar Modelo")
		#tb.pack(expand=1,fill='both')
		##Insertando o label para o contexto inicial 
		#lb_Text_Inicial=Label(pagina_Entregavel,text="Escolher Projeto:",bg="light goldenrod")
		#lb_Text_Inicial.place(x=30,y=10)
		##Instar o Combobox para escolher os Resultados para o Entregavel
		#cmb_Projectos_Entregavel=ttk.Combobox(pagina_Entregavel,width=15)
		#cmb_Projectos_Entregavel['values']=("Agricola","Pecuario")
		#cmb_Projectos_Entregavel.place(x=50,y=40)
		#cmb_Projectos_Entregavel.current(0)
		##Instertando o botao  Entregavel
		#bt_Entrar_Modelo=Button(pagina_Entregavel,width=13,text="Plataforma \nEntregavel")
		#bt_Entrar_Modelo["command"]=partial(janela_Modelos.bt_Entrar_Projeto_Entregavel_cmb_Click,cmb_Projectos_Entregavel)
		#bt_Entrar_Modelo.place(x=180,y=40)
#





		##Insertando os Labels com a descripcao da escolha do Projeto
		#lb_Escolher_Projeto=Label(master_janela_APP_MONITORAMENTO_TREINO,text="Escolhe tipo do projeto: ",bg="light goldenrod")
		#lb_Escolher_Projeto.place(x=120,y=70)
		##Instar o Combobox para escolher o Projeto para rodar o Modelo
		#cmb_Projectos=ttk.Combobox(master_janela_APP_MONITORAMENTO_TREINO,width=15)
		#cmb_Projectos['values']=("Agricola","Pecuario")
		#cmb_Projectos.place(x=255,y=70)
		#cmb_Projectos.current(0)
		##Insertando os Labels com a descripcao
		#lb_descripcao_impotar=Label(master_janela_APP_MONITORAMENTO_TREINO,text="Importar Base de Dados: ",bg="light goldenrod")
		#lb_descripcao_impotar.place(x=120,y=105)
		##Insertando as caixas de Textos para importar base dados
		#txt_Base_Dados_Import=Entry(master_janela_APP_MONITORAMENTO_TREINO,width=40)
		#txt_Base_Dados_Import.place(x=255,y=105)
		##Insertando botao de Importar Base de Dados
		#bt_Importar_Dados=Button(master_janela_APP_MONITORAMENTO_TREINO,width=9,text="Importar")
		#bt_Importar_Dados["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Importar_Base_Click,txt_Base_Dados_Import)
		#bt_Importar_Dados.place(x=510,y=105)
		##Insertando botao de Excutar Script SQL
		#bt_Mostrar_Tabela=Button(master_janela_APP_MONITORAMENTO_TREINO,width=17,text="Mostrar Informação")
		#bt_Mostrar_Tabela["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Mostrar_Tabela_Click,cmb_Projectos.current(0),txt_Base_Dados_Import,master_janela_APP_MONITORAMENTO_TREINO)
		#bt_Mostrar_Tabela.place(x=120,y=140)
		##
		##
		##
		##Insertando botao de Exportar Base Treino
		#bt_Executar_Modelo=Button(master_janela_APP_MONITORAMENTO_TREINO,width=15,text="Executar Modelo")
		#bt_Executar_Modelo["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Executar_Modelo_Click,cmb_Projectos.current(0),txt_Base_Dados_Import,master_janela_APP_MONITORAMENTO_TREINO)
		#bt_Executar_Modelo.place(x=140,y=380)
		##Insertando botao de Guardar Base Treino
		#bt_Guardar_Base=Button(master_janela_APP_MONITORAMENTO_TREINO,width=20,text="Guardar Base de Treino")
		#bt_Guardar_Base["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Guardar_Base_Click,cmb_Projectos.current(0))
		#bt_Guardar_Base.place(x=140,y=640)
		##Insertando botao de Exportar Base Treino
		#bt_Exportar_Base=Button(master_janela_APP_MONITORAMENTO_TREINO,width=20,text="Exportar Base de Treino")
		#bt_Exportar_Base["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Exportar_Base_Click,cmb_Projectos.current(0))
		#bt_Exportar_Base.place(x=325,y=640)
#
		##Insertando botao de Cerrar
		#bt_Cerrar=Button(master_janela_APP_MONITORAMENTO_TREINO,width=9,text="Cerrar")
		#bt_Cerrar["command"]=partial(janela_APP_MONITORAMENTO_TREINO.bt_Cerrar_Janela_Click,master_janela_APP_MONITORAMENTO_TREINO)
		#bt_Cerrar.place(x=510,y=640)
#================================================================================================================
#=========================CLASSE APP MODELO RECORRENTE===========================================================================
#================================================================================================================

#main(master)
master_janela_Modelos=Tk()
janela_Modelos.Inicializando(master_janela_Modelos)
master_janela_Modelos.mainloop()
#master_janela_Plataforma_SQL=Tk()
#janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,"Pecuario")
#master_janela_Plataforma_SQL.mainloop()
#master_janela_APP_MODELO_TREINAMENTO=Tk()
#janela_APP_MODELO_TREINAMENTO.Inicializando(master_janela_APP_MODELO_TREINAMENTO)
#master_janela_APP_MODELO_TREINAMENTO.mainloop()
#master_janela_APP_MONITORAMENTO=Tk()
#janela_APP_MONITORAMENTO.Inicializando(master_janela_APP_MONITORAMENTO,"Agricola")
#master_janela_APP_MONITORAMENTO.mainloop()







#de#f bt_Conectar_Click(txt_Servidor,txt_Base_Dados):
#	print (txt_Servidor.get())
#	print (txt_Base_Dados.get())
#def bt_Sair_Click():
#	if (messagebox.askyesno("SAIR!!","Verdaderamente quer sair?")):
#		messagebox.showinfo("Informação","Volte Sempre!")
#		janela_Conect_BD.quit()
#janela_Conect_BD=Tk()
#janela_Conect_BD.title("CONECTAR_BASE_DADOS SQL")
#janela_Conect_BD["bg"]="light goldenrod"
##LaguraxAltura+Distancia_Esquerda+Distacia_do_Topo
#janela_Conect_BD.geometry("330x120+400+250")
##Insertando os Labels Servidor
#lb_Servidor=Label(janela_Conect_BD,text="Servidor SQL :",bg="light goldenrod")
#lb_Servidor.place(x=50,y=10)
##Insertando as caixas de Textos Servidor
#txt_Servidor=Entry(janela_Conect_BD)
#txt_Servidor.place(x=140,y=10)
##Insertando os Labels Base de Dados
#lb_Base_Dados=Label(janela_Conect_BD,text="Base de Dados:",bg="light goldenrod")
#lb_Base_Dados.place(x=50,y=40)
##Insertando as caixas de Textos Base de Dados
#txt_Base_Dados=Entry(janela_Conect_BD)
#txt_Base_Dados.place(x=140,y=40)
##Instertando os BOtoes
#bt_Conectar=Button(janela_Conect_BD,width=9,text="Conectar")
#bt_Conectar["command"]=partial(bt_Conectar_Click,txt_Servidor,txt_Base_Dados)
#bt_Conectar.place(x=50,y=80)
#bt_Sair=Button(janela_Conect_BD,width=8,text="Sair",command=bt_Sair_Click)
#bt_Sair.place(x=200,y=80)
#janela_Conect_BD.mainloop()#