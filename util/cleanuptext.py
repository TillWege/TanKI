file = open("./Docs/test1.txt")
lines = file.readlines()
checkedLines = [""]


for line in lines:
    if not (line.startswith("[") or line.startswith("")):
        checkedLines.append(line)


print(len(lines))
print(len(checkedLines))

output = open("./Docs/test1.txt", "w")
for element in checkedLines:
    output.write(element)
output.close()