def square_sum(nums):
    return sum(x ** 2 for x in nums)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    result = square_sum(nums)
    print(f"Square sum: {result}")

