import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import requests


url ="https://www.bog.gov.gh/treasury-and-the-markets/daily-interbank-fx-rates/"




response = requestsget(url)
soup = BeautifulSoup(url, "html.parser")

print(soup)
