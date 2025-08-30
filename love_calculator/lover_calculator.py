def calculate_love_score(hisName:str,herName:str):
    word_to_compare_first = ['T', 'R', 'U', 'E']
    word_to_compare_second = ['L', 'O', 'V', 'E']

    combination_of_name = hisName.upper() + herName.upper()
    counts_first={}
    counts_second={}
    for i in range(len(combination_of_name)):
        if combination_of_name[i] in word_to_compare_first and combination_of_name[i] in word_to_compare_second:
            counts_first[combination_of_name[i]] = counts_first.get(combination_of_name[i],0) + 1
            counts_second[combination_of_name[i]] = counts_second.get(combination_of_name[i],0) + 1
        elif combination_of_name[i] in word_to_compare_first:
            counts_first[combination_of_name[i]] = counts_first.get(combination_of_name[i],0) + 1
        elif combination_of_name[i] in word_to_compare_second:
            counts_second[combination_of_name[i]] = counts_second.get(combination_of_name[i],0) + 1

    
    first_score = str(sum(counts_first.values()))


    second_score = str(sum(counts_second.values()))


    
    love_score = first_score + second_score
    print(f"Love Score = {love_score}")
       

calculate_love_score("Kanye West","Kim Kardashian")


# Example: How it Calculates:
# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53

