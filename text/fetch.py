import random
import urllib2
import re

random.seed()

with open('./catalogue/whitelist.csv') as f:
    links = [url.strip() for url in f.readlines()]

link = random.choice(links)

text = urllib2.urlopen(link).read()

print text

for s in re.findall('(?:\. )([A-Z].{38,138}\.)', text):
    print s