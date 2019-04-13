# -*- coding: utf8 -*-
from mobi import Mobi
class Files:
    def __init__(self):
        print("File class is working... ")

    def save_file(self, line_to_save):
        self.line_to_save = line_to_save
        self.file = open("ebook_list.txt", 'a')
        self.file.writelines(line_to_save)