# Mods

## Installation

Clone the repository and install all requirements:
```bash
git clone https://github.com/buckneer/Mods.git
cd Mods
pip install -r requirements.txt
```
## Usage

If you want to solve modular equations, run _equation.py_ :
```bash
python equations.py
```
or if you want to convert a number into modded number, run _modout.py_:
```bash
python modout.py
```

## Equation.py
First input is the number of equations you want to solve then it will ask you as many times as you entered to input:
- Rest
- Mod

Result will be displayed in table.

You can always cancel script by running: **Ctrl+C**

**Example**
```input
input: 3 equations
input: 3(mod5), 1(mod7), 6(mod8)
```
![example](https://user-images.githubusercontent.com/42391164/122809328-40f7a700-d2ce-11eb-811a-d76dd3dd1673.png)


## Modout.py

You'll have to input number you want to convert, as well as the 'code' you want the number to be converted.

**Example**
```
input number: 83
input mod: 5,3,2
output: (3,2,1)
83(5,3,2) => (3,2,1)
```

![example_mod](https://user-images.githubusercontent.com/42391164/122809155-05f57380-d2ce-11eb-85ee-ebb8a09771e1.png)
