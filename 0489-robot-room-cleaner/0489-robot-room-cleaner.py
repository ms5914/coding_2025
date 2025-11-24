# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def clean(x, y, index):
            # print(x, y)
            # print(visited)
            robot.clean()
            visited.add((x, y))
            
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for i in range(4):
                new_index = (i+index)%4
                new_x = x+directions[new_index][0]
                new_y = y+directions[new_index][1]
                if not (new_x, new_y) in visited:
                    if robot.move():
                        clean(new_x, new_y, new_index)
                        go_back()
                robot.turnRight()
        
        clean(0, 0, 0)
                

                    


        