from bs4 import BeautifulSoup as bs
import requests
## Helper Function ##

def get_infobox_data(link):
    '''
    Given a article link, extract data from the infobox into a dictionary.
    Expexted return:
    {'Date': 'July 21, 1919',
     'Destination': 'White City amusement park, Chicago, Illinois',
     'Fatalities': '13 (2 passengers, 1 crew, 10 on ground)',
     'Flight origin': 'Grant Park, Chicago, Illinois',
     'Name': 'Goodyear dirigible Wingfoot Air Express catches fire and crashes',
     'Operator': 'Goodyear Tire and Rubber Company'}
    '''

    return data_dict


# Prepare soup
base = 'https://en.wikipedia.org'
path = '/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft'
response = requests.get(base + path)
soup = bs(response.text, 'html.parser')

# Identify all of the accident links.
#bolds = soup.find_all('b')
bolds = soup.find_all('b')[:-1]
counter = 0
for b in bolds:
    link = b.find('a')
    if link == None:
        print("################it does not have link, skip####################")
    else:
        print(link.encode(errors="ignore"))
        print(link.attrs['href'].encode(errors="ignore"))
        print(link.attrs['title'].encode(errors="ignore"))
        # print(link.text.encode(errors="ignore"))
