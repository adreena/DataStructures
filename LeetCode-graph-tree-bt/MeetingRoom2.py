'''
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
'''
import heapq
def meetingRooms(times):
    times.sort(key=lambda x: x[0])
    rooms = [times[0][1]]
    for time in times:
        if time[0] >= rooms[-1]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, time[1])
    return len(rooms)
