# Mathematical Transformation with Two Lists

def topower(num,power):
    return num**power

nums = [1,2,3,4]
powers = [2,3,4,5]

result = list(map(topower,nums,powers))
print(result)

