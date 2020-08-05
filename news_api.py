import requests

response = requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-01&sortBy=publishedAt&apiKey=2dc1ba1b0b604a4881004c7548977742")

data = response.json()

articles = data["articles"]

for i in articles:
    print(i["title"])
    print()