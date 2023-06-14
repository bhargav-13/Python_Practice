# *args       = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#                      * unpacking operator
#     1.Default arguments(like c++)  2. keyword Arguments(python feature) 3.arbitory argument(python feature) 4. positioning arg(simple that we use in c++)
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3,4))

def print_adress(**kargs):
    for value in kargs.values():
        print(f"{value}", end=",")

print_adress(street="kailas nagar", city="junagadh", state="gujarat")