# -*- coding: utf-8 -*-

from collections import Counter
import PyPDF2
import os

pl = open('2.5.pdf', 'rb')
plread = PyPDF2.PdfFileReader(pl)


some_text = ''
for n in range(10, 770):
    some_get_page = plread.getPage(n)
    some_page = some_get_page.extractText()
    some_text = some_text + some_page

with open('c:/tmp.txt', 'w', encoding='utf16') as fg:
        fg.write(some_text)


with open('c:/tmp.txt', 'r') as myfile:
    string = myfile.read().translate({ord(c): " " for c in "1234567890!@#$%^&*()[]{};:,./<>?\|`~-=_+"}).lower()

list1 = [x.lower() for x in string.split()]
counts = Counter(list1).most_common(100)

for x in (list([x[1] for x in counts])):
    out = []
    for n in counts:
        if n[1] == x:
            out.append(n[0])
    out.sort()
    for x in out:
        print(x.capitalize())

print (counts)

os.remove('c:/tmp.txt')