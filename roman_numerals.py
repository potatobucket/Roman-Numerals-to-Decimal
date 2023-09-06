numerals = {
    "i" : 1,
    "v" : 5,
    "x" : 10,
    "l" : 50,
    "c" : 100,
    "d" : 500,
    "m" : 1000
}

running = True
testNumber = "MMM"

def check_if_input_is_in_range():
    userInput = int(input("What roman number do you want to convert? (1 - 3,000)\n"))
    if userInput < 1 or userInput > 3000:
        userInput = int(input("Please enter a number between 1 and 3,000.\n"))
        return "Number outside of operating parameters."
    else:
        return userInput

# numbers = [numerals[x] for x in testNumber.lower()]

# print(numbers)

if __name__ == "__main__":
    # while running == True:
    #     print(check_if_input_is_in_range())
    numbers = [numerals[x] for x in testNumber.lower()]
    total = 0
    for value in numbers:
        if value < numbers.index(value) + 1:
            total -= value
        else:
            total += value
    print(total)
