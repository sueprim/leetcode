class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)
        
    def pop(self):
        """
        :rtype: nothing
        """
        tmp = self.stack.pop()
        if tmp == self.minStack[-1]: 
            self.minStack.pop()
            
    def top(self):
        """
        :type x: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
