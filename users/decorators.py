from django.shortcuts import redirect

def user_not_authenticated(function=None, redirect_url='/'):
    """
    este decorator sirve para saber si el usuario no esta registrado, redireccionando a la pagina principal
    si es necesario por defecto
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator