def find_index_of_nearest(num, nums):
    if nums:
        sub = list(map(lambda x: abs(x - num), nums))
        return sub.index(min(sub))
