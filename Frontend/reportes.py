
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Image, BaseDocTemplate
from reportlab.lib.colors import red, black, red, blue, green
from datetime import datetime
from reportlab.lib.pagesizes import LETTER, inch, landscape, letter
import os


class ReciboFactura:
    """Objeto para crear un recibo asociado a una factura"""

    def __init__(self):
        """Inicializa el titulo de la factura
        fecha = datetime.now()

        data = datetime.now()
        fomato_f = " %A %d-%B-%Y %H: %M: %S %p "
        titulo = str(data.strftime(fomato_f))"""

        titulo = 'Factura-PRUEBA.pdf'
        # nombre_pdf = os.path.join('Facturas/', titulo)
        # self.factura = canvas.Canvas(titulo, pagesize=A4)

        self.factura = canvas.Canvas(titulo, pagesize=A4)
        # self.factura.setPageSize(landscape(A4))

        """self.elements = []
        logo = "./imagenes/icon_fact.png"
        my_image = Image(logo, 2 * inch, 2 * inch)
        self.elements.append(my_image)"""

    def crear_esqueleto(self):
        _, h = A4
        # ORIGINAL
        # self.factura.setFont("Times-Roman", 16)
        # self.factura.drawString(225, h - 120, "Id Factura: ")
        self.factura.line(x1=20, x2=580, y1=h - 125, y2=h - 125)
        self.factura.setFont("Times-Roman", 11)
        self.factura.drawString(20, h - 135, 'NOMBRE:')
        self.factura.drawString(20, h - 150, 'No. CÉDULA:')
        self.factura.drawString(20, h - 165, 'DIRECCIÓN:')
        self.factura.drawString(20, h - 180, 'FECHA EMISIÓN:')
        self.factura.line(x1=20, x2=580, y1=h - 190, y2=h - 190)
        self.factura.drawString(235, h - 200, "DETALLE DE LA FACTURA")

        # CLIENTE
        # self.factura.setFont("Times-Roman", 16)
        # self.factura.drawString(225, h - 575, "Id Factura: ")
        self.factura.line(x1=20, x2=580, y1=h - 580, y2=h - 580)
        self.factura.setFont("Times-Roman", 11)
        self.factura.drawString(20, h - 590, 'NOMBRE:')
        self.factura.drawString(20, h - 605, 'No. CÉDULA:')
        self.factura.drawString(20, h - 620, 'DIRECCIÓN:')
        self.factura.drawString(20, h - 635, 'FECHA EMISIÓN:')
        self.factura.line(x1=20, x2=580, y1=h - 645, y2=h - 645)
        self.factura.drawString(235, h - 655, "DETALLE DE LA FACTURA")

    def dibujar_tabla(self, lista_productos):
        _, h = A4
        centinela = 0
        data = [[' Cod.', '                                           Implemento', 'Cant.', 'Precio', 'Subtotal'],
                ]
        for productos in lista_productos:
            lista = []
            lista.append(str(productos.id))
            lista.append(str(productos.descripcion))
            lista.append(str(productos.cantidad))
            lista.append(str(productos.precio))
            lista.append(str(productos.sub_total))
            data.append(lista)
            centinela = centinela + 20

        table = Table(data, colWidths=[50, 360, 50, 50, 50], )
        table.setStyle(TableStyle(
            [
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ])
        )

        punto_separacion = h - 150 - centinela
        table.wrapOn(self.factura, 100, 100)
        table.drawOn(self.factura, x=20, y=h - 220 - centinela)
        table.drawOn(self.factura, x=20, y=h - 675 - centinela)

        self.factura.drawString(500, punto_separacion - 85, 'Total: ')
        self.factura.drawString(500, punto_separacion - 105, 'Pago: ')
        self.factura.drawString(490, punto_separacion - 125, 'Cambio: ')

        self.factura.drawString(500, punto_separacion - 540, 'Total: ')
        self.factura.drawString(500, punto_separacion - 560, 'Pago: ')
        self.factura.drawString(490, punto_separacion - 580, 'Cambio: ')

        return punto_separacion

    def detalles_factura(self, object):
        obj_factura = object
        punto = self.dibujar_tabla(obj_factura.lista_productos)
        self.crear_esqueleto()
        self.llenar_factura(obj_factura, punto)

    def llenar_factura(self, object, punto):
        w, h = A4
        # self.factura.setFont("Times-Roman", 16)
        # self.factura.setFillColor(red)
        # self.factura.drawString(350, h - 120, str(object.id_factura))
        self.factura.setFont("Times-Roman", 11)
        self.factura.setFillColor(black)
        self.factura.drawString(110, h - 135, str(object.nom_ape_al))
        self.factura.drawString(110, h - 150, str(object.n_c_al))
        self.factura.drawString(110, h - 165, str(object.dir_al))
        self.factura.drawString(110, h - 180, str(object.fecha_creacion))

        self.factura.drawString(540, punto - 85, str(object.total))
        self.factura.drawString(540, punto - 105, str(object.pago))
        self.factura.drawString(540, punto - 125, str(object.cambio))

        # self.factura.setFont("Times-Roman", 16)
        # self.factura.setFillColor(red)
        # self.factura.drawString(350, h - 575, str(object.id_factura))
        # self.factura.setFont("Times-Roman", 11)
        self.factura.setFillColor(black)
        self.factura.drawString(110, h - 590, str(object.nom_ape_al))
        self.factura.drawString(110, h - 605, str(object.n_c_al))
        self.factura.drawString(110, h - 620, str(object.dir_al))
        self.factura.drawString(110, h - 635, str(object.fecha_creacion))

        self.factura.drawString(540, punto - 535, str(object.total))
        self.factura.drawString(540, punto - 555, str(object.pago))
        self.factura.drawString(540, punto - 575, str(object.cambio))

    def save(self):
        self.factura.showPage()
        self.factura.save()

    def __del__(self):
        pass
