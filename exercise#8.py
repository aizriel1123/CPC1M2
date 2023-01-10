data = [5, 3, 7]

print(data[2])  # 7
print(data[-1])  # 7
print(len(data))  # 3
print(data[0:2])  # [5, 3]
print(0 in data)  # False
print(data + [2, 10, 5])  # [5, 3, 7, 2, 10, 5]
print(tuple(data))  # (5, 3, 7)

data[0] = -data[0]
data.append(10)
data.insert(2, 22)
del data[1]
data.sort()

print(data)  # [-5, 7, 10, 22]