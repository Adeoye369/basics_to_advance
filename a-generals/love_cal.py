
def calculate_love_score(name1, name2):
    true_count = {}
    love_count = {}
    sum_t = sum_l = 0
    names = name1 + name2
    for ch in names.upper():

        if ch in 'TRUE':
            true_count.setdefault(ch, 0)
            true_count[ch] += 1
        
        if ch in 'LOVE':
            love_count.setdefault(ch, 0)
            love_count[ch] += 1
        
    for (_, v) in true_count.items(): sum_t+=v
    for (_, v) in love_count.items() : sum_l+=v
    print(str(sum_t) + str(sum_l))

calculate_love_score("Angela Yu", "Jack Bauer")

            