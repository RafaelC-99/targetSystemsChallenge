stringValue = str(input("Enter with a string: "))
i=len(stringValue)-1
reversedString = ""
while(i>=0):
    reversedString += stringValue[i]
    i-=1
    

print("Original value: " + stringValue)
print("Reversed value: " + reversedString)