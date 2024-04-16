import json


class ContentItem:
    def __init__(self, title, content, url):
        self.title = title
        self.content = content
        self.url = url

    def __repr__(self):
        return str({"title": self.title, "content": self.content, "url": self.url})


class Content:
    def __init__(self, name: str):
        self.contents: list[ContentItem] = []
        self.name = name

    def __repr__(self):
        return json.dumps([str(i) for i in self.contents], ensure_ascii=False)

    def append(self, item: ContentItem) -> None:
        self.contents.append(item)

    def get(self, index: int = None) -> list | ContentItem:
        if index:
            return self.contents[index]
        else:
            return self.contents

    def length(self) -> int:
        return len(self.contents)
