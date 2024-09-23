
ziph = {'name': 'Ziphley', 'species': 'cat-kun', 'age': 22, 'hobby': 'sleep', 'weight(lb)': 54.0}


# for k in ziph.keys():
#     print(f"key: {k}") # print keys


# for v in ziph.values(): 
#     print(f'value: {v}') # print values


# for i in ziph.items():
#     print(f"item {i}") # print key - value

# for k,v in ziph.items():
#     print(f"item :=> {k}, => {v}") # print key - value



print([list(z) for z in list(ziph.items())])
