from django.http import JsonResponse
from normal      import helpers as normal_helpers
import json

# Widok 'ping' zwraca odpowiedź typu JsonResponse dla zapytania GET '/ping/'.
def ping(request):
    return JsonResponse({"message": "Normal Ping"}, status=200)

# Widok 'users' obsługuje zapytania POST i PUT na '/users/'.
def users(request):
    # Parsowanie danych JSON z ciała żądania
    json_data = json.loads(request.body)

    # Sprawdzenie, czy 'imie' znajduje się w danych żądania
    if 'imie' not in json_data:
        return JsonResponse({"message": "Niepoprawne dane zapytania"}, status=400)

    # Obsługa różnych metod HTTP: POST i PUT
    if request.method == 'POST':
        return normal_helpers.logowanie(json_data)  # Wywołanie funkcji logowanie z pliku hepleprs
    elif request.method == 'PUT':
        return normal_helpers.rejestracja(json_data)  # Wywołanie funkcji rejestracja z pomocnika
    else:
        return JsonResponse({"message": "Niepoprawna metoda"}, status=400)
