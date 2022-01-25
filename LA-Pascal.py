class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascal_list = [[1]]

        if numRows == 1:
            return pascal_list
        else:
            for i in range(1, numRows):
                check_list = pascal_list[-1]
                mid_list = []
                for element in range(len(check_list) - 1):
                    mid_list.append(check_list[element] + check_list[element + 1])

                pascal_list.append([1] + mid_list + [1])

        return pascal_list