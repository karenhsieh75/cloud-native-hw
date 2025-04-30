def square_sum(nums):
    try:
        return sum(int(x) ** 2 for x in nums)
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = square_sum(nums)
    print(f"Square sum of {nums} = {result}")