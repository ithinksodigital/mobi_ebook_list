# -*- coding: utf8 -*-
from mobi import Mobi
import os
from save_file import Files
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    r = ReadEbook()
    r.read_file("/ebook_list.txt")
    return render_template('index.html', list = r.list)



class ReadEbook:
    def read_file(self, file_to_read):
        self.list = []
        self.file_to_read = file_to_read
        self.file = open(file_to_read, 'r')

        for i in self.file.readlines():
            self.list.append(i)
            self.list.sort()

        return self.list




if __name__ == '__main__':
    app.run()