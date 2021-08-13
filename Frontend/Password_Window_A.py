# Import Modules
from _datetime import datetime
from tkinter import *
import mariadb
from tkinter import messagebox, ttk


class Password:

    def __init__(self, root):

        self.root = root
        self.root.title("SYST_CONTROL--›Usuarios")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (USUARIOS: CAMBIAR CONTRASEÑA)')
        self.texto1.config(font=("Copperplate Gothic Bold", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=75, pady=0)

        # =============================================================
        # CREACIÓN DE LA BARRA DE MENÚ
        # =============================================================
        self.menubarra = Menu(self.root)

        # =============================================================
        # CREACIÓN DEL MENÚ
        # =============================================================
        self.menubarra.add_cascade(label='ALUMNOS')
        self.root.config(menu=self.menubarra)
        self.menus = Menu(self.root)
        self.Column1 = Menu(self.menus, tearoff=0)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ PRINCIPAL
        # =============================================================
        self.menus.add_cascade(label='INICIO', menu=self.Column1)
        self.Column1.add_command(label='Menú Inicio', command=self.principal_btn)
        self.Column2 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ ALUMNO
        # =============================================================
        self.menus.add_cascade(label='ALUMNOS', menu=self.Column2)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        self.cuaderno = ttk.Notebook(self.root, width=1340, height=625)
        self.cuaderno.grid(row=1, column=0, sticky='nw', padx=10, pady=5)

        # =============================================================
        # CREACIÓN DEL MENÚ ASESORES
        # =============================================================
        self.menus.add_cascade(label='ASESORES', menu=self.Column3)
        self.Column3.add_command(label='Menú Asesores', command=self.assesor_btn)
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ CURSOS
        # =============================================================
        self.menus.add_cascade(label='CURSOS', menu=self.Column4)
        self.Column4.add_command(label='Menú Cursos', command=self.courses_btn)
        self.Column5 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ FACTURACIÓN
        # =============================================================
        self.menus.add_cascade(label='FACTURACIÓN', menu=self.Column5)
        self.Column5.add_command(label='Menú Facturación', command=self.facturation_btn)
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ REPORTES
        # =============================================================
        self.menus.add_cascade(label='REPORTES', menu=self.Column6)
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column7)
        self.Column7.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column7.add_command(label='Cambiar Contraseña')
        self.Column7.add_separator()
        self.Column7.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column7.add_separator()
        self.Column8 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column8)
        self.Column8.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column8.add_separator()
        self.Column8.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column8.add_separator()
        self.root.config(menu=self.menus)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10), bg='Honeydew2',
                            relief=RIDGE)
        self.footer.place(x=0, y=703)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='Honeydew2',
                              relief=RIDGE)
        self.footer_1.place(x=212, y=704)

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=195, bg='black',
                              fg='white')
        self.footer_4.place(x=0, y=725)

        # Manage Frame
        self.Manage_Frame = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame.place(x=375, y=200, width=600, height=300)

        self.m_title = Label(self.Manage_Frame, text="-ADMINISTAR USUARIOS-\nCAMBIAR CONTRASEÑA",
                             font=("Copperplate Gothic Bold", 16, "bold"), bg='#0d1e24', fg="White")
        self.m_title.grid(row=0, column=0, columnspan=1, padx=10, pady=30)

        # Variables
        self.username = StringVar()
        self.old_password = StringVar()
        self.new_password = StringVar()

        self.User_Frame = Frame(self.Manage_Frame, bg='#0d1e24')
        self.User_Frame.grid(row=1, column=0, padx=100, pady=10)

        self.lbl_us = Label(self.User_Frame, text="USUARIO", width='10', font=('Copperplate Gothic Bold', 10),
                            bg='#808080', fg="#0A090C")
        self.lbl_us.grid(row=1, column=0, padx=0, pady=5, sticky="E")

        self.e_us = Entry(self.User_Frame, textvariable=self.username, bd=5, relief=GROOVE)
        self.e_us.grid(row=1, column=1, padx=10, pady=5, sticky="W")
        self.e_us.focus()

        self.l_c_ant = Label(self.User_Frame, text="CONTRASEÑA ANTERIOR", font=('Copperplate Gothic Bold', 10),
                             bg='#808080', fg="#0A090C")
        self.l_c_ant.grid(row=2, column=0, padx=0, pady=5, sticky="S")

        self.e_c_ant = Entry(self.User_Frame, show="*", textvariable=self.old_password, bd=5, relief=GROOVE)
        self.e_c_ant.grid(row=2, column=1, padx=10, pady=5, sticky="W")

        self.l_n_cont = Label(self.User_Frame, text="NUEVA CONTRASEÑA", font=('Copperplate Gothic Bold', 10),
                              bg='#808080', fg="#0A090C")
        self.l_n_cont.grid(row=3, column=0, padx=0, pady=5, sticky="E")

        self.e_n_cont = Entry(self.User_Frame, show="*", textvariable=self.new_password, bd=5, relief=GROOVE)
        self.e_n_cont.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        self.chg_btn = Button(self.Manage_Frame, text="CAMBIAR CONTRASEÑA", font=('Copperplate Gothic Bold', 10),
                              bg="#00A1E4", fg="#FFFCF9", relief=GROOVE, width=20, command=self.change_pass)
        self.chg_btn.grid(row=2, column=0, padx=200, pady=5)

    def change_pass(self):
        if self.username.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®) (ERROR)", "POR FAVOR INGRESE EL CAMPO: USUARIO")
        elif self.old_password.get() == "":
            messagebox.showerror("SYST_CONTROL(IFAP®) (ERROR)", "POR FAVOR INGRESE EL CAMPO: CONTRASEÑA ANTERIOR")

        elif self.new_password.get() == "":
            messagebox.showerror("SYST_CONTROL(IFAP®) (ERROR)", "POR FAVOR INGRESE EL CAMPO: CONTRASEÑA NUEVA")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()
            sql = "SELECT contraseña FROM usuarios WHERE usuario='" + self.username.get() + "' and contraseña='" \
                  + self.old_password.get() + "'"
            self.curr.execute(sql)

            if self.curr.fetchall():
                self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
                self.curr = self.connect.cursor()
                self.sql = f"""UPDATE usuarios SET contraseña='{self.new_password.get()}'\
                WHERE usuario='{self.username.get()}'"""
                self.curr.execute(self.sql)
                self.connect.commit()

                messagebox.showinfo("SYST_CONTROL(IFAP®)", "CAMBIO DE CONTRASEÑA EXITOSO\nUSUARIO: " +
                                    self.username.get() + "\nCONTRASEÑA: " + self.new_password.get())
                self.limpiar()

            else:
                messagebox.showerror("ERROR!!!", "NO SE PUDO REALIZAR LA ACCIÓN: CAMBIO DE CONTRASEÑA.\n"
                                                 "\t(INGRESE SU CREDENCIALES ACTUALES)")
                self.limpiar()

    def limpiar(self):
        self.username.set('')
        self.old_password.set('')
        self.new_password.set('')
        self.e_us.focus()

    def logout(self):
        self.root.destroy()

        from Frontend.login_form import Login
        st_root = Tk()
        Login(st_root)
        st_root.mainloop()

    def principal_btn(self):
        self.root.destroy()

        from Frontend.Principal_Window_A import Principal
        st_root = Tk()
        Principal(st_root)
        st_root.mainloop()

    def student_btn(self):
        self.root.destroy()

        from Frontend.Student_Window_A import Student
        st_root = Tk()
        Student(st_root)
        st_root.mainloop()

    def assesor_btn(self):
        self.root.destroy()

        from Frontend.Assesor_Window_A import Assesor
        st_root = Tk()
        Assesor(st_root)
        st_root.mainloop()

    def courses_btn(self):
        self.root.destroy()

        from Frontend.Course_Window_A import Course
        st_root = Tk()
        Course(st_root)
        st_root.mainloop()

    def facturation_btn(self):
        self.root.destroy()

        from Frontend.Facturation_Window_A import Ventana_Principal
        st_root = Tk()
        Ventana_Principal(st_root)
        st_root.mainloop()

    def salir_principal(self):
        self.sa = messagebox.askyesno('CERRAR SESIÓN', 'CERRAR SYST_CONTROL(IFAP®)')
        if self.sa:
            exit()

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL INSTITUTO(INFO)
    # =============================================================
    def caja_info_ifap(self):
        self.men1 = messagebox.showinfo('SIST_CONTROL (IFAP®)', 'INSTITUTO DE FORMACIÓN ACADEMICA PROEZAS(IFAP®)')

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL SISTEMA(INFO)
    # =============================================================
    def caja_info_sist(self):
        self.men2 = messagebox.showinfo('SIST_CONTROL (IFAP®)',
                                        'SIST_CONTROL (IFAP®) v2.0\n'
                                        'El uso de este software queda sujeto a los términos y condiciones del '
                                        'contrato "BJM DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 BJM DESING®. Todos los derechos reservados')


if __name__ == '__main__':
    root = Tk()
    application = Password(root)
    root.mainloop()
