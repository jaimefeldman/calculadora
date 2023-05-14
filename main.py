import sys
import calculadora


from termcolor import colored

def main():
    print("probando la calculadora")
    res = calculadora.suma(10,10)
    print(f"sumando 10 + 10 = {res}")

if __name__ == "__main__":
    sys.exit(main())
