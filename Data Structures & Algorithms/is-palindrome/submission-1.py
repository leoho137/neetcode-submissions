class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.lower().replace(" ", "")
        valid = True
        head = 0
        tail = len(new) - 1
        while tail - head >= 1:
            if new[tail] > 'z' or new[tail] < 'a' and (new[tail] > '9' or new[tail] < '0'):
                tail -= 1
            elif new[head] > 'z' or new[head] < 'a' and (new[head] > '9' or new[head] < '0'):
                head += 1
            elif new[tail] == new[head]:
                head += 1
                tail -= 1
            else:
                return False
        return True