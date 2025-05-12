# Lyra Programming Language

This is a college project focused on designing and implementing a custom programming language called Lyra. The project involves building a compiler that translates Lyra code into assembly-like stack-based virtual machine code, providing a deeper understanding of compiler construction.

# Example Code
Here is an example of a simple Lyra program for matrix addition:
```
matrix m1[2][2] = ((3,4),(5,6))
matrix m2[2][2] = ((7,8),(9,1))
matrix m3[2][2]
int i = 0 
int j = 0
while(i < 2) do
    while (j < 2) do
        m3[i][j] = m1[i][j] + m2[i][j]
        j = j + 1 
    end 
    j = 0
    i = i + 1
end

i = 0
j = 0

while(i < 2) do
    while(j < 2) do
        writei(m3[i][j])
        writes(" ")
        j = j + 1
    end
    j = 0
    i = i + 1
end
```
# Generated code
```
PUSHI 3
PUSHI 4
PUSHI 5
PUSHI 6
PUSHI 7
PUSHI 8
PUSHI 9
PUSHI 1
PUSHN 4
PUSHI 0
PUSHI 0
label1c: NOP
PUSHG 12
PUSHI 2
INF
JZ label1f
label0c: NOP
PUSHG 13
PUSHI 2
INF
JZ label0f
PUSHGP
PUSHI 8
PADD
PUSHG 12
PUSHI 2
MUL
PUSHG 13
ADD
PUSHGP
PUSHI 0
PADD
PUSHG 12
PUSHI 2
MUL
PUSHG 13
ADD
LOADN
PUSHGP
PUSHI 4
PADD
PUSHG 12
PUSHI 2
MUL
PUSHG 13
ADD
LOADN
ADD
STOREN
PUSHG 13
PUSHI 1
ADD
STOREG 13
JUMP label0c
label0f: NOP
PUSHI 0
STOREG 13
PUSHG 12
PUSHI 1
ADD
STOREG 12
JUMP label1c
label1f: NOP
PUSHI 0
STOREG 12
PUSHI 0
STOREG 13
label3c: NOP
PUSHG 12
PUSHI 2
INF
JZ label3f
label2c: NOP
PUSHG 13
PUSHI 2
INF
JZ label2f
PUSHGP
PUSHI 8
PADD
PUSHG 12
PUSHI 2
MUL
PUSHG 13
ADD
LOADN
WRITEI
PUSHS " "
WRITES
PUSHG 13
PUSHI 1
ADD
STOREG 13
JUMP label2c
label2f: NOP
PUSHI 0
STOREG 13
PUSHG 12
PUSHI 1
ADD
STOREG 12
JUMP label3c
label3f: NOP
```
# Usage
1.	Write the Lyra code in a txt file.
2.	Run the compiler to generate assembly-like code:
```
python main.py <lyra_file>.txt
```
3.	Copy the generated code into the [Virtual Machine](https://ewvm.epl.di.uminho.pt/) provided by Uminho.
4.	The virtual machine interprets and runs it, allowing you to see the output of the program.
