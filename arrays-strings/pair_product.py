def pair_product(numbers, target_product):
    prev_nums = {}

    for index, nums in enumerate(numbers):
        pair = target_product / nums

        if pair in prev_nums:
            return(index, prev_nums[pair])
    
        prev_nums[nums] = index

print(pair_product([5,6,2,7,8,4],8))