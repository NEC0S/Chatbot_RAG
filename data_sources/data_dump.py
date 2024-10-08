from .pdf_handler import PDFHandler
from .url_handler import URLHandler
from .text_handler import TextHandler

class DataDump:
    def __init__(self):
        self.pdf_handler = PDFHandler()
        self.url_handler = URLHandler()
        self.text_handler = TextHandler()

    def load_data(self):
        docs = []
        docs.extend(self.pdf_handler.load_pdfs())
        docs.extend(self.url_handler.load_urls())
        docs.extend(self.text_handler.load_texts())
        return docs
