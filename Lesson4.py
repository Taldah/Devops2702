import requests
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver1 = webdriver.Chrome()
import names
repos = requests.get("https://api.github.com/users/avielb/repos")
my_names = []
for i in range(3):
       if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}"
).json()["age"] <= 120:
        my_names.append(i)
uni = requests.get("http://universities.hipolabs.com/search?country=Israel")

driver.get("https://www.ycombinator.com/")
driver1.get("https://hub.docker.com")

#title = driver.find_element(by="title", value="Y Combinator")
assert len(repos.json()) > 5
assert len(my_names) == 0
assert len(uni.json()) > 5
assert driver.title == "Y Combinator"
assert driver1.title == "Docker Hub Container Image Library | App Containerization"
sleep(4)
driver.close()