from bs4 import BeautifulSoup
import requests
from article import Article

URL = "https://www.schneier.com/feed/atom/"

'''
The class parses the content of the given URL and creates a list of Articles from it.
'''
class Scraper:
    def __init__(self):
        self.page = requests.get(URL)
        self.soup = BeautifulSoup(self.page.text, "xml")

    def get_url(self):
        return URL

    '''
    Cut unnecessary content from the element as less tokens means less cost.
    '''
    def parse_element(self, element: str) -> str:
        # most common html elements
        html_elements = ("<p>", "</p>", "<blockquote>", "</blockquote>", "\n")
        parsed_element = element
        for html_elementselement in html_elements:
            parsed_element = parsed_element.replace(html_elementselement, "")

        return parsed_element

    '''
    Parse the content of the URL and return a list of Articles.
    '''
    def scrape_for_articles(self) -> list[Article]:
        article_list = []
        entries = self.soup.find_all('entry')
        for entry in entries:
            # create an Article and set its attributes
            article = Article()

            bs4_title = entry.find('title')
            article.set_title(str(bs4_title.string))

            bs4_link = entry.find('link')
            href_value = bs4_link.get('href')
            article.set_link(str(href_value))
            
            bs4_content = entry.find('content')
            article.set_content(self.parse_element(str(bs4_content.string)))

            article_list.append(article)
        return article_list