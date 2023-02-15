# Ask user for their name

# #Split user's name into first anme and last name
# first, last = name.split(" ")

# print("Hello,", last)
# #Say hello to user
def main():
    hello()
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="World"):
    print("Hello,",to)

main()