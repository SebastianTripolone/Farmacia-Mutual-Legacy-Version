from django.contrib import admin
from datetime import date
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from django.utils.html import format_html
from reportlab.pdfbase.ttfonts import TTFont
from .models import Article, ArticleSeries, Empleado, Proveedor, Paciente, telefono, direccion, Laboratorio, Movimiento
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = ['title', 'subtitle', 'slug', 'published', 'image',]

class ArticleResources(resources.ModelResource):
    class Meta:
        model = Article
        fieldsets = [
        ("Informacion", {'fields': ["title", "subtitle", "id_Laboratorio", "tipo_Producto" , "article_slug" , "series", "image"]}),
        ("Presentacion", {"fields": ["content"]}),
        ("Fecha", {"fields": ["modified"]})
    ]

        clean_model_instances = True
        export_order = ["title", "subtitle", "article_slug", "series"]

class ArticleAdmin(ImportExportModelAdmin):
    fieldsets = [
        ("Informacion", {'fields': ["title", "subtitle", "principio_activo" ,"article_slug" ,  "tipo_Producto" , "id_Laboratorio", "series", "image"]}),
        ("Presentacion", {"fields": ["content"]}),
        ("Fecha", {"fields": ["modified"]})
    ]

    list_display=(
    'title',
    'stock_actual'
    )


class EmpleadoAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido',
        'dni',
        'calcularEdad',
        'foto_del_empleado'
    )
    
    def foto_del_empleado(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.fto_Empleado.url))
    
    def export_selected_to_pdf(modeladmin, request, queryset):
     
         response = HttpResponse(content_type='application/pdf')
         response['Content-Disposition'] = 'attachment; filename="Empleados.pdf"'

         p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

         pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
         pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
         
         p.setFont("Arial-Bold", 12)
         p.drawString(100, 750, "Listas de empleados")
         p.setFont("Arial", 12)
         y = 720
         for item in queryset:
            p.drawString(120, y, f"Empleado: {item.id_Empleado}")
            p.drawString(120, y - 20, f"Nombre: {item.nombre}")
            p.drawString(120, y - 40, f"Apellido: {item.apellido}")
            p.drawString(120, y - 60, f"Dni: {item.dni}")
            p.drawString(120, y - 80, f"Trabajo: {item.trabajo}")
            y -= 120
         p.showPage()
         p.save()
         return response

    export_selected_to_pdf.short_description = "Exportar Empleados seleccionados a PDF"
    actions = [export_selected_to_pdf]
    
    def calcularEdad(self,obj):
        today= date.today()
        age= today.year-obj.nacimiento.year-((today.month, today.day)<(obj.nacimiento.month, obj.nacimiento.day))
        return age
    
    calcularEdad.short_description='Edad'
    
    list_filter=(
        'nombre',
        'apellido',
        'trabajo'
        
    )   
    
    search_fields=(
        'nombre',
        'apellido',
        'trabajo',
        'dni'
    )
    
class ProveedorAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
        'foto_del_proveedor'
        
    )
    
    def foto_del_proveedor(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.fto_proveedor.url))

    list_filter=(
        'nombre',
    )   

class LaboratorioAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
        'foto_del_laboratorio'
    )
        
    def foto_del_laboratorio(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.fto_Laboratorio.url))

    list_filter=(
        'nombre',
    )   

class PacienteAdmin (admin.ModelAdmin):
    list_display=(
        'nombre',
        'apellido',
        'dni',
        'calcularEdad',
        'foto_del_paciente'
    )
    
    def foto_del_paciente(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.fto_Paciente.url))
    
    list_filter=(
        'nombre',
        'apellido',
        
    )
    
    search_fields=(
        'nombre',
        'apellido',
        'dni'
    )
    
    def calcularEdad(self,obj):
        today= date.today()
        age= today.year-obj.nacimiento.year-((today.month, today.day)<(obj.nacimiento.month, obj.nacimiento.day))
        return age
    
    calcularEdad.short_description='Edad'
    
    def export_selected_to_pdf(modeladmin, request, queryset):
     
         response = HttpResponse(content_type='application/pdf')
         response['Content-Disposition'] = 'attachment; filename="Pacientes.pdf"'

         p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

         pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
         pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
         
         p.setFont("Arial-Bold", 12)
         p.drawString(100, 750, "Listas de pacientes")
         p.setFont("Arial", 12)
         y = 720
         for item in queryset:
            p.drawString(120, y, f"Paciente: {item.id_Paciente}")
            p.drawString(120, y - 20, f"Nombre: {item.nombre}")
            p.drawString(120, y - 40, f"Apellido: {item.apellido}")
            p.drawString(120, y - 60, f"Dni: {item.dni}")
            p.drawString(120, y - 80, f"Fecha de nacimiento: {item.nacimiento}")
            y -= 120
         p.showPage()
         p.save()
         return response

    export_selected_to_pdf.short_description = "Exportar Pacientes seleccionados a PDF"
    actions = [export_selected_to_pdf]

class MovimientoAdmin (admin.ModelAdmin):
    list_display=(
        'tipo',
        'cantidad',
        )
    list_filter=(
        'tipo',
        'cantidad'
    )   
    search_fields=(
        'tipo',
        'cantidad',
    ) 
    
    def export_selected_to_pdf(modeladmin, request, queryset):
     
         response = HttpResponse(content_type='application/pdf')
         response['Content-Disposition'] = 'attachment; filename="Movimientos.pdf"'

         p = canvas.Canvas(response, pagesize=(595, 842))  # Tamaño A4

         pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
         pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
         
         p.setFont("Arial-Bold", 12)
         p.drawString(100, 750, "Listas de movimientos")
         p.setFont("Arial", 12)
         y = 720
         for item in queryset:
            p.drawString(120, y, f"Movimiento: {item.id_Movimiento}")
            p.drawString(120, y - 20, f"Tipo: {item.tipo}")
            p.drawString(120, y - 40, f"Producto: {item.id_articulo}")
            p.drawString(120, y - 60, f"Paciente: {item.id_Paciente}")
            y -= 120
         p.showPage()
         p.save()
         return response

    export_selected_to_pdf.short_description = "Exportar Movimientos seleccionados a PDF"
    actions = [export_selected_to_pdf]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Laboratorio,LaboratorioAdmin)
admin.site.register(telefono)
admin.site.register(direccion)
admin.site.register(Movimiento,MovimientoAdmin)