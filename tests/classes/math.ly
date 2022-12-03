class Foo() {
    foo:int = 1
    bar:int = 2
}

def mulByTwo(a: int):int {
    b = 2
    foo = Foo()
    b += foo.bar
    return a & b
}

def main():int{
    return mulByTwo(1)
}
