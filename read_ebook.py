# -*- coding: utf8 -*-
from mobi import Mobi
from save_file import Files
import os

class ListEbook():
    def __init__(self, path):
        self.path = path
        files = []
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.mobi' in file:
                    files.append(os.path.join(r, file))


        for f in files:
            book = Mobi(f)
            book.parse()
            try:
                title = book.title()
                author = book.author()

                author = author.decode()
                title = title.decode()

                result = author + ' - ' + title + "\n"
                print(result)

                w = Files()
                w.save_file(result)


            except:
                print("pass", f)


l = ListEbook("path/to/mobi")
