from collections import defaultdict

def group_anagrams(words):
    # Outer dictionary to group by sorted characters
    anagram_groups = defaultdict(lambda: defaultdict(int))

    for word in words:
        # Sort the word to form the key
        sorted_word = ''.join(sorted(word))
        
        # Increment the count of the word in the inner dictionary
        anagram_groups[sorted_word][word] += 1

    return anagram_groups

# Example usage
words = ["listen", "silent", "enlist", "rat", "tar", "art", "cheat", "teach", "cat", "act"]
result = group_anagrams(words)

# Print the results
for key, value in result.items():
    print(f"Key (Sorted): {key} -> {dict(value)}")
