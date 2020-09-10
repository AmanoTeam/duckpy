class ResultDict(dict):
    def __init__(self, title: str, description: str, url: str):
        self.title = title
        self.description = description
        self.url = url
        super().__init__(title=title, description=description, url=url)
