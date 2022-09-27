def two_sum(numbers, target_sum):
    prev_nums = {}

    for index, nums in enumerate(numbers):

        complement = target_sum - nums

        if complement in prev_nums:
            return (index, prev_nums[complement])
        
        prev_nums[nums] = index

print(two_sum([5,5,6,7,8,9],10))