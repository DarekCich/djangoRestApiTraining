# Plik wsgi.py w Django jest wykorzystywany do obsługi aplikacji internetowych
# za pomocą WSGI (Web Server Gateway Interface). WSGI to standardowy interfejs
# komunikacyjny między aplikacją internetową napisaną w języku Python a serwerem internetowym.
# Służy do obługi żądań synchronicznych
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()
