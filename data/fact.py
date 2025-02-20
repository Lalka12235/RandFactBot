import requests
import bs4 

url = 'https://randstuff.ru/fact/'


def get_fact():
    response = requests.get(url)


    soup = bs4.BeautifulSoup(response.text, 'lxml')

    content = soup.find('table', class_ ='text').text

    return content


if __name__ == '__main__':
    get_fact()