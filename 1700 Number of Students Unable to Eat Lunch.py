class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #brute
        students = deque(students)
        sandwiches = deque(sandwiches)
        check = True
        idx = 0
        while check : 
            check = False
            if len(sandwiches) != 0 :
                idx = sandwiches[0]
            for i in range(len(students)) : 
                temp = students.popleft()
                if idx == temp : 
                    sandwiches.popleft()
                    check = True
                    break
                else : 
                    students.append(temp)
        return len(sandwiches) 
