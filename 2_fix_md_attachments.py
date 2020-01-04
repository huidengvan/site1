import csv

def build_attdic():
    attdic = {}
    with open('jos_kunena_attachments.csv', newline='') as csvfile:
        creader = csv.reader(csvfile,delimiter=',')
        #reader = csv.DictReader(csvfile)
        line_count = 0
        for row in creader:
            #print(', '.join(row))
            attdic[row[0]] = row[1]

    #print(attdic)
    return attdic

import glob
#print(glob.glob("gen/*.md"))

attdict = build_attdic()

import re
for filename in glob.glob("gen/*.md"):
    textfile = open(filename, 'r')
    filetext = textfile.read()
    textfile.close()
    matches = re.findall("\[attachment.*\/attachment\]", filetext)
    if len(matches) > 0:
        print(filename, matches)
        for m in matches:
            attid = m[m.find('=')+1:m.find(']')]
            print(attid, attdict[attid])
            newcontent = re.sub('\[attachment.*\/attachment\]',attdict[attid], filetext)
            print(newcontent)
            textfile = open(filename, 'w')
            textfile.write(newcontent)
            textfile.close()

print('done.')       

