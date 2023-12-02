from django.http import JsonResponse

# Funkcja widoku 'ping'.
# Widok to funkcja lub klasa, która przyjmuje żądanie HTTP i zwraca odpowiedź HTTP.
def ping(request):
    return JsonResponse({"messege": "Zabezpieczony Ping"}, status=200)
