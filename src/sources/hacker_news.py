import requests
from bs4 import BeautifulSoup

from src.contents import ContentItem, Content
from src.utils import feed, llm


class HackerNewsContentItem(ContentItem):
    def __init__(self, title, content, url):
        super().__init__(title, content, url)

    def llm_summarize(self):
        self.content = llm.summarize(self.content)


def fetch() -> Content:
    rss_content = feed.parse_rss("https://news.ycombinator.com/rss")
    content = Content("Hacker News")
    for item in rss_content.channel.items:
        link = item.link.content
        item_content = get_content(link)
        content.append(HackerNewsContentItem(item.title.content, item_content, link))
    return content


def get_content(url: str) -> str:
    res = requests.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    for data in soup(["style", "script", "svg"]):
        data.decompose()
    return " ".join(soup.stripped_strings)
