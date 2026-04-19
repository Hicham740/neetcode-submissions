class Solution:
    def isPalindrome(self, s: str) -> bool:
        k ="";
        s =s.lower();
        t =''.join(ch for ch in s if ch.isalnum())

        return t == t[::-1]
        
