# -- encoding: utf-8 --
__author__ = 'mep'

import sys
import csv

''' Reverse name: Get last part of name and move it to beginning '''
reverse = lambda name: name.split().pop() + ' ' + ' '.join([v for v in name.split()[:-1]])

def open_cd(file_name):
    '''
    Open CableDesigner CSV
    :param file_name:  Name of csv file
    :return: List of tuples of names found. Tuple has name & reversed name
    '''
    retval = []

    f = open(file_name)
    reader = csv.reader(f, delimiter=';')
    for line in reader:
        # Name is in first column
        retval.append((line[0], reverse(line[0])))
    return retval

def open_doora(file_name):
    '''
    Open DooraNet CSV
    :param file_name:  Name of csv file
    :return: List of tuples of names found. Tuple has name & reversed name
    '''
    retval =[]

    f = open(file_name)
    reader = csv.reader(f, delimiter=';')
    for line in reader:
        if line[0][0:4] == 'LASK':
            # Name is in third column & has a number in front of it that
            # needs to be removed
            name = ' '.join(line[2].split()[1:])
            retval.append((name, reverse(name)))
    return retval

s = open_doora(sys.argv[2])
s2 = open_cd(sys.argv[1])

doora =[]
# Following compares unreversed names from dooranet file to reversed
# file names. This is done by creating sets from both lists of names
# and doing a difference operation to them.
for i in (set([i[0] for i in s])-set([i[1] for i in s2])):
    if i not in doora:
        doora.append(i)

cable =[]
# Following compares unreversed names from cable designer to reversed
# names from dooanet.
for i in (set([i[0] for i in s2])-set([i[1] for i in s])):
    if i not in cable:
        cable.append(i)

print "Puuttuvat Doorasta"

for i in sorted(doora):
    print i

print
print "Puuttuvat CableDesigneristä"
for i in sorted(cable):
    print i
