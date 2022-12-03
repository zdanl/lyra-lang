# Lyra
### Intentional Programming Language
--------------
![Lyra Logo](lyra1.jpg)

Lyra is a powerful and versatile programming language that combines the simplicity and expressiveness of Python3.12 and Perl5.10 with the power and efficiency of asynchronous programming and performance of LLVM. Its friendly and intuitive syntax makes it easy to learn and use, while its advanced compilation, subset and tools lead to mission assurance in various fields. Its design and optimization techniques allow it to tackle even the most demanding engineering tasks. With Lyra, you can design, synthesize, and manufacture CPUs, SoCs, and other microprocessors, as well build scalable and efficient operating systems, web and mobile apps, and more.
This is the official description and, so far, documentation website.

## Road Map

| Predicted Version | Description of Progress | Timestamp |
| --------------- | --------------- | --------------- |
| Original | Type system, Functional Language, Lexer/Compiler | This was the original work |
| 0.1 | Multiline comments and different styles of it were contributed, OOP discussed | 30/11/2022 |
| 0.2 | Implementation of the entire AST is still in progress | 03/12/2022 |

You may soon use indentation OR sharp braces, and you may use a semicolon whenever you like. 
 
 ![Lyra Logo](lyra3.jpg)
 
 ## Features
- **it's fast and compiled**, With C/Julia comparable speed and LLVM's cutting-edge optimizations, Lyra eliminates the need for tedious performance tweaking on your end.

- **it's statically typed** so you don't need to guess the type of the variable if your coworker didn't spend the time to use meaningful names and you can make use of compile-time checks, autocomplete and more

- **it's simple and expressive** because the code should be easily readable and it shouldn't make you guess what it does, but you can give it your very personal touch and style



## How to run, compile or translate .ly files/projects

```
./lyra --compile <filename>
./lyra --generate-ast <filename>
./lyra --print-ast <filename>
./lyra --generate-llvm <filename>
./lyra --print-llvm <filename>
./lyra --generate-hdl <filename>
./lyra --help

```
 
## ./lyra

This is the compiler.

It supports multiple features as in just printing the AST, generating LLVM IR, compilation, or translation into Hardware Description Language (HDL).

## Functions, Synonym Naming Conventions and Braces OR Indents

```
def logic_gate:2(n_input:int):int{
    if n_input <= 1{
        return 1
    }
    return n * fact(n_input-1)
}

sub logic_gate_2(n:int):int:
    if n > 5:
        return 0

function logic_gate_3(n_input1:int, n_input2:sha1) {
    n_input2 ^= n_input1 << 0x44
    return n_input2
}

def main():int{
    return fact(6)
}
```

## Conditionals

```
def if-expression():int{
    server_load = 300
    server_load ^= 44
    
    if server_load < 200 {
        printf('wow you are 18\n')
    } else {
        printf('i guess you are not 18\n')
    }
    
    if server_load >= 400:
        printf('foo')

    return 0
}
```

## Loops

```
def main():int{

    printf('while loop\n')
    x = 0
    while x < 10{
        printf('x = %i\n',x)
        x = x+1
    }

    printf('Until loop\n')

    x = 0
    until x > 10{
        printf('x = %i\n',x)
        x = x+1
    }

    return 0
}
````

## Multi Line Comments and Single Line Flavours

```
# this is a comment

#=
    this is a julia style multi line comment
#=

/*
    this is a c style multi line comment
*/

// this is a c style single line comment

```
