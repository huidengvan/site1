
import glob
#print(glob.glob("gen/*.md"))
old_url_prefix='https:\/\/luminouswisdomca\.org\/media\/kunena\/attachments\/'
new_url_prefix='https://huidengvan.s3-us-west-2.amazonaws.com/attachments/'

import re
for filename in glob.glob("content/archive/*.md"):
    textfile = open(filename, 'r')
    filetext = textfile.read()
    textfile.close()
    matches = re.findall(old_url_prefix, filetext)
    if len(matches) > 0:
        print(filename, matches)
        for m in matches:
            newcontent = re.sub(old_url_prefix,new_url_prefix, filetext)
            print(newcontent)
            textfile = open(filename, 'w')
            textfile.write(newcontent)
            textfile.close()

print('done.')       

