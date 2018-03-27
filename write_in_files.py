# Script Name		: write_in_files.py
# Author		    : Ajay Rajbhar
# Created		    : 27th March 2018
# Last Modified	: 
# Version		    : 1.0

# Description		: This is a very simple script that opens up a file and writes whatever is set "


def write_to_file(filename, txt):
  with open(filename, 'w') as file_object:
      s = file_object.write(txt)
      
    
if __name__ == '__main__':
  write_to_file('test.txt', 'I am Ajay Rajbhar')
