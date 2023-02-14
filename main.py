from tkinter import *
import tkinter
from tkinter import ttk
import csv
import os

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
    path = 'c/files/scheduling'
    arq = path + '/' + name + '.csv'

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(arq):
        file = open(arq, 'w')
    file.close()

def business_exists(name_file, id):
    with open(name_file, 'r', encoding='utf-8') as arq:
            lojas_csv = csv.reader(arq, delimiter=',')
            for linha in lojas_csv:
                if str(id) == linha[1]:
                    print("já esta aq pow")
                    return False
    
    return True

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
        self.button_lost = Button(self.frame_2, text="Esqueceu a Senha?", width=15, anchor=N, font=(font_button_ext), highlightthickness=-1, bg=back, fg=collor_font, relief='flat')
        

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
        id = str(self.entry_name.get())
        passnumber = str(self.entry_pass.get())
        # Busca nos estabelecimentos
        with open("c/files/estabelecimentos.csv", 'r', encoding='utf-8') as arq:
            lojas_csv = csv.reader(arq, delimiter=',')
            for linha in lojas_csv:
                if id == linha[1] and passnumber == linha[4]:
                    print("deu certo")
                    break
                
        # Busca nos clientes
        with open('c/files/clientes.csv', 'r', encoding='utf-8') as arq:
            clientes_csv = csv.reader(arq, delimiter=',')
            for linha in clientes_csv:
                if id == linha[1] and passnumber == linha[4]:
                    self.new_window_home(id=id, passnumber=passnumber)
                    break
    def new_window_home(self, id, passnumber):
        self.destroy()
        home = HomeClient(id, passnumber)
        home.mainloop()

    def new_window_sub(self):
        self.destroy()
        subs = Registration()
        subs.mainloop()

# Cadastro ------------------------------------------------------
class Registration(Tk):
    def __init__(self, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry("750x500")
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
            name = str(self.entry_name.get())
            cpf = int(self.entry_cpf.get())
            age = int(self.entry_id.get())
            address = str(self.entry_set.get())
            password = to_ascii(str(self.entry_pass.get()))

            if(business_exists(name_file='c/files/clientes.csv', id=cpf)): # Verifica se já exite o cadastro
                print(name + str(cpf) + str(age) + address + str(password))
        elif self.state == 1: # Estabelecimento 
            name = str(self.entry_name_est.get())
            cnpj = int(self.entry_cnpj.get())
            business = str(self.entry_ramo.get())
            address = str(self.entry_set_est.get())
            password = to_ascii(str(self.entry_pass_est.get()))

            if(business_exists(name_file='c/files/estabelecimentos.csv', id=cnpj)): # Verifica se já exite o cadastro
                new_business_csv(name=name.lower())
                print(name + str(cnpj) + str(business) + address + str(password))

    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()

# Home Client ---------------------------------------------------------
class HomeClient(Tk):
    def __init__(self, id, passnumber, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry("750x500")
        self.config(bg=bg)
        self.resizable(width=width, height=height)

        self.id = id
        self.passnumber = passnumber

        self.widgets_init_home()
        
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
        # Agendamento --------------------------------------
        self.lab_name = Label(self.frame_2, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_store = Label(self.frame_2, text="Loja:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_serv = Label(self.frame_2, text="Serviço:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_day = Label(self.frame_2, text="Dia:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_hour = Label(self.frame_2, text="Horário:", font=(font_label), bg=back, fg=collor_font, relief="flat")

        # Entry --------------------------------
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.combox_store = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        self.combox_serv = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        self.combox_day = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        self.combox_hour = ttk.Combobox(self.frame_2, width=22, font=(font_label))
        # Entry Lista ------------------
        self.list_agend = Listbox(self.frame_3, width=35, font=font_label,fg=collor_font)

        # Buttons ------------------------------
        self.button_confirm = Button(self.frame_4, text="Agendar", width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
        self.button_client = Button(self.frame_4, text="Remover", width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor_r, fg=back)
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
        self.lab_name.place(x=0, y=75)
        self.lab_store.place(x=0, y=120)
        self.lab_serv.place(x=0, y=168)
        self.lab_day.place(x=0, y=215)
        self.lab_hour.place(x=0, y=260)

        # Entry --------------------------------
        self.entry_name.place(x=90, y=75)
        self.combox_store.place(x=90, y=120)
        self.combox_serv.place(x=90, y=168)
        self.combox_day.place(x=90, y=215)
        self.combox_hour.place(x=90, y=260)
        # Entry Agendamento
        self.list_agend.place(x=15, y=75)

        # Buttons -----------------------------------------
        self.button_confirm.place(x=200, y=0)
        self.button_client.place(x=400, y=0)
        self.button_ret.place(x=0, y=15)

    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()


# Main ----------------------------------------------------------------
login = Login("350x350")
login.mainloop()
