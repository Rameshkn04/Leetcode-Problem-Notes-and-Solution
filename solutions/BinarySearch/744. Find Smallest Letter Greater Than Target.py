class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
      left, right = 0, len(letters)-1
      while left <= right:
        mid = (left + right) //2
        if letters[mid] <= target:
          left += 1
        else:
          right -=1
      return letters[left % len(letters)]

Input: letters = ["c","f","j"], target = "a"
Output: "c"
