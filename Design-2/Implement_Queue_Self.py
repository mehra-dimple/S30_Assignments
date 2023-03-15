# Time Complexity: O(1)
# Approach: Used two stacks as input and output stack.
# Input stack is being used to store push values
# Output stack is being used for pop and peek operations.
# Elements of input stack will be put in reverse order in output stack.


class MyQueue(object):

    def __init__(self):
        self.ip_stack = []
        self.op_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ip_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.op_stack == None:
            while(self.ip_stack):
                self.op_stack.append(self.ip_stack.pop())
            
        return self.op_stack.pop()


    def peek(self):
        """
        :rtype: int
        """
        if not self.op_stack:
            while(self.ip_stack):
                self.op_stack.append(self.ip_stack.pop())

        return self.op_stack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.ip_stack) == 0 and (self.op_stack) == 0:
            return True
        else:
            return False 