

import json

import pdfplumber
from nltk.tokenize.texttiling import TextTilingTokenizer
import nltk
import os

class BookParsed:
    
    def __init__(self,title,path):
        self.title = title
        self.path = path
        self.pages = dict()
        self.content = ""
    
    def load_pages(self):
        with pdfplumber.open(self.path,unicode_norm='NFD') as pdf:
            for page in pdf.pages:
                number = page.page_number        
                width = page.width
                height = page.height
                bounding_box = (0, height * 0.07, width, height * 0.93)
                cropped_page = page.within_bbox(bounding_box)
                clean_text = cropped_page.extract_text()
                self.pages[number] = clean_text 
            self.content = ", ".join(self.pages.values())
            
    
    def clean_data(self):
        ##whitspaces and lines
        pass
    
            
    
    def split_into_chapters(self):
        tiling_tokenizer = TextTilingTokenizer(w=40, k=20)
        sections = tiling_tokenizer.tokenize(
            self.content
        )
        folder_name = 'chunks'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_path = os.path.join(folder_name, "book_chunks.json")
        with open(file_path, 'w') as f:
            json.dump(sections, f, indent=4)
        return sections
        
    
book = BookParsed("doc",'pdf/mvll.pdf')
book.load_pages()
book.split_into_chapters()


        
        