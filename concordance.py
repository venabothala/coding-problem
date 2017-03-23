#!/usr/bin/env python

'''
concordance.py

This script will generate Concordance of a text document written in English

Usage: python concordance.py <input_file_name> <output_file_name>
Ex: python concordance.py input.txt output.txt

Sample Output:
a => 3 [1, 1, 2]
all => 1 [2]
alphabetical => 1 [2]
.
.
write => 1 [1]
written => 1 [1]

Author: Vamshi Enabothala
03/23/2017
'''

import sys
import string

def main(argv):

    # extract the command line arguments
    if (len(argv) < 3):
        print ("Expecting 2 Input Arguements: Input filename and Output filename\n")
        print ("Usage: python concordance.py <input_file_name> <output_file_name>\n")
        print ("Ex: python concordance.py input.txt output.txt\n")
        sys.exit()

    ip_fpath = argv[1].strip()
    op_fpath = argv[2].strip()

    ip_fhandle = open(ip_fpath, "r+")
    op_fhandle = open(op_fpath, "w+")

    ip_fcontents = ip_fhandle.read()

    op_dict = {}
    line_number = 1
    for i in ip_fcontents.splitlines():
        for j in i.split():
            op_word = j.translate(None, string.punctuation).lower().strip()
            op_dict.setdefault(op_word,[]).append(line_number)
        line_number += 1

    for i in sorted(op_dict.keys()):
        if i:
            print ("%s => %s %s" % (i, len(op_dict[i]), op_dict[i]))
            op_fhandle.write("%s => %s %s\n" % (i, len(op_dict[i]), op_dict[i]))

    print ("Execution Completed")
    ip_fhandle.close()
    op_fhandle.close()

if __name__ == "__main__":
        main(sys.argv)
