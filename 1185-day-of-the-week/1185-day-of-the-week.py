class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dates = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        # this is a unique number code
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        y = year
        m = month
        if m < 3:
            y -= 1
        # this is a important folmula
        return dates[((y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + day) % 7)]

