from os import walk

def import_folder(path):
    
    for data in walk(path):
        print(data)

import_folder('assets/player')