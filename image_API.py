import requests
import os

# API-Zugriffsschlüssel
API_KEY = 'HIER EINSETZEN'

# Suchbegriff für Kaninchen
query = 'feldhase'

# Anzahl der Bilder, die du herunterladen möchtest
num_images = 50

# API-Anfrage senden
url = f'https://pixabay.com/api/?key={API_KEY}&q={query}&per_page={num_images}'
response = requests.get(url)
data = response.json()

# Bilder herunterladen
for i, hit in enumerate(data['hits']):
    img_url = hit['largeImageURL']
    img_data = requests.get(img_url).content
    with open(f'rabbit_{i}.jpg', 'wb') as f:
        f.write(img_data)