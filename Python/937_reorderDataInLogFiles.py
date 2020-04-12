'''You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered
lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 '''


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = list()
        nonLetterLogs = list()
        for each in logs:
            curr = each.split(' ')
            if curr[1].isdigit():
                nonLetterLogs.append(each)
            else:
                letterLogs.append(curr)
        letterLogs.sort(key=lambda x: (x[1:], x[0]))
        result = list()
        for each in letterLogs:
            curr = ' '.join(each)
            result.append(curr)
        result += nonLetterLogs

        return result