'''Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code.
This represents the result of splitting the original source code string by the newline character \n.'''


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        comment = False
        result = list()
        for each in source:
            j = 0
            if not comment:
                current = ''
            while j < len(each):
                if each[j:j+2] == '/*' and not comment:
                    comment = True
                    j += 2
                elif each[j:j+2] == '*/' and comment:
                    comment = False
                    j += 2
                elif not comment and each[j:j+2] == '//':
                    break
                elif not comment:
                    current += each[j]
                    j += 1
                else:
                    j += 1
            if current and not comment:
                result.append(current)

        return result