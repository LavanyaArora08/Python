with open('cube_series.txt', 'w') as f:
    nums = input("Enter a series of numbers")
    nums_list = nums.split(' ')
    cubes_list = [int(num) ** 3 for num in nums_list]
    print(cubes_list)
    for cube in cubes_list:
        f.write(str(cube) + '\n')
    print("Cube series written to file.")