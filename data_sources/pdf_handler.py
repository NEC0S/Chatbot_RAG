import PyPDF2
from llama_index.core import Document

class PDFHandler:
    def load_pdfs(self):
        pdf_files = [
            r'C:\Users\Abhishek\Documents\NogTech\Model_Card_Claude_3.pdf'
        ]
        docs = []
        for pdf_file in pdf_files:
            with open(pdf_file, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text()
                docs.append(Document(text=text, metadata={"source": pdf_file}))
        return docs
