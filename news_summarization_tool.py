from argparse import ArgumentParser
from article import Article
from history_manager import History_manager
from html_writer import Html_writer
import llm_summarizer  
from scraper import Scraper
from utils import Model

'''
Reads the model used for summarizing the articles from the command line and returns the corresponding model enum.
'''
def read_model() -> Model:
    parser = ArgumentParser(
        prog='headlines_publisher',
        description='Reads articles from websites and summarizes them with LLMs')
    parser.add_argument('-m', '--model', choices=['GPT', 'Llama2', 'FalconsAI'], default='GPT')
    args = parser.parse_args()
    return Model.GPT if args.model == 'GPT' else Model.Llama2 if args.model == 'Llama2' else Model.FalconsAI

'''
Main function of the program that reads the articles from the website and summarizes them with the chosen model.
'''
def main():
    # read model from command line argument
    model = read_model()

    # first scrap the website for the arcticles
    scraper = Scraper()
    scraped_article_list: list[Article] = scraper.scrape_for_articles()

    history_manager = History_manager()
    article_list: list[Article] = []
    for article in scraped_article_list:
        # skip articles which have already been processed   
        url = scraper.get_url()
        if history_manager.find_article(url, article.get_title()):
            print("Article already processed ", article.get_title())
            continue

        # store new article title to history
        history_manager.write_to_history(url, article.get_title())
        
        # give GPT the article to summarize and store in article list the result
        article.set_summary(llm_summarizer.create_content_summary(model, article.get_content())) 
        article_list.append(article) #TODO remove comment

    # send the new articles to html_writer to be displayed
    html_writer = Html_writer()
    html_writer.display_articles(article_list)


if __name__ == "__main__":
    main()
