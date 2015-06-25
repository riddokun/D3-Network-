import time, json, datetime, csv, sys

csvfile = open('comm-data-Fri.csv', 'rb') #change to Friday
jsonfile = open('friday810.json', 'wb')

fieldnames = ("Timestamp", "from", "to", "location")
node = []
link = []
startFrom = 24686

reader = csv.DictReader(csvfile, fieldnames)
i = 0


for row in reader:
    # print row["Timestamp"] # Gets the time stamp
    # if row["Timestamp"] == "6/6/2014 9:00:00 AM": # Lazy
    str2 = ''.join(row["Timestamp"])
    if i > 0:
        stime = time.strptime(str2, "%Y-%m-%d %H:%M:%S")  # string does not contain "hours" or "minutes" so need to check this is before or after the start date
        mtime = time.mktime(stime)
        starttime = time.mktime(time.strptime("2014-06-06 08:00:00",  "%Y-%m-%d %H:%M:%S"))
        endtime = time.mktime(time.strptime("2014-06-06 08:10:00",  "%Y-%m-%d %H:%M:%S"))
        if starttime <= mtime <= endtime:
            print str2
            t = row["from"]
            f = row["to"]
            l = []
            # if f is in node...
            if f in node:
                l.append(node.index(f))  # push that node of f into the link
                if t in node:  # if t is in node...
                    l.append(node.index(t))  # push that node of t into link
                else:
                    node.append(t)
                    l.append(node.index(t))
            else:
                node.append(f)
                l.append(node.index(f))
                if t in node:
                    l.append(node.index(t))
                else:
                    node.append(t)
                    l.append(node.index(t))
            link.append(l)
            # if i == 10000:
            #     break
        elif mtime >= endtime:
            break
    i += 1

csvfile.close()

jsonfile.write('{\n\t"nodes" : [' '\n')
idx = 0
for n in node:    #write all nodes in the jsonfile
    jsonfile.write("\t\t{")
    jsonfile.write('"id": "')
    jsonfile.write(''.join(map(str, n)))

    idx += 1
    if idx == len(node):
        jsonfile.write('"\n\t\t}],\n')
    else:
        jsonfile.write('"},\n')

idx = 0
jsonfile.write('\t"links" : [' '\n')
for l in link:
    jsonfile.write("\t\t{")
    jsonfile.write('"source" : ')
    jsonfile.write(str(l[0]))
    jsonfile.write(', "target" : ')
    jsonfile.write(str(l[1]))
    jsonfile.write(', "weight": 1')

    idx += 1
    if idx == len(link):
        jsonfile.write("}\n\t]\n}")

    else:
        jsonfile.write("},\n")

jsonfile.close()