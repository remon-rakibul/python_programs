def assignment_solution(list_of_words):
    space = ''
    for word in list_of_words:
        print(space+word)
        space += ' '*(len(word)-1)
        
assignment_solution(["Wellcome", "to", "misfit"])
assignment_solution(["programming", "is", "my", "passion"])