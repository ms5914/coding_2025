class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count_words = Counter(words)
        words_taken_count = 0
        centre = False
        for word, count in count_words.items():
            if word[0] == word[1]:
                if count%2 == 0:
                    words_taken_count+=count
                else:
                    words_taken_count+=(count-1)
                    centre = True
            elif word[0]<word[1]:
                words_taken_count+=2*min(count, count_words[word[1]+word[0]])
        return words_taken_count*2 + 2 if centre else words_taken_count*2


        #you can also use a matrix of size 26*26. Each element showing the count of word a[i]+a[j]


        