"""
Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

  ? Find the sum of all the multiples of 3 or 5 below 1000 ?

Solution

- Loop through to the number below the given digit
- Find all multiples of 3 then of 5 and append them to a list
- Sum up the elements of the list
- Result is the Sum of multiples of 3 and 5

Functions
* Take input of the sum of which multiples and below which number
* Find multiples between 3 and 5. Return A list of the multiples
* Obtain the sum of the multiples btn 3 and 5


"""
# Gets the factor(s) we want to find its multiples


def getFactors():
    print("Enter the number(s) to find its multiples (Separate numbers with spaces):")
    numbers = input()
    return (map(int, numbers.split(" ")))

# Find all the multiples of a factor below a number limit


def findMultiples(multiples_list, factors, number_limit):

    for number in range(1, number_limit):
        for factor in factors:
            if (number % factor == 0):
                multiples_list.append(number)
    return multiples_list

# Finds duplicate multiples in the list for factors more than 1


def removeListDuplicates(multiples_list):
    for multiple in multiples_list:
        multipleDuplicateCount = multiples_list.count(multiple)
        if multipleDuplicateCount > 1:
            for _ in range(multipleDuplicateCount - 1):
                multiples_list.remove(multiple)
    return multiples_list

# Sums the lis of multiples


def sumMultiples(multiples_list):
    return sum(multiples_list, 0)


if __name__ == "__main__":
    print("****** Solution 1 ******")
    print("Finding sum of multiples of factor(s) below a certain number limit\n")
    multiples_list = []
    factors = list(getFactors())

    print("Enter the number limit")
    number_limit = int(input())

    multiples_list = findMultiples(multiples_list, factors, number_limit)
    multiples_list = removeListDuplicates(multiples_list)
    sum_of_multiples = sumMultiples(multiples_list)

    print(sum_of_multiples)
