from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.onrender.com', 'localhost']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LANGUAGE_CODE = 'es-ar'

TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 100,
    'selector': 'textarea',
    "menubar": "file edit view insert format tools table help",
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'undo redo | backcolor casechange permanentpen formatpainter removeformat formatselect fontselect fontsizeselect',
    'toolbar2': 'bold italic underline blockquote | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code | tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry',
    'contextmenu': 'formats | link image',
    'block_formats': 'Paragraph=p; Header 1=h1; Header 2=h2',
    'fontsize_formats': "8pt 10pt 12pt 14pt 16pt 18pt",
    'content_style': "body { font-family: Arial; background: white; color: black; font-size: 12pt}",
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'}, {'text': 'HTML/XML', 'value': 'markup'},],
    'image_class_list': [{'title': 'Fluid', 'value': 'img-fluid', 'style': {} }],
    'width': 'auto',
    "height": "600px",
    'image_caption': True,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 5

SOCIALACCOUNT_LOGIN_ON_GET=True


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': '881839903286-cb5hkvklgaingt8sf4g8ee7oqq37fr0s.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}



LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = [
    'users.backends.EmailBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
    ]

RECAPTCHA_PUBLIC_KEY = '6Ld17_UnAAAAAEOu6bLgk3UvbONdbIUD7aTg9fUc'
RECAPTCHA_PRIVATE_KEY = '6Ld17_UnAAAAAOWs0zTT-UxMYONIZ9Eo4vdUM1aG'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'itechproject232@gmail.com'
EMAIL_HOST_USER = 'itechproject232@gmail.com'
EMAIL_HOST_PASSWORD = 'qiwequrtchyncciw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 14400


CKEDITOR_UPLOAD_PATH= "uploads/"
CKEDITOR_IMAGE_BACKEND= "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 300,
    },
}

JAZZMIN_SETTINGS = {
    "site_logo": "logo2.jpeg",
    "login_logo": "logo2.jpeg",
    "site_icon": "logo2.jpeg", 
    "site_title": "Farmacia Mutual",
    "site_header": "Farmacia Mutual",
    "site_brand": "Farmacia Mutual",
    "welcome_sign": "Bienvenido a la Farmacia Mutual",
    "order_with_respect_to": ["auth.user", "auth.Group", "main.Article", "main.Series"],
    "show_ui_builder": False,
    "topmenu_links": [
        {"name": "Soporte","url": "http://superiorlapaz.edu.ar/", "new_window": True}, 
    ],
    "icons":{
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "main.direccion":"fas fa-address-card",
        "main.Empleado": "fas fa-user",
        "main.Paciente": "fas fa-hospital-user",
        "main.Proveedor": "fas fa-users",
        "main.Laboratorio":"far fa-building",
        "main.telefono": "fas fa-phone",
        "main.Movimiento": "fas fa-chevron-circle-right",
        "main.Article":"fas fa-pills",
        "main.ArticleSeries":"fas fa-medkit",
        "users.CustomUser":"fas fa-user",
        "django.site":"fas fa-globe"

    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}