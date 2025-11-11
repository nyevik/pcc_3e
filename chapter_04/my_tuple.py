#tuple is an immutable list
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

print(dimensions[0])
print(dimensions[1])
#what happens if we try to change a value?
#dimensions[0] = 250  # This will raise a TypeError because tuples are immutable