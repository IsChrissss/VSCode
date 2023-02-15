def main():
    x = convert(input("Enter a text: "))
    print(x)

def convert(x):
    return x.replace(":)","🙂").replace(":(","🙁")

main()
