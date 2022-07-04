str1 = input("Podaj jakiś wyraz: ")
str2 = str1[-1] + str1[1:len(str1)-1] + str1[0]
print("Odwrócony napis: ", str2)