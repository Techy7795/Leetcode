class Solution:
    def generate(self, open_count: int, close_count: int, n: int, current: str, ans: list):
        """
        A recursive helper function to generate all combinations
        of balanced parentheses.

        :param open_count: The number of open parentheses used so far.
        :param close_count: The number of close parentheses used so far.
        :param n: The total number of pairs of parentheses.
        :param current: The current string being built.
        :param ans: The list storing all valid combinations.
        """
        # Base case: if the number of open and close parentheses used
        # is equal to the total number of pairs, add the string to the result.
        if open_count == close_count == n:
            ans.append(current)
            return

        # If the number of open parentheses used is less than the total
        # number of pairs, add an open parenthesis and call the function recursively.
        if open_count < n:
            self.generate(open_count + 1, close_count, n, current + '(', ans)

        # If the number of close parentheses used is less than the number
        # of open parentheses, add a close parenthesis and call the function recursively.
        if close_count < open_count:
            self.generate(open_count, close_count + 1, n, current + ')', ans)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # Start the recursive generation with initial values
        self.generate(0, 0, n, "", ans)
        return ans
    
        