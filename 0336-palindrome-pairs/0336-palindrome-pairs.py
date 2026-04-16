class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        word_map = {}
        for i in range(len(words)):
            word_map[words[i]] = i

        result = []

        def is_pal(s):
            return s == s[::-1]

        for i in range(len(words)):
            word = words[i]

            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if is_pal(left):
                    rev = right[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([word_map[rev], i])

                if j != len(word) and is_pal(right):
                    rev = left[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([i, word_map[rev]])

        return result