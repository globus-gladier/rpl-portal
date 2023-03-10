import os
from urllib.parse import urlsplit, urlunsplit, urlencode
import copy
import re

def title(result):
    if not result[0].get("dc"):
        return
    """The title for this Globus Search subject"""
    return result[0]["dc"]["titles"][0]["title"]


def all_files(result):
    new_files = []
    for file in result[0]["files"]:
        url = file.get("url")
        path = urlsplit(url).path
        new_url = urlunsplit(("https", "g-cd34a.fd635.8443.data.globus.org", path, "", ""))
        new_files.append(new_url)
    return new_files

def final_plates(result):
    fs = {}
    for f in all_files(result):
        
     
       
        if re.match(".*plate_.\.jpg", f):
            
          
            fs[f.split('/')[-1]] = f
    
    return fs
    return None
def results(result):
    return result[0]["project_metadata"]