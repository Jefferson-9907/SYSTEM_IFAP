from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
from tkinter.ttk import Treeview, Combobox

import mariadb

from modelos import ProductoFacturar, Factura
from reportes import ReciboFactura
import Frontend.login_form


class Facturation_F:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Facturación")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('./recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')

        self.imagenes = {
            'nuevo': PhotoImage(file='imagenes/001-mas.png'),
            'editar': PhotoImage(file='imagenes/002-lapiz.png'),
            'eliminar': PhotoImage(file='imagenes/003-eliminar.png'),
            'reportes': PhotoImage(file='imagenes/004-actualizar.png'),
            'new': PhotoImage(file='imagenes/icon_new_ind.png'),
            'block': PhotoImage(file='imagenes/icon_block.png'),
            'buscar': PhotoImage(file='imagenes/icon_buscar.png'),
            'todo': PhotoImage(file='imagenes/icon_ver_todo.png'),
            'facturar': PhotoImage(file='imagenes/comprobar.png'),
            'aceptar': PhotoImage(file='imagenes/icon_aceptar.png')
        }

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (FACTURACIÓN)')
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
        self.cuaderno = ttk.Notebook(self.root, width=1340, height=625)
        self.cuaderno.grid(row=1, column=0, sticky='nw', padx=10, pady=5)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ PRINCIPAL
        # =============================================================
        self.menus.add_cascade(label='INICIO', menu=self.Column1)
        self.Column1.add_command(label='Menú Inicio', command=self.principal_btn)
        self.Column2 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ FACTURACIÓN
        # =============================================================
        self.menus.add_cascade(label='FACTURACIÓN', menu=self.Column2)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column3)
        self.Column3.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column3.add_command(label='Cambiar Contraseña', command=self.pass_btn)
        self.Column3.add_separator()
        self.Column3.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column3.add_separator()
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10), bg='Honeydew2',
                            relief=RIDGE)
        self.footer.place(x=0, y=703)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10),
                              bg='Honeydew2',
                              relief=RIDGE)
        self.footer_1.place(x=212, y=704)

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=195, bg='black',
                              fg='white')
        self.footer_4.place(x=0, y=725)

        self.factura = Factura()
        self.validatecommand = self.root.register(self.solo_numero)
        self.validate_subtotal = self.root.register(self.mostrar_sub_total)

        # LABELFRAME OPCIONES PRINCIPALES DE FACTURACIÓN
        self.labelframe_superior = LabelFrame(self.root, width=600, height=63, bg='#0d1e24')
        self.labelframe_superior.place(x=20, y=75)

        self.l_Buscar = Label(self.labelframe_superior, text="BUSCAR :", bg='#0d1e24', fg="White",
                              font=("Copperplate Gothic Bold", 10, "bold"))
        self.l_Buscar.place(x=5, y=15)

        self.txtBuscar = Entry(self.labelframe_superior, width=20)
        self.txtBuscar.bind('<Return>', self.buscar_productos)
        self.txtBuscar.place(x=90, y=15)

        self.btnBuscar = Button(self.labelframe_superior, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                command=lambda: self.buscar_productos(1), compound="right")
        self.btnBuscar.image = self.imagenes['buscar']
        self.btnBuscar.place(x=220, y=10)

        self.show_all_btn = Button(self.labelframe_superior, image=self.imagenes['todo'], text='VER TODO',
                                   command=self.listar_productos, width=85, compound="right")
        self.show_all_btn.image = self.imagenes['todo']
        self.show_all_btn.place(x=315, y=10)

        self.BtnReportes = Button(self.labelframe_superior, image=self.imagenes['reportes'],
                                  command=self.listar_productos, text='REFRESCAR', width=80, compound="right")
        self.BtnReportes.image = self.imagenes['reportes']
        self.BtnReportes.place(x=415, y=10)

        self.BtnNuevo = Button(self.labelframe_superior, text='LIMPIAR', image=self.imagenes['new'], width=70,
                               command=self.nueva_factura, compound="right")
        self.BtnNuevo.image = self.imagenes['new']
        self.BtnNuevo.place(x=510, y=10)

        self.label_facturacion = LabelFrame(self.root, width=715, height=605, bg='#0d1e24')
        self.label_facturacion.place(x=625, y=75)

        # TABLA CON PRODUCTOS
        self.labelproductos = LabelFrame(self.root, bg='#0d1e24')
        self.labelproductos.place(x=20, y=145, width=600, height=535)

        # Table Frame
        Table_Frame_impl = Frame(self.labelproductos)
        Table_Frame_impl.place(x=5, y=5, width=590, height=520)

        Y_scroll = Scrollbar(Table_Frame_impl, orient=VERTICAL)
        self.listdetalle = Treeview(Table_Frame_impl, columns=("id_impl", "id_cur", "desc", "valor", "disp", "stock"),
                                    yscrollcommand=Y_scroll.set)
        self.listdetalle.tag_configure('gr', background='green')

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.listdetalle.yview)
        self.listdetalle.heading("id_impl", text="CÓD.")
        self.listdetalle.heading("id_cur", text="CURSO")
        self.listdetalle.heading("desc", text="DESCRIPCIÓN")
        self.listdetalle.heading("valor", text="VALOR")
        self.listdetalle.heading("disp", text="ESTADO")
        self.listdetalle.heading("stock", text="CUPOS")

        self.listdetalle['show'] = "headings"
        self.listdetalle.column("id_impl", width=5)
        self.listdetalle.column("id_cur", width=5)
        self.listdetalle.column("desc", width=290)
        self.listdetalle.column("valor", width=5)
        self.listdetalle.column("disp", width=10)
        self.listdetalle.column("stock", width=5)

        self.listdetalle.pack(fill=BOTH, expand=1)
        self.listdetalle.bind('<Double-1>', self.widget_agregar_producto_factura)
        self.listar_productos()

        data = datetime.now()
        fomato_f = "%A - %d/%B/%Y"

        self.lb_fecha = Label(self.label_facturacion, text='FECHA:  ' + str(data.strftime(fomato_f)),
                              font=('Copperplate Gothic Bold', 8), bg='#0d1e24', fg="White")
        self.lb_fecha.place(x=460, y=10)

        self.lb_cod_factura = Label(self.label_facturacion, text='No. FACTURA', font=('Copperplate Gothic Bold', 12),
                                    bg='#0d1e24', fg="White")
        self.lb_cod_factura.place(x=185, y=10)

        self.codigo_factura = StringVar()
        self.txt_cod_factura = Entry(self.label_facturacion, state='readonly', textvariable=self.codigo_factura,
                                     fg='Red', width=10, font=('Copperplate Gothic Bold', 14), relief=RIDGE)
        self.txt_cod_factura.place(x=315, y=10)
        self.codigo_factura.set(1)

        self.search_field = StringVar()
        self.l_ced_al = Label(self.label_facturacion, text='No. C.I ALUMNO', font=("Britannic", 10, "bold"),
                              bg='#0d1e24', fg="White")
        self.l_ced_al.place(x=10, y=40)
        self.e_n_ced_al = Entry(self.label_facturacion, textvariable=self.search_field, width=19)
        self.e_n_ced_al.place(x=125, y=40)

        self.b_buscar_al = Button(self.label_facturacion, text='BUSCAR', font=('Copperplate Gothic Bold', 8),
                                  bg='#333333', fg='white', command=self.search_data_al)
        self.b_buscar_al.place(x=250, y=40)

        self.l_name = Label(self.label_facturacion, text='NOMBRES', font=("Britannic", 10, "bold"),
                            bg='#0d1e24', fg="White")
        self.l_name.place(x=10, y=70)
        self.nombres_al = StringVar()
        self.name_e = Entry(self.label_facturacion, width=25, textvariable=self.nombres_al, state='readonly')
        self.name_e.place(x=90, y=70)

        self.ape_l = Label(self.label_facturacion, text='APELLIDOS', font=("Britannic", 10, "bold"), bg='#0d1e24',
                           fg="White")
        self.ape_l.place(x=250, y=70)
        self.apellidos_al = StringVar()
        self.ape_e_ = Entry(self.label_facturacion, width=25, textvariable=self.apellidos_al, state='readonly')
        self.ape_e_.place(x=335, y=70)

        self.lb_direccion = Label(self.label_facturacion, text='DIRECCIÓN', font=("Britannic", 10, "bold"),
                                  bg='#0d1e24', fg="White")
        self.lb_direccion.place(x=10, y=100)
        self.direcccion_al = StringVar()
        self.dir_e_al = Entry(self.label_facturacion, width=66, textvariable=self.direcccion_al, state='readonly')
        self.dir_e_al.place(x=90, y=100)

        self.detalle_factura = Treeview(self.label_facturacion, columns=('#0', '#1', '#2', '#3'))
        self.detalle_factura.place(x=10, y=190, width=690, height=275)

        self.detalle_factura.column('#0', width=475)
        self.detalle_factura.column('#1', width=70)
        self.detalle_factura.column('#2', width=70)
        self.detalle_factura.column('#3', width=70)

        self.detalle_factura.heading('#0', text='Implemento')
        self.detalle_factura.heading('#1', text='Cant.')
        self.detalle_factura.heading('#2', text='P. Unit')
        self.detalle_factura.heading('#3', text='Subtotal')

        self.lb_detalle = Label(self.label_facturacion, text='-----DETALLE FACTURA-----',
                                font=("Britannic", 11, "bold"),
                                bg='#0d1e24', fg="White")
        self.lb_detalle.place(x=255, y=160)

        self.total = StringVar()
        self.lb_total = Label(self.label_facturacion, text='TOTAL  $', font=("Britannic", 10, "bold"), width=8)
        self.lb_total.place(x=555, y=475)
        self.tx_total = Entry(self.label_facturacion, state='readonly', textvariable=self.total, width=11)
        self.tx_total.place(x=630, y=475)

        self.lb_pago = Label(self.label_facturacion, text='PAGO    $', font=("Britannic", 10, "bold"), width=8)
        self.lb_pago.place(x=555, y=500)
        self.txt_pago = Entry(self.label_facturacion, validate='key', validatecommand=(self.validatecommand, "%S"),
                              width=11)
        self.txt_pago.bind('<Return>', self.calcular_cambio)
        self.txt_pago.place(x=630, y=500)

        self.cambio = StringVar()
        self.lb_cambio = Label(self.label_facturacion, text='CAMBIO $', font=("Britannic", 10, "bold"), width=8)
        self.lb_cambio.place(x=555, y=525)
        self.tx_cambio = Entry(self.label_facturacion, state='readonly', textvariable=self.cambio, width=11)
        self.tx_cambio.place(x=630, y=525)

        self.lb_moneda = Label(self.label_facturacion, text='Moneda :', font=("Britannic", 10, "bold"))
        self.lb_moneda.place(x=300, y=475)
        self.tipo_moneda = Combobox(self.label_facturacion, values=['$-USD', 'CORD-NIO '], width=10)
        self.tipo_moneda.place(x=375, y=475)

        self.BtnBloquear = Button(self.label_facturacion, text='FACTURAR', font=("Britannic", 10, "bold"),
                                  image=self.imagenes['facturar'], compound="right", width=100,
                                  command=self.guardar_factura)
        self.BtnBloquear.images = self.imagenes['facturar']
        self.BtnBloquear.place(x=350, y=500)

    def solo_numero(self, char):
        return char in '1234567890.'

    def buscar_productos(self, event):
        """
        Funcion asociada a widget buscar para la busqueda de un
        producto
        """
        if self.txtBuscar.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: CÓD. IMPLEMENTO")
            self.txtBuscar.focus()

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()
            self.varia = self.txtBuscar.get()

            sql = f"""SELECT descripcion FROM implementos WHERE descripcion LIKE "{self.varia}%" """
            self.curr.execute(sql)
            self.curr.fetchall()
            if self.curr.rowcount == 1:
                sql1 = f"""SELECT id_implemento, id_curso, descripcion, costo_implemento, estado, inventario\
                        FROM implementos WHERE descripcion={self.varia}"""

                self.curr.execute(sql1)
                self.rows = self.curr.fetchall()

                if len(self.rows) != 0:
                    self.listdetalle.delete(*self.listdetalle.get_children())
                    for row in self.rows:
                        self.listdetalle.insert('', END, values=row)
                    self.connect.commit()
            else:
                messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO DEL IMPLEMENTO CON EL CÓDIGO: " +
                                     str(self.varia))

    def ventana_productos(self):
        """
         Widget que muestra los productos en general
         o ya filtrado en una busqueda
        """
        self.labelproductos = LabelFrame(self.root, bg='#0d1e24')
        self.labelproductos.place(x=20, y=145, width=600, height=535)

        # Table Frame
        Table_Frame_impl = Frame(self.labelproductos)
        Table_Frame_impl.place(x=5, y=5, width=590, height=520)

        Y_scroll = Scrollbar(Table_Frame_impl, orient=VERTICAL)
        self.listdetalle = Treeview(Table_Frame_impl, columns=("id_impl", "id_cur", "desc", "valor", "disp", "stock"),
                                    yscrollcommand=Y_scroll.set)
        self.listdetalle.tag_configure('gr', background='green')

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.listdetalle.yview)
        self.listdetalle.heading("id_impl", text="CÓD.")
        self.listdetalle.heading("id_cur", text="CURSO")
        self.listdetalle.heading("desc", text="DESCRIPCIÓN")
        self.listdetalle.heading("valor", text="VALOR")
        self.listdetalle.heading("disp", text="ESTADO")
        self.listdetalle.heading("stock", text="CUPOS")

        self.listdetalle['show'] = "headings"
        self.listdetalle.column("id_impl", width=5)
        self.listdetalle.column("id_cur", width=5)
        self.listdetalle.column("desc", width=290)
        self.listdetalle.column("valor", width=5)
        self.listdetalle.column("disp", width=10)
        self.listdetalle.column("stock", width=5)

        self.listdetalle.pack(fill=BOTH, expand=1)
        self.listdetalle.bind('<Double-1>', self.widget_agregar_producto_factura)
        self.listar_productos()

    def widget_buscar_producto(self):
        """
         Ventana hija para buscar un producto
         y actualizarlo
        """
        self.VtBuscar = Toplevel()
        self.VtBuscar.geometry('340x60')
        self.VtBuscar.title('BUSCAR IMPLEMENTO')
        self.VtBuscar.resizable(False, False)
        self.VtBuscar.grab_set()
        self.VtBuscar.transient(master=self.root)

        self.Manage_Frame_busc_impl = Frame(self.VtBuscar, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_busc_impl.place(x=5, y=5, width=330, height=50)

        self.lbCodigoED = Label(self.Manage_Frame_busc_impl, text='CÓD. IMPLEMENTO', font=("Britannic", 10, "bold"),
                                bg='#0d1e24', fg="White")
        self.lbCodigoED.place(x=10, y=10)
        self.txtCodigoED = Entry(self.Manage_Frame_busc_impl, width=12)
        self.txtCodigoED.place(x=140, y=10)

    def widgets_producto(self):
        """
         Ventana hija asociada al boton nuevo que funciona para
         agregar o modifcar un producto
        """
        self.nuevo_producto = Toplevel()
        self.nuevo_producto.title('AGREGAR IMPLEMENTO')
        self.nuevo_producto.geometry('450x250')
        self.nuevo_producto.resizable(False, False)
        self.nuevo_producto.transient(master=self.root)
        self.nuevo_producto.grab_set()

        # Widgets para añadir un producto

        self.Manage_Frame_add_impl = Frame(self.nuevo_producto, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_add_impl.place(x=5, y=5, width=440, height=240)

        self.lbCodigo = Label(self.Manage_Frame_add_impl, text='CÓDIGO', font=("Britannic", 10, "bold"), bg='#0d1e24',
                              fg="White")
        self.lbCodigo.place(x=20, y=10)
        self.txtCodigo = Entry(self.Manage_Frame_add_impl, width=10)
        self.txtCodigo.place(x=120, y=10)

        self.lbId_curso = Label(self.Manage_Frame_add_impl, text='CÓD. CURSO', font=("Britannic", 10, "bold"),
                                bg='#0d1e24', fg="White")
        self.lbId_curso.place(x=20, y=50)
        self.txtId_curso = Entry(self.Manage_Frame_add_impl, width=10)
        self.txtId_curso.place(x=120, y=50)

        self.lbNombre = Label(self.Manage_Frame_add_impl, text='DESCRIPCIÓN', font=("Britannic", 10, "bold"),
                              bg='#0d1e24', fg="White")
        self.lbNombre.place(x=20, y=80)
        self.txtNombre = Entry(self.Manage_Frame_add_impl, width=50)
        self.txtNombre.place(x=120, y=80)

        self.lbPrecio = Label(self.Manage_Frame_add_impl, text='PRECIO', font=("Britannic", 10, "bold"), bg='#0d1e24',
                              fg="White")
        self.lbPrecio.place(x=20, y=110)
        self.txtPrecio = Entry(self.Manage_Frame_add_impl, width=10, validate='key',
                               validatecommand=(self.validatecommand, "%S"))
        self.txtPrecio.place(x=120, y=110)

        self.lbStock = Label(self.Manage_Frame_add_impl, text='CUPOS', font=("Britannic", 10, "bold"), bg='#0d1e24',
                             fg="White")
        self.lbStock.place(x=20, y=140)
        self.txtStock = Entry(self.Manage_Frame_add_impl, width=10, validate='key',
                              validatecommand=(self.validatecommand, "%S"))
        self.txtStock.place(x=120, y=140)

        self.estado = Label(self.Manage_Frame_add_impl, text='DISPONIBLE', font=("Britannic", 10, "bold"), bg='#0d1e24',
                            fg="White")
        self.estado.place(x=20, y=170)
        self.valor = BooleanVar()
        self.txtEstado = Checkbutton(self.Manage_Frame_add_impl, variable=self.valor, onvalue=True, offvalue=False,
                                     bg='#0d1e24', fg="Black")
        self.txtEstado.place(x=120, y=170)

    def search_data_al(self):
        if self.search_field.get() == "":
            messagebox.showerror("SYST_CONTROL (IFAP®)-ERROR!!!", "INGRESE EL CAMPO: No. CÉDULA ESTUDIANTE")

        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_n_ced_e = self.search_field.get()
        sql = f"""SELECT id_estudiante FROM estudiantes WHERE id_estudiante={self.search_n_ced_e}"""
        self.curr.execute(sql)
        self.curr.fetchall()

        if self.curr.rowcount == 1:
            self.sql = f"""SELECT * FROM estudiantes 
            WHERE id_estudiante={self.search_n_ced_e}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                for self.row in self.rows:
                    self.nombres_al.set(self.row[1])
                    self.apellidos_al.set(self.row[2])
                    self.direcccion_al.set(self.row[4])

        else:
            pass

    def agregar_producto_factura(self, ):
        """
         Funcion asociada para agregar un producto a la
         factura
        """
        producto_factura = ProductoFacturar()
        producto_factura.id_factura = self.codigo_factura.get()
        producto_factura.id = self.codigo.get()
        producto_factura.descripcion = self.descripcion.get()
        producto_factura.precio = float(self.precio.get())
        producto_factura.cantidad = int(self.txt_cantidad.get())
        producto_factura.sub_total = str(producto_factura.calcular_subtotal())

        id = self.validar_producto_existente_factura(producto_factura.descripcion)  # Valida si el producto esta
        # existente solo para aumentar su cantidad
        if id:
            self.factura.remover_producto(producto_factura.descripcion)
            producto_facturar_edit = self.detalle_factura.item(id)
            producto_viejo_valores = producto_facturar_edit['values']
            producto_factura_cant_ant = int(producto_viejo_valores[0])
            self.detalle_factura.delete(id)
            nueva_cantidad = int(producto_factura.cantidad) + int(producto_factura_cant_ant)
            producto_factura.cantidad = nueva_cantidad
            producto_factura.sub_total = str(producto_factura.calcular_subtotal())
            self.detalle_factura.insert('', 0, text=producto_factura.descripcion, values=(
                producto_factura.cantidad, producto_factura.precio, producto_factura.sub_total), iid=id)

        else:
            self.detalle_factura.insert('', 0, text=producto_factura.descripcion, values=(
                producto_factura.cantidad, producto_factura.precio, producto_factura.sub_total))
        self.factura.lista_productos.append(producto_factura)

        self.producto_factura.destroy()
        self.total.set(str(self.factura.calcular_total()))

    def mostrar_sub_total(self, event):
        # Calcula el subtotal del un producto y lo muestra
        sub_total = float(self.precio.get()) * int(self.txt_cantidad.get())
        self.sub_total.set(str(sub_total))

    def widget_agregar_producto_factura(self, event):
        """
         Ventana hija asociada al momento de selecionar
         un producto y muestra su informacion y la cantidad
         de producto requerida
        """
        id = self.listdetalle.focus()
        producto_focus = self.listdetalle.item(id)
        lista = []
        for atributos in producto_focus['values']:
            lista.append(atributos)

        self.producto_factura = Toplevel()
        self.producto_factura.geometry('475x220')
        self.producto_factura.title('AGREGAR A FACTURA')
        self.producto_factura.wait_visibility()
        self.producto_factura.grab_set()
        self.producto_factura.transient(master=self.root)

        self.lb_cod_producto = Label(self.producto_factura, text='CÓD. IMPLEMENTO', font=("Britannic", 10, "bold"))
        self.lb_cod_producto.place(x=10, y=10)
        self.codigo = StringVar()
        self.tx_codigo = Entry(self.producto_factura, state='readonly', textvariable=self.codigo, width=10)
        self.tx_codigo.place(x=150, y=10)
        self.codigo.set(producto_focus['text'])
        self.codigo.set(lista[0])

        self.lb_cod_curso = Label(self.producto_factura, text='CÓD. CURSO', font=("Britannic", 10, "bold"))
        self.lb_cod_curso.place(x=10, y=40)
        self.cod_curso = StringVar()
        self.txtcod_curso = Entry(self.producto_factura, state='readonly', textvariable=self.cod_curso, width=10)
        self.txtcod_curso.place(x=150, y=40)
        self.cod_curso.set(lista[1])

        self.lb_nb_producto = Label(self.producto_factura, text='DESCRIPCIÓN', font=("Britannic", 10, "bold"))
        self.lb_nb_producto.place(x=10, y=70)
        self.descripcion = StringVar()
        self.txt_nb_producto = Entry(self.producto_factura, state='readonly', textvariable=self.descripcion, width=50)
        self.txt_nb_producto.place(x=150, y=70)
        self.descripcion.set(lista[2])

        self.lb_precio = Label(self.producto_factura, text='PRECIO', font=("Britannic", 10, "bold"))
        self.lb_precio.place(x=10, y=100)
        self.precio = StringVar()
        self.txt_precio = Entry(self.producto_factura, state='readonly', textvariable=self.precio, width=10)
        self.txt_precio.place(x=150, y=100)
        self.precio.set(lista[3])

        self.lb_cantidad = Label(self.producto_factura, text='CANTIDAD', font=("Britannic", 10, "bold"))
        self.lb_cantidad.place(x=10, y=130)
        self.cantidad = StringVar()
        self.cantidad.set('1')
        self.txt_cantidad = Entry(self.producto_factura, textvariable=self.cantidad, validate='key',
                                  validatecommand=(self.validatecommand, "%S"), width=10)
        self.txt_cantidad.bind('<Return>', self.mostrar_sub_total)
        self.txt_cantidad.place(x=150, y=130)
        self.txt_cantidad.focus()

        self.lb_sub_total = Label(self.producto_factura, text='SUB-TOTAL', font=("Britannic", 10, "bold"))
        self.lb_sub_total.place(x=10, y=160)

        self.sub_total = StringVar()
        self.txt_sub_total = Entry(self.producto_factura, state='readonly', textvariable=self.sub_total, width=10)
        self.txt_sub_total.place(x=150, y=160)

        self.btAdd = Button(self.producto_factura, text='AÑADIR A FACTURA', font=("Britannic", 10, "bold"),
                            command=self.agregar_producto_factura)
        self.btAdd.place(x=175, y=185)

    def listar_productos(self):
        # Lista todos los productos activos
        conexion = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        cursor = conexion.cursor()
        consulta = 'SELECT * FROM implementos'
        cursor.execute(consulta)
        # Lista todos los productos activos
        rows = cursor.fetchall()

        if len(rows) != 0:
            # self.listdetalle.delete(self.listdetalle.get_children())
            for row in rows:
                self.listdetalle.insert('', END, values=row)

            conexion.commit()
        conexion.close()

    def nueva_factura(self):
        # Limpiar productos en facturas
        self.search_field.set('')
        self.nombres_al.set('')
        self.apellidos_al.set('')
        self.direcccion_al.set('')

        id_detalle = self.detalle_factura.get_children()
        for item in id_detalle:
            self.detalle_factura.delete(item)

        self.total.set('')
        self.tipo_moneda.current(1)
        self.cambio.set('')
        self.txt_pago.delete(0, END)

    def validar_producto_existente_factura(self, nombre):
        """
        Funcion que verifica si un producto esta añadido a la factura
        Si el caso es verdadero la cantidad solo se actualiza
        """
        lista_producto = self.detalle_factura.get_children()

        for productos in lista_producto[::-1]:
            producto_agregado = self.detalle_factura.item(productos)
            if nombre == producto_agregado['text']:
                return productos
            else:
                return False

    def calcular_cambio(self, event):
        # Calcula el cambio
        billete = float(self.txt_pago.get())
        cambio = billete - float(self.total.get())
        self.cambio.set(str(cambio))

    def guardar_factura(self):
        """Guarda el registro de la factura"""
        if self.txt_pago != '':  # Si el pago no esta vacio
            factura = self.factura

            for productos_factura in self.factura.lista_productos:
                productos_factura.guardar()

            factura.id_factura = self.codigo_factura.get()
            id_al = self.name_e.get()
            lista_al = id_al.split('_')
            factura.id_alumno = lista_al[0]
            factura.nom_ape_al = self.name_e.get() + " " + self.apellidos_al.get()
            """factura.nombres_al = self.name_e.get()
            factura.ape_al = self.apellidos_al.get()"""
            factura.n_c_al = self.e_n_ced_al.get()
            factura.dir_al = self.dir_e_al.get()
            data = datetime.now()
            fomato_f = "%A %d-%B-%Y--%H:%M:%S %p "
            form_fecha = "%d-%m-%Y"
            factura.fecha = str(data.strftime(form_fecha))
            form_hora = "%H:%M:%S"
            factura.hora = str(data.strftime(form_hora))
            factura.fecha_creacion = str(data.strftime(fomato_f))
            factura.pago = self.txt_pago.get()
            factura.cambio = self.cambio.get()
            recibo = ReciboFactura()  # Instancia del recibo factura
            recibo.detalles_factura(factura)  # se pasa el objeto para ser llenado el recibo
            recibo.save()

            recibo.__del__()

            factura.guardar()
            factura.lista_productos.clear()
            self.nueva_factura()
            self.listar_productos()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO: PAGO NO PUEDE ESTAR VACÍO!!!")

    def logout(self):
        root = Toplevel()
        Frontend.login_form.Login(root)
        self.root.withdraw()
        root.deiconify()

    def principal_btn(self):
        self.root.destroy()

        from Principal_Window_F import Principal_F
        st_root = Tk()
        Principal_F(st_root)
        st_root.mainloop()

    def pass_btn(self):
        self.root.destroy()

        from Password_Window_F import Password_F
        st_root = Tk()
        Password_F(st_root)
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
                                        'contrato "J.C.F DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 J.C.F DESING®. Todos los derechos reservados')


if __name__ == '__main__':
    root = Tk()
    application = Facturation_F(root)
    root.mainloop()
