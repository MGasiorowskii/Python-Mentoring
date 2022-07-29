data = {}

while input:
    key = input("Input name of city: ")
    value = (input("Input number of degrees: "))

    if key == "" or value == "":
        break

    if key in data.keys():
        data[key] += float(value)
    else:
        data[key] = float(value)


print(data)

