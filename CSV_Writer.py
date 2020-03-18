
# Open-source, you can use it, i guess.

cols = int(input("How many columns?"))
entries = 0
headings = []
endwrite = []
temp = ""
for i in range(1, int(cols) + 1):
    headings.append(input("Column " + str(i) + " header: "))
    temp = temp + headings[-1] + ","
temp = temp[0:-1] + "\n"
endwrite.append(temp)

ans = ""
while ans.lower() != "f":
    if ans != "spec":
        ans = input("(C)reate a new entry or (F)inish the file or (U)ndo last entry: ")
    else:
        ans = "c"
    if ans.lower() == "c":

        temp = ""
        for i in range(0, cols):
            temp = temp + input("Entry " + str(entries) + " value for " + headings[i] + ": ") + ","
        temp = temp[0:-1] + "\n"
        endwrite.append(temp)
        entries = entries + 1

    elif ans.lower() == "u":
        endwrite.remove(endwrite[-1])
        print("Entry " + str(entries) + " Deleted.")
        entries = entries - 1
    elif ans.lower() == "f":
        continue
    else:
        print("Invalid answer. Defaulting to creation of an entry.")
        ans = "spec"
        continue

print("The output .csv file is ready. Provide a name.")
ans = input(">> ")
endfile = open(ans + ".csv", "w")
endfile.writelines(endwrite)
print(ans + ".csv has been written.")
