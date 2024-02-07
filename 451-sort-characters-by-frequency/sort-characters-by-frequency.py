class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Counts the frequency of each character, from collections import Counter
        char_count = Counter(s)

        # Step 2: Sort characters based on their frequency(values) in descending order
        sorted_chars = sorted(char_count, key=char_count.get, reverse=True)

        # Step 3: Build the result string by repeating characters according to their frequency
        result = ''
        for char in sorted_chars:
            result += char * char_count[char]

        # Step 4: Return the final sorted string
        return result  