def sum_nums(nums):
    """Given a list of numbers, return the sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE


    # for num in nums:
    #   while num >=   0:
    #     num += num
    #     return num
    sum = 0
    for num in nums:
        sum = sum + num
    return sum



print("sum_nums returned", sum_nums([1, 2, 3, 4]))
