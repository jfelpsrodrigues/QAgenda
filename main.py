from tkinter import *
import tkinter

# Collors ---------------------------
back = '#f6ffec'
collor_font = '#333652'
obj_collor = '#FAD02C'
button_collor = '#417B5A'
black = "black"
white = 'white'

# Fonts -----------------------------
font_title = 'Roboto 18'
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

    def widgets_sub(self):
        # Frames
        self.frame_1 = Frame(self, width=350, height=50, background=black, relief='flat')
        self.frame_2 = Frame(self, width=350, height=300, background=black, relief='flat')



class Login(Tk):
    def __init__(self, geometry, width=False, height=False, bg=back):
        super().__init__()

        self.title("QAgenda")
        self.geometry(geometry)
        self.config(bg=bg)
        self.resizable(width=width, height=height)

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
        self.button_confirm = Button(self.frame_2, text="Entrar",width=10, height=1, relief='flat', font=(font_button), highlightthickness=1, bg=button_collor, fg=back)
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
    
    def new_window_sub(self):
        self.destroy()
        subs = Registration("700x473")
        subs.mainloop()

# ----------- Main ----------------
login = Login("350x350")
login.widgets_init_sigin()

login.mainloop()

