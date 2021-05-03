dict = {"banana": 900, "apple": 370, "orange": 250}

print(dict["banana"])

print("banana" in dict)

print("keys")
for k in dict.keys():
    print(k)

print("values")
for v in dict.values():
    print(v)

print("keys and values")
for k, v in dict.items():
    print(k, v)
