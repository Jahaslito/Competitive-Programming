class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        size = len(words)
        wordIndex = {}

        for i in range(size):
            index = words[i][-1]
            word = words[i].replace(index, "")
            wordIndex[index] = word
        sortedWordIndex = sorted(wordIndex.items())
        sentence = []
        for j in range(len(sortedWordIndex)):
            sentence.append(sortedWordIndex[j][1])
            
        return " ".join(sentence)
