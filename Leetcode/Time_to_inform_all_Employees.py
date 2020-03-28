class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = {}
        start = 0
        for i in range(len(manager)):
            if(manager[i] == -1): start = i
            if(manager[i] not in d):
                d[manager[i]] = [i]
            else:
                d[manager[i]].append(i)
        def dfs(curnode):
            answer = 0
            if(curnode not in d):
                return 0;
            for i in range(len(d[curnode])):
                mosttime = informTime[curnode] + dfs(d[curnode][i])
                answer = max(answer, mosttime)
                
            return answer
        return dfs(start)
