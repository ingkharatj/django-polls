from selenium import webdriver
import requests

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """

    browser = webdriver.Chrome('Users\Ing\Downloads\chromedriver')
    browser.get(url)
    links = []
    elements = browser.find_element_by_tag_name('a')
    for url in elements:
        links.append(url.get_attribute('href'))

    browser.close()
    return links

def invalid_urls(urllist):
    invalid_lists = []
    for url in urllist:
        r = requests.head(url)
        if r.status_code == 404:
            invalid_lists.append(url)
    return invalid_lists

def main():
    link = get_links("https://cpske.github.io/ISP/")
    for url in link_list:
        print("Valid: " + url)
    print()
    invalid_url = invalid_urls(link_list)
    for inva_url in invalid_url:
        print("Invalid: " + inva_url)

if __name__ == "__main__":
    link_list = get_links("https://cpske.github.io/ISP/")
    for url in link_list:
        print("Valid: " + url)
    print()
    invalid_url = invalid_urls(link_list)
    for inv_url in invalid_url:
        print("Invalid: " + inv_url)
