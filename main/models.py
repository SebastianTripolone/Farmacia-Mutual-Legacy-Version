# django_website/main/models.py
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
import os

class Empleado (models.Model): 
    JOB_CHOICES =(
        ('Auxiliar', 'Auxiliar'), 
        ('Administrativo', 'Administrativo'),
        ('Farmaceutico', 'Farmaceutico'),
        ('Medico', 'Medico'),
        
    )
    id_Empleado = models.AutoField(primary_key=True)
    nombre= models.CharField ('Nombre',max_length=17)   
    apellido = models.CharField ('Apellido',max_length=50)
    dni= models.IntegerField ('Dni')
    id_usuarios= models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    trabajo= models.CharField('Puesto', max_length=20, choices= JOB_CHOICES)
    nacimiento = models.DateField('Nacimiento')
    id_Direccion = models.ForeignKey('main.direccion', on_delete=models.CASCADE)
    id_Telefonos = models.ForeignKey('main.telefono', on_delete=models.CASCADE)
    fto_Empleado= models.ImageField('Foto de Perfil', upload_to='static/usuarios', null=True,blank=True)
    
    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural='Empleados'
        unique_together=('nombre','apellido','dni')
    
    def __str__(self):
        return self.apellido + ' - ' + self.nombre
    

    

class Paciente (models.Model): 
    id_Paciente = models.AutoField(primary_key=True)
    nombre= models.CharField ('Nombre',max_length=17)   
    apellido = models.CharField ('Apellido',max_length=50)
    dni= models.IntegerField ('Dni')
    nacimiento = models.DateField('Nacimiento')
    id_Direccion = models.ForeignKey('main.direccion', on_delete=models.CASCADE)
    id_Telefonos = models.ForeignKey('main.telefono', on_delete=models.CASCADE)
    fto_Paciente= models.ImageField('Foto de Perfil del Paciente', upload_to='static/usuarios', null=True,blank=True)
    
    class Meta:
        verbose_name= 'Paciente'
        verbose_name_plural='Pacientes'
        unique_together=('nombre','apellido','dni')
    
    def __str__(self):
        return self.nombre + ' - ' + self.apellido 
    
class Proveedor (models.Model): 
    id_Proveedor = models.AutoField(primary_key=True)
    nombre= models.CharField ('Nombre',max_length=17)   
    r_Social = models.CharField ('Razon Social',max_length=50)
    id_Direccion = models.ForeignKey('main.direccion', on_delete=models.CASCADE)
    id_Telefonos = models.ForeignKey('main.telefono', on_delete=models.CASCADE)
    correo= models.CharField ('Correo Electronico',max_length=50)
    fto_proveedor= models.ImageField('Foto de Proveedor', upload_to='static/usuarios', null=True,blank=True)
    
    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural='Proveedores'
        unique_together=('nombre','r_Social','correo')
    
    def __str__(self):
        return self.nombre 

class Laboratorio(models.Model):
    id_Laboratorio=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_Direccion = models.ForeignKey('main.direccion',null=True,blank=True, on_delete=models.CASCADE)
    id_Telefonos = models.ForeignKey('main.telefono',null=True,blank=True, on_delete=models.CASCADE)
    fto_Laboratorio= models.ImageField('Imagen laboratorio', upload_to='static/usuarios', null=True,blank=True)
    
    class Meta:
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'
        unique_together = ('nombre', 'id_Direccion', 'id_Telefonos')

    def __str__(self):
        return self.nombre

class telefono (models.Model):
    id_Telefonos=models.AutoField(primary_key=True)
    numero_Telefono=models.IntegerField ('Numero',null=True)
    numero_Opcional= models.IntegerField ('Numero opcional',null=True)
       
class direccion (models.Model):
    id_Direccion=models.AutoField(primary_key=True)
    calle=models.CharField ('Calle',max_length=50)
    número=models.IntegerField ('Numero')
    piso=models.IntegerField ('N° Piso',null=True)
    departamento=models.CharField ('Departamento',max_length=50,null=True)
    localidad=models.CharField ('Localidad',max_length=50)
    provincia=models.CharField ('Provincia',max_length=50)
    código_Postal=models.IntegerField ('Codigo Postal',null=True)
    
    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
    
    def __str__(self):  
        return self.calle + '-' + self.localidad
    
class Movimiento(models.Model):
    JOB_CHOICES =(
        ('0', 'Ingreso'), 
        ('1', 'Egreso'),    
    )
    
    id_Movimiento = models.AutoField(primary_key=True)
    tipo= models.CharField('Tipo de movimiento', max_length=1, choices= JOB_CHOICES)
    cantidad=models.IntegerField ('Cantidad')
    id_articulo = models.ForeignKey('main.Article', on_delete=models.CASCADE)
    fecha_Caducidad=models.DateField('Fecha de caducidad')
    recetas= models.ImageField('Recetas', null=True,blank=True)
    duplicado = models.ImageField('Duplicado', null=True,blank=True)
    id_Proveedor = models.ForeignKey('main.Proveedor', null=True,blank=True, on_delete=models.CASCADE)
    id_Paciente = models.ForeignKey('main.Paciente',null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' - ' + self.apellido + ' - ' + self.trabajo + '-' 

    def __str__(self):
        return 'Numero de movimiento: {} - Tipo: {} - Producto: {}'.format(
            self.id_Movimiento,
            self.tipo,
            self.id_articulo,
        )


class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.slug), instance)
        return None

    title = models.CharField("Tipo de Producto",max_length=200)
    subtitle = models.CharField("subtitulo", max_length=200, default='', blank=True)
    slug = models.SlugField("Etiqueta", null=False, blank=False, unique=True)
    published = models.DateTimeField('Fecha Publicada', default=timezone.now)
    image = models.ImageField("Imagen", default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None
    
    tipo_choice = (
        ('venta libre', 'Venta Libre'),
        ('bajo receta', 'Bajo Receta'),
        ('bajo receta duplicada', 'Bajo receta duplicado-Lista IV'),
    )

    title = models.CharField("Nombre Comercial", max_length=200)
    id_articulo = models.AutoField(primary_key=True)
    subtitle = models.CharField("Accion Farmatologica",max_length=200, default="", blank=True)
    article_slug = models.SlugField("Codigo de Barra", null=False, blank=False, unique=True)
    id_Laboratorio = models.ForeignKey('main.Laboratorio', on_delete=models.CASCADE)
    principio_activo=models.CharField ('Droga',max_length=17)
    content = RichTextField("Presentacion", blank=True, default='')
    tipo_Producto=models.CharField(choices=tipo_choice, max_length=45)
    notes = RichTextField(blank=True, default='')
    published = models.DateTimeField("Fecha publicada", default=timezone.now)
    modified = models.DateTimeField("Fecha modificada", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    image = models.ImageField("Imagen", default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-published']

    @property
    def stock_actual(self):
        movimientos = Movimiento.objects.filter(id_articulo=self)
        stock = 0
        for movimiento in movimientos:
            if movimiento.tipo == '0':  # Ingreso
                stock += movimiento.cantidad
            elif movimiento.tipo == '1':  # Egreso
                stock -= movimiento.cantidad
        return stock

        