from prettytable import PrettyTable

results = PrettyTable()

results.field_names = ['mod', 'res', '(mod*mod)/(N/mod)', 'Xi', 'Results']



n = input("Number of equations")

# Arrays
equations = []  # Equations from user
mods = [] # mods extracted from equations
divided_mods = [] # N number for every equation
xi = [] # I have no idea what this is
row_results = [] # Result by row

N = 1
final_result = 0

for i in range(int(n)):

    res = input("Rest")
    mod = input("Mod")

    equation = {"mod": mod, "res": res}
   
    equations.append(equation)

     
# * Find n
for j in equations:
    mods.append(j['mod'])
    N = N * int(j['mod'])



# * Find divided mods
for i in mods:
    divided_mods.append(N/int(i))


# * Find xi
for i in range(int(n)):
    mod = equations[i]['mod']
    divided_mod = divided_mods[i]
    modded = int(divided_mod) % int(mod)
    print(f"{divided_mod} % {mod} = {modded}")


    for x in range(int(mod)):
        term = (x * int(modded)) % int(mod)
        if term == 1:
            xi.append(x)
            

# * Find row result

for i in range(int(n)):
    res = equations[i]['res']
    n_results = divided_mods[i]
    x = xi[i]

    row_results.append(int(res)*int(n_results)*int(x))


# * Find final result
for i in range(int(n)):
    final_result = final_result + row_results[i]


 # Add data to table
for i in range(int(n)):
    results.add_row([equations[i]['mod'], equations[i]['res'], N/int(equations[i]['mod']), xi[i], row_results[i]])

    

results.add_row([str(N), '.', '.', '.', str(final_result)])

print(results)