import os
import requests
import datetime
import logging
import re
import json 

def write_to_file(filename, content):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'a') as f: 
        if f.tell() != 0:  
            f.write('================\n')  
        f.write(content + '\n')