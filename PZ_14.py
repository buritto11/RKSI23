# Из текстового файла (wtiter.txt) выбрать фамилии писателей и годы жизни, а также произведения ими написанные. Посчитать общее количество произведений в данном файле.
import re
spicok = []
all_proisv = []
f = open("writer.txt", encoding="utf-8")
for line in f:
    spicok.append(line)
for li in range(2,len(spicok)):
    p=re.compile(r"^\w*")
    res = re.match(p,spicok[li])
    yars = re.compile(r"([(][0-9]+.-[0-9]+[)])")
    y = re.search(yars,spicok[li])
    k = re.compile(r"([«].+[»]+)")
    proisv = re.search(k,spicok[li])
    if proisv is None:
        print("Автор:",res[0],"Годы жизни -",y[0])
    else:
        print("Автор:",res[0],"Годы жизни -",y[0],"Произведения",proisv[0],"\n")
        all_proisv += proisv[0].split('«')
fff = [i for i in all_proisv if i]
print("Количество произведений",len(fff))
