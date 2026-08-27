"""My first exercise in COMP110"""

__author__ = "730664641"


def greet(name: str) -> str:
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
