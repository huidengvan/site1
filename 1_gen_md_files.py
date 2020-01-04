import json

fname = 'jos_kunena_messages_text.json'
with open(fname) as f:
  json_data = json.load(f)

print(json_data[2]['data'][1]['subject'])
print(json_data[2]['data'][1]['message'])
#for x in data:
    
 #   if(x['type'] == 'table') :
  #      print(x)

line_count = 0
for row in json_data[2]['data']:
    #print(', '.join(row))
    f = open('gen/' +row['id'] + '.md', "w")
    #f.write("Now the file has more content!")
    
    f.write('---\n')
    f.write('title: "' + row['subject'] + '"\n' )
    f.write('date: ' + row['postedtime'] + '-08:00\n' )
    f.write('draft: false\n')

    if row['subject'].find('2015届') > 0 :
        f.write('tags: ["2015届"]\n')
    
    if row['subject'].find('2016届') > 0 :
        f.write('tags: ["2016届"]\n')

    if row['subject'].find('2018届') > 0 :
        f.write('tags: ["2018届"]\n')

    if row['subject'].find('2019届') > 0 :
        f.write('tags: ["2019届"]\n')
    
    f.write('categories: ["慧灯禅修班"]\n')
    #print(row[0], row[2], row[4], row[5])
    f.write('---\n')

    #https://luminouswisdomca.org/media/kunena/attachments/336/71.pdf
    # select id, concat('https://luminouswisdomca.org/',folder,'/', filename) FROM `jos_kunena_attachments` WHERE 1


    f.write(row['message'] + '\n')
    line_count += 1

    f.close()
    #if line_count == 400:
    #    break
print(f'Processed {line_count} lines.')


