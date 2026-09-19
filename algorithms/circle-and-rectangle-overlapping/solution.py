class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter<x1:
            close_x=x1
        elif xCenter>x2:
            close_x=x2
        else:
            close_x=xCenter

        if yCenter<y1:
            close_y=y1
        elif yCenter>y2:
            close_y=y2
        else:
            close_y=yCenter

        dist_x=abs(close_x-xCenter)
        dist_y=abs(close_y-yCenter)

        if (dist_x**2+ dist_y**2)<=radius**2:
            return True
        return False