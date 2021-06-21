


number = input("Please enter your number: \n")

# digits = [int(i) for i in str(number)]

mod_type = input("Insert mod, separated by comma: \n")

mod = mod_type.split(",")


modded = []


for i in mod:
    modded.append(int(number) % int(i))



print(f"{modded}")




