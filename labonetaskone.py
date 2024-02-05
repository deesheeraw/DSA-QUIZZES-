

def summation(arr):
    return sum(arr)

def maximum(arr):
    return max(arr)

n = int(input("Enter the length of the array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter an integer: ")))

print("Sum of the integers in the array:", summation(arr))
print("Largest integer in the array:", maximum(arr))