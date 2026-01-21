#Universidade:UMC
#Curso:Engenharia de Software
#Diciplina:Software Básico

##Nomes dos desenvolvedores##
#Gabriel Henrique da silva dos santos
#RGM:11251103734
#Enrico Soares ramos da silva
#RGM:11252101522
#Guilherme Bezerra da silva
#RGM:11252100081
#Helio Goulart Ferreira filho
#RGM:11252101559


#####################################

            ##AGE_MED##

#####################################

#bibliotecas:
import os
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import PIL as pl
from PIL import Image, ImageTk
os.system('cls')

#####################################
#configuração de tela
windown = tk.Tk()
windown.title("Age_Medic")
windown.geometry("800x600")
windown.maxsize(800,600)
windown.minsize(800,600)
windown.configure(bg="#FFFFFF")

#####################################
#sair_da_aplicacao
def sair_aplicacao():
    print("saindo...")
    windown.destroy()


#####################################
#menu_inside

#menu_up():
def menu_up():
    global scp
    scp = 1
    #titulo():
    #til.place(x=300,y=50)
    #subtitulo
    #subtitle.place(x=330,y=100)
    #versão():
    ver.place(x=1,y=570)
    #botao01
    botao1.pack()
    botao1.place(x=305,y=365)
    #botao02
    botao2.pack()
    botao2.place(x=305,y=415)
    #Logo
    Lab_logo.place(x=250,y=30)
    #Sub_Logo
    Lab_Sub_logo.place(x=15,y=480)
    #interface
    interface.place(x=250,y=320)
    #botão_voltar
    bot_sair.place_forget()

    #Menu paciente
    #interface menu conta
    interface_menu_conta.place_forget()

    #botão criar uma conta
    bot_CUC.place_forget()

    #fazer login
    bot_FL.place_forget()

    #fazer sistema de controle desaparecer
    Espaço_de_controle_down()

    #deletar informaçoes apos login
    ent_CPF_FL.delete(0, tk.END)
    ent_NOME_FL.delete(0, tk.END)
    ent_SENHA_FL.delete(0, tk.END)

    #deletar informaçoes apos login
    ent_CPF.delete(0, tk.END)
    ent_NOME.delete(0, tk.END)
    ent_SENHA.delete(0, tk.END)


#menu_down():
def menu_down():
    print("saindo do menu")
    #titulo():
    til.place_forget()
    #subtitulo
    subtitle.place_forget()
    #versão():
    #ver.place_forget()
    #botao01
    botao1.place_forget()
    #botao02
    botao2.place_forget()
    #Logo
    Lab_logo.place_forget()
    #Sub_logo
    #Lab_Sub_logo.place_forget()
    #interface
    interface.place_forget()
    
#####################################
#Estrurura Lógica
####Estrutura da AgeMed#####

def carregar_dados():
    dados = {}

    try:
        with open("dados_medicos.txt", "r") as f:
            for linha in f:
                linha = linha.strip()

                # ignora linhas vazias
                if not linha:
                    continue

                partes = linha.split(",")

                # precisa ter exatamente 3 partes
                if len(partes) != 3:
                    continue

                cpf, nome, senha = partes

                # remove espaços
                cpf = cpf.strip()

                # ignora cpf inválido
                if not cpf.isdigit():
                    continue

                # converte para inteiro e salva
                dados[int(cpf)] = [nome.strip(), senha.strip()]

    except FileNotFoundError:
        # arquivo ainda não existe, tudo bem
        pass

    return dados



# Função para SALVAR arquivo***
def salvar_dados(dados):
    with open("dados_medicos.txt", "w") as f:
        for cpf, info in dados.items():
            nome, senha = info
            f.write(f"{cpf},{nome},{senha}\n")



# Função de CADASTRO***
def cadastrar_usuario():
    # pega textos
    raw_cpf = ent_CPF.get()
    nome = ent_NOME.get().strip()
    senha = ent_SENHA.get().strip()

    # remove tudo que não é número
    cpf_str = "".join([c for c in raw_cpf if c.isdigit()])

    if cpf_str == "":
        messagebox.showerror("Erro", "Digite um CPF válido.")
        return

    cpf = int(cpf_str)

    # verifica duplicado
    if cpf in dados:
        messagebox.showerror("Erro", "Este CPF já está cadastrado!")
        return

    # adiciona ao dicionário
    dados[cpf] = [nome, senha]

    # salva
    salvar_dados(dados)

    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

    # limpa campos
    ent_CPF.delete(0, tk.END)
    ent_NOME.delete(0, tk.END)
    ent_SENHA.delete(0, tk.END)


# carrega arquivo sem risco de erro
dados = carregar_dados()


##############################


def login_usuario():
    global EC_nome
    global EC_cpf
    global EC_senha

    EC_nome = ent_NOME_FL.get()
    EC_cpf = ent_CPF_FL.get()
    EC_senha = ent_SENHA_FL.get()

    # limpar CPF (deixar só números)
    cpf_str = "".join([c for c in EC_cpf if c.isdigit()])

    if cpf_str == "":
        messagebox.showerror("Erro", "Digite um CPF válido.")
        return

    cpf = int(cpf_str)

    # verifica se cpf existe
    if cpf not in dados:
        messagebox.showerror("Erro", "CPF não encontrado.")
        return


    # comparar nome
    if EC_nome != dados[cpf][0]:
        messagebox.showerror("Erro", "Nome incorreto.")
        return


    # compara senha
    senha_correta = dados[cpf][1]

    if EC_senha != senha_correta:
        messagebox.showerror("Erro", "Senha incorreta.")
        return

    # se tudo ok → abre área do usuário
    Espaço_de_controle_up()


#####################################
#SCP
#sistema de controle de passos

global scp
scp = 1
#scp(1) = menu
#scp(2) = menu paciente
#scp(3) = criar conta

#alternador():

def alternador():
    global scp
    if scp == 1:
        menu_up()
        
    if scp == 2:
        Menu_Paciente_up()
        Criar_conta_down()
        Fazer_login_down()
        
        #mudar a iterface de cor
        interface_menu_conta.configure(bg="#6ca5bf")
           
    if scp == 3:
        Criar_conta_up()

        #mudar a interface de cor
        interface_menu_conta.configure(bg="#6ca5bf")

    if scp == 4:
        Fazer_login_up()

        #mudar iterface de cor
        interface_menu_conta.configure(bg="#6ca5bf")

def scp_less():
    global scp

    if scp == 4:
        scp = scp - 2
        print(scp)
        alternador()

    else: 
        scp = scp - 1
        print(scp)
        alternador()

def scp_more():
    global scp
    scp = scp + 1
    print(scp)
    alternador()

def scp_FL():
    global scp
    scp = 4
    print(scp)
    alternador()


#####################################
#Menu_Paciente_Inside

#Menu_Paciente_up():
def Menu_Paciente_up():

    #deletar informaçoes apos login
    ent_CPF_FL.delete(0, tk.END)
    ent_NOME_FL.delete(0, tk.END)
    ent_SENHA_FL.delete(0, tk.END)

    #deletar informaçoes apos login
    ent_CPF.delete(0, tk.END)
    ent_NOME.delete(0, tk.END)
    ent_SENHA.delete(0, tk.END)

    print("Menu_Paciente_up")
    menu_down()
    
    #interface menu conta
    interface_menu_conta.place(x=250,y=150)

    #botao para sair
    bot_sair.place(x=1,y=1)

    #botão criar uma conta
    bot_CUC.place(x=305,y=240)

    #fazer login
    bot_FL.place(x=305,y=290)


def Menu_Paciente_down():
    print("Menu_Paciente_down")

    #interface menu conta
    #interface_menu_conta.place_forget()
    #botao para sair
    bot_sair.place_forget()
    #botão criar uma conta
    bot_CUC.place_forget()
    #fazer login
    bot_FL.place_forget()


#####################################
#CRIAR CONTA

#Criar_conta_up():
def Criar_conta_up():
    Menu_Paciente_down()

    #Til_CR
    til_CR.place(x=350,y=153)

    #CPF
    lab_CPF.place(x=330,y=200)  
    ent_CPF.place(x=316,y=230)

    #NOME
    lab_NOME.place(x=322,y=270)  
    ent_NOME.place(x=316,y=300)

    #SENHA
    lab_SENHA.place(x=318,y=340)  
    ent_SENHA.place(x=316,y=370)

    #Botão_inserir_CR
    bot_inserir_CR.place(x=275,y=445)

    #botao para sair
    bot_sair.place(x=1,y=1)


#Criar_conta_down():
def Criar_conta_down():
    #Til_CR
    til_CR.place_forget()
    #CPF
    lab_CPF.place_forget()  
    ent_CPF.place_forget()
    #NOME
    lab_NOME.place_forget()
    ent_NOME.place_forget()
    #SENHA
    lab_SENHA.place_forget()
    ent_SENHA.place_forget()
    #Botão_inserir_CR
    bot_inserir_CR.place_forget()
    #botao para sair
    
#####################################
#FAZER LOGIN

#Fazer_login_up():
def Fazer_login_up():
    Menu_Paciente_down()

    #Til_CR
    til_FL.place(x=350,y=153)

    #CPF
    lab_CPF_FL.place(x=330,y=200)  
    ent_CPF_FL.place(x=316,y=230)

    #NOME
    lab_NOME_FL.place(x=322,y=270)  
    ent_NOME_FL.place(x=316,y=300)

    #SENHA
    lab_SENHA_FL.place(x=318,y=340)  
    ent_SENHA_FL.place(x=316,y=370)

    #Botão_inserir_CR
    bot_inserir_CR_FL.place(x=275,y=445)

    #botao para sair
    bot_sair.place(x=1,y=1)


#Fazer_login_down():
def Fazer_login_down():
    #Til_CR
    til_FL.place_forget()
    #CPF
    lab_CPF_FL.place_forget()
    ent_CPF_FL.place_forget()
    #NOME
    lab_NOME_FL.place_forget()
    ent_NOME_FL.place_forget()
    #SENHA
    lab_SENHA_FL.place_forget()
    ent_SENHA_FL.place_forget()
    #Botão_inserir_CR
    bot_inserir_CR_FL.place_forget()
    #botao para sair
    #bot_sair.place(x=1,y=1)

#####################################
#Espaço_de_controle_inside


def Espaço_de_controle_up():
    carregar_agendamentos_no_treeview()

    #sistema de login():
    til_EC64.configure(text= f"Seja Bem vindo {EC_nome}")

    #fazer a interface login desaparecer
    Fazer_login_down()
    interface_menu_conta.place_forget()
    bot_sair.place_forget()

    #invocar widgets
    interface_EC.place(x=1,y=102)
    til_EC64.place(x=75,y=115)
    tv.place(x=80,y=200)
    bot_deslogar.place(x=1,y=1)
    bot_inserir_EC.place(x=80,y=400)
    bot_excluir_EC.place(x=280,y=400)



def Espaço_de_controle_down():

    #invocar widgets
    til_EC64.place_forget()
    tv.place_forget()
    bot_deslogar.place_forget()
    bot_inserir_EC.place_forget()
    interface_EC.place_forget()
    bot_excluir_EC.place_forget()


#####################################
#menu_outside

#icone
Logo = Image.open("Logo Age.png")
largura = 300
altura = 270
logo_red = Logo.resize((largura,altura))

logo_tk = ImageTk.PhotoImage(logo_red)
windown.logo_tk = logo_tk

Lab_logo = tk.Label(
    windown,
    image= logo_tk
)

#icone
Sub_Logo = Image.open("Sub Logo.png")
Sub_largura = 110
Sub_altura = 80
Sub_logo_red = Sub_Logo.resize((Sub_largura,Sub_altura))

Sub_Logo_tk = ImageTk.PhotoImage(Sub_logo_red)
windown.sublogo_tk = Sub_Logo_tk

Lab_Sub_logo = tk.Label(
    windown,
    image= Sub_Logo_tk
)

#interface
interface = tk.Canvas(
    windown,
    width= 300,
    height= 300,
    bg="#6cbf6d"
)

#titulo_da_aplicação
til = tk.Label(
    windown,
    text = "AGE MEDIC",
    font= ("Segoe UI" , 28, "bold"),
    bg="#FFFFFF",
    fg="#2596be"
)

#subtitulo
subtitle = tk.Label(
    windown,
    text = "Sistema de Saude",
    font= ("Segoe UI" , 14, "bold"),
    bg="#FFFFFF",
    fg="#6bc06c"
)

#versão
ver = tk.Label(
    windown,
    text = "Versão_1.0 Alpha",
    font= ("Segoe UI" , 14,),
    fg= "White",
    bg="#202124"
)
#ver.pack()
#ver.place(x=0,y=380)

#botao_01
botao1 = tk.Button(
    windown,
    text= "Menu(Paciente)",
    font= ("Segoe UI", 14, "bold"),
    width= 16,
    height= 1,  
    bg="#2596be",
    fg="White",
    command=scp_more

)
#botao1.pack()
#botao1.place(x=250,y=150)

#botao_02
botao2 = tk.Button(
    windown,
    text= "SAIR",
    font= ("Segoe UI", 14, "bold"),
    width= 16,
    height= 1,  
    bg="#2596be",
    fg="White",
    command= sair_aplicacao
)
#botao2.pack()
#botao2.place(x=250,y=200)

###########################################
#Menu_Paciente_outside

#interface_menu_conta
interface_menu_conta = tk.Canvas(
    windown,
    width= 300,
    height= 350,
    bg="#6ca5bf"
)

#criar uma conta
bot_CUC = tk.Button(
    windown,
    text= "Criar uma CONTA",
    font= ("Segoe UI", 14, "bold"),
    width= 16,
    height= 1,  
    bg="#2596be",
    fg="White",
    command=scp_more
)

#fazer login
bot_FL = tk.Button(
    windown,
    text= "fazer LOGIN",
    font= ("Segoe UI", 14, "bold"),
    width= 16,
    height= 1,  
    bg="#2596be",
    fg="White",
    command= scp_FL
)

#botao_sair
bot_sair = tk.Button(
    windown,
    text= "voltar",
    font= ("Segoe UI", 14, "bold"),
    width= 8,
    height= 1,  
    bg="#2596be",
    fg="White",
    command=scp_less
)


###########################################
#Criar_conta_outside

#CPF
lab_CPF = tk.Label(
    windown,
    text= "Digite seu CPF:",
    font= ("Segoe UI", 14, "bold"),
    bg="#2596be",
    fg="White"
)

ent_CPF= tk.Entry(
    windown,
    font= ("Segoe UI", 12),
    width= 18
)

#NOME
lab_NOME = tk.Label(
    windown,
    text= "Digite seu NOME:",
    font= ("Segoe UI", 14, "bold"),
    bg="#2596be",
    fg="White"
)

ent_NOME= tk.Entry(
    windown,
    font= ("Segoe UI", 12),
    width= 18
)

#SENHA
lab_SENHA = tk.Label(
    windown,
    text= "Digite sua SENHA:",
    font= ("Segoe UI", 14, "bold"),
    bg="#2596be",
    fg="White"
)

ent_SENHA= tk.Entry(
    windown,
    font= ("Segoe UI", 12),
    width= 18
)

#botao_inserir_CR
bot_inserir_CR = tk.Button(
    windown,
    text= "Inserir DADOS",
    font= ("Segoe UI", 12, "bold"),
    width= 24,
    height= 1,  
    bg="#2596be",
    fg="White",
    command= cadastrar_usuario
)

#titulo_da_CR
til_CR = tk.Label(
    windown,
    text = "Cadastro",
    font= ("Segoe UI" , 16, "bold"),
    bg="#273E66",
    fg="#FFFFFF"
)


###########################################
#Fazer_login_outside

#CPF_FL
lab_CPF_FL = tk.Label(
    windown,
    text= "#Digite seu CPF:",
    font= ("Segoe UI", 14, "bold"),
    bg="#2596be",
    fg="White"
)

ent_CPF_FL= tk.Entry(
    windown,
    font= ("Segoe UI", 12),
    width= 18
)

#NOME
lab_NOME_FL = tk.Label(
    windown,
    text= "#Digite seu NOME:",
    font= ("Segoe UI", 14, "bold"),
    bg="#2596be",
    fg="White"
)

ent_NOME_FL= tk.Entry(
    windown,
    font= ("Segoe UI", 12),
    width= 18
)

#SENHA
lab_SENHA_FL = tk.Label(
    windown,
    text= "#Digite sua SENHA:",
    font= ("Segoe UI", 14, "bold"),
    bg="#2596be",
    fg="White"
)

ent_SENHA_FL= tk.Entry(
    windown,
    font= ("Segoe UI", 12),
    width= 18
)

#botao_inserir_CR
bot_inserir_CR_FL = tk.Button(
    windown,
    text= "Inserir DADOS",
    font= ("Segoe UI", 12, "bold"),
    width= 24,
    height= 1,  
    bg="#2596be",
    fg="White",
    command= login_usuario
)

#titulo_da_CR
til_FL = tk.Label(
    windown,
    text = "Fazer Login",
    font= ("Segoe UI" , 16, "bold"),
    bg="#273E66",
    fg="#FFFFFF"
)

###########################################
#Espaço_de_controle_outside
#64 = apenas um codigo interno


#interface_EC
interface_EC = tk.Canvas(
    windown,
    width= 800,
    height= 80,
    bg="#37474f"
)

til_EC64 = tk.Label(
    windown,
    text = "Nome do paciente",
    font= ("Segoe UI" , 28, "bold"),
    bg="#37474f",
    fg="#c2d6de"
)

#botao_deslogar
bot_deslogar = tk.Button(
    windown,
    text= "deslogar",
    font= ("Segoe UI", 14, "bold"),
    width= 8,
    height= 1,  
    bg="#308c1c",
    fg="White",
    command=menu_up
)

#LISTA
tv = ttk.Treeview(
    windown,
    columns=("Paciente","Data","Especialidade","Medico","Queixa"),
    show="headings",
    height= 8,
)

tv.heading("Paciente",text="Paciente")
tv.heading("Data",text="Data")
tv.heading("Especialidade",text="Especialidade")
tv.heading("Medico",text="Medico")
tv.heading("Queixa",text="Queixa")

tv.column("Paciente", width=125)
tv.column("Data", width=125)
tv.column("Especialidade", width=125)
tv.column("Medico", width=125)
tv.column("Queixa", width=125)



def salvar_agendamento():
    paciente = ent_PACIENTE.get().strip()
    data = ent_DATA.get().strip()
    especialidade = ent_ESPECIALIDADE.get().strip()
    medico = ent_MEDICO.get().strip()
    queixa = ent_QUEIXA.get().strip()

    if not paciente or not data or not especialidade or not medico or not queixa:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # arquivo específico do usuário
    arquivo = f"agendamentos_{EC_cpf}.txt"

    # salvar no arquivo
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"{paciente},{data},{especialidade},{medico},{queixa}\n")

    # adicionar no Treeview
    tv.insert("", "end", values=(paciente, data, especialidade, medico, queixa))

    messagebox.showinfo("Sucesso", "Agendamento salvo com sucesso!")

    # limpar os campos
    ent_PACIENTE.delete(0, tk.END)
    ent_DATA.delete(0, tk.END)
    ent_ESPECIALIDADE.delete(0, tk.END)
    ent_MEDICO.delete(0, tk.END)
    ent_QUEIXA.delete(0, tk.END)



def carregar_agendamentos_no_treeview():
    tv.delete(*tv.get_children())  # limpa a tabela

    arquivo = f"agendamentos_{EC_cpf}.txt"

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    paciente, data, esp, medico, queixa = linha.split(",")
                    tv.insert("", "end", values=(paciente, data, esp, medico, queixa))
    except FileNotFoundError:
        pass  # usuário novo -> sem consultas ainda



#abrir nova tela
def abrir_nova_tela():
    global lab_PACIENTE, ent_PACIENTE
    global lab_DATA, ent_DATA
    global lab_ESPECIALIDADE, ent_ESPECIALIDADE
    global lab_MEDICO, ent_MEDICO
    global lab_QUEIXA, ent_QUEIXA

    nova_tela = tk.Toplevel(windown)  # cria nova janela
    nova_tela.title("Nova Tela")
    nova_tela.geometry("300x350")


    #Paciente
    lab_PACIENTE = tk.Label(
        nova_tela,
        text= "Paciente:",
        font= ("Segoe UI", 14, "bold"),
        bg="#2596be",
        fg="White"
    )

    ent_PACIENTE= tk.Entry(
        nova_tela,
        font= ("Segoe UI", 12),
        width= 18
    )

    #Data
    lab_DATA = tk.Label(
        nova_tela,
        text= "data:",
        font= ("Segoe UI", 14, "bold"),
        bg="#2596be",
        fg="White"
    )

    ent_DATA= tk.Entry(
        nova_tela,
        font= ("Segoe UI", 12),
        width= 18
    )


    #Especialidade
    lab_ESPECIALIDADE = tk.Label(
        nova_tela,
        text= "Especialidade:",
        font= ("Segoe UI", 14, "bold"),
        bg="#2596be",
        fg="White"
    )

    ent_ESPECIALIDADE= tk.Entry(
        nova_tela,
        font= ("Segoe UI", 12),
        width= 18
    )


    #Médico
    lab_MEDICO = tk.Label(
        nova_tela,
        text= "Médico:",
        font= ("Segoe UI", 14, "bold"),
        bg="#2596be",
        fg="White"
    )

    ent_MEDICO= tk.Entry(
        nova_tela,
        font= ("Segoe UI", 12),
        width= 18
    )


    #Queixa
    lab_QUEIXA = tk.Label(
        nova_tela,
        text= "Queixa:",
        font= ("Segoe UI", 14, "bold"),
        bg="#2596be",
        fg="White"
    )

    ent_QUEIXA= tk.Entry(
        nova_tela,
        font= ("Segoe UI", 12),
        width= 18
    )

    #botao_inserir_dados_gerais
    bot_IDG = tk.Button(
    nova_tela,
    text= "Inserir",
    font= ("Segoe UI", 10, "bold"),
    width= 8,
    height= 1,  
    bg="#26444c",
    fg="White",
    command=salvar_agendamento
)


    lab_PACIENTE.pack()
    ent_PACIENTE.pack()
    lab_DATA.pack()
    ent_DATA.pack()
    lab_ESPECIALIDADE.pack()
    ent_ESPECIALIDADE.pack()
    lab_MEDICO.pack()
    ent_MEDICO.pack()
    lab_QUEIXA.pack()
    ent_QUEIXA.pack()
    bot_IDG.pack()


def cancelar_consulta():
    selecionado = tv.selection()

    if not selecionado:
        messagebox.showerror("Erro", "Selecione uma consulta para cancelar!")
        return

    # pegar valores da linha selecionada
    valores = tv.item(selecionado)["values"]
    paciente, data, especialidade, medico, queixa = valores

    arquivo = f"agendamentos_{EC_cpf}.txt"

    # ler todas as consultas
    novas_linhas = []

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    if linha != f"{paciente},{data},{especialidade},{medico},{queixa}":
                        novas_linhas.append(linha)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de agendamentos não encontrado!")
        return

    # reescrever o arquivo sem a consulta cancelada
    with open(arquivo, "w", encoding="utf-8") as f:
        for linha in novas_linhas:
            f.write(linha + "\n")

    # remover do Treeview
    tv.delete(selecionado)

    messagebox.showinfo("Sucesso", "Consulta cancelada com sucesso!")


bot_inserir_EC = tk.Button(
    windown,
    text= "Agendar Consulta",
    font= ("Segoe UI", 14, "bold"),
    width= 16,
    height= 1,  
    bg="#2596be",
    fg="White",
    command= abrir_nova_tela
)


bot_excluir_EC = tk.Button(
    windown,
    text= "Cancelar Consulta",
    font= ("Segoe UI", 14, "bold"),
    width= 16,
    height= 1,  
    bg="#2596be",
    fg="White",
    command= cancelar_consulta
)







#execultador do progama
menu_up()
windown.mainloop()