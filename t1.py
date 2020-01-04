import csv
with open('gongxiu2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, dialect='excel',delimiter=';')
    #reader = csv.DictReader(csvfile)
    line_count = 0
    for row in spamreader:
        #print(', '.join(row))
        f = open('gen/' +row[1] + '.md', "w")
        #f.write("Now the file has more content!")
        
        f.write('---\n')
        f.write('title: "' + row[0] + '"\n' )
        f.write('date: ' + row[4] + '-08:00\n' )
        f.write('draft: false\n')

        if row[0].find('2015届') > 0 :
            f.write('tags: ["2015届"]\n')
        
        if row[0].find('2016届') > 0 :
            f.write('tags: ["2016届"]\n')

        if row[0].find('2018届') > 0 :
            f.write('tags: ["2018届"]\n')

        if row[0].find('2019届') > 0 :
            f.write('tags: ["2019届"]\n')
        
        f.write('categories: ["慧灯禅修班"]\n')
        #print(row[0], row[2], row[4], row[5])
        f.write('---\n')

        #https://luminouswisdomca.org/media/kunena/attachments/336/71.pdf
        # select id, concat('https://luminouswisdomca.org/',folder,'/', filename) FROM `jos_kunena_attachments` WHERE 1


        f.write(row[5] + '\n')
        line_count += 1

        f.close()
        #if line_count == 400:
        #    break
    print(f'Processed {line_count} lines.')
        #print(row[0])