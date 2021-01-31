# BEGIN (write your solution here)
from operator import sub


def get_sum_crossing(interval, intervals):
    start = interval[0]
    finish = interval[1]
    sum_of_crossing = - sub(finish, start)
    for i in intervals:
        if i[0] <= start and finish <= i[1]:
            sum_of_crossing += sub(finish, start)
        elif i[0] < start <= i[1]:
            sum_of_crossing += sub(i[1], start)
    return sum_of_crossing


def sum_of_intervals(intervals):
    sum_of_crossing = []
    for interval in intervals:
        sum_of_crossing.append(get_sum_crossing(interval, intervals))
    sum_of_all_intervals = sum(map(lambda x: x[1] - x[0], intervals))
    return sub(sum_of_all_intervals, sum(sum_of_crossing))
# END
