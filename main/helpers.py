import os
import json
nazwa_pliku = 'users.json'

def sprawdz_imie(imie):
  if not os.path.exists(nazwa_pliku):
      # Tworzenie pustego pliku users.json, jeśli nie istnieje
      with open(nazwa_pliku, 'w') as f:
          json.dump([], f)
          return 0

  with open(nazwa_pliku, 'r') as f:
      dane = json.load(f)
      if imie in dane:
          return 0
      else: 
        return 1
      