from tkinter import *
import tkinter
import csv

# Collors ---------------------------
back = '#f6ffec'
collor_font = '#333652'
obj_collor = '#FAD02C'
button_collor = '#417B5A'
button_collor_b = "#8EB1C7"
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

class Registration(Tk):
    def __init__(self, geometry, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry(geometry)
        self.config(bg=bg)
        self.resizable(width=width, height=height)


        self.widgets_init_sub()
        self.ret_client()

    def widgets_sub(self):
        # Frames
        self.frame_1 = Frame(self, width=300, height=35, background=back, relief='flat')
        self.frame_2 = Frame(self, width=320, height=321, background=back, relief='flat')
        self.frame_3 = Frame(self, width=320, height=321, background=back, relief='flat')
        self.frame_4 = Frame(self, width=710, height=50, background=back, relief='flat')

        # Objects
        self.label_line_div =  Label(self, text="", font=(font_obj), height=135, bg=button_collor_b, fg=back, relief='flat')
        self.lab_line = Label(self.frame_1, text="", anchor=N, font=(font_obj), width=280, bg=obj_collor, fg=back, relief='flat')

        # Labels -----------------------------------
        self.lab_title = Label(self.frame_1, text="Cadastre-se no QAgenda! ", anchor=N, font=(font_title_b), bg=back, fg=collor_font, relief='flat')
        # Cliente
        self.lab_name = Label(self.frame_2, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_cpf = Label(self.frame_2, text="CPF:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_id = Label(self.frame_2, text="Idade:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_set = Label(self.frame_2, text="Setor:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pass = Label(self.frame_2, text="Senha:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        # Estabelecimento
        self.lab_name_est = Label(self.frame_3, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_cnpj = Label(self.frame_3, text="CNPJ:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_ramo = Label(self.frame_3, text="Serviço:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_set_est = Label(self.frame_3, text="Setor:", font=(font_label), bg=back, fg=collor_font, relief="flat")
        self.lab_pass_est = Label(self.frame_3, text="Senha:", font=(font_label), bg=back, fg=collor_font, relief="flat")

        # Entry --------------------------------
        self.entry_name = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_cpf = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_id = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_set = Entry(self.frame_2, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pass = Entry(self.frame_2, width=23, bg=white, fg=black, show="*", font=(font_label), highlightthickness=1, relief='flat')
        # Entry Estabelecimento
        self.entry_name_est = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_cnpj = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_ramo = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_set_est = Entry(self.frame_3, width=23, bg=white, fg=black, font=(font_label), highlightthickness=1, relief='flat')
        self.entry_pass_est = Entry(self.frame_3, width=23, bg=white, fg=black, show="*", font=(font_label), highlightthickness=1, relief='flat')

        # Buttons ------------------------------
        self.button_confirm = Button(self.frame_4, text="Confirmar",width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
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

    def ret_login(self):
        self.destroy()
        login = Login("350x350")
        login.mainloop()


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
        self.lab_name = Label(self.frame_2, text="Nome:", font=(font_label), bg=back, fg=collor_font, relief="flat")
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
        name = str(self.entry_name.get())
        passnumber = str(self.entry_pass.get())
        # Busca nos estabelecimentos
        with open("c/files/estabelecimentos.csv", 'r', encoding='utf-8') as arq:
            lojas_csv = csv.reader(arq, delimiter=',')
            for linha in lojas_csv:
                if name == linha[0] and passnumber == linha[4]:
                    print("deu certo")
                    break
                
        # Busca nos clientes
        with open('c/files/clientes.csv', 'r', encoding='utf-8') as arq:
            clientes_csv = csv.reader(arq, delimiter=',')
            for linha in clientes_csv:
                if name == linha[0] and passnumber == linha[4]:
                    print("deu certo")
                    break
        
    
    def new_window_sub(self):
        self.destroy()
        subs = Registration("750x500")
        subs.mainloop()

# ----------- Main ----------------
login = Login("350x350")

login.mainloop()

