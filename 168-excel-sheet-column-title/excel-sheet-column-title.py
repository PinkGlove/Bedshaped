class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, res = divmod(columnNumber, 26)
            ans += chr(res + ord("A"))
        return "".join(ans[::-1])