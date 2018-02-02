# Import package
import requests
from bs4 import BeautifulSoup

# Specify the url: url
url = "https://afternoonnaps.github.io"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

#Create BS Object
soup = BeautifulSoup(text)

# Print the html
print(soup.prettify())