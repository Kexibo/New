def minimumsum(num):
    d1 = num // 1000
    d2 = (num % 1000) // 100
    d3 = (num % 100) // 10
    d4 = num % 10

    nums = [d1,d2,d3,d4]
    nums = sorted(nums)

    num1 = nums[0] * 10 + nums[2]
    num2 = nums[1] * 10 + nums[3]

    return num1 + num2


print(minimumsum(2931))