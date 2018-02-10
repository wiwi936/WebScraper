"""
Utils
"""

import os 
import re 

def clean_data(data):
    try: 
        data = data.strip(' \t\n\r')
    except: 
        pass
    return data

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

def get_filename(url):
    return url[url.rfind("/")+1:]

def folder_exist(folder):
    if not os.path.isdir(folder): 
        os.mkdir(folder)
