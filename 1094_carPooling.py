'''You are driving a vehicle that has capacity empty seats initially available for passengers.
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip:
the number of passengers that must be picked up, and the locations to pick them up and drop them off.
The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. '''


import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = list()
        cap = 0
        for n, s, e in trips:
            while heap and heap[0][0] <= s:
                cap -= heap[0][1]
                heapq.heappop(heap)
            heapq.heappush(heap, (e, n))
            cap += n
            if cap > capacity:
                return False
        return True