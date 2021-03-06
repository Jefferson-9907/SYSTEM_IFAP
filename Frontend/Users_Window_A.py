# Import Modules
import random
from _datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk

import mariadb

import Backend.connection
import Model_class.users_registration

import Frontend.Principal_Window_A
import Frontend.login_form
import Frontend.Student_Window_A
import Frontend.Matricula_Window_A
import Frontend.Assesor_Window_A
import Frontend.Course_Window_A
import Frontend.Paralelo_Window_A
import Frontend.Implements_Window_A
import Frontend.Facturation_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A


class Users:

    def __init__(self, root):

        self.root = root
        self.root.title("SYST_CONTROL--›Usuarios")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')

        imagenes = {
            'nuevo': PhotoImage(file='recursos\\icon_aceptar.png'),
            'matricular': PhotoImage(file='recursos\\icon_add.png'),
            'editar': PhotoImage(file='recursos\\icon_update.png'),
            'eliminar': PhotoImage(file='recursos\\icon_del.png'),
            'limpiar': PhotoImage(file='recursos\\icon_clean.png'),
            'buscar': PhotoImage(file='recursos\\icon_buscar.png'),
            'todo': PhotoImage(file='recursos\\icon_ver_todo.png'),
        }

        # =============================================================
        # BANNER PANTALLA ESTUDIANTES
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (ESTUDIANTES)"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=1367)

        self.slider()
        self.heading_color()

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

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
        self.Column2.add_command(label='Menú Alumnos', command=self.student_btn)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL MENÚ ASESORES
        # =============================================================
        self.menus.add_cascade(label='ASESORES', menu=self.Column3)
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
        self.Column7.add_command(label='Cambiar Contraseña', command=self.pass_btn)

        self.Column7.add_separator()
        self.Column7.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column7.add_separator()
        self.Column8 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='AYUDA', menu=self.Column8)
        self.Column8.add_command(label='Tutorial')
        self.Column9 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column9)
        self.Column9.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column9.add_separator()
        self.Column9.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column9.add_separator()
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

        # Variables
        self.id_us_1 = IntVar()
        self.e_us_1 = StringVar()
        self.e_email_1 = StringVar()
        self.e_contr_1 = StringVar()
        self.e_c_contr_1 = StringVar()
        self.e_tipo_1 = StringVar()

        self.search_field_us = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        Manage_Frame.place(x=15, y=75, width=385, height=600)

        m_title = Label(Manage_Frame, text="-ADMINISTAR USUARIOS-", font=("Copperplate Gothic Bold", 16, "bold"),
                        bg='#0d1e24', fg="White")
        m_title.grid(row=0, columnspan=2, padx=25, pady=50)

        self.l_id_us = Label(Manage_Frame, text='ID USUARIO', width='15', font=('Copperplate Gothic Bold', 10),
                             bg='#808080')
        self.l_id_us.grid(column=0, row=1, padx=0, pady=5)
        self.e_id_us = Entry(Manage_Frame, textvariable=self.id_us_1, width='33', state="disabled")
        self.e_id_us.grid(column=1, row=1, padx=0, pady=5, sticky="W")

        self.l_us = Label(Manage_Frame, text='USUARIO', width='15', font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_us.grid(column=0, row=2, padx=0, pady=5)
        self.e_us = Entry(Manage_Frame, textvariable=self.e_us_1, width='33')
        self.e_us.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_email = Label(Manage_Frame, text='EMAIL', width='15', font=('Copperplate Gothic Bold', 10),
                             bg='#808080')
        self.l_email.grid(column=0, row=3, padx=1, pady=5)
        self.e_email = Entry(Manage_Frame, textvariable=self.e_email_1, width='33')
        self.e_email.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        self.l_contr = Label(Manage_Frame, text='CONTRASEÑA', width='15', font=('Copperplate Gothic Bold', 10),
                             bg='#808080')
        self.l_contr.grid(column=0, row=4, padx=1, pady=5)
        self.e_contr = Entry(Manage_Frame, textvariable=self.e_contr_1, width='33')
        self.e_contr.grid(column=1, row=4, padx=1, pady=5, sticky="W")

        self.l_c_contr = Label(Manage_Frame, text='REPITA CONTRASEÑA', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_c_contr.grid(column=0, row=5, padx=1, pady=5)
        self.e_c_contr = Entry(Manage_Frame, textvariable=self.e_c_contr_1, width='33')
        self.e_c_contr.grid(column=1, row=5, padx=1, pady=5, sticky="W")

        self.l_tipo = Label(Manage_Frame, text='TIPO USUARIO', width='15', font=('Copperplate Gothic Bold', 10),
                            bg='#808080')
        self.l_tipo.grid(column=0, row=6, padx=1, pady=5)
        self.e_tipo = Entry(Manage_Frame, textvariable=self.e_tipo_1, width='33')
        self.e_tipo.grid(column=1, row=6, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame = Frame(Manage_Frame, bg='#0d1e24')
        self.btn_frame.place(x=10, y=500, width=360)

        self.add_btn = Button(self.btn_frame, image=imagenes['nuevo'], text='REGISTAR', command=self.add_us,
                              compound=TOP, width=75)
        self.add_btn.image = imagenes['nuevo']
        self.add_btn.grid(row=0, column=0, padx=3, pady=10)

        self.up_btn = Button(self.btn_frame, image=imagenes['editar'], text='MODIFICAR', command=self.update_us,
                             compound=TOP, width=75)
        self.up_btn.image = imagenes['editar']
        self.up_btn.grid(row=0, column=2, padx=3, pady=10)
        self.up_btn["state"] = "disabled"

        self.del_btn = Button(self.btn_frame, image=imagenes['eliminar'], text='ELIMINAR', command=self.delete_us,
                              compound=TOP, width=75)
        self.del_btn.image = imagenes['eliminar']
        self.del_btn.grid(row=0, column=3, padx=3, pady=10)
        self.del_btn["state"] = "disabled"

        self.clean_btn = Button(self.btn_frame, image=imagenes['limpiar'], text='LIMPIAR', command=self.clear_field_us,
                                compound=TOP, width=75)
        self.clean_btn.image = imagenes['limpiar']
        self.clean_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=405, y=75, width=940, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, font=("Arial", 10, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_field_us, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_us, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame

        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=920, height=525)

        X_scroll = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame, columns=("id_u", "us", "corr", "cont", "tip"),
                                  yscrollcommand=Y_scroll.set, xscrollcommand=X_scroll.set)

        X_scroll.pack(side=BOTTOM, fill=X)
        Y_scroll.pack(side=RIGHT, fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)
        # bg="#00A1E4", fg="#FFFCF9", font=("Arial", 10, "bold")
        self.Table.heading("id_u", text="ID USUARIO")
        self.Table.heading("us", text="USUARIO")
        self.Table.heading("corr", text="EMAIL")
        self.Table.heading("cont", text="CONTRASEÑA")
        self.Table.heading("tip", text="TIPO")

        self.Table['show'] = "headings"
        self.Table.column("id_u", width=20)
        self.Table.column("us", width=70)
        self.Table.column("corr", width=70)
        self.Table.column("cont", width=70)
        self.Table.column("tip", width=5)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_us)

        self.show_data_us()

    def slider(self):
        """
            creates slides for heading by taking the text,
            and that text are called after every 100 ms
        """
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1

        self.heading.after(100, self.slider)

    def heading_color(self):
        """
        configures heading label
        :return: every 50 ms returned new random color.
        """
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def add_us(self):
        try:
            obj_user_database = Model_class.users_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_user_database.get_database())

            query = "select * from estudiantes;"
            data = self.db_connection.select(query)
            # print(data)
            self.usuario_list = []
            self.email_list = []
            for values in data:
                # print(values)
                usuario_data_list = values[1]
                self.usuario_list.append(usuario_data_list)
                email_data_list = values[2]
                self.email_list.append(email_data_list)
                # print(self.final_list)
                # print(self.data_list)
        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

        if self.e_us.get() == "" or self.e_email.get() == "" or self.e_contr.get() == "" \
                or self.e_tipo.get() == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        elif self.e_us.get() in self.usuario_list:
            messagebox.showerror("YA EXISTE!!!", f"{self.e_us.get()} EL USUARIO YA EXISTE, INTENTE OTRO NOMBRE")

        elif self.e_email.get() in self.email_list:
            messagebox.showerror("YA EXISTE!!!", f"{self.e_email.get()} EMAIL YA EXISTE, INTENTE OTRO EMAIL")

        elif self.e_contr.get() != self.e_c_contr.get():
            messagebox.showerror("NO COINCIDEN!!!", "SU CONTRASEÑA DEBE DE COINCIDIR EN LA CONFIRMACIÓN")

        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de usuarios después de la validación exitosa de esos datos
        """
        try:
            obj_usuarios_database = Model_class.users_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_usuarios_database.get_database())

            obj_usuarios_database = Model_class.users_registration.UsersRegistration(self.e_us.get(),
                                                                                     self.e_email.get(),
                                                                                     self.e_contr.get(),
                                                                                     self.e_tipo.get())
            query = 'insert into usuarios (usuario,email,contrasena,tipo) values (%s,%s,%s,%s);'
            values = (obj_usuarios_database.get_usuario(), obj_usuarios_database.get_email(),
                      obj_usuarios_database.get_contrasena(), obj_usuarios_database.get_t_usuario())
            self.db_connection.insert(query, values)
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS GUARDADOS CORRECTAMENTE\n "
                                                       f"USUARIO={values[0]},\n "
                                                       f"EMAIL={values[1]}\n"
                                                       f"CONTRASEÑA={values[2]}\n,"
                                                       f"TIPO USUARIO={values[3]}")
            self.show_data_us()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def clear_field_us(self):
        self.id_us_1.set('')
        self.e_us_1.set('')
        self.e_email_1.set('')
        self.e_contr_1.set('')
        self.e_c_contr_1.set('')
        self.e_tipo_1.set('')
        self.e_us.focus()
        self.add_btn["state"] = "normal"
        self.up_btn["state"] = "disabled"
        self.del_btn["state"] = "disabled"

    def get_fields_us(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.id_us_1.set(row[0])
        self.e_us_1.set(row[1])
        self.e_email_1.set(row[2])
        self.e_contr_1.set(row[3])
        self.e_c_contr_1.set(row[3])
        self.e_tipo_1.set(row[4])
        self.add_btn["state"] = "normal"
        self.up_btn["state"] = "normal"
        self.del_btn["state"] = "normal"

    def update_us(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="ddbb_sys_ifap")
        self.curr = self.connect.cursor()

        query = f"""UPDATE usuarios SET id_usuario="{self.e_id_us.get()}", 
        usuario="{self.e_us.get()}",
        email="{self.e_email.get()}", 
        contrasena="{self.e_contr.get()}",
        tipo="{self.e_tipo.get()}" WHERE id_usuario={self.e_id_us.get()}"""

        self.curr.execute(query)
        self.connect.commit()
        self.show_data_us()
        messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL USUARIO"
                                                   f"USUARIO: {self.e_us.get()} "
                                                   f"CONTRASEÑA: {self.e_contr.get()}\n"
                                                   f"HAN SIDO ACTUALIZADOS DEL REGISTRO")
        self.clear_field_us()

    def delete_us(self):
        try:
            obj_user_database = Model_class.users_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_user_database.get_database())

            tree_view_content = self.Table.focus()
            tree_view_items = self.Table.item(tree_view_content)
            tree_view_values = tree_view_items['values'][1]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ALIMINAR AL USUARIO: {tree_view_values}")
            if ask is True:
                query = "delete from usuarios where usuario=%s;"
                self.db_connection.delete(query, (tree_view_values,))
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL USUARIO: {tree_view_values} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")
                self.clear_field_us()
                self.show_data_us()
            else:
                pass

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def search_data_us(self):
        obj_user_database = Model_class.users_registration.GetDatabase('use ifap;')
        self.db_connection.create(obj_user_database.get_database())
        query = "select * from usuarios where usuario LIKE '%" + str(self.search_field_us.get()) + "%'"
        data = self.db_connection.select(query)

        self.Table.delete(*self.Table.get_children())

        for values in data:
            data_list = [values[0], values[1], values[2], values[3], values[4]]
            self.Table.insert('', END, values=data_list)

    def show_data_us(self):
        try:
            obj_usuarios_database = Model_class.users_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_usuarios_database.get_database())

            query = "select * from usuarios;"
            data = self.db_connection.select(query)
            # print(data)
            self.Table.delete(*self.Table.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3], values[4]]
                # print(data_list)
                self.Table.insert('', END, values=data_list)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def logout(self):
        root = Toplevel()
        Frontend.login_form.Login(root)
        self.root.withdraw()
        root.deiconify()

    def principal_btn(self):
        root = Toplevel()
        Frontend.Principal_Window_A.Principal(root)
        self.root.withdraw()
        root.deiconify()

    def student_btn(self):
        root = Toplevel()
        Frontend.Student_Window_A.Student(root)
        self.root.withdraw()
        root.deiconify()

    def matricula_btn(self):
        root = Toplevel()
        Frontend.Matricula_Window_A.Matricula(root)
        self.root.withdraw()
        root.deiconify()

    def assesor_btn(self):
        root = Toplevel()
        Frontend.Assesor_Window_A.Assesor(root)
        self.root.withdraw()
        root.deiconify()

    def courses_btn(self):
        root = Toplevel()
        Frontend.Course_Window_A.Course(root)
        self.root.withdraw()
        root.deiconify()

    def paralelos_btn(self):
        root = Toplevel()
        Frontend.Paralelo_Window_A.Paralelo(root)
        self.root.withdraw()
        root.deiconify()

    def implements_btn(self):
        root = Toplevel()
        Frontend.Implements_Window_A.Implement(root)
        self.root.withdraw()
        root.deiconify()

    def facturation_btn(self):
        root = Toplevel()
        Frontend.Facturation_Window_A.Ventana_Principal(root)
        self.root.withdraw()
        root.deiconify()

    def report_btn(self):
        root = Toplevel()
        Frontend.Report_Window_A.Reports(root)
        self.root.withdraw()
        root.deiconify()

    def pass_btn(self):
        root = Toplevel()
        Frontend.Password_Window_A.Password(root)
        self.root.withdraw()
        root.deiconify()

    def users_btn(self):
        root = Toplevel()
        Frontend.Users_Window_A.Users(root)
        self.root.withdraw()
        root.deiconify()

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
    application = Users(root)
    root.mainloop()
