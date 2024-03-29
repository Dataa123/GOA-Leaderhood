# def dissapear(nums):
#     for i in nums[:]:
#         if i == 0:
#             nums.remove(i)
#     return nums

# print(dissapear([0, 1, 0, 0, 2, 3, 0, 0]))

# def dissapear(nums):
#     i = 0
#     while i in nums:
#         nums.remove(i)
#     return nums

# print(dissapear([0, 1, 0, 0, 2, 3, 0]))

# def dissapear(nums):
#     while nums.count(0):
#         nums.remove(0)
#     return nums

# print(dissapear([0, 1, 0, 0, 2, 3, 0]))


num = int(input("Enter number: "))
numbers = input("Enter numbers: ")
indexes = input("Enter indexes: ")

numbers = numbers.split(" ")
indexes = indexes.split(" ")
index1 = int(indexes[0])
index2 = int(indexes[1])

first_number = numbers[index1]

listn = []

flip_numbers = numbers[index1:index2]
flip_numbers = flip_numbers[::-1]
flip_numbers = " ".join(flip_numbers)

if num != len(numbers):
    print("It's wrong")
else:
    for i in numbers:
        listn.append[str(first_number)]
        listn.append[flip_numbers]
        listn.append[index2 + 1]

print(numbers)