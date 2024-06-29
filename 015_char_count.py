import pprint as pp

msg = '''
"thhis is a very long 
character that we whant to do the, only charalong
 character count oo "
 '''
count = {}

for ch in msg:
    count.setdefault(ch, 0)
    count[ch] += 1

val = pp.pformat(count) # to get value as string
pp.pprint(count) # to get value as output

