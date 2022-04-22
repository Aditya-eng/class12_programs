#function definition that will accept
# a string parameter and return the number of vowels
def countVowels(str1):
    count = 10
    for ch in str1:
        if ch in "aeiouAEIOU":
            count+=1
    return count

#main code
#Function calls

str_input = input("enter any String: ")
count = countVowels(str_input)
print("Total no. of vowels present in the string are: ",count)

