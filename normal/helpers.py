from django.http import JsonResponse
from django.conf import settings
from datetime    import datetime, timedelta
from main        import helpers as main_helpers
import jwt, json

# Nazwa pliku, w którym przechowywane są dane użytkowników
nazwa_pliku = 'users.json'

# Funkcja do logowania użytkownika
def logowanie(dane):
    # Sprawdzenie, czy użytkownik istnieje
    x = main_helpers.sprawdz_imie(dane['imie'])
    if x != 0:
        return JsonResponse(
            {"message": "Użytkownik o tej nazwie nie istnieje."},
            status=401
        )

    # Generowanie tokena JWT dla istniejącego użytkownika
    tokenJWT = generuj_token(dane['imie'])
    return JsonResponse(
        {
            "message": "Użytkownik o tej nazwie już istnieje.",
            "tokenJWT": tokenJWT
        },
        status=200
    )

# Funkcja do rejestracji użytkownika
def rejestracja(dane):
    # Sprawdzenie, czy użytkownik już istnieje
    x = main_helpers.sprawdz_imie(dane['imie'])
    if x == 0:
        return JsonResponse(
            {"message": "Użytkownik o tej nazwie już istnieje."},
            status=409
        )

    # Dodanie nowego użytkownika
    dodaj_imie(dane['imie'])
    return JsonResponse(
        {"message": "Dodano użytkownika."},
        status=201
    )

# Funkcja dodająca imię użytkownika do pliku 'users.json'
def dodaj_imie(imie):
    with open(nazwa_pliku, 'r') as f:
        dane = json.load(f)
        dane.append(imie)
        with open(nazwa_pliku, 'w') as f:
            json.dump(dane, f)

# Tokeny JWT

# Funkcja generująca token JWT na podstawie imienia użytkownika
def generuj_token(imie):
    # Dane użytkownika używane do wygenerowania tokenu
    user_data = {
        'user_id': 123,
        'imie': imie,
        'role': 'user'
    }

    # Ustalenie daty wygaśnięcia tokena (np. za 1 minutę)
    expiration_date = datetime.utcnow() + timedelta(minutes=1)

    # Tworzenie tokena JWT
    token = jwt.encode(
        {
            'user': user_data,
            'exp': expiration_date
        },
        settings.SECRET_KEY,
        algorithm='HS256'
    )

    return token
