class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s= s.replace(",", "").replace(" ", "").replace(":", "")

        print(s)

        if s == s[::-1]:
            print("palindrome")
            return True
        else:
            print("Not palindrome")
            return False

text= "A man, a plan, a canal: Panama"

Solution().isPalindrome("A man, a plan, a canal: Panama")