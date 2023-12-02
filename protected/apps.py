from django.apps import AppConfig

# Klasa konfiguracyjna aplikacji Protected.
# AppConfig to klasa bazowa w Django służąca do konfiguracji aplikacji.

class ProtectedConfig(AppConfig):
    # Pole default_auto_field
    # Określa, który pole zostanie użyte jako klucz główny (primary key) 
    # w przypadku automatycznie generowanych pól (np. w modelach).
    default_auto_field = 'django.db.models.BigAutoField'

    # Pole name
    # Określa nazwę aplikacji.
    name = 'protected'
