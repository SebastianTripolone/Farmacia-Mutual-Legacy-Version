from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse

def user_is_authenticated(function=None, redirect_url='login'):
    """
    los decorators sirven para que podamos ver si el usuario esta autorizado para acceder a dicha vista
    y este mande un mensaje de error cuando no esta registrado redireccionando a la pagina principal
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, "Inicie Sesion antes de comprar el producto")
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator