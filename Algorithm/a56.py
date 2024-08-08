class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Сортируем интервалы по начальной точке
        intervals.sort(key=lambda x: x[0])
        res = []
        count_intervals = 0
        interval = []

        while count_intervals < len(intervals):
            if not interval:
                interval = intervals[count_intervals]
                count_intervals += 1
                continue

            current_interval = intervals[count_intervals]

            # Если текущий интервал пересекается с последним добавленным, объединяем их
            if interval[1] >= current_interval[0]:
                interval[1] = max(interval[1], current_interval[1])
            else:
                # Добавляем не пересекающийся интервал в результат
                res.append(interval)
                interval = current_interval

            count_intervals += 1

        # Добавляем последний интервал
        res.append(interval)
        return res


s = Solution()
sp = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(sp))