def count_vowels(name):
    vowels = "aeiou"
    count = 0
    for i in vowels:
        if i in name:
            count += 1
    return count

def check_acceptance(name):
    vowels = "aeiou"  # Defining vowels again
    vowel_count = count_vowels(name)
    
    if vowel_count == len(vowels):  # All vowels are present
        print("Accepted")
    else:
        print("Rejected")

# Main program
name = input("Enter your name: ")

check_acceptance(name)
