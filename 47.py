import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("https:\\ffs\fgss")
except InvalidURL:
     print("Invalid url was given")
