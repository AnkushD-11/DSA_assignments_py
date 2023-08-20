#Q7. Reverse a string in python

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: "!dlroW ,olleH"

#Q8. Check for palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")  # Remove spaces and punctuation, and convert to lowercase
    return s == s[::-1]

input_string = "A man, a plan, a canal, Panama!"
result = is_palindrome(input_string)
print(result)  # Output: True

#Q9. Abbreviation in python

def get_abbreviation(word):
    words = word.split()  # Split the word into individual words if it contains spaces
    abbreviation = ''.join(word[0].upper() for word in words)  # Take the first letter of each word and convert to uppercase
    return abbreviation

input_word = "central processing unit"
abbreviation = get_abbreviation(input_word)
print("Abbreviation:", abbreviation)  # Output: CPU

#Q10. Write a program to implement searching and sorting in a list of words.

def linear_search(words, target):
    for i, word in enumerate(words):
        if word == target:
            return i
    return -1

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    print("Original List:", words)

    target = "fig"
    linear_index = linear_search(words, target)
    print(f"Linear Search: '{target}' found at index {linear_index}")

if __name__ == "__main__":
    main()