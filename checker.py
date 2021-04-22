import requests
from bs4 import BeautifulSoup


def check(url_list):
    # This product is no longer available.
    i = 1
    for x in url_list:
        print(str(i))
        i = i + 1
        page = requests.get(x)
        st_code = page.status_code
        if st_code == 404:
            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup)
            alert_text = soup.find('article', {'class': 'alert-danger'})
            if not alert_text:
                print(x)


urls_file = open("urls.txt", "r")
check(urls_file)
