__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil 
from zipfile import ZipFile

# Part 1

def clean_cache():

    if os.path.exists('cache'):
        shutil.rmtree('cache')
        os.mkdir('cache')
    else:
        os.mkdir('cache')

# Part 2

def cache_zip(folder_data_zip,folder_cache):
    
    clean_cache()

    with ZipFile(folder_data_zip, 'r') as zip:
        zip.extractall(folder_cache)

folder_data_zip = os.path.join(os.getcwd(), 'data.zip')        
folder_cache = os.path.join(os.getcwd(), 'cache')

cache_zip(folder_data_zip,folder_cache)

# part 3

folder_abs_path = os.path.abspath('cache')

def cached_files():
    
    list_of_all_files = [os.path.join(folder_abs_path, file) for file in os.listdir(folder_abs_path)]
    
    return list_of_all_files

print(str(cached_files()))

# part 4

def find_password(list_of_all_files):
    
    for file in list_of_all_files:
        open_file = open(file, 'r')
        search_lines = open_file.readlines()

        for line in search_lines:

            if 'password' in line:
                password = line[line.find(' ') +1:-1]
                
                return password
        open_file.close()

# Print the password

print(find_password(cached_files()))


