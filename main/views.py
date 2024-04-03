from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .decorators import user_is_authenticated
from .models import Article, ArticleSeries
import random

# Create your views here.
def homepage(request):
      
      articulos= list(Article.objects.all())
      cantidad_articulos_seccion_1 = 4
      cantidad_articulos_seccion_2 = 4
      cantidad_articulos_seccion_3 = 4

      articulos_seccion_1 = random.sample(list(articulos), min(cantidad_articulos_seccion_1, len(articulos)))
      articulos_seccion_2 = random.sample(list(articulos), min(cantidad_articulos_seccion_2, len(articulos)))
      articulos_seccion_3 = random.sample(list(articulos), min(cantidad_articulos_seccion_3, len(articulos)))

      return render(request, 'main/home.html', {
        'articulos_seccion_1': articulos_seccion_1,
        'articulos_seccion_2': articulos_seccion_2,
        'articulos_seccion_3': articulos_seccion_3
    })

def acercade(request):
    
    return render(
        request=request,
        template_name='main/acercade.html'
    )

def productos(request):
    matching_series = ArticleSeries.objects.all()
    
    return render(
        request=request,
        template_name='main/productos.html',
        context={
            "objects": matching_series,
            "type": "series"
        } )


def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()

    return render(
        request=request,
        template_name='main/productos.html',
        context={
            "objects": matching_series,
            "type": "article"
            })

@user_is_authenticated
def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article}
                  )

def new_series(request):
    return redirect('/')

def new_post(request):
    return redirect('/')

def series_update(request, series):
    return redirect('/')

def series_delete(request, series):
    return redirect('/')

def article_update(request, series, article):
    return redirect('/')

def article_delete(request, series, article):
    return redirect('/')
# Create your views here.
