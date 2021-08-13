# Import Modules
from _datetime import datetime
import mariadb
from tkinter import *
from tkinter import messagebox, ttk

import CRUD


class Student_S:

    def __init__(self, root):
        self.acciones = CRUD.Form_Estudent()

        self.root = root
        self.root.title("SYST_CONTROL--›ALUMNOS")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)

        imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_aceptar.png'),
            'matricular': PhotoImage(file='./recursos/icon_add.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'eliminar': PhotoImage(file='./recursos/icon_del.png'),
            'limpiar': PhotoImage(file='./recursos/icon_clean.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),

        }

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (ALUMNOS)')
        self.texto1.config(font=("Britannic", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=475, pady=0)

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
        self.Column2.add_command(label='Menú Alumnos')
        self.Column2.add_command(label='Matriculación', command=self.matricula_btn)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        self.cuaderno = ttk.Notebook(self.root, width=1000, height=625)
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
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column5)
        self.Column5.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column5.add_command(label='Cambiar Contraseña', command=self.pass_btn)
        self.Column5.add_separator()
        self.Column5.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column5.add_separator()
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='AYUDA', menu=self.Column6)
        self.Column6.add_command(label='Tutorial')
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column7)
        self.Column7.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column7.add_separator()
        self.Column7.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column7.add_separator()
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
        self.n_ced_al = StringVar()
        self.nombres_al = StringVar()
        self.apellidos_al = StringVar()
        self.edad_al = IntVar()
        self.direccion_al = StringVar()
        self.correo_al = StringVar()
        self.n_celular_al = StringVar()
        self.n_telefono_al = StringVar()
        self.ma_edad = StringVar()
        self.representante_al = StringVar()
        self.n_c_representante_al = StringVar()
        self.observacion_al = StringVar()

        self.search_field = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        Manage_Frame.place(x=15, y=75, width=385, height=605)

        m_title = Label(Manage_Frame, text="-ADMINISTAR ESTUDIANTES-", font=("Copperplate Gothic Bold", 16, "bold"),
                        bg='#0d1e24', fg="White")
        m_title.grid(row=0, columnspan=2, padx=10, pady=50)

        self.l_cedula = Label(Manage_Frame, text='No. CÉDULA', width='15', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_cedula.grid(column=0, row=1, padx=1, pady=5)
        self.e_cedula = Entry(Manage_Frame, textvariable=self.n_ced_al, width='13')
        self.e_cedula.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_cedula.focus()

        self.l_nombres = Label(Manage_Frame, text='NOMBRES', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_nombres.grid(column=0, row=2, padx=0, pady=5)
        self.e_nombres = Entry(Manage_Frame, textvariable=self.nombres_al, width='33')
        self.e_nombres.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_apellidos = Label(Manage_Frame, text='APELLIDOS', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_apellidos.grid(column=0, row=3, padx=1, pady=5)
        self.e_apellidos = Entry(Manage_Frame, textvariable=self.apellidos_al, width='33')
        self.e_apellidos.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        self.l_edad = Label(Manage_Frame, text='EDAD', width='15', font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_edad.grid(column=0, row=4, padx=1, pady=5)
        self.e_edad = Entry(Manage_Frame, textvariable=self.edad_al, width='8')
        self.e_edad.grid(column=1, row=4, padx=1, pady=5, sticky="W")

        self.l_direccion = Label(Manage_Frame, text='DIRECCIÓN', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_direccion.grid(column=0, row=5, padx=1, pady=5)
        self.e_direccion = Entry(Manage_Frame, textvariable=self.direccion_al, width='33')
        self.e_direccion.grid(column=1, row=5, padx=1, pady=5, sticky="W")

        self.l_correo = Label(Manage_Frame, text='CORREO', width='15', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_correo.grid(column=0, row=6, padx=1, pady=5)
        self.e_correo = Entry(Manage_Frame, textvariable=self.correo_al, width='33')
        self.e_correo.grid(column=1, row=6, padx=1, pady=5, sticky="W")

        self.l_celular = Label(Manage_Frame, text='No. CELULAR', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_celular.grid(column=0, row=7, padx=1, pady=5)
        self.e_celular = Entry(Manage_Frame, textvariable=self.n_celular_al, width='13')
        self.e_celular.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        self.l_telefono = Label(Manage_Frame, text='No. TELÉFONO', width='15', font=('Copperplate Gothic Bold', 10),
                                bg='#808080')
        self.l_telefono.grid(column=0, row=8, padx=1, pady=5)
        self.e_telefono = Entry(Manage_Frame, textvariable=self.n_telefono_al, width='13')
        self.e_telefono.grid(column=1, row=8, padx=1, pady=5, sticky="W")

        self.l_representante = Label(Manage_Frame, text='REPRESENTANTE', width='15',
                                     font=('Copperplate Gothic Bold', 10),
                                     bg='#808080')
        self.l_representante.grid(column=0, row=9, padx=1, pady=5)
        self.e_representante = Entry(Manage_Frame, textvariable=self.representante_al, width='33')
        self.e_representante.grid(column=1, row=9, padx=1, pady=5, sticky="W")

        self.l_n_c_representante = Label(Manage_Frame, text='NOMBRE REPR.', width='15',
                                         font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_c_representante.grid(column=0, row=10, padx=1, pady=5)
        self.e_n_c_representante = Entry(Manage_Frame, textvariable=self.n_c_representante_al, width='33')
        self.e_n_c_representante.grid(column=1, row=10, padx=1, pady=5, sticky="W")

        self.l_observacion = Label(Manage_Frame, text='OBSERV.', width='15', font=('Copperplate Gothic Bold', 10),
                                   bg='#808080')
        self.l_observacion.grid(column=0, row=11, padx=1, pady=5)
        self.e_observacion = Entry(Manage_Frame, textvariable=self.observacion_al, width='33')
        self.e_observacion.grid(column=1, row=11, padx=1, pady=5, sticky="W")

        # Button Frame
        btn_frame = Frame(Manage_Frame, bg='#0d1e24')
        btn_frame.place(x=10, y=500, width=360)

        self.add_btn = Button(btn_frame, image=imagenes['nuevo'], text='REGISTAR', command=self.add_student,
                              compound=TOP)
        self.add_btn.image = imagenes['nuevo']
        self.add_btn.grid(row=0, column=0, padx=3, pady=10)

        self.m_btn = Button(btn_frame, image=imagenes['matricular'], text='MATRICULAR', command=self.mat_al,
                            compound=TOP)
        self.m_btn.image = imagenes['matricular']
        self.m_btn.grid(row=0, column=1, padx=3, pady=10)
        self.m_btn["state"] = "disabled"

        self.up_btn = Button(btn_frame, image=imagenes['editar'], text='MODIFICAR', command=self.update,
                             compound=TOP)
        self.up_btn.image = imagenes['editar']
        self.up_btn.grid(row=0, column=2, padx=3, pady=10)
        self.up_btn["state"] = "disabled"

        self.del_btn = Button(btn_frame, image=imagenes['eliminar'], text='ELIMINAR', command=self.delete,
                              compound=TOP)
        self.del_btn.image = imagenes['eliminar']
        self.del_btn.grid(row=0, column=3, padx=3, pady=10)
        self.del_btn["state"] = "disabled"

        self.clean_btn = Button(btn_frame, image=imagenes['limpiar'], text='LIMPIAR', command=self.clear_field,
                                compound=TOP)
        self.clean_btn.image = imagenes['limpiar']
        self.clean_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=405, y=75, width=940, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field, font=("Arial", 10, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame
        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=920, height=525)

        X_scroll = Scrollbar(Table_Frame, orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame, columns=("ci", "nom", "ape", "edad", "dir"),
                                  yscrollcommand=Y_scroll.set, xscrollcommand=X_scroll.set)

        X_scroll.pack(side=BOTTOM, fill=X)
        Y_scroll.pack(side=RIGHT, fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("ci", text="No. C.I")
        self.Table.heading("nom", text="NOMBRES")
        self.Table.heading("ape", text="APELLIDOS")
        self.Table.heading("edad", text="EDAD")
        self.Table.heading("dir", text="DIRECCIÓN")

        self.Table['show'] = "headings"
        self.Table.column("ci", width=20)
        self.Table.column("nom", width=70)
        self.Table.column("ape", width=90)
        self.Table.column("edad", width=5)
        self.Table.column("dir", width=115)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields)

        self.show_data()

    def add_student(self):
        if self.n_ced_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA")
            self.e_cedula.focus()

        elif self.nombres_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: NOMBRES")
            self.e_nombres.focus()

        elif self.apellidos_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: APELLIDOS")
            self.e_apellidos.focus()

        elif self.edad_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "LA EDAD DEBE SER MAYOR A '0' AÑOS\n"
                                                                "POR FAVOR INGRESE EL CAMPO: EDAD")
            self.e_edad.focus()

        elif self.direccion_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: DIRECCIÓN")
            self.e_direccion.focus()

        elif self.correo_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: CORREO")
            self.e_correo.focus()

        elif self.n_celular_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. DE CELULAR")
            self.e_celular.focus()

        elif self.observacion_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: OBSERVACIONES")
            self.e_observacion.focus()

        else:
            datos = (self.n_ced_al.get(), self.nombres_al.get(), self.apellidos_al.get(),
                     self.edad_al.get(), self.direccion_al.get(), self.correo_al.get(),
                     self.n_celular_al.get(), self.n_telefono_al.get(), self.representante_al.get(),
                     self.n_c_representante_al.get(), self.observacion_al.get())
            self.acciones.reg_est(datos)

            self.n_ced_al.set('')
            self.nombres_al.set('')
            self.apellidos_al.set('')
            self.edad_al.set('')
            self.direccion_al.set('')
            self.correo_al.set('')
            self.n_celular_al.set('')
            self.n_telefono_al.set('')
            self.representante_al.set('')
            self.n_c_representante_al.set('')
            self.observacion_al.set('')
            self.e_cedula.focus()

            self.show_data()
            # self.clear_field()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ESTUDIANTE GUARDADOS EN EL REGISTRO CORRECTAMENTE!!!")
            self.sa = messagebox.askyesno("SYST_CONTROL(IFAP®)",
                                          "DATOS DEL ESTUDIANTE GUARDADOS EN EL REGISTRO CORRECTAMENTE!!!\n"
                                          "¿DESEAS MATRICULAR CON LOS DATOS INGRESADOS?")
            if self.sa:
                self.mat_al()
            else:
                pass

    def clear_field(self):
        self.n_ced_al.set('')
        self.nombres_al.set('')
        self.apellidos_al.set('')
        self.edad_al.set('')
        self.direccion_al.set('')
        self.correo_al.set('')
        self.n_celular_al.set('')
        self.n_telefono_al.set('')
        self.representante_al.set('')
        self.n_c_representante_al.set('')
        self.observacion_al.set('')
        self.e_cedula.focus()
        self.m_btn["state"] = "disabled"
        self.up_btn["state"] = "disabled"
        self.del_btn["state"] = "disabled"

    def get_fields(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.n_ced_al.set(row[0])
        self.nombres_al.set(row[1])
        self.apellidos_al.set(row[2])
        self.edad_al.set(row[3])
        self.direccion_al.set(row[4])
        self.correo_al.set(row[5])
        self.n_celular_al.set(row[6])
        self.n_telefono_al.set(row[7])
        self.representante_al.set(row[8])
        self.n_c_representante_al.set(row[9])
        self.observacion_al.set(row[10])
        self.m_btn["state"] = "normal"
        self.up_btn["state"] = "normal"
        self.del_btn["state"] = "normal"

    def update(self):
        if self.n_ced_al.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE MODIFICAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()

            sql = f"""UPDATE estudiantes SET nombres="{self.nombres_al.get()}", apellidos="{self.apellidos_al.get()}",\
            edad="{self.edad_al.get()}", direccion="{self.direccion_al.get()}", correo="{self.correo_al.get()}",\
            celular="{self.n_celular_al.get()}", telefono="{self.n_telefono_al.get()}",\
            representante="{self.representante_al.get()}", cedula_r="{self.n_c_representante_al.get()}",\
            observacion="{self.observacion_al.get()}" WHERE id_estudiante={self.n_ced_al.get()}"""
            self.curr.execute(sql)
            self.connect.commit()

            self.show_data()
            # self.connect.close()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ESTUDIANTE: " + self.nombres_al.get() +
                                " CON No. C.I: " + self.n_ced_al.get() + " HAN SIDO ACTUALIZADOS EN EL "
                                                                         "REGISTRO CORRECTAMENTE!!!")
            self.n_ced_al.set('')
            self.nombres_al.set('')
            self.apellidos_al.set('')
            self.edad_al.set('')
            self.direccion_al.set('')
            self.correo_al.set('')
            self.n_celular_al.set('')
            self.n_telefono_al.set('')
            self.representante_al.set('')
            self.n_c_representante_al.set('')
            self.observacion_al.set('')
            self.e_cedula.focus()

    def delete(self):
        if self.n_ced_al.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.conn.cursor()
            self.sql = f"""DELETE FROM estudiantes WHERE id_estudiante={self.n_ced_al.get()}"""
            self.curr.execute(self.sql)

            self.conn.commit()
            self.show_data()
            self.clear_field()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ESTUDIANTE ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")

    def search_data(self):
        if self.search_field.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA")

        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_n_ced = self.search_field.get()
        sql = f"""SELECT id_estudiante FROM estudiantes WHERE id_estudiante={self.search_n_ced}"""
        self.curr.execute(sql)
        self.curr.fetchall()

        if self.curr.rowcount == 1:
            self.sql = f"""SELECT id_estudiante, nombres, apellidos, edad, direccion, correo , celular, telefono,\
                        representante, cedula_r, observacion FROM estudiantes WHERE id_estudiante={self.search_n_ced}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                self.Table.delete(*self.Table.get_children())
                for self.row in self.rows:
                    self.Table.insert('', END, values=self.row)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO CON EL No. DE CÉDULA: " +
                                 self.search_n_ced)
            self.search_field.set('')

    def show_data(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS estudiantes("
                          "id_estudiante VARCHAR(20) PRIMARY KEY,"
                          "nombres VARCHAR(50),"
                          "apellidos VARCHAR(50),"
                          "edad INT,"
                          "direccion VARCHAR(50),"
                          "correo VARCHAR(50),"
                          "celular VARCHAR(20),"
                          "telefono VARCHAR(20),"
                          "representante VARCHAR(50), "
                          "cedula_r VARCHAR(20), "
                          "observacion VARCHAR(50))")

        self.curr.execute("SELECT * FROM estudiantes")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table.delete(*self.Table.get_children())
            for self.row in self.rows:
                self.Table.insert('', END, values=self.row)

            self.connect.commit()
        self.connect.close()

    def logout(self):
        self.root.destroy()

        from Login_Window import Login
        st_root = Tk()
        Login(st_root)
        st_root.mainloop()

    def principal_btn(self):
        self.root.destroy()

        from Secretaria.Principal_Window_S import Principal_S
        st_root = Tk()
        Principal_S(st_root)
        st_root.mainloop()

    def mat_al(self):
        self.root.destroy()

        from Secretaria.Matricula_Window_S import Matricula_S
        st_root = Tk()
        Matricula_S(st_root)
        st_root.mainloop()

    def matricula_btn(self):
        self.root.destroy()

        from Secretaria.Matricula_Window_S import Matricula_S
        st_root = Tk()
        Matricula_S(st_root)
        st_root.mainloop()

    def assesor_btn(self):
        self.root.destroy()

        from Secretaria.Assesor_Window_S import Assesor_S
        st_root = Tk()
        Assesor_S(st_root)
        st_root.mainloop()

    def courses_btn(self):
        self.root.destroy()

        from Secretaria.Course_Window_S import Course_S
        st_root = Tk()
        Course_S(st_root)
        st_root.mainloop()

    def pass_btn(self):
        self.root.destroy()

        from Secretaria.Password_Window_S import Password_S
        st_root = Tk()
        Password_S(st_root)
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
    application = Student_S(root)
    root.mainloop()
