import requests
import pandas
import html
from bs4 import BeautifulSoup



def main():
    # your code here
    
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    page = requests.get(url)
    
    print(page.content)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("td").text
    print(soup.prettify())
    print("---------------")
    print(soup.tr)
    


if __name__ == '__main__':
    main()



