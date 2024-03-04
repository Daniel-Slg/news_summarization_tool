import csv 

'''
The History_manager reads the articles from the history.csv file and stores the list of articles for each website in to the history cache. 
The cache and the history storage file are updated when a new article is added. 
'''
class History_manager:
    def __init__(self):
        self.config_file = "history.csv"
        self.fields = ["website", "article"] #add date, add author, etc.
        self.history: dict[str, set] = {} # dictionary of websites with set of articles 
        self.read_history()

    '''
    Add the website as a key to the cache if not there, otherwise add the article to the website set. 
    '''
    def write_to_cache(self, website: str, article: str):
        if website in self.history:
            print("Added Article :", article)
            self.history[website].add(article)
            print(len(self.history[website]))
        else:
            print("Create new Article set :", article)
            self.history[website] = {article}

    '''
    Read the csv data and fill the cache. 
    '''
    def read_history(self):
        self.history = {} # clear the history cache  
        with open(self.config_file, mode = "r", encoding="utf-8") as file:
            csv_file = csv.DictReader(file, fieldnames = self.fields)
            for line in csv_file:
                self.write_to_cache(line["website"], line["article"])
        #self.print_cache()
 
    '''            
    Write the new article into the csv data and the cache. 
    '''
    def write_to_history(self, website: str, new_article: str):
        new_history = {
            "website": website,
            "article": new_article
        }
        # write to history file
        with open(self.config_file, mode = "a", newline="", encoding="utf-8") as file:  #, encoding="utf-8"
            writer = csv.DictWriter(file, fieldnames = self.fields)
            writer.writerows([new_history])
        # update the cache
        self.write_to_cache(website, new_article)

    '''
    Search for an article in the cache. 
    '''
    def find_article(self, website: str, new_article: str) -> bool:
        if website not in self.history:
            return False
        return new_article in self.history[website]

    '''
    Return the cache.
    '''
    def get_history(self) -> list[str]:
        return self.history

    '''
    Print the cache for testing.
    '''
    def print_cache(self):
        print("==================================================================================")
        for website in self.history:
            print(website)
            for article in self.history[website]:
                print(article)