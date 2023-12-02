import os
# Plik asgi.py w Django jest używany do obsługi aplikacji internetowych za pomocą ASGI
# (Asynchronous Server Gateway Interface).
# ASGI jest interfejsem obsługi żądań asynchronicznych w aplikacjach Django,
# pozwalającym na obsługę wielu protokołów komunikacyjnych i typów serwerów, w tym serwerów asynchronicznych.
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_asgi_application()
