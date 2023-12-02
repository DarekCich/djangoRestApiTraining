from django.http import HttpResponse
from protected import helpers as protected_helpers

# Middleware w Django to mechanizm, który pozwala na manipulację 
# żądaniami (requests) i odpowiedziami (responses) serwera Django 
# przed ich przekazaniem widokom (views) aplikacji.

class CustomMiddleware:
    def __init__(self, get_response):
        # Inicjalizacja middleware. 
        # 'get_response' to funkcja, która odbiera żądanie i zwraca odpowiedź.
        self.get_response = get_response

    def __call__(self, request):  
        # Metoda __call__ jest wywoływana przy każdym żądaniu do serwera Django.

        # Sprawdzamy, czy ścieżka żądania zaczyna się od '/protected/'.
        if request.path.startswith('/protected/'):
            # Jeśli tak, sprawdzamy czy token autoryzacyjny jest prawidłowy 
            # za pomocą funkcji 'sprawdz_token' z modułu 'protected_helpers'.
            if not protected_helpers.sprawdz_token(request.META.get('HTTP_AUTHORIZATION')):
                # Jeśli token jest nieprawidłowy, zwracamy odpowiedź HTTP 400
                # (Bad Request) z komunikatem o błędzie.
                return HttpResponse("Nieprawidłowe dane. Wystąpił błąd.", status=400)
            
            # W przeciwnym wypadku (poprawny token), przechodzimy dalej.
            pass

        # Wywołujemy oryginalną funkcję get_response, aby przekazać żądanie 
        # dalej w procesie middleware.
        response = self.get_response(request)
        
        # Zwracamy odpowiedź (response).
        return response
