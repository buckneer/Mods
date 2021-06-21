from prettytable import PrettyTable
from PyInquirer import prompt
from termcolor import colored, cprint
from time import sleep
import os

def processPrint(step, text, step_color = 'red', color = 'blue'):
    step_colored = colored(f'[{step}] ', step_color)
    process_colored = colored(f'{text}', color)
    message = step_colored +  process_colored
    cprint(message)
    

def heading(text, color = 'blue'):
    print(colored(f"------------------- {text} -------------------", color))
    sleep(2)


results = PrettyTable()

results.field_names = ['mod', 'res', '(mod*mod)/(N/mod)', 'Xi', 'Results']



questions = [
    {'type' : 'input', 'name' : 'res', 'message': 'Rest'}, 
    {'type' : 'input', 'name' : 'mod', 'message': 'Mod'}
]

e_question = [
    {'type' : 'input', 'name': 'n', 'message': 'Number of equations'}
]


try:

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

        processPrint("Creating equation", f"x = {equation['res']}(mod{equation['mod']}) ")

        equations.append(equation)

    os.system("cls")
        
    # * Find n
    for i in range(int(n)):
        mods.append(equations[i]['mod'])
        N = N * int(equations[i]['mod'])
        processPrint("Calculating N", f"N = {N}")



    heading(f"For {i + 1} equation")
    for i in range(int(n)):

        #* Find divided mods
        divided_mods.append(N/int(mods[i]))
        print("\n")
        heading("Finding N for every row")
        print("\n")
        processPrint("Dividing N by current mod", f"(mod*mod)/(N/mod) = {divided_mods[i]}")
        print("\n")



        #* Find xi
        heading("Searching for xi")
        print("\n")
        mod = equations[i]['mod']
        divided_mod = divided_mods[i]
        modded = int(divided_mod) % int(mod)

        processPrint(f"Reducing mods to calculte xi for {mod}", f"{divided_mod} % {mod} = {modded}")
        processPrint("Trying to find x for which mod is equal to 1", f"(x * {modded} ) % {mod} = 1")

        for x in range(int(mod)):
            term = (x * int(modded)) % int(mod)
            
            if not term == 1:
                processPrint(f"x = {x}", f"equation is = {term}")
            else:
                processPrint(f"x = {x}", f"Equation is true for {x}", color='green')
                xi.append(x)
                break
        print("\n")


        heading("Result by row (res * (mod*mod)/(N/mod) * xi)")
        print("\n")
        # processPrint("Result by row", "")
        #* Find row result
        res = equations[i]['res']
        n_results = divided_mods[i]
        x = xi[i]
        
        row_results.append(int(res)*int(n_results)*int(x))
        processPrint("Row", f"{res} * {n_results} * {x} = {int(res)*int(n_results)*int(x)}")
        print("\n")


        #* Find final result
        heading("Final Result")
        print("\n")
        final_result = final_result + row_results[i]
        processPrint("Result", f"{row_results} = {final_result} ")
        print("\n")

        #* Add data to table
        results.add_row([equations[i]['mod'], equations[i]['res'], N/int(equations[i]['mod']), xi[i], row_results[i]])

        

    results.add_row([str(N), '.', '.', '.', str(final_result)])
    heading("Drawing table")
    print("\n")
    print(results)
    print("\n")
except KeyboardInterrupt:
    print("Exiting...")