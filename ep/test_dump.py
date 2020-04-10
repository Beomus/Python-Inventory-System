mydict = {'hello': ('world', 'cool')}
mydict['new'] = 'what', 'sup'
newdict = dict(mydict)
print(mydict)
print(mydict==newdict)
print(dict(mydict).pop('new')[0] == 'what')
print(newdict)
print(mydict)
