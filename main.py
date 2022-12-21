import requests
from send_email import send_email

topic = "google"
api_key = "fd6fe4868dd048bba71677d1188d3084"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&sortBy=publishedAt" \
      "&apiKey=fd6fe4868dd048bba71677d1188d3084" \
      "&language=en"

request = requests.get(url)

# Gets a dictionary with data for NewsAPI
content = request.json()

# Access the articles titles and description
body = ""
for article in content["articles"][:25]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" + body + article["title"] \
               + "\n" + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
