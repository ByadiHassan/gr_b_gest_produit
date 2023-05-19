'''
d={'nom':'ASSIMI','prénom':'Ahmed','CIN':'X4013345'}
d.update({'Adresse':'Khemisset'})
d['Tel']='066669939'
print(d)
d['Tel']='076669939'
print(d)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)

for item in d.items():
    print (item)

for key,value in d.items():
    print (key,'------->',value)


for key in d.keys():
    print (key,'------->',d[key])

for key in d.keys():    
    print(key + ' '*(15-len(key)),end=' ')
print()
for key in d.keys():
    print (d[key]+ ' '*(15-len(d[key])),end=' ')
'''

s={10,11,12,13,10,10,11}
s.add(16)
s.add(12)
print(type(s))
print(s)