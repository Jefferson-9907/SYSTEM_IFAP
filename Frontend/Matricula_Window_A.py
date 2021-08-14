# Import Modules
from _datetime import datetime
import mariadb
from tkinter import *
from tkinter import messagebox, ttk
import random

import Backend.connection
import Model_class.matricula_registration

import Frontend.Principal_Window_A
import Frontend.login_form
import Frontend.Student_Window_A
import Frontend.Assesor_Window_A
import Frontend.Course_Window_A
import Frontend.Paralelo_Window_A
import Frontend.Implements_Window_A
import Frontend.Facturation_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A
import Frontend.Users_Window_A


class Matricula:

    def __init__(self, root):

        self.root = root
        self.root.title("SYST_CONTROL--›MATRICULACIÓN")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('./recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')

        self.imagenes = {
            'matricula': PhotoImage(file='./recursos/icon_n_al.png'),
            'matricular': PhotoImage(file='./recursos/icon_aceptar.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'eliminar': PhotoImage(file='./recursos/icon_del.png'),
            'limpiar': PhotoImage(file='./recursos/icon_clean.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),
            'actualizar': PhotoImage(file='./recursos/icon_upd.png')
        }

        # =============================================================
        # BANNER PANTALLA MATRÍCULA
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (MATRÍCULAS)"
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

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (MATRICULACIÓN)')
        self.texto1.config(font=("Britannic", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=455, pady=0)

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
        self.Column2.add_command(label='Matriculación')
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        self.cuaderno = ttk.Notebook(self.root, width=1345, height=625)
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
        self.footer_4 = Label(self.root, text='DESING® | Derechos Reservados 2021', width=195, bg='black', fg='white')
        self.footer_4.place(x=0, y=725)

        # Variables
        self.e_n_mat_al_m = StringVar()
        self.e_nombres_al = StringVar()
        self.e_n_paralelo = StringVar()
        self.e_nombres_as = StringVar()

        self.search_field = StringVar()

        # Manage Frame
        self.Manage_Frame_m = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_m.place(x=20, y=75, width=435, height=350)

        self.m_title = Label(self.Manage_Frame_m, text="-ADMINISTRAR MATRÍCULA-",
                             font=("Copperplate Gothic Bold", 16, "bold"), bg='#0d1e24', fg="White")
        self.m_title.grid(column=0, row=0, columnspan=3, padx=50, pady=25, sticky="W")

        self.Manage_Frame_m_1 = Frame(self.root, bd=4, bg='#0d1e24')
        self.Manage_Frame_m_1.place(x=25, y=150, width=420, height=250)

        self.l_n_c_al_m = Label(self.Manage_Frame_m_1, text='C.I ESTUDIANTE', width='15',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_c_al_m.grid(column=0, row=0, padx=5, pady=5, sticky="W")
        self.e_n_c_al_m = Entry(self.Manage_Frame_m_1, textvariable=self.e_n_mat_al_m, width='15')
        self.e_n_c_al_m.grid(column=1, row=0, padx=0, pady=5, sticky="W")
        self.e_n_c_al_m.focus()

        self.search_btn = Button(self.Manage_Frame_m_1, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_al, compound="right")
        self.search_btn.image = self.imagenes['buscar']
        self.search_btn.grid(column=1, row=0,  padx=100, pady=10)

        self.v_l_nombres = Label(self.Manage_Frame_m_1, text='NOMBRES', width='15',
                                 font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.v_l_nombres.grid(column=0, row=1, padx=0, pady=5)
        self.v_e_nombres = Entry(self.Manage_Frame_m_1, textvariable=self.e_nombres_al, width='40')
        self.v_e_nombres.grid(column=1, row=1, padx=0, pady=5, sticky="W")
        self.v_e_nombres["state"] = "disabled"

        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "select * from paralelos"
            paralelos_tuple = self.db_connection.select(query)

            self.paralelos_list = []
            for i in paralelos_tuple:
                paralelos_name = i[2]
                self.paralelos_list.append(paralelos_name)

        except BaseException as msg:
            print(msg)

        self.l_cur_m = Label(self.Manage_Frame_m_1, text='PARALELO', width='15', font=('Copperplate Gothic Bold',
                                                                                       10), bg='#808080')
        self.l_cur_m.grid(column=0, row=2, padx=5, pady=5, sticky="W")
        self.e_id_par_al_m = ttk.Combobox(self.Manage_Frame_m_1, textvariable=self.e_n_paralelo, width='30')
        self.e_id_par_al_m['values'] = self.paralelos_list
        self.e_id_par_al_m.grid(column=1, row=2, padx=1, pady=5, sticky="W")

        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "select * from asesores"
            asesores_tuple = self.db_connection.select(query)

            self.asesores_list = []
            for i in asesores_tuple:
                asesores_name = i[1] + " " + i[2]
                self.asesores_list.append(asesores_name)

        except BaseException as msg:
            print(msg)

        self.v_l_n_as_m = Label(self.Manage_Frame_m_1, text='ASESOR', width='15', font=('Copperplate Gothic Bold',
                                                                                        10), bg='#808080')
        self.v_l_n_as_m.grid(column=0, row=3, padx=5, pady=5, sticky="W")
        self.v_e_n_as_m = ttk.Combobox(self.Manage_Frame_m_1, textvariable=self.e_nombres_as, width='33')
        self.v_e_n_as_m['values'] = self.asesores_list
        self.v_e_n_as_m.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame_m = Frame(self.root, bg='#0d1e24')
        self.btn_frame_m.place(x=50, y=320, width=375, height=75)

        self.add_btn = Button(self.btn_frame_m, image=self.imagenes['matricular'], text='MATRICULAR', width=80,
                              command=self.add_mat_al, compound=TOP)
        self.add_btn.image = self.imagenes['matricular']
        self.add_btn.grid(row=0, column=1, padx=3, pady=10)
        self.add_btn["state"] = "normal"

        self.up_btn = Button(self.btn_frame_m, image=self.imagenes['editar'], text='MODIFICAR', width=80, compound=TOP)
        self.up_btn.image = self.imagenes['editar']
        self.up_btn.grid(row=0, column=2, padx=3, pady=10)
        self.up_btn["state"] = "disabled"

        self.del_btn = Button(self.btn_frame_m, image=self.imagenes['eliminar'], text='ELIMINAR', width=80,
                              command=self.delete_m, compound=TOP)
        self.del_btn.image = self.imagenes['eliminar']
        self.del_btn.grid(row=0, column=3, padx=3, pady=10)
        self.del_btn["state"] = "disabled"

        self.clean_btn = Button(self.btn_frame_m, image=self.imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_m, compound=TOP)
        self.clean_btn.image = self.imagenes['limpiar']
        self.clean_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=460, y=75, width=885, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field, font=("Arial", 10, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_m, compound="right")
        self.search_btn.image = self.imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=self.imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_m, compound="right")
        self.show_all_btn.image = self.imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        self.click_home()

        self.act_btn = Button(self.Detail_Frame, image=self.imagenes['actualizar'], text='ACTUALIZAR', width=100,
                              command=self.matricula_btn, compound="right")
        self.act_btn.image = self.imagenes['actualizar']
        self.act_btn.grid(row=0, column=4, padx=10, pady=10)

        # Table Frame administar matrícula

        self.Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        self.Table_Frame.place(x=5, y=60, width=865, height=525)

        self.Y_scroll = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(self.Table_Frame, columns=("no_ma", "ci_est", "n_est", "a_est"),
                                  yscrollcommand=self.Y_scroll.set)

        self.Y_scroll.pack(side=RIGHT, fill=Y)
        self.Y_scroll.config(command=self.Table.yview)

        self.Table.heading("no_ma", text="No. MAT.")
        self.Table.heading("ci_est", text="C.I ESTUDIANTE")
        self.Table.heading("n_est", text="ID PARALELO")
        self.Table.heading("a_est", text="ID ASESOR")

        self.Table['show'] = "headings"
        self.Table.column("no_ma", width=10)
        self.Table.column("ci_est", width=20)
        self.Table.column("n_est", width=75)
        self.Table.column("a_est", width=75)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_m)
        self.show_data_m()

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

    def click_home(self):
        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "SELECT COUNT(*) FROM matriculas;"
            data = self.db_connection.select(query)
            for value in data:
                self.no_matriculas = value[0]

            total_matriculas = Label(self.Detail_Frame, text=f" TOTAL MATRÍCULAS: {self.no_matriculas}",
                                     font=("Copperplate Gothic Bold", 12, "bold"), bg='#a27114', fg="White")
            total_matriculas.grid(row=0, column=5, padx=60, pady=10)

        except BaseException as msg:
            print(msg)

    def search_data_al(self):
        self.n_c_al = self.e_n_mat_al_m.get()
        if self.e_n_mat_al_m.get() == "":
            messagebox.showerror("SYST_CONTROL (IFAP®)-ERROR!!!", "INGRESE EL CAMPO: No. CÉDULA ESTUDIANTE")

        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="ddbb_sys_ifap")
        self.curr = self.connect.cursor()

        sql = f"""SELECT id_estudiante FROM estudiantes WHERE id_estudiante={self.n_c_al}"""
        self.curr.execute(sql)
        self.curr.fetchall()

        if self.curr.rowcount == 1:
            self.sql = f"""SELECT * FROM estudiantes WHERE id_estudiante={self.n_c_al}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            for value in self.rows:
                self.e_nombres_al.set(value[1] + " " + value[2])

        else:
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ERROR)", f"EL ESTUDIANTE CON No. DE CÉDULA: "
                                                                    f"{self.n_c_al}\n"
                                                                    f"NO SE ENCUENTRA EN EL REGISTRO DE ESTUDIANTES")

    def add_mat_al(self):
        try:
            obj_course_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            query = "select id_matricula from matriculas;"
            data = self.db_connection.select(query)

            self.matriculas_list = []
            for values in data:
                # print(values)
                matriculas_data_list = values[0]
                self.matriculas_list.append(matriculas_data_list)

        except BaseException as msg:
            messagebox.showerror("Error", f"{msg}")

        if self.e_n_mat_al_m.get() == '' or self.e_nombres_al.get() == '' or self.e_n_paralelo.get() == '' or \
                self.e_nombres_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de estudiantes después de la validación exitosa de esos datos
        """
        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            obj_matricula_database = Model_class.matricula_registration.MatriculaRegistration(
                self.e_n_mat_al_m.get(),
                self.e_nombres_al.get(),
                self.e_n_paralelo.get(),
                self.e_nombres_as.get(),
                )
            query = 'insert into estudiantes (id_estudiante, nombres, apellidos, edad, direccion, correo, celular, ' \
                    'telefono, representante, cedula_r, observacion) values (%s, %s, %s, %s, %s, %s, %s, %s, ' \
                    '%s, %s, %s);'
            values = (obj_matricula_database.get_id_matricula(), obj_matricula_database.get_estudiante(),
                      obj_matricula_database.get_paralelo(), obj_matricula_database.get_asesor(),
                      )

            self.db_connection.insert(query, values)
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"MATRÍCULA DEL ESTUDIANTE: {values[1]}\n "
                                                       f"CON No. DE CÉDULA: {values[0]}\n"
                                                       f"REGISTRADO HA SIDO REGISTRADA CORRECTAMENTE")
            self.show_data_m()
            self.clear_field_m()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def clear_field_m(self):
        self.e_n_mat_al_m.set('')
        self.e_nombres_al.set('')
        self.e_n_paralelo.set('')
        self.e_nombres_as.set('')
        self.add_btn["state"] = "normal"
        self.up_btn["state"] = "disabled"
        self.del_btn["state"] = "disabled"

    def get_fields_m(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.e_n_mat_al_m.set(row[0])
        self.e_nombres_al.set(row[1])
        self.e_n_paralelo.set(row[2])
        self.e_nombres_as.set(row[3])
        self.add_btn["state"] = "disabled"
        self.up_btn["state"] = "normal"
        self.del_btn["state"] = "normal"

    def validation(self):
        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "select * from matriculas;"
            data = self.db_connection.select(query)
            # print(data)
            self.matriculas_list = []
            for values in data:
                # print(values)
                n_c_i = values[0]
                self.matriculas_list.append(n_c_i)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

        if self.e_n_mat_al_m.get() == '' or self.e_nombres_al.get() == '' or self.e_n_paralelo.get() == '' or \
                self.e_nombres_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.update()

    def update(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="ddbb_sys_ifap")
        self.curr = self.connect.cursor()

        query = f"""UPDATE matriculas SET id_matricula="{self.e_n_mat_al_m.get()}", 
                    estudiante="{self.e_nombres_al.get()}", paralelo="{self.e_n_paralelo.get()}",\
                    asesor="{self.e_nombres_as.get()}" WHERE id_matricula={self.e_n_mat_al_m.get()}"""

        self.curr.execute(query)
        self.connect.commit()
        self.show_data_m()
        messagebox.showinfo("SYST_CONTROL(IFAP®)", f"LA MATRÍCULA DEL ESTUDIANTE: {self.e_nombres_al.get()}\n"
                                                   f"CON No. DE CÉDULA: {self.e_n_mat_al_m.get()}\n"
                                                   f"HA SIDO ACTUALIZADA DEL REGISTRO CORRECTAMENTE!!!")
        self.clear_field_m()

    def delete_m(self):
        if self.n_mat_al_m.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="ddbb_sys_ifap")
            self.curr = self.conn.cursor()

            self.sql = f"""DELETE FROM matricula WHERE id_matricula='{self.n_mat_al_m.get()}'"""
            self.curr.execute(self.sql)

            self.conn.commit()
            self.show_data_m()
            self.clear_field_m()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "MATRÍCULA ELIMINADA DEL REGISTRO CORRECTAMENTE!!!")

    def search_data_m(self):
        if self.search_field.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA")
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="ddbb_sys_ifap")
        self.curr = self.connect.cursor()
        self.search_n_ced = self.search_field.get()
        sql = f"""SELECT id_matricula, id_estudiante, id_paralelo, id_asesor\
        FROM matricula WHERE id_matricula={self.search_n_ced}"""
        self.curr.execute(sql)
        self.curr.fetchall()

        if self.curr.rowcount == 1:
            self.search_field.set('')
            self.sql = f"""SELECT id_matricula, id_estudiante, id_paralelo, id_asesor\
            FROM matricula WHERE id_matricula={self.search_n_ced}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                self.Table.delete(*self.Table.get_children())
                for self.row in self.rows:
                    self.Table.insert('', END, values=self.row)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO CON EL No. CÉDULA: " +
                                 self.search_n_ced)
            self.search_field.set('')

    def show_data_m(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="ddbb_sys_ifap")
        self.curr = self.connect.cursor()

        self.curr.execute("SELECT * FROM matriculas ORDER BY id_matricula ASC ")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table.delete(*self.Table.get_children())
            for self.row in self.rows:
                self.Table.insert('', END, values=self.row)

            self.connect.commit()
        self.connect.close()

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
    application = Matricula(root)
    root.mainloop()
