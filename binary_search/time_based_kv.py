class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map.keys():
            self.time_map[key] = []

        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.time_map.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]

            elif values[mid][1] < timestamp:
                left = mid + 1
                result = values[mid][0]
            
            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
