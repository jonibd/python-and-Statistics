matrix = []

for i in range(3):
    row = list(map(int, input(f"Row {i+1}:").split()))
    matrix.append(row)

print("Matrix is:")
for row in matrix:
    print(row)


