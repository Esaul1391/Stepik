class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_list = []
        insert_list = newInterval

        for i in intervals:
            # Если текущий интервал не пересекается с новым, добавляем его в результат
            if insert_list[1] < i[0]:
                new_list.append(insert_list)
                new_list.extend(intervals[intervals.index(i):])
                return new_list
            elif insert_list[0] > i[1]:
                new_list.append(i)
            else:
                # Обновляем границы вставляемого интервала, объединяя его с текущим интервалом
                insert_list = [min(insert_list[0], i[0]), max(insert_list[1], i[1])]

        # Добавляем последний объединенный интервал
        new_list.append(insert_list)
        return new_list





s = Solution()
sp = [[1,2],[3,5],[6,7],[8,10],[12,16]]
print(s.insert(sp, [4,8]))