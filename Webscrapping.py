# EXAMPLE

from bs4 import BeautifulSoup
import requests, openpyxl

# excel = openpyxl.Workbook()
# sheet = excel.active
# sheet.title = 'Bikes'
# sheet.append(['bikes','Methodology','revenue'])

try:
    response = requests.get('https://www.mbaskool.com/business-lists/top-brands/17638-top-10-bike-companies-in-world.html')
    soup = BeautifulSoup(response.text,'html.parser')
    
    bike_name = soup.find_all('h3')
    new = soup.find_all('h2')
    revenue = soup.find_all('strong')

    for list_name in bike_name:
        data = list_name.text

        for news in new:
            data2 = news.text

            for rev in revenue:
                data3 = rev.text.split('(million $)')
                data3 = rev.text.replace('[]'," ")
                # print(data,data2,data3)
                # sheet.append([data,data2,data3])

except Exception as e:
    print(e)

# excel.save('bikes.xlsx')



# EXAMPLE 2
from bs4 import BeautifulSoup
import requests, openpyxl

try:
    response = requests.get("https://www.magicbricks.com/blog/top-7-affordable-localities-to-live-in-bangalore/120115.html")
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the 'ul' element with class 'tablofCntnt__listWrapper'
    list_wrapper = soup.find('ul', class_="tablofCntnt__listWrapper")

    if list_wrapper:
        # Find all 'li' elements with class 'tablofCntnt__list' within the 'ul'
        places = list_wrapper.find_all("li", class_="tablofCntnt__list")

        for place in places:
            # Find the 'a' element within the 'li' and get its text
            place_name = place.a.text
            print(place_name)
    else:
        print("List wrapper not found on the page.")
except Exception as e:
    print(e)

#EXAMPLE 3

from bs4 import BeautifulSoup
import requests

try:
    response = requests.get("https://www.mbaskool.com/business-lists/top-brands/17638-top-10-bike-companies-in-world.html")
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the elements you want to scrape based on the HTML structure
    elements = soup.find_all('h3')

    for element in elements:
        # Extract the data you need from the 'element'
        data = element.text
        print(data)
except Exception as e:
    print(e)

#EXAMPLE 4

from bs4 import BeautifulSoup
import requests

try:
    response = requests.get("https://www.caranddriver.com/features/a42187877/10best-cars-2023/")
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the elements you want to scrape based on the HTML structure
    elements = soup.find_all('h2', attrs={"data-node-id": True, "class": "body-h2 css-mu4ig0 et3p2gv0"})

    for element in elements:
        # Extract the data you need from the 'element'
        data = element.text
        print(data)
except Exception as e:
    print(e)

#EXAMPLE 5

from bs4 import BeautifulSoup
import requests

try:
    response = requests.get("https://www.caranddriver.com/features/a42187877/10best-cars-2023/")
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the elements you want to scrape based on the HTML structure
    elements = soup.find_all('h2', class_="css-mu4ig0 et3p2gv0")

    for element in elements:
        # Extract the data you need from the 'element'
        data = element.text
        print(data)
except Exception as e:
    print(e)