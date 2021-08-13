# Import Modules
from _datetime import datetime
from tkinter import *
import random
from tkinter import messagebox
from tkinter.ttk import Treeview
from ttkthemes import themed_tk as tk

import Backend.connection
import Model_class.course_registration

import Frontend.Principal_Window_A
import Frontend.login_form
import Frontend.Student_Window_A
import Frontend.Matricula_Window_A
import Frontend.Assesor_Window_A
import Frontend.Paralelo_Window_A
import Frontend.Implements_Window_A
import Frontend.Facturation_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A
import Frontend.Users_Window_A


class Course:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Cursos")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('./recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_aceptar.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'eliminar': PhotoImage(file='./recursos/icon_del.png'),
            'limpiar': PhotoImage(file='./recursos/icon_clean.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),

        }

        # =============================================================
        # BANNER PANTALLA CURSOS
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (CURSOS)"
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
        self.menubarra.add_cascade(label='CURSOS')
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
        self.Column3.add_command(label='Menú Asesores', command=self.assesor_btn)
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ CURSOS
        # =============================================================
        self.menus.add_cascade(label='CURSOS', menu=self.Column4)
        self.Column4.add_command(label='Menú Cursos')
        self.Column4.add_command(label='Menú Paralelos', command=self.paralelos_btn)
        self.Column4.add_command(label='Implementos', command=self.implements_btn)
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

        # Manage Frame Cursos
        self.Manage_Frame_cur = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_cur.place(x=15, y=85, width=500, height=275)

        m_title_c = Label(self.Manage_Frame_cur, text="-ADMINISTAR CURSOS-", font=("Copperplate Gothic Bold", 16,
                                                                                   "bold"), bg='#a27114', fg="White")
        m_title_c.grid(row=0, columnspan=2, padx=110, pady=20)

        self.id_curso = IntVar()
        self.nombre_cur = StringVar()
        self.costo_matricula = DoubleVar()
        self.costo_mensual = DoubleVar()
        self.search_field_curso = StringVar()

        self.l_id_curso = Label(self.Manage_Frame_cur, text='ID CURSO', width='18',
                                font=('Copperplate Gothic Bold', 10),
                                bg='#808080')
        self.l_id_curso.grid(column=0, row=1, padx=1, pady=5)
        self.e_id_curso = Entry(self.Manage_Frame_cur, textvariable=self.id_curso, width='10')
        self.e_id_curso.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_id_curso.focus()
        self.id_curso.set('')

        self.l_n_curso = Label(self.Manage_Frame_cur, text='NOMBRE CURSO', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_curso.grid(column=0, row=2, padx=1, pady=5)
        self.e_n_curso = Entry(self.Manage_Frame_cur, textvariable=self.nombre_cur, width='40')
        self.e_n_curso.grid(column=1, row=2, padx=1, pady=5, sticky="W")

        self.l_cost_mat = Label(self.Manage_Frame_cur, text='COSTO MATRÍCULA', width='18',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_cost_mat.grid(column=0, row=3, padx=0, pady=5)
        self.e_cost_mat = Entry(self.Manage_Frame_cur, textvariable=self.costo_matricula, width='8')
        self.e_cost_mat.grid(column=1, row=3, padx=0, pady=5, sticky="W")

        self.l_cost_men = Label(self.Manage_Frame_cur, text='COSTO MENSUAL', width='18',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_cost_men.grid(column=0, row=4, padx=1, pady=5)
        self.e_cost_men = Entry(self.Manage_Frame_cur, textvariable=self.costo_mensual, width='8')
        self.e_cost_men.grid(column=1, row=4, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame = Frame(self.Manage_Frame_cur, bg='#a27114')
        self.btn_frame.place(x=20, y=190, width=455)

        self.add_btn = Button(self.btn_frame, image=imagenes['nuevo'], text='REGISTAR', width=80,
                              command=self.add_cur, compound=TOP)
        self.add_btn.image = imagenes['nuevo']
        self.add_btn.grid(row=0, column=1, padx=15, pady=10)

        self.update_btn = Button(self.btn_frame, image=imagenes['editar'], text='MODIFICAR', width=80,
                                 command=self.update_cur, compound=TOP)
        self.update_btn.image = imagenes['editar']
        self.update_btn.grid(row=0, column=2, padx=15, pady=10)
        self.update_btn["state"] = "disabled"

        self.delete_btn = Button(self.btn_frame, image=imagenes['eliminar'], text='ELIMINAR', width=80,
                                 command=self.delete_cur, compound=TOP)
        self.delete_btn.image = imagenes['eliminar']
        self.delete_btn.grid(row=0, column=3, padx=15, pady=10)
        self.delete_btn["state"] = "disabled"

        self.clear_btn = Button(self.btn_frame, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_cur, compound=TOP)
        self.clear_btn.image = imagenes['limpiar']
        self.clear_btn.grid(row=0, column=4, padx=15, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#a27114')
        self.Detail_Frame.place(x=520, y=85, width=825, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field_curso,
                                font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_cur, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_cur, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame

        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=805, height=530)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table_cur = Treeview(Table_Frame, columns=("id_cur", "nom_cur", "cos_cur", "cost_men"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Table_cur.xview)
        scroll_y.config(command=self.Table_cur.yview)
        self.Table_cur.heading("id_cur", text="ID")
        self.Table_cur.heading("nom_cur", text="NOMBRE")
        self.Table_cur.heading("cos_cur", text="V. MATRÍCULA")
        self.Table_cur.heading("cost_men", text="V. MENSUAL")

        self.Table_cur['show'] = "headings"
        self.Table_cur.column("id_cur", width=5)
        self.Table_cur.column("nom_cur", width=70)
        self.Table_cur.column("cos_cur", width=5)
        self.Table_cur.column("cost_men", width=5)

        self.Table_cur.pack(fill=BOTH, expand=1)
        self.Table_cur.bind('<ButtonRelease 1>', self.get_fields_cur)

        self.show_data_cur()

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

    def add_cur(self):
        try:
            obj_course_database = Model_class.course_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            query = "select id_curso from cursos;"
            data = self.db_connection.select(query)

            self.cursos_list = []
            for values in data:
                # print(values)
                curso_data_list = values[0]
                self.cursos_list.append(curso_data_list)

        except BaseException as msg:
            messagebox.showerror("Error", f"{msg}")

        if self.id_curso.get() == '' or self.nombre_cur.get() == '' or self.costo_matricula.get() == '' or \
                self.costo_mensual.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de usuarios después de la validación exitosa de esos datos
                """
        try:
            obj_course_database = Model_class.course_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            obj_course_database = Model_class.course_registration.CourseRegistration(self.e_id_curso.get(),
                                                                                     self.e_n_curso.get(),
                                                                                     self.e_cost_mat.get(),
                                                                                     self.e_cost_men.get())
            query = 'insert into cursos (id_curso, nombre_curso, costo_matricula, costo_mensual) values (%s,%s,%s,%s);'
            values = (obj_course_database.get_id_curso(), obj_course_database.get_nombre_cur(),
                      obj_course_database.get_costo_matricula(), obj_course_database.get_costo_mensual())
            self.db_connection.insert(query, values)
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL CURSO GUARDADOS CORRECTAMENTE\n "
                                                       f"ID CURSO: {values[0]},\n "
                                                       f"NOMBRE DE CURSO: {values[1]}\n"
                                                       f"COSTO MATRÍCULA: {values[2]}\n,"
                                                       f"COSO MENSUAL: {values[3]}")
            self.show_data_cur()

        except BaseException as msg:
            messagebox.showerror("ERROR!!!", f"NO SE HAN PODIDO GUARDAR LOS DATOS DEL USUARIO {msg}")

    def clear_field_cur(self):
        self.id_curso.set('')
        self.nombre_cur.set('')
        self.costo_matricula.set('')
        self.costo_mensual.set('')
        self.e_id_curso.focus()
        self.update_btn["state"] = "disabled"
        self.delete_btn["state"] = "disabled"

    def get_fields_cur(self, row):
        self.cursor_row = self.Table_cur.focus()
        self.content = self.Table_cur.item(self.cursor_row)
        row = self.content['values']
        self.id_curso.set(row[0])
        self.nombre_cur.set(row[1])
        self.costo_matricula.set(row[2])
        self.costo_mensual.set(row[3])
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

    def update_cur(self):
        try:
            obj_course_database = Model_class.course_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            obj_course_database = Model_class.course_registration.CourseRegistration(self.e_id_curso.get(),
                                                                                     self.e_n_curso.get(),
                                                                                     self.e_cost_mat.get(),
                                                                                     self.e_cost_men.get())
            query = 'update cursos set id_curso=%s, nombre_curso=%s, costo_matricula=%s ,costo_mensual=%s'
            values = (obj_course_database.get_id_curso(), obj_course_database.get_nombre_cur(),
                      obj_course_database.get_costo_matricula(), obj_course_database.get_costo_mensual())
            self.db_connection.insert(query, values)
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL CURSO ACTUALIZADOS CORRECTAMENTE\n "
                                                       f"ID CURSO: {values[0]},\n "
                                                       f"NOMBRE DE CURSO: {values[1]}\n"
                                                       f"COSTO MATRÍCULA: {values[2]}\n,"
                                                       f"COSO MENSUAL: {values[3]}")
            self.clear_field_cur()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®) (ERROR)", f"NO SE HAN PODIDO ACTUALIZAR "
                                                                f"LOS DATOS DEL CURSO: {msg}")
            self.clear_field_cur()

    def delete_cur(self):
        try:
            obj_curse_database = Model_class.course_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_curse_database.get_database())

            tree_view_content = self.Table_cur.focus()
            tree_view_items = self.Table_cur.item(tree_view_content)
            tree_view_values = tree_view_items['values'][1]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ALIMINAR AL CURSO: {tree_view_values}")
            if ask is True:
                query = "delete from cursos where nombre_curso=%s;"
                self.db_connection.delete(query, (tree_view_values,))
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL CURSO: {tree_view_values} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")
                self.clear_field_cur()
                self.show_data_cur()
            else:
                pass

        except BaseException as msg:
            messagebox.showerror("Error", f"SE GENERÓ UN ERROR AL INTENTAR ELIMINAR DATOS DE UN CURSO: {msg}")

    # =======================================================================
    # ========================Searching Started==============================
    # =======================================================================
    @classmethod
    def binary_search(cls, _list, target):
        """this is class method searching for user input into the table"""
        start = 0
        end = len(_list) - 1

        while start <= end:
            middle = (start + end) // 2
            midpoint = _list[middle]
            if midpoint > target:
                end = middle - 1
            elif midpoint < target:
                start = middle + 1
            else:
                return midpoint

    @classmethod
    def bubble_sort(self, _list):
        """this class methods sort the string value of user input such as name, email"""
        for j in range(len(_list) - 1):
            for i in range(len(_list) - 1):
                if _list[i].upper() > _list[i + 1].upper():
                    _list[i], _list[i + 1] = _list[i + 1], _list[i]
        return _list

    def search_data_cur(self):
        a = self.search_field_curso.get()
        if self.search_field_curso.get() != '':
            if a.isnumeric():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN NÚMEROS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE CURSO")
                self.search_field_curso.set("")
            elif a.isspace():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN ESPACIOS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE CURSO")
                self.search_field_curso.set("")
            else:
                if a.isalpha():
                    try:
                        search_list = []
                        for child in self.Table_cur.get_children():
                            val = self.Table_cur.item(child)["values"][1]
                            search_list.append(val)

                        sorted_list = self.bubble_sort(search_list)
                        self.output = self.binary_search(sorted_list, self.search_field_curso.get())

                        if self.output:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->ENCONTRADO",
                                                f"EL CURSO: '{self.output}' HA SIDO ENCONTRADO")

                            obj_course_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_course_database.get_database())

                            query = "select * from cursos where nombre_curso LIKE '" + str(self.output) + "%'"
                            # print(output)
                            data = self.db_connection.select(query)
                            # print(data)
                            self.Table_cur.delete(*self.Table_cur.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3]]

                                # self.student_tree.delete(*self.student_tree.get_children())
                                self.Table_cur.insert('', END, values=data_list)
                                self.search_field_curso.set("")

                        else:
                            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR",
                                                 "CURSO NO ENCONTRADO,\nSE MOSTRARÁN RESULTADOS RELACIONADOS.")

                            obj_course_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_course_database.get_database())

                            query = "select * from cursos where nombre_curso LIKE '%" + \
                                    str(self.search_field_curso.get()) + "%'"

                            data = self.db_connection.select(query)
                            self.Table_cur.delete(*self.Table_cur.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3]]

                                self.Table_cur.insert('', END, values=data_list)
                                self.search_field_curso.set("")

                    except BaseException as msg:
                        print(msg)
                else:
                    self.search_data_cur()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL CURSO.")

    def show_data_cur(self):
        try:
            obj_course_database = Model_class.course_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            query = "select * from cursos;"
            data = self.db_connection.select(query)

            self.Table_cur.delete(*self.Table_cur.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3]]

                self.Table_cur.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

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
    # FUNCIÓN CAJA DE INFORMACIÓN DEL SISTEMA(INFO)
    # =============================================================
    def caja_info_sist(self):
        self.men2 = messagebox.showinfo('SIST_CONTROL (IFAP®)',
                                        'SIST_CONTROL (IFAP®) v2.0\n'
                                        'El uso de este software queda sujeto a los términos y condiciones del '
                                        'contrato "J.C.F DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 BJM DESING®. Todos los derechos reservados')


def root():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    Course(root)
    root.mainloop()

if __name__ == '__main__':
    root()
