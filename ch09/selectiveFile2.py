#! python3
# Program: Selective copy that walks through folder tree and searches for files with a certain file extension

import glob, os, shutil

# define file location & extension type
files = glob.iglob(os.path.join('D:\\wnk2', "*.jpg"))

#
for file in files:
    if os.path.isfile(file):
        print('Copying file %s' % file + ' to C:\\Users\\tyya\\Pictures\\wnkpc ') # Print out what is done
        try:
            shutil.copy2(file, 'C:\\Users\\tyya\\Pictures\\wnkpc') # Copy to the new directory
        except Exception:
            pass
