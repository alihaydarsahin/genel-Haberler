import requests
import pandas as pd

# News API URL ve API anahtarınız
url = "https://newsapi.org/v2/top-headlines"
api_key = "Haber sitesinden api key aldım"  # API anahtarınızı buraya girin

# İlgili kategoriler
related_categories = ['technology', 'science', 'health', 'business', 'entertainment']

# Her kategori için veri saklamak için bir liste
selected_articles = []

# Her kategori için istek gönder
for category in related_categories:
    params = {
        'category': category,
        'country': 'us',
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = [{
            "title": article['title'],
            "date": article['publishedAt'],
            "summary": article['description'],
            "url": article['url'],
            "category": category  # Kategoriyi ekliyoruz
        } for article in data['articles']]
        
        selected_articles.extend(articles)
    else:
        print(f"{category} kategorisi için API isteği başarısız oldu:", response.status_code)

# Tüm haberleri DataFrame'e aktar
df = pd.DataFrame(selected_articles)

# CSV'ye kaydet
df.to_csv("related_categories_news.csv", index=False)
print("İlişkili kategorilerdeki haberler CSV dosyasına kaydedildi.")
