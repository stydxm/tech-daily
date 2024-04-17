import base64

import requests

from src.contents import Content, ContentItem
from src.utils import feed, llm


class GithubTrendingContentItem(ContentItem):
    def __init__(self, title, content, url):
        super().__init__(title, content, url)
        self.content = get_readme(self.title)

    def llm_summarize(self):
        if len(self.content) > 15000:
            self.content = self.content[:15000]
        self.content = llm.project_summarize(self.content)


def fetch(date_range: str = "daily") -> Content:
    assert date_range in ["daily", "weekly", "monthly"]
    rss_content = feed.parse_rss(f"https://rsshub.app/github/trending/{date_range}/any")
    content = Content("GitHub Trending")
    for item in rss_content.channel.items:
        content.append(GithubTrendingContentItem(title=item.title.content,
                                                 content=item.description.content,
                                                 url=item.link.content))
    return content


def get_readme(project_path: str) -> str:
    response = requests.get(f"https://api.github.com/repos/{project_path}/contents/README.md").json()
    readme = base64.b64decode(response["content"]).decode()
    if len(readme) > 15000:
        readme = readme[:15000]
    return readme
