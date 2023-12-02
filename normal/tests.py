from django.test import TestCase
from django.http import JsonResponse

# Import funkcji ping z odpowiedniego modułu
from normal.views import ping

class PingTestCase(TestCase):
  def test_ping_returns_normal_ping(self):
    # Tworzenie obiektu żądania HttpRequest (może być pusty)
    request = self.client.get('/ping/')

    # Wywołanie funkcji ping i przechwycenie odpowiedzi
    response = ping(request)

    # Sprawdzenie, czy otrzymana odpowiedź to JsonResponse
    self.assertIsInstance(response, JsonResponse)

    # Sprawdzenie, czy odpowiedź ma status 200 (OK)
    self.assertEqual(response.status_code, 200)

    # Sprawdzenie, czy treść odpowiedzi to oczekiwany komunikat "Normal Ping"
    self.assertEqual(response.content.decode(), '{"message": "Normal Ping"}')
