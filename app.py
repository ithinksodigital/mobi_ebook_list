# -*- coding: utf8 -*-
from mobi import Mobi
import os
from save_file import Files
from flask import Flask, request, render_template
from flask import send_file


app = Flask(__name__)

@app.route('/')
def my_form():
    r = ReadEbook()
    r.read_file("ebook_list.txt")
    return render_template('index.html', list = r.list)



@app.route('/', methods=['POST'])
def add_book():
    pass

@app.route('/download')
def downloadFile ():
    path = "ebook_list.txt"
    return send_file(path, as_attachment=True)



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