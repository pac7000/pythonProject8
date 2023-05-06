#  This code check all the subfolder and print out the pdf inside it in red
import os

def print_pdf_names(folder):
    for root, dirs, files in os.walk(folder):
        # print subfolder name in blue
        print('\033[34m' + root + '\033[0m')
        for file in files:
            if file.endswith('.pdf'):
                # print pdf names in red
                print('\033[31m' + file + '\033[0m')

print_pdf_names('.')

