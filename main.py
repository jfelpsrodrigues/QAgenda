from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import os
from qAgenda import *

# Collors ---------------------------
back = '#f6ffec'
collor_font = '#333652'
obj_collor = '#FAD02C'
button_collor = '#417B5A'
button_collor_b = "#8EB1C7"
button_collor_r = "#55449E"
grey = '#d9d9d9'
black = "black"
white = 'white'

# Fonts -----------------------------
font_title = 'Roboto 18'
font_title_b = 'Roboto 18 bold'
font_obj = 'Roboto 1'
font_label = 'Roboto 12'
font_button = 'Roboto 13'
font_button_ext = 'Roboto 10'

# Func -------------------------------------------
def to_ascii(text):
    ascii_values = [ord(character) for character in text] # tranformar todas as letra em num da tabela ascii
    num_str = ''
    for i in ascii_values:
        num_str += str(i)
    return int(num_str)

def new_business_csv(name):
    path = 'files/scheduling'
    arq = path + '/' + name + '.csv'

    if not os.path.exists(arq):
        file = open(arq, 'w')
    file.close()

def business_exists(name_file, id):
    with open(name_file, 'r', encoding='utf-8') as arq:
            colunas = list(csv.reader(arq, delimiter=','))
            for linha in colunas:
                if(len(linha) == 0):
                    break
                elif id == int(linha[1]):
                    return False
    
    return True

def AqrList(name_file):
        with open(name_file, 'r', encoding='unicode_escape') as arq:
            lojas_csv = csv.reader(arq, delimiter=',')
            list_lojas = list(lojas_csv)
            return list_lojas

# Login ------------------------------------------------------
class Login(Tk):
    def __init__(self, geometry, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry(geometry)
        self.config(bg=bg)
        self.resizable(width=width, height=height)

        self.widgets_init_sigin()

    def widgets_sigin(self):
        # Frames
        self.frame_1 = Frame(self, width=350, height=50, background=back, relief='flat')
        self.frame_2 = Frame(self, width=350, height=300, background=back, relief='flat')

        # Labels
        self.lab_login = Label(self.frame_1, text="Login", anchor=NE, font=(font_title), bg=back, fg=collor_font, relief='flat')
        self.lab_line = Label(self.frame_1, text="", anchor=NW, font=(font_obj), width=300, bg=obj_collor, fg=back, relief='flat')
        self.lab_name = Label(self.frame_2, text="CPF/CNPJ:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pass = Label(self.frame_2, text="Senha:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        
        # Entry
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pass = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, show='*', relief='flat')
        
        # Buttons
        self.button_confirm = Button(self.frame_2, text="Entrar", command=self.search_login, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
        self.button_inscr = Button(self.frame_2, text="Cadastrar", command=self.new_window_sub, width=10, anchor=N, font=(font_button_ext), highlightthickness=-1, bg=back, fg=collor_font, relief='flat')
        self.button_lost = Button(self.frame_2, text="Esqueceu a Senha?", command=self.new_window_recovery, width=15, anchor=N, font=(font_button_ext), highlightthickness=-1, bg=back, fg=collor_font, relief='flat')
        

    def widgets_init_sigin(self):
        self.widgets_sigin()

        # Frames Init
        self.frame_1.grid(row=0, column=0, pady=2, sticky=NSEW)
        self.frame_2.grid(row=1, column=0, pady=2, sticky=NSEW)

        # Labels Init
        self.lab_login.place(x=15, y=5)
        self.lab_line.place(x=15, y=40)
        self.lab_name.place(x=15, y=15)
        self.lab_pass.place(x=15, y=60)

        # Entry Init
        self.entry_name.place(x=105, y=15)
        self.entry_pass.place(x=105, y=60)

        # Button Init
        self.button_confirm.place(x=115, y=150)
        self.button_inscr.place(x=38, y=200)
        self.button_lost.place(x=172, y=200)

    def search_login(self):
        existe = 0
        try:
            id = int(self.entry_name.get())
            passnumber = int(self.entry_pass.get())
            # Busca nos estabelecimentos
            with open("files/estabelecimentos.csv", 'r', encoding='unicode_escape') as arq:
                lojas_csv = csv.reader(arq, delimiter=',')
                list_lojas = list(lojas_csv)
                for linha in list_lojas:
                    if id == int(linha[1]) and passnumber == int(linha[4]):
                        self.new_window_home_store(id=id, passnumber=passnumber)
                        existe = 1
                        break
                    
            # Busca nos clientes
            with open("files/clientes.csv", 'r', encoding='unicode_escape') as arq:
                clientes_csv = list(csv.reader(arq, delimiter=','))
                for linha in clientes_csv:
                    if id == int(linha[1]) and passnumber == int(linha[4]):
                        self.new_window_home_client(id=id, passnumber=passnumber)
                        existe = 1
                        break
            
            if existe == 0:
                messagebox.showerror("Erro", "Usuário não cadastrado\n")

        except:
            messagebox.showerror("Erro", "Verifique os dados digitados\n")

    # Chama a tela do cliente
    def new_window_home_client(self, id, passnumber):
        self.destroy()
        home = HomeClient(id, passnumber)
        home.mainloop()

    # Chama a tela do estabelecimento
    def new_window_home_store(self, id, passnumber):
        self.destroy()
        home = HomeStore(id, passnumber)
        home.mainloop()

    # Chama a tela da recuperação de senha
    def new_window_recovery(self):
        self.destroy()
        window = Recovery("350x350")
        window.mainloop()

    # Chama a tela do cadastro
    def new_window_sub(self):
        self.destroy()
        subs = Registration()
        subs.mainloop()

# Recuperação ------------------------------------------------------
class Recovery(Tk):
    def __init__(self, geometry, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry(geometry)
        self.config(bg=bg)
        self.resizable(width=width, height=height)

        self.widgets_init_sigin()

    def widgets_sigin(self):
        # Frames
        self.frame_1 = Frame(self, width=350, height=50, background=back, relief='flat')
        self.frame_2 = Frame(self, width=350, height=300, background=back, relief='flat')

        # Labels
        self.lab_login = Label(self.frame_1, text="Recuperar Senha", anchor=NE, font=(font_title), bg=back, fg=collor_font, relief='flat')
        self.lab_line = Label(self.frame_1, text="", anchor=NW, font=(font_obj), width=300, bg=obj_collor, fg=back, relief='flat')
        self.lab_name = Label(self.frame_2, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pass = Label(self.frame_2, text="CPF/CNPJ:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        
        # Entry
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pass = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        
        # Buttons
        self.button_confirm = Button(self.frame_2, text="Cadastrar", command=self.new_window_sub, width=10, height=1, relief='flat', font=font_button_ext, highlightthickness=-1, bg=back, fg=black)
        self.button_inscr = Button(self.frame_2, text="Login", command=self.ret_login, width=10, anchor=N, font=font_button_ext, highlightthickness=1, bg=button_collor_b, fg=back, relief='flat')
        self.button_lost = Button(self.frame_2, text="Lembrar senha", command=self.recovery_login, width=15, anchor=N, font=font_button_ext, highlightthickness=1, bg=button_collor, fg=back, relief='flat')
        

    def widgets_init_sigin(self):
        self.widgets_sigin()

        # Frames Init
        self.frame_1.grid(row=0, column=0, pady=2, sticky=NSEW)
        self.frame_2.grid(row=1, column=0, pady=2, sticky=NSEW)

        # Labels Init
        self.lab_login.place(x=15, y=5)
        self.lab_line.place(x=15, y=40)
        self.lab_name.place(x=15, y=15)
        self.lab_pass.place(x=15, y=60)

        # Entry Init
        self.entry_name.place(x=105, y=15)
        self.entry_pass.place(x=105, y=60) # Para o CPF

        # Button Init
        self.button_confirm.place(x=115, y=200) # Para tela de cadastro
        self.button_inscr.place(x=200, y=150) # Para tela de login
        self.button_lost.place(x=30, y=150) # Para lembrar a senha

    def recovery_login(self):
        ver = False # Variavel de verificação: False - Não esta na lista, True - Esta na lista
        try:
            # Pega as informações digitadas na tela
            name = str(self.entry_name.get())
            ident = int(self.entry_pass.get())

            # Tranformar o arquivo em lista
            client_list = AqrList("files/clientes.csv")

            # Procura o login na lista
            for item in client_list:
                if name == str(item[0]) and ident == int(item[1]):
                    senha = "Sua senha é " + str(item[4])
                    messagebox.showinfo("Sucesso", senha)
                    ver = True
            
            if not ver:
                messagebox.showerror("Erro", "Seu cadastro não foi encontrado!\nVerifique os dados ou faça um novo cadastro.\n")
        except:
            messagebox.showerror("Erro", "Verifique os dados e tente novamente\n")
            

    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()

    def new_window_sub(self):
        self.destroy()
        subs = Registration()
        subs.mainloop()

# Cadastro ------------------------------------------------------
class Registration(Tk):
    def __init__(self, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry("780x500")
        self.config(bg=bg)
        self.resizable(width=width, height=height)

        self.state = -1 # O valor de 0 será para o cliente e de 1 para o estabelecimento

        self.widgets_init_sub()
        self.ret_client()

    def widgets_sub(self):
        # Frames -------------------------------------
        self.frame_1 = Frame(self, width=300, height=35, background=back, relief='flat')
        self.frame_2 = Frame(self, width=320, height=321, background=back, relief='flat')
        self.frame_3 = Frame(self, width=320, height=321, background=back, relief='flat')
        self.frame_4 = Frame(self, width=710, height=50, background=back, relief='flat')

        # Objects --------------------------------------
        self.label_line_div =  Label(self, text="", font=(font_obj), height=135, bg=button_collor_b, fg=back, relief='flat')
        self.lab_line = Label(self.frame_1, text="", anchor=N, font=(font_obj), width=280, bg=obj_collor, fg=back, relief='flat')

        # Labels -----------------------------------
        self.lab_title = Label(self.frame_1, text="Cadastre-se no QAgenda! ", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        # Cliente --------------------------------------
        self.lab_name = Label(self.frame_2, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_cpf = Label(self.frame_2, text="CPF:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_id = Label(self.frame_2, text="Idade:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_set = Label(self.frame_2, text="Bairro:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pass = Label(self.frame_2, text="Senha:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        # Estabelecimento ---------------------------
        self.lab_name_est = Label(self.frame_3, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_cnpj = Label(self.frame_3, text="CNPJ:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_ramo = Label(self.frame_3, text="Serviço:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_set_est = Label(self.frame_3, text="Bairro:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pass_est = Label(self.frame_3, text="Senha:", font=(font_label), bg=back, fg=collor_font, relief="flat")

        # Entry --------------------------------
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_cpf = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_id = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_set = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pass = Entry(self.frame_2, width=23, bg=white, fg=black, show="*", font=(font_label), highlightthickness=1, relief='flat')
        # Entry Estabelecimento ------------------
        self.entry_name_est = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_cnpj = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_ramo = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_set_est = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pass_est = Entry(self.frame_3, width=23, bg=white, fg=black, show="*", font=(font_label), highlightthickness=1, relief='flat')

        # Buttons ------------------------------
        self.button_confirm = Button(self.frame_4, text="Confirmar", command=self.write_register, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
        self.button_client = Button(self.frame_2, text="Cliente", command=self.ret_client, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor_b, fg=back)
        self.button_est = Button(self.frame_3, text="Loja", command=self.ret_estabelecimento, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor_b, fg=back)
        self.button_ret = Button(self.frame_4, text="Retornar", command=self.ret_login, width=10, anchor=N, font=(font_button_ext), highlightthickness=-1, bg=back, fg=collor_font, relief='flat')

    def widgets_init_sub(self):
        self.widgets_sub()

        # Frames Init
        self.frame_1.place(x=50, y=5)
        self.frame_2.place(x=50, y=56)
        self.frame_3.place(x=390, y=56)
        self.frame_4.place(x=20, y=440)

        # Objects
        self.label_line_div.place(x=377, y=20)
        self.lab_line.place(x=0, y=30)

        # Labels Text ----------------------------
        self.lab_title.place(x=0, y=0)
        self.lab_name.place(x=0, y=75)
        self.lab_cpf.place(x=0, y=120)
        self.lab_id.place(x=0, y=168)
        self.lab_set.place(x=0, y=215)
        self.lab_pass.place(x=0, y=260)
        # Text Estabelecimento
        self.lab_name_est.place(x=15, y=75)
        self.lab_cnpj.place(x=15, y=120)
        self.lab_ramo.place(x=15, y=168)
        self.lab_set_est.place(x=15, y=215)
        self.lab_pass_est.place(x=15, y=260)

        # Entry --------------------------------
        self.entry_name.place(x=90, y=75)
        self.entry_cpf.place(x=90, y=120)
        self.entry_id.place(x=90, y=168)
        self.entry_set.place(x=90, y=215)
        self.entry_pass.place(x=90, y=260)
        # Entry Estabelecimento
        self.entry_name_est.place(x=105, y=75)
        self.entry_cnpj.place(x=105, y=120)
        self.entry_ramo.place(x=105, y=168)
        self.entry_set_est.place(x=105, y=215)
        self.entry_pass_est.place(x=105, y=260)

        # Buttons -----------------------------------------
        self.button_confirm.place(x=295, y=0)
        self.button_client.place(x=172, y=0)
        self.button_est.place(x=15, y=0)
        self.button_ret.place(x=0, y=15)

    def ret_client(self):
        self.entry_name.config(state='normal')
        self.entry_cpf.config(state='normal')
        self.entry_id.config(state='normal')
        self.entry_set.config(state='normal')
        self.entry_pass.config(state='normal')

        self.button_client.config(bg=button_collor_b)
        self.button_est.config(bg=grey)

        self.entry_name_est.config(state='disabled')
        self.entry_cnpj.config(state='disabled')
        self.entry_ramo.config(state='disabled')
        self.entry_set_est.config(state='disabled')
        self.entry_pass_est.config(state='disabled')
        
        self.state = 0

    def ret_estabelecimento(self):
        self.entry_name_est.config(state='normal')
        self.entry_cnpj.config(state='normal')
        self.entry_ramo.config(state='normal')
        self.entry_set_est.config(state='normal')
        self.entry_pass_est.config(state='normal')

        self.button_est.config(bg=button_collor_b)
        self.button_client.config(bg=grey)

        self.entry_name.config(state='disabled')
        self.entry_cpf.config(state='disabled')
        self.entry_id.config(state='disabled')
        self.entry_set.config(state='disabled')
        self.entry_pass.config(state='disabled')

        self.state = 1

    def write_register(self):
        if self.state == 0: # Cliente
            name = str(self.entry_name.get()).lower()
            cpf = int(self.entry_cpf.get())
            age = int(self.entry_id.get())
            address = str(self.entry_set.get())
            password = int(self.entry_pass.get())

            if(business_exists(name_file='files/clientes.csv', id=cpf)): # Verifica se já exite o cadastro
                CadastroCliente(nome=name, bairro=address, senha=password, cpf=cpf, idade=age)
                self.ret_login()
        elif self.state == 1: # Estabelecimento 
            name = str(self.entry_name_est.get()).lower()
            cnpj = int(self.entry_cnpj.get())
            business = str(self.entry_ramo.get())
            address = str(self.entry_set_est.get())
            password = int(self.entry_pass_est.get())

            if(business_exists(name_file='files/estabelecimentos.csv', id=cnpj)): # Verifica se já exite o cadastro
                new_business_csv(name=name.lower())
                CadastroLoja(name=name, bairro=address, ramo=business, cnpj=cnpj, senha=password)
                self.ret_login()

    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()

# Home Client ---------------------------------------------------------
class HomeClient(Tk):
    def __init__(self, id, passnumber, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry("780x500")
        self.config(bg=bg)
        self.resizable(width=width, height=height)

        self.id = id
        self.passnumber = passnumber

        self.widgets_init_home()
        self.init_values()
        
    def widgets_sub(self):
        # Frames -------------------------------------
        self.frame_1 = Frame(self, width=300, height=35, background=back, relief='flat') # Frame do Title
        self.frame_2 = Frame(self, width=320, height=321, background=back, relief='flat') # Frame do Agendamento
        self.frame_3 = Frame(self, width=320, height=321, background=back, relief='flat') # Frame da lista de agendamento
        self.frame_4 = Frame(self, width=710, height=50, background=back, relief='flat') # Frame rodape

        # Objects --------------------------------------
        self.label_line_div =  Label(self, text="", font=(font_obj), height=135, bg=button_collor_b, fg=back, relief='flat')
        self.lab_line = Label(self.frame_1, text="", anchor=N, font=(font_obj), width=280, bg=obj_collor, fg=back, relief='flat')

        # Labels -----------------------------------
        self.lab_title = Label(self.frame_1, text="Bem-Vindo ao QAgenda!   ", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        self.lab_h2_one = Label(self.frame_2, text="Faça seu Agendamento! ", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        self.lab_h2_two = Label(self.frame_3, text="Seus Agendamentos! ", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        # Agendamento
        self.lab_name = Label(self.frame_2, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_store = Label(self.frame_2, text="Loja:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_serv = Label(self.frame_2, text="Serviço:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_day = Label(self.frame_2, text="Dia:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_hour = Label(self.frame_2, text="Horário:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        # Lista 
        self.lab_list = Label(self.frame_3, text="Escolha a Loja:", font=(font_label), bg=back, fg=collor_font, relief="flat")

        # Entry --------------------------------
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.combox_store = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        self.combox_day = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        self.combox_hour = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        # Entry Lista ------------------
        self.combox_list = ttk.Combobox(self.frame_3, width=19, font=(font_label))
        self.list_agend = Listbox(self.frame_3, width=35, font=font_label,fg=collor_font)

        # Buttons ------------------------------
        self.button_confirm = Button(self.frame_4, text="Agendar", command=self.agendar, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
        self.button_client = Button(self.frame_4, text="Remover", command=self.remove_agenda, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor_r, fg=back)
        self.button_list = Button(self.frame_4, text="Agendamentos", command=self.init_listbox, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor_b, fg=back)
        self.button_ret = Button(self.frame_4, text="Retornar", command=self.ret_login, width=10, anchor=N, font=(font_button_ext), highlightthickness=-1, bg=back, fg=collor_font, relief='flat')

    def widgets_init_home(self):
        self.widgets_sub()

        # Frames Init
        self.frame_1.place(x=50, y=5)
        self.frame_2.place(x=50, y=56)
        self.frame_3.place(x=390, y=56)
        self.frame_4.place(x=20, y=440)

        # Objects
        self.label_line_div.place(x=377, y=20)
        self.lab_line.place(x=0, y=30)

        # Labels Text ----------------------------
        self.lab_title.place(x=0, y=0) # Posição Titulo
        self.lab_h2_one.place(x=0, y=5) # Posição "Faca seu agendamento"
        self.lab_h2_two.place(x=15, y=5) # Posiçao "Seus agendamentos"
        # Labels Agendamento
        self.lab_name.place(x=0, y=100)
        self.lab_store.place(x=0, y=145)
        self.lab_day.place(x=0, y=193)
        self.lab_hour.place(x=0, y=240)
        # Label list
        self.lab_list.place(x=15, y=55)

        # Entry --------------------------------
        self.entry_name.place(x=90, y=100)
        self.combox_store.place(x=90, y=145)
        self.combox_day.place(x=90, y=193)
        self.combox_hour.place(x=90, y=240)
        # Entry Agendamento
        self.combox_list.place(x=130, y=55)
        self.list_agend.place(x=15, y=85)

        # Buttons -----------------------------------------
        self.button_confirm.place(x=200, y=0)
        self.button_list.place(x=400, y=0)
        self.button_client.place(x=550, y=0)
        self.button_ret.place(x=0, y=15)
            
    def init_values(self):
        # Init Values -----------------------------------------
        self.list = AqrList("files/estabelecimentos.csv")
        self.stores = [row[0] for row in self.list]
        self.combox_store["values"] = self.stores
        self.combox_list["values"] = self.stores
        self.combox_day["values"] = [day for day in range(1, 8)]
        self.combox_hour["values"] = [hour for hour in range(0, 25)]
    
        self.list = AqrList("files/clientes.csv")
        for i in self.list:
            if(int(self.id) == int(i[1])):
                self.entry_name.insert(0, i[0])

        self.entry_name["state"] = 'readonly'

    def init_listbox(self):
        # Verificar se foi selecionado alguma loja
        if(self.combox_list.current() != -1):
            # Busca o nome do arquivo e cria uma lista com ele
            name_store = str(self.combox_list.get())
            name_file_store = "files/scheduling/" + name_store + ".csv"
            self.list = AqrList(name_file_store)
            # conta o tamanho da lista
            num_itens = len(self.list)
            if(num_itens == 0):
                messagebox.showerror("Erro", "Não há Agendamentos\n")
            else:
                # Adiciona somente os agendamentos do cliente especifico
                list_agenda = [] 
                for item in self.list:
                    if int(item[2]) == self.id:
                        list_agenda.append(item)

                # Limpar o listbox
                self.list_agend.delete(0, END)    
                for item in list_agenda:
                    item = "dia: " + item[0] + " - Hora: " + str(int(item[1])) + " - CPF: " + item[2]
                    self.list_agend.insert(END, item)
        else:
            messagebox.showerror("Erro", "Nenhuma loja foi selecionada\nTente Novamente!")
    
    def remove_agenda(self):
        # Verificar se foi selecionado alguma loja
        if(self.combox_list.current() != -1):
            # Armazena quantos itens tem na listbox
            num_itens = self.list_agend.size()
            # Cria a string do nome do arquivo a ser aberto
            name_store = str(self.combox_list.get())
            name_file_store = "files/scheduling/" + name_store + ".csv"
            # Verifica se exite algum item
            if(num_itens == 0):
                messagebox.showerror("Erro", "Não há Agendamentos\nTente Novamente!")
            else:
                # Remove o primeiro agendamento daquele cliente naquela loja
                RemoverAgendamento(file_name=name_file_store, cpf=int(self.id))
                if num_itens == 1:
                    self.list_agend.delete(0, END)
                else:
                    self.init_listbox()
                # Exibe uma mensagem de sucesso na tela
                messagebox.showinfo("Sucesso", "O primeiro agendamento foi removido com sucesso!")    
        else:
            messagebox.showerror("Erro", "Nenhuma loja foi selecionada\nTente Novamente!")

    def agendar(self):
        try:
            value_day = int(self.combox_day.get())
            value_hour = int(self.combox_hour.get())
            value_store = str(self.combox_store.get())
            value_name = str(self.entry_name.get())
            name_store = "files/scheduling/" + value_store + ".csv"
            RealizarAgendamento(file_name=name_store, dia=value_day, horario=value_hour, cpf=self.id, name=value_name)
            OrdenacaoAgendamento(file_name=name_store)
        except:
            messagebox.showerror("Erro", "Verifique os dados e tente novamente!")
            

    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()

# Home Store ---------------------------------------------------------
class HomeStore(Tk):
    def __init__(self, id, passnumber, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry("780x500")
        self.config(bg=bg)
        self.resizable(width=width, height=height)

        self.id = id
        self.passnumber = passnumber

        self.widgets_init_home()
        self.init_values()
        
    def widgets_sub(self):
        # Frames -------------------------------------
        self.frame_1 = Frame(self, width=300, height=35, background=back, relief='flat') # Frame do Title
        self.frame_2 = Frame(self, width=320, height=321, background=back, relief='flat') # Frame do Agendamento
        self.frame_3 = Frame(self, width=320, height=321, background=back, relief='flat') # Frame da lista de agendamento
        self.frame_4 = Frame(self, width=710, height=50, background=back, relief='flat') # Frame rodape

        # Objects --------------------------------------
        self.label_line_div =  Label(self, text="", font=(font_obj), height=135, bg=button_collor_b, fg=back, relief='flat')
        self.lab_line = Label(self.frame_1, text="", anchor=N, font=(font_obj), width=280, bg=obj_collor, fg=back, relief='flat')

        # Labels -----------------------------------
        self.lab_title = Label(self.frame_1, text="Bem-Vindo ao QAgenda!   ", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        self.lab_h2_one = Label(self.frame_2, text="Cadastre seus Serviços!", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        self.lab_h2_two = Label(self.frame_3, text="Seus Agendamentos!", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        # Agendamento --------------------------------------
        self.lab_name = Label(self.frame_2, text="Empresa:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_serv = Label(self.frame_2, text="Serviço:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pay = Label(self.frame_2, text="Preço:", font=(font_label), bg=back, fg=collor_font, relief="flat")

        # Entry --------------------------------
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_serv = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pay = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        # Entry Lista ------------------
        self.list_agend = Listbox(self.frame_3, width=35, font=font_label,fg=collor_font)

        # Buttons ------------------------------
        self.button_confirm = Button(self.frame_4, text="Cadastrar", command=self.cad_servico, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
        self.button_client = Button(self.frame_4, text="Remover", command=self.remove_agenda, width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor_r, fg=back)
        self.button_ret = Button(self.frame_4, text="Retornar", command=self.ret_login, width=10, anchor=N, font=(font_button_ext), highlightthickness=-1, bg=back, fg=collor_font, relief='flat')

    def widgets_init_home(self):
        self.widgets_sub()

        # Frames Init
        self.frame_1.place(x=50, y=5)
        self.frame_2.place(x=50, y=56)
        self.frame_3.place(x=390, y=56)
        self.frame_4.place(x=20, y=440)

        # Objects
        self.label_line_div.place(x=377, y=20)
        self.lab_line.place(x=0, y=30)

        # Labels Text ----------------------------
        self.lab_title.place(x=0, y=0) # Posição Titulo
        self.lab_h2_one.place(x=0, y=5) # Posição "Faca seu agendamento"
        self.lab_h2_two.place(x=15, y=5) # Posiçao "Seus agendamentos"
        # Labels Agendamento
        self.lab_name.place(x=0, y=120)
        self.lab_serv.place(x=0, y=165)
        self.lab_pay.place(x=0, y=210)

        # Entry --------------------------------
        self.entry_name.place(x=90, y=120)
        self.entry_serv.place(x=90, y=165)
        self.entry_pay.place(x=90, y=210)
        # Entry Agendamento
        self.list_agend.place(x=15, y=75)

        # Buttons -----------------------------------------
        self.button_confirm.place(x=200, y=0)
        self.button_client.place(x=400, y=0)
        self.button_ret.place(x=0, y=15)

    def init_values(self):
        self.list = AqrList("files/estabelecimentos.csv")
        # Procura o nome da empresa na lista
        for i in self.list:
            if(int(self.id) == int(i[1])):
                self.entry_name.insert(0, i[0])
                name_story = i[0]

        self.entry_name["state"] = 'readonly' #Desabilita o entry para o nome da empresa

        name_file_store = "files/scheduling/" + name_story + ".csv"
        self.list = AqrList(name_file_store)
        num_itens = len(self.list)
        # Limpar o listbox
        self.list_agend.delete(0, END)
        if num_itens == 0:
            self.list_agend.insert(END, "Não há agendamentos")
        # escrever cada item na listbox    
        for item in self.list:
            item = "dia: " + item[0] + " - Hora: " + str(int(item[1])) + " - Nome: " + item[3]
            self.list_agend.insert(END, item)

    def cad_servico(self):
        name_value = str(self.entry_name.get())
        serv_value = self.entry_serv.get()
        pay_value = self.entry_pay.get()
        if(len(pay_value) == 0 or len(serv_value) == 0):
            messagebox.showerror("Erro", "Verifique os dados e tente novamente\n")
        else:
            messagebox.showinfo("Sucesso", "O Serviço foi cadastrado com sucesso\n")

    def remove_agenda(self):
        # Armazena quantos itens tem na listbox
        num_itens = self.list_agend.size()

        # Verifica se exite algum item
        if num_itens == 0 or self.list_agend.get(0) == "Não há agendamentos":
            messagebox.showerror("Erro", "Não há Agendamentos\n")
        else:
            # Cria a string do nome do arquivo a ser aberto
            name_store = str(self.entry_name.get())
            name_file_store = "files/scheduling/" + name_store + ".csv"
            # Obter agendamento selecionado
            selection = self.list_agend.curselection()
            if selection:
                # Tranformar o arquivo em lista
                self.list = AqrList(name_file_store)
                # Obtém o índice do primeiro item selecionado
                index = selection[0]
                # Obtém o texto do item selecionado
                name_client = self.list_agend.get(index)
                # Faz o tratamento da string do cliente
                name_client_list = str(name_client).split()
                name_client = name_client_list[-1]

                # Busca o cpf do cliente selecionado
                for item in self.list:
                    name_in_list = str(item[3]).replace(" ", "") # Faz o tratamento da string da lista
                    if name_client == name_in_list:
                        id_client = int(item[2]) 
                
                # Remove o primeiro agendamento daquele cliente naquela loja
                RemoverAgendamento(file_name=name_file_store, cpf=id_client)
                self.init_values()
                # Exibe uma mensagem de sucesso na tela
                messagebox.showinfo("Sucesso", "O primeiro agendamento deste cliente foi removido com sucesso!")
            else:
                messagebox.showerror("Erro", "Não foi selecionado nenhum agendamento\nTente Novamente!")
        
    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()


# Main ----------------------------------------------------------------
login = Login("350x350")
login.mainloop()
