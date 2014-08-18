# -- encoding: utf-8 --
__author__ = 'mep'

import sys
import csv

''' Reverse name: Get last part of name and move it to beginning '''
reverse = lambda name: name.split().pop() + ' ' + ' '.join([v for v in name.split()[:-1]])

'''
Open CableDesigner CSV
:param file_name:  Name of csv file
:return: List of tuples of names found. Tuple has name & reversed name
'''
open_cd = lambda file_name: [(x[0], reverse(x[0])) for x in csv.reader(open(file_name), delimiter=';')]

'''
Name is in third column & has a number in front of it that needs to be removed.
'''
doora_extract = lambda s: ' '.join(s[2].split()[1:])

'''
Open DooraNet CSV
:param file_name:  Name of csv file
:return: List of tuples of names found. Tuple has name & reversed name
'''
open_doora = lambda file_name:  [(doora_extract(x), reverse(doora_extract(x)))
                                 for x in csv.reader(open(file_name), delimiter=';') if x[0][0:4] == 'LASK']

s = open_doora(sys.argv[2])
s2 = open_cd(sys.argv[1])

doora = set()
# Following compares unreversed names from dooranet file to reversed
# file names. This is done by creating sets from both lists of names
# and doing a difference operation to them.
for i in (set([i[0] for i in s])-set([i[1] for i in s2])-set(i[0] for i in s2)):
    doora.add(i)

cable =set()
# Following compares unreversed names from cable designer to reversed
# names from dooranet.
for i in (set([i[0] for i in s2])-set([i[1] for i in s])-set(i[0] for i in s)):
    cable.add(i)
#cable = []
print "Puuttuvat Doorasta"

for i in sorted(doora):
    print i

print
print "Puuttuvat CableDesigneristä"
for i in sorted(cable):
    print i
