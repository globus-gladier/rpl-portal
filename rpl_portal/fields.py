import os
from urllib.parse import urlsplit, urlunsplit, urlencode
import copy
import re

def title(result):
    if not result[0].get("dc"):
        return
    t = result[0]["project_metadata"]
    if not ("experiment" in t):
        """The title for this Globus Search subject"""
        
        
        return result[0]["dc"]["titles"][0]["title"]
   

    return result[0]["project_metadata"]["experiment"]



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
            t = f.split('/')[-1]
            n = re.search("\d+", t).group()
            fs["Plate "+ n] = f
    
    return fs
    return None
def exp_plates(result):
    fs = []
    for f in all_files(result):
        
     
       
        if re.match(".*expected\.png", f):
            
            fs = [f] + fs
    fs.sort(reverse=True, key=lambda x: int(re.search("\d+", x.split("/")[-1]).group()))

    return fs
def real_plates(result):
    fs = []
    for f in all_files(result):
        
     
       
        if re.match(".*measured\.png", f):
            
          
          fs = [f] + fs
    fs.sort(reverse=True, key=lambda x: int(re.search("\d+", x.split("/")[-1]).group()))
    return fs

def convergence_graph(result):
    fs = []
    for f in all_files(result):
        if re.match(".*graph\.png", f):
            
          
            fs = f
    
    return fs

def colors(result):
    fs = []
    for f in all_files(result):
        if re.match(".*mixed_colors\.png", f):
            
          
            fs = f
    
    return fs
def target_color(result):
    fs = {}
    for f in all_files(result):
        
     
       
        if re.match(".*target_color\.png", f):
            
          return f

    
    return fs

def best_color(result):
    fs = {}
    for f in all_files(result):
        
        if re.match(".*best_color\.png", f):
            
          
            return f
    return fs
def final_img(result):
    fs = {}
    for f in all_files(result):
           if re.match(".*final_image.jpg", f):
               return f
    return fs
    return None
def results(result):
    return result[0]["project_metadata"]
def exp_type(result):
    if "exp_type" in result[0]["project_metadata"]:
       return result[0]["project_metadata"]["exp_type"]
    return "tests"
# def exp_label(result):
#     if result[0]["project_metadata"]["exp_label"]:
#         return result[0]["project_metadata"]["exp_label"]
#     return None
