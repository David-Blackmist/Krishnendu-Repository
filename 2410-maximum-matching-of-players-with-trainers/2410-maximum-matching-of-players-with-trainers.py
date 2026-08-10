class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        i=0
        j=0
        count=0
        m=len(players)
        n=len(trainers)
        while i<m and j<n:
            if players[i]<=trainers[j]:
                count +=1
                i +=1
                j +=1
            elif players[i]> trainers[j]:
                j +=1
        return count

                