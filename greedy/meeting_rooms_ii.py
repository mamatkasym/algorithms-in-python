"""
Given an array of meeting time intervals `intervals` where intervals[i] = [start_i, end_i], return the minimum number
of conference rooms required.
Source: https://leetcode.com/problems/meeting-rooms-ii/
"""


def min_meeting_rooms(intervals: list[tuple[int, int]]) -> int:
    start_times = [interval[0] for interval in intervals]
    end_times = [interval[1] for interval in intervals]

    start_times.sort()
    end_times.sort()
    # pointers to start_times and end_times, and number of rooms required
    s = e = rooms = 0
    rooms = 0
    while s < len(intervals):
        # free up rooms whenever the conference is finished
        if start_times[s] >= end_times[e]:
            e += 1
            rooms -= 1
        s += 1
        rooms += 1
    return rooms
