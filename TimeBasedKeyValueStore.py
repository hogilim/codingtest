class TimeMap:

    def __init__(self):
        self.tm = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm.append([key, value, timestamp])

    def get(self, key: str, timestamp: int) -> str:



if __name__ == "__main__":
    obj = TimeMap()
    f = ["TimeMap","set","get","get","set","get","get"]
    s = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
    output = [[]]
    for i in range(1,len(f)):
        if f[i] == "set":
            output.append(obj.set(s[i][0], s[i][1], s[i][2]))
        if f[i] == "get":
            output.append(obj.get(s[i][0], s[i][1]))
    print(output)
