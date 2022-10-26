
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    count = []
    times = 0
    for i in range(len(nums)):
        print(nums[i])
        for j in reversed(nums):
            print(j)
            if nums[i] > j:
                times += 1
        count.append(times)
        times = 0


    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    smallerNumbersThanCurrent(nums)