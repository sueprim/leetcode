class Solution(object):
    def asteroidCollision(self, asteroids):
    
        i = 0
        while i < (len(asteroids)-1):

            if asteroids[i] > 0 and asteroids[i+1] < 0 and i >=0:
                
                if abs(asteroids[i]) < abs(asteroids[i+1]):
                    del asteroids[i]
                    i-= 1
                
                elif abs(asteroids[i]) > abs(asteroids[i+1]):
                    del asteroids[i+1]
                    i -= 1
            
                else:
                    del asteroids[i]
                    del asteroids[i]
                    i-= 1
            else:
                i += 1

        return asteroids
