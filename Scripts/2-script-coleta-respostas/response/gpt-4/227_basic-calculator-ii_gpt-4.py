class Solution:
    def calculate(self, s):
        stack = []
        current_number = 0
        operation = '+'
        s = s.replace(' ', '')
        
        for i in range(len(s)):
            if s[i].isdigit():
                current_number = current_number * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack[-1] = stack[-1] * current_number
                elif operation == '/':
                    stack[-1] = int(stack[-1] / current_number)
                operation = s[i]
                current_number = 0
        
        return sum(stack)