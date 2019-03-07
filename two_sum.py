#two sum
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

numbers = 5

def check(target, record):
    for num in range(len(record)-1):
        for x in range(1,len(record)):
            sum = record[num] + record[x]
            if sum == target:
                return num,x

def main():
    record = list()
    for num in range(numbers):
        number_new = int(input('Enter the number: '))
        record.append(number_new)
    target = int(input('Enter the target sum: '))
    print('The index of the numbers which add up to the target sum are:',(check(target, record)))

if __name__ == "__main__":
    main()
