# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is
# 17.

# Bonus: Can you do this in one pass?


# My Solution!!
sample_list = [10, 15, 3, 7]
k = 10


def do_numbers_from_list_sum_k(list, k):
    if len(list) <= 1:
        return False

    main_number = list[0]
    for i in range(1, len(list)):
        if main_number + list[i] == k:
            return True

    if (do_numbers_from_list_sum_k(list[1:], k)):
        return True

    return False


print(do_numbers_from_list_sum_k(sample_list, k))
print(int(''))


# Another Solution
def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False
