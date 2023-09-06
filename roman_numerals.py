numerals = {
    "i" : 1,
    "v" : 5,
    "x" : 10,
    "l" : 50,
    "c" : 100,
    "d" : 500,
    "m" : 1000
}

# testNumber = "MMM"
testNumber = "MCMLXXXVI"
# testNumber = "IV"

def roman_numeral_conversion(numeral):
    numbers = [numerals[x] for x in numeral.lower()]
    total = 0
    for index, value in enumerate(numbers):
        if index + 1 <= len(numbers) - 1:
            if value < numbers[index + 1]:
                total += -value
            else:
                total += value
    total += numbers[-1]
    return total

if __name__ == "__main__":
    print(roman_numeral_conversion(testNumber))
