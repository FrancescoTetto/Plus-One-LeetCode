class Solution(object):
    def plusOne(self, digits):
        # Convert the digits list to a string, then to an integer
        the_number = int(''.join(map(str, digits)))
        
        # Add one to the integer
        the_number_1 = the_number + 1
        
        # Convert the resulting number back to a list of digits
        convert_back = [int(numbers) for numbers in str(the_number_1)]
        
        return convert_back

solution = Solution()
digits = [1, 2, 3]

print(solution.plusOne(digits))  # Output: [1, 2, 4]
