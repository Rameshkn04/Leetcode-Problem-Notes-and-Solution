class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            # pack words into the line
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            gaps = j - i - 1
            line = ""

            # last line OR only one word → left justified
            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                space_each = total_spaces // gaps
                extra = total_spaces % gaps

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (space_each + (1 if extra > 0 else 0))
                    if extra > 0:
                        extra -= 1
                line += words[j - 1]

            res.append(line)
            i = j

        return res
