from prettytable import PrettyTable
from PyInquirer import prompt


results = PrettyTable()

results.field_names = ['mod', 'res', '(mod*mod)/(N/mod)', 'Xi', 'Results']



questions = [
    {'type' : 'input', 'name' : 'res', 'message': 'Rest'}, 
    {'type' : 'input', 'name' : 'mod', 'message': 'Mod'}
]

e_question = [
    {'type' : 'input', 'name': 'n', 'message': 'Number of equations'}
]

num = prompt(e_question)

n = num['n']

# Arrays
equations = []  # Equations from user
mods = [] # mods extracted from equations
divided_mods = [] # N number for every equation
xi = [] # I have no idea what this is
row_results = [] # Result by row

N = 1
final_result = 0

for i in range(int(n)):

    # res = input("Rest")
    # mod = input("Mod")


    answers = prompt(questions)

    equation = {"mod": answers['mod'], "res": answers['res']}
   
    equations.append(equation)

     
# * Find n
for i in range(int(n)):
    mods.append(equations[i]['mod'])
    N = N * int(equations[i]['mod'])





for i in range(int(n)):

    #* Find divided mods
    divided_mods.append(N/int(mods[i]))

    #* Find xi
    mod = equations[i]['mod']
    divided_mod = divided_mods[i]
    modded = int(divided_mod) % int(mod)
    print(f"{divided_mod} % {mod} = {modded}")


    for x in range(int(mod)):
        term = (x * int(modded)) % int(mod)
        if term == 1:
            xi.append(x)



    #* Find row result
    res = equations[i]['res']
    n_results = divided_mods[i]
    x = xi[i]

    row_results.append(int(res)*int(n_results)*int(x))


    #* Find final result
    final_result = final_result + row_results[i]

    #* Add data to table
    results.add_row([equations[i]['mod'], equations[i]['res'], N/int(equations[i]['mod']), xi[i], row_results[i]])

    

results.add_row([str(N), '.', '.', '.', str(final_result)])

print(results)