'''Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".'''

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new_str = ''
        for each in address:
            if each == '.':
                new_str = new_str + '[' + '.' + ']'
            else:
                new_str += each
        return new_str