class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda meeting:meeting[0])

        # Priority queue for available rooms
        availableRooms = list(range(n))
        heapq.heapify(availableRooms)

        # Priority queue for next available room sorted by the time it becomes available again
        nextMeetingEnd = []

        # Dict that represents the amount of times each room was used
        data = {i: 0 for i in range(n)}

        time = 0
        index = 0
        # Loops over until all meetings have been concluded
        while index < len(meetings):
            # Updates time
            time = max(time, meetings[index][0])

            # Update available meetings if one or more of the meetings had finished
            while len(nextMeetingEnd) > 0 and nextMeetingEnd[0][0] <= time:
                nextMeeting = heapq.heappop(nextMeetingEnd)
                heapq.heappush(availableRooms, nextMeeting[1])

            # Handle next meeting with an available Room
            if len(availableRooms) != 0:
                nextRoom = heapq.heappop(availableRooms)
                meeting = meetings[index]
                index += 1
                heapq.heappush(nextMeetingEnd, (time + (meeting[1] - meeting[0]), nextRoom))
                data[nextRoom] += 1
            else:
                nextMeeting = heapq.heappop(nextMeetingEnd)
                # Push room to available rooms priority queue
                heapq.heappush(availableRooms, nextMeeting[1])
                time = nextMeeting[0]

        return max(data, key=data.get)