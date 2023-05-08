#!/usr/bin/env python
# coding: utf-8

import re
import sys
import mailbox
from os import listdir
from os.path import isfile, join


n = len(sys.argv)

all_files = [f for f in listdir('enron/') if isfile(join('enron/', f))]
# print(all_files)
all_mails = []
for file in all_files:
    all_mails.append(mailbox.mbox(join('enron/', file)))

# Implementation of term_search task

if(sys.argv[1]=="term_search"):
    terms = set()
    for i in range(2, n):
        terms.add(sys.argv[i].lower())
    counter = 0
    for mail in all_mails:
    #     print(mail)
        for msg in mail:
    #         print(msg)
            all_strings_present = 0
            all_strings_present = all(re.findall(s, msg.get_payload(), flags=re.I) for s in terms)
            if all_strings_present:
                counter += 1
                print(str(counter)+". "+str(msg['X-From'])+" <"+str(msg['From'])+"> "+str(msg['date']))
    print("Result Found: ",counter)

# Implementation of address_search task
elif(sys.argv[1]=="address_search"):
    name = set()
    addr = set()
    for i in range(2, n):
        name.add(sys.argv[i].lower())
    for mail in all_mails:
    #     print(mail)
        for msg in mail:
    #         print(msg)
            all_strings_present = 0
            all_strings_present = all(re.findall(s, str(msg['X-From']), flags=re.I) for s in name)
            if all_strings_present:
                addr.add(str(msg['From']))
    for i, address in enumerate(addr):
        print(str(i+1)+". <"+address+"> ")
    print("Result Found: ",len(addr))

# Implementation of interaction_search task
elif(sys.argv[1]=="interaction_search"):
    convo = set()
    adr1 = sys.argv[2]
    adr2 = sys.argv[3]
    for mail in all_mails:
    #     print(mail)
        for msg in mail:
    #         print(msg)
            if adr1==str(msg['From']) and adr2==str(msg['To']):
                convo.add(adr1+"> -> <"+adr2+"> [Subject: "+msg['Subject']+"]")
            if adr2==str(msg['From']) and adr1==str(msg['To']):
                convo.add(adr2+"> -> <"+adr1+"> [Subject: "+msg['Subject']+"]")
    for i, item in enumerate(convo):
        print(str(i+1)+". <"+item)
    print("Result Found: ",len(convo))

# Close all the files
for mail in all_mails:
    mail.close()
