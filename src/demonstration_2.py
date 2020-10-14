"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here

    digits.reverse()
    digits[0] += 1

    for i in range(len(digits) - 1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i + 1] += 1

    if digits[-1] == 10:
        digits[-1] = 0
        digits.append(1)


    digits.reverse()
    return digits

print(plus_one([1, 3, 2]))
print(plus_one([3, 2, 1, 9]))
print(plus_one([9, 9, 9]))

