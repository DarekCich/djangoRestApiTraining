from django.urls import path
from protected   import views

# Lista wzorców adresów URL dla aplikacji Django.
# Wzorzec adresu URL to definicja ścieżki URL oraz funkcji widoku,
# która ma być wywoływana w przypadku dopasowania danego żądania.

urlpatterns = [
    # Definicja ścieżki URL dla endpointu '/ping/'.
    # Gdy żądanie dotrze na adres '/ping/', zostanie wykonana funkcja widoku 'views.ping'.
    # Adres '/ping/' jest względny i należy do wzorca adresu URL aplikacji.
    path('ping/', views.ping),
]
