# Data Validation

# Using filter(), return only elements that:
# Contain only alphabets
# AND have length greater than 3



def check_data(value):
    return value.isalpha() and len(value) > 3
data = ["Raj", "123", "Aman", "45B", "Riya", "007"]   

result = list(filter(check_data,data))
print(result)