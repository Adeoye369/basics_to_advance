import re

# str1 = 'this is the first no +454-333-2344 the second is'

# phone_re = re.compile(r'(\+\d\d\d)-(\d\d\d-\d\d\d\d)')

# # for the first string
# n = phone_re.search(str1)
# if n : print("country code = ",n.group(1),", Phone = ", n.group(2))


hero = 'The new  Superwoman, Superman, Superdog and Supergirl'
hero1 = 'Human Hulklklklk Hulk'

output = re.compile('Hu(lk)*').findall(hero1)
print(output)

