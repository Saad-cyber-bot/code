for x in range(50):
    if x == 5:
        print(x)
    else:
        pass

print(next((x for x in range(50) if x == 5), None))