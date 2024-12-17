import sys

def read():
    return input().strip().split(':')[1].strip()

def combo(operand,a,b,c):
    if operand<4:
        return operand
    return [a,b,c][operand-4]
def simulate(code,a,b,c,output, pc=0):

    while pc >=0 and pc<len(code):
        command = code[pc]
        operand = code[pc+1]
        #print(pc,a,b,c, command, operand)

        if command == 0:#adv
            a = a// (2**combo(operand, a,b,c))
        if command == 1: #bxl
            b = b ^ operand
        if command ==2: #bst
            b = combo(operand,a,b,c)%8
        if command == 3 and a!=0:#jnz
            pc = operand
        else:
            pc+=2
        if command ==4: #bxc
            b = b^c
        if command ==5: #out
            output.append(combo(operand,a,b,c)%8)
        if command ==6: #bdv
            b = a// (2**combo(operand, a,b,c))
        if command ==7: #cdv
            c = a// (2**combo(operand, a,b,c))
            
        #print(pc,a,b,c, command, operand)
        #print()
            

a = int(read())
b = int(read())
c = int(read())
input()
program = [int(x) for x in read().split(",")]

output = []

simulate(program, a,b,c, output)
print(",".join([str(x) for x in output]))
