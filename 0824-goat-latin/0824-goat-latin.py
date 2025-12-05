class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def process_word(word, i):
            if word[0] not in ("aeiouAEIOU"):
                word = word[1:]+word[0]
            
            word = word+"ma"+"a"*i
            return word
        
        return " ".join([process_word(word, i+1) for i, word in enumerate(sentence.split(" "))])

        