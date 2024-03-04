from bs4 import BeautifulSoup
from article import Article

MAX_DISPLAYED = 10

'''
The Hthml_writer creates the content of the html file.
'''
class Html_writer:
    def __init__(self):
        self.html_path = "summary_result.html"

    '''
    Write the amount of MAX_DISPLAYED from the given articles list into the html file. 
    If less then MAX_DISPLAYED are given, add old articles untill the limit MAX_DISPLAYED is reached.   
    '''
    def display_articles(self, articles: list[Article]):
        displayed_articles = self.read_articles()
        # append the displayed articles at the end of the new articles 
        articles.extend(displayed_articles)
        # limit the number of articles to MAX_DISPLAYED
        if len(articles) > MAX_DISPLAYED:
            over_limit = len(articles) - MAX_DISPLAYED
            del articles[-over_limit:]

        # write the new content on the html 
        with open(self.html_path, "w", encoding="utf-8") as file:
            file.write('<html>\n<head>\n<meta charset="utf-8">\n<h1>Cybersecurity News</h1>\n</head>\n<body>\n')
            for article in articles:
                file.write('<div>\n')
                file.write(f'<h2>{article.get_title()}</h2>\n')
                file.write('<content>\n')
                file.write(f'<p>{article.get_summary()}</p>\n')
                file.write('</content>\n')
                file.write(f'<a href={article.get_link()}>Read More</a>\n') 
                file.write('</div>\n')
            file.write("</body>\n</html>")
    
    '''
    Reads and returns the existing articles from the html.    
    '''
    def read_articles(self) -> list[Article]:
        displayed_articles: list[Article] = []
        zipped_articles: list[tuple] = []

        with open(self.html_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            titles = soup.find_all("h2")
            contents = soup.find_all("content")
            links = soup.find_all("a")
            #get the strings of the result set into a list
            titles_list = [title.get_text() for title in titles] 
            content_list = [content.get_text().strip() for content in contents]
            links_list = [link.get('href') for link in links]
            zipped_articles = zip(titles_list, content_list, links_list)

        for zipped_article in zipped_articles:
            article = Article()
            article.set_title(zipped_article[0])
            article.set_summary(zipped_article[1])
            article.set_link(zipped_article[2])
            displayed_articles.append(article)

        return displayed_articles
       
            
            
        
