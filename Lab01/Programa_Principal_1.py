from functools import partial
from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
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
	#Funcao para chamar pelo menu no Projeto Agricola
	def bt_Projeto_Agricola_mn_Click():
		Projeto_Escolhido="Agricola"
		master_janela_Plataforma_SQL=Tk()
		app_janela_Plataforma_SQL=janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido)
		master_janela_Plataforma_SQL.mainloop()
		print("Entrou no projeto Agricola")
	#Funcao para chamar pelo menu no Projeto Pecuario
	def bt_Projeto_Pecuario_mn_Click():
		Projeto_Escolhido="Pecuario"
		master_janela_Plataforma_SQL=Tk()
		app_janela_Plataforma_SQL=janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL,Projeto_Escolhido)
		master_janela_Plataforma_SQL.mainloop()
		print("Entrou no projeto Pecuario")
	#Funcao para chamar pelo menu no Monitoramento Agricola
	def bt_Monitoramento_Agricola_mn_Click():
		Projeto_Escolhido="Agricola"
		print("Entrou no Monitoramento Agricola")
	#Funcao para chamar pelo menu no Monitoramento Pecuario
	def bt_Monitoramento_Pecuario_mn_Click():
		Projeto_Escolhido="Pecuario"
		print("Entrou no Monitoramento Pecuario")
	#Funcao para chamar pelo boton e combobox nos Projetos
	def bt_Entrar_Projeto_cmb_Click(cmb_Projectos):
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
	#Funcao para chamar pelo boton e combobox no Monitoramento
	def bt_Entrar_Monitoramento_cmb_Click(cmb_Projectos_Monitoramento):
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
		master_janela_Modelos.geometry("300x210+400+250")
		#Insertndo um frame para os menus
		#frm_Menu=Frame(master_janela_Modelos)
		#frm_Menu.pack()
		#Insertando a lista de Menus
		mn_Menu=Menu(master_janela_Modelos)
		#Sub Menus Pojetos
		mn_Sub_Menu_Projetos=Menu(mn_Menu)
		mn_Menu.add_cascade(label="Projetos",menu=mn_Sub_Menu_Projetos)
		mn_Sub_Menu_Projetos.add_command(label="Agricola",command=janela_Modelos.bt_Projeto_Agricola_mn_Click)
		mn_Sub_Menu_Projetos.add_command(label="Pecuario",command=janela_Modelos.bt_Projeto_Pecuario_mn_Click)
		mn_Sub_Menu_Projetos.add_separator()
		mn_Sub_Menu_Projetos.add_command(label="Sair",command=janela_Modelos.bt_Sair_Click)
		
		#Sub Menu Monitoramento
		mn_Monitoramento=Menu(mn_Menu)
		mn_Monitoramento.add_command(label="Agricola",command=janela_Modelos.bt_Monitoramento_Agricola_mn_Click)
		mn_Monitoramento.add_command(label="Pecuario",command=janela_Modelos.bt_Monitoramento_Pecuario_mn_Click)
		mn_Menu.add_cascade(label="Monitoramento",menu=mn_Monitoramento)
		master_janela_Modelos.config(menu=mn_Menu)
		#Insertando o label para o contexto inicial 	
		lb_Text_Inicial=Label(master_janela_Modelos,text="\n'Escolhe uma das opções para processar \n PROJETOS ou MONITORAMENTO'\n",bg="light goldenrod")
		lb_Text_Inicial.pack(side=TOP)
		#Insertando os tabs para os Projetos  e Monitoramento
		tb=ttk.Notebook(master_janela_Modelos)
		#Tab Projeto
		pagina_Projetos=ttk.Frame(tb)
		tb.add(pagina_Projetos,text="Projetos")
		tb.pack(expand=YES,fill=X)
		#Insertando o label para o contexto inicial 
		lb_Text_Inicial=Label(pagina_Projetos,text="Escolher Projeto: ",bg="light goldenrod")
		lb_Text_Inicial.place(x=30,y=10)
		#Instar o Combobox para escolher o Projeto
		cmb_Projectos=ttk.Combobox(pagina_Projetos,width=15)
		cmb_Projectos['values']=("Agricola","Pecuario")
		cmb_Projectos.place(x=50,y=40)
		cmb_Projectos.current(0)
		#Instertando o botao para entrar aos projetos para entrar
		bt_Entrar=Button(pagina_Projetos,width=9,text="Entrar")
		bt_Entrar["command"]=partial(janela_Modelos.bt_Entrar_Projeto_cmb_Click,cmb_Projectos)
		bt_Entrar.place(x=180,y=40)

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
		#Instertando o botao para entrar aos monitoramentos
		bt_Entrar=Button(pagina_Monitoramento,width=9,text="Entrar")
		bt_Entrar["command"]=partial(janela_Modelos.bt_Entrar_Monitoramento_cmb_Click,cmb_Projectos_Monitoramento)
		bt_Entrar.place(x=180,y=40)
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
#main(master)
master_janela_Modelos=Tk()
janela_Modelos.Inicializando(master_janela_Modelos)
master_janela_Modelos.mainloop()
#master_janela_Plataforma_SQL=Tk()
#janela_Plataforma_SQL.Inicializando(master_janela_Plataforma_SQL)
#master_janela_Plataforma_SQL.mainloop()




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