import jwt
from datetime import datetime
from main import settings, helpers as main_helpers

# Moduł helpers służy do obsługi różnych funkcji pomocniczych związanych z JWT i aplikacją.

# Funkcja sprawdzająca poprawność tokenu JWT.
# Sprawdza, czy token jest poprawny, czy nie wygasł i czy użytkownik istnieje.
def sprawdz_token(token):
    try:
        # Weryfikacja i dekodowanie tokenu JWT
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        # Pobranie danych z tokenu (np. dane użytkownika)
        user_data = decoded_token.get('user')

        # Sprawdzenie czy token nie wygasł
        token_exp = decoded_token.get('exp')
        if datetime.utcnow() > datetime.utcfromtimestamp(token_exp):
            return False  # Token wygasł

        # Sprawdzenie czy użytkownik istnieje w bazie danych
        x = main_helpers.sprawdz_imie(user_data['imie'])
        if x != 0:
            return False  # Użytkownik nie istnieje

        # Walidacja przeszła pomyślnie
        return True

    except jwt.ExpiredSignatureError:
        return False  # Wygasły token

    except jwt.InvalidTokenError:
        return False  # Nieprawidłowy token lub niepowodzenie w dekodowaniu
