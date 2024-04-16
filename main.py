from datetime import datetime

from dotenv import load_dotenv
from md2pdf.core import md2pdf

load_dotenv()
from src.sources import github_trending, hacker_news, arxiv

markdown_file = open("temp/result.md", "w", encoding="utf-8")
time = datetime.now().strftime("%Y年%m月%d日")
markdown_file.write(f"# {time}\n\n")
contents = [github_trending.fetch(), hacker_news.fetch(), arxiv.fetch("cs.CV")]
for i in contents:
    markdown_file.write(f"## {i.name}\n\n")
    for j in i.contents:
        if hasattr(j, "llm_summarize"):
            j.llm_summarize()
        markdown_file.write(f"### [{j.title}]({j.url})\n{j.content}\n\n")
md2pdf(pdf_file_path="temp/result.pdf", md_file_path="temp/result.md")
# print(contents)
