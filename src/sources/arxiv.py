import bs4
import requests
import os
from src.contents import Content, ContentItem
from src.utils import llm, rag


class ArxivContentItem(ContentItem):
    def __init__(self, title, content, url):
        super().__init__(title, content, url)

    def llm_summarize(self):
        self.content = llm.summarize(self.content)


def fetch(category: str) -> Content:
    assert category is not None
    content = Content("arxiv " + category)
    html = requests.get("https://papers.cool/arxiv/" + category).text
    soup = bs4.BeautifulSoup(html, "html.parser")
    papers_div = soup.html.body.div
    papers = [papers_div.contents[i] for i in range(1, len(papers_div.contents) - 1, 2)]
    papers = papers[:10 if len(papers) > 10 else len(papers)]
    # for paper in papers:
    #     res = requests.get("https://papers.cool/arxiv/star", {"key": "kimi", "paper": paper["id"]})
    for paper in papers:
        # res = requests.get("https://papers.cool/arxiv/kimi", {"paper": paper["id"]})
        # print(str(paper["id"])+res.text[:20 if len(papers) > 20 else len(papers)])
        title = paper.h2.contents[3].get_text()
        url = paper.h2.contents[1]["href"]
        filename = paper["id"] + ".pdf"
        if not os.path.exists("temp/"):
            os.mkdir("temp/")
        # try:
        if not os.path.exists("temp/" + filename):
            res = requests.get("https://arxiv.org/pdf/" + filename)
            assert res.status_code == 200
            f = open("temp/" + filename,"wb")
            f.write(res.content)
            f.close()
        content.append(ArxivContentItem(title=title,
                                        content=rag.summarize_paper(filename),
                                        url=url))
        # except Exception as e:
        #     print(e)

    return content
