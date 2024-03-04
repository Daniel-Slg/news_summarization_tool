'''
Class that describes the article structure. 
'''
class Article:
    def __init__(self):
        self.title = ""
        self.summary = ""
        self.content = "" 
        self.link = ""
        self.result = ""

    def get_title(self) -> str:
        return self.title
    
    def get_summary(self) -> str:
        return self.summary

    def get_content(self) -> str:
        return self.content
    
    def get_link(self) -> str:
        return self.link
        
    def set_title(self, title: str) -> None:
        self.title = title

    def set_summary(self, summary: str) -> None:
        self.summary = summary

    def set_content(self, content: str) -> None:
        self.content = content

    def set_link(self, link: str) -> None:
        self.link = link

    def print_article(self) -> None:
        print(f"Title: {self.title} Link: {self.link} Summary: {self.summary} Content: {self.content}" )
