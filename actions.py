"""
Actions
"""

import csv
import os
import requests
import urllib
import uuid
from pprint import pprint

import utils

class Action():
    """
    Actions abstract class
    """
    def do(self, result):
        raise NotImplementedError("Must implement this")

class Blank(Action):
    """
    Print blank line
    Example:
    actions.Blank()
    """
    def do(self, result):
        print()

class GetCount(Action):
    """
    Print result len
    Example:
    actions.GetCount()
    """
    def do(self, result):
        print("Count: {}".format(len(result)))

class ExportConsole(Action):
    """
    Print result
    Example:
    actions.ExportConsole()
    """
    def do(self, result):
        if result: pprint(result)

class ExportCSV(Action):
    """
    Export results from finders to csv (uuid filename) on folder output_folder
    Example:
    actions.ExportCSV(output_folder)
    """
    def __init__(self, folder):
        self._folder = folder
        
    def do(self, result):
        utils.folder_exist(self._folder) 
        filename = os.path.join(self._folder, str(uuid.uuid4()) + ".csv")
        with open(filename, 'w', newline='') as fp:
            w = csv.writer(fp, delimiter=';', lineterminator='\n')
            w.writerows(result)
        print("File created: {}".format(filename))

class Download(Action):
    """
    Download results from finders on folder output_folder (uuid filename)
    Example:
    actions.Download(output_folder)
    """
    def __init__(self, folder):
        self._folder = folder
        
    def do(self, result):
        counter = 0
        utils.folder_exist(self._folder) 
        for file in result:
            try:
                r = requests.get(file)
                with open(os.path.join(self._folder, utils.get_filename(file)), 'wb') as outfile:
                    outfile.write(r.content)
                counter += 1
            except: pass
        print("Downloaded: {}".format(counter))

class JoinURL(Action):
    """
    Update results appending url self.__url on the beggining
    Example:
    actions.JoinURL(url)
    """
    def __init__(self, url):
        self.__url = url
        
    def do(self, result):
        for i in range(len(result)):
            result[i] = urllib.parse.urljoin(self.__url, result[i]) if not utils.is_valid_url(result[i]) else result[i]
