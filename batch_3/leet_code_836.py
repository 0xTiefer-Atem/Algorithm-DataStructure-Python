"""
矩形重叠-逆向思维

矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x 轴，左右边平行于 y 轴。

如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。


示例 1：

输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true


示例 2：

输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false


示例 3：

输入：rec1 = [0,0,1,1], rec2 = [2,2,3,3]
输出：false

"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2

        if rec1_x1 == rec1_x2 or rec1_y1 == rec1_y2 or rec2_x1 == rec2_x2 or rec2_y1 == rec2_y2:
            return False

        if rec1_x1 >= rec2_x2 or rec1_x2 <= rec2_x1 or rec1_y2 <= rec2_y1 or rec1_y1 >= rec2_y2:
            return False

        return True


if __name__ == '__main__':
    # rec1 = [0, 0, 1, 1]
    # rec2 = [1, 0, 2, 1]


    # true
    rec1 = [7, 8, 13, 15]
    rec2 = [10, 8, 12, 20]

    s = Solution()

    print(s.isRectangleOverlap(rec1, rec2))
