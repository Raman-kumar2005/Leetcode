class Solution:
    def sumGame(self, nums: str) -> bool:
        length = len(nums)
        my_list = list(nums)
        def digit_sum(half_list):
            total = 0
            q_count = 0
            for char in half_list:
                if char == "?":
                    q_count += 1
                else:
                    total += int(char)
            return total, q_count
       
        left_sum, left_q = digit_sum(my_list[:length//2])
        right_sum, right_q = digit_sum(my_list[length//2:])
        if 2 * left_sum + 9 * left_q == 2 * right_sum + 9 * right_q:
            return False
        else:
            return True
