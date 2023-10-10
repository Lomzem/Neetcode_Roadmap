class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.time_map.keys():
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])

    # {"foo": [["bar", 1], ["bar2", 3], ["bar3", 4], ["bar4", 5]}

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.time_map[key]) - 1
        if len(self.time_map[key]) == 0:
            return ""

        nearest = (left + right) // 2

        while left <= right:
            mid = self.time_map[key][(left + right) // 2]
            if mid > timestamp:
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
