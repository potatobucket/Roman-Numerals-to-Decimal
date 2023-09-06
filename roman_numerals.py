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
# testNumber = "MCMLXXXVI"
# testNumber = "IV"
total = 0

# def check_if_input_is_in_range():
#     userInput = int(input("What roman number do you want to convert? (1 - 3,000)\n"))
#     if userInput < 1 or userInput > 3000:
#         userInput = int(input("Please enter a number between 1 and 3,000.\n"))
#         return "Number outside of operating parameters."
#     else:
#         return userInput

numbers = [numerals[x] for x in testNumber.lower()]

for index, value in enumerate(numbers):
    if index + 1 <= len(numbers) - 1:
        if value < numbers[index + 1]:
            total += -value
        else:
            total += value

print(total)

# for index, value in enumerate(numbers):
#     if index + 1 < 10:
#         if value < numbers[index] + 1:
#             total += -value
#         else:
#             total += value
# print(total)

# print(numbers[numbers.index(50) + 1])

# for index, value in enumerate(numbers):
#     print(index, value)

# if __name__ == "__main__":
#     # while running == True:
#     #     print(check_if_input_is_in_range())
#     numbers = [numerals[x] for x in testNumber.lower()]
#     for index, value in enumerate(numbers):
#         if index + 1 <= len(numbers):
#             if value < numbers[index + 1]:
#                 total -= value
#             else:
#                 total += value
#     print(total)
