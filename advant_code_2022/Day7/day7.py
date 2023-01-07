#Input:
P = ['A','B','C','D','E','F','G']
R = [('A','B'),('B','C'),('A','C'),('D','C'),('D','E'),('F','G')]

N = len(P)
cluster = {}
q = []
c = 1
for i in range(N):    
    if P[i] not in cluster:
        q.append(P[i])
        cluster[P[i]] = c 
        while len(q) != 0:    
            head = q.pop(0)
            for j in range(N):
                if (head,P[j]) in R or (P[j],head) in R:
                    if P[j] not in cluster:
                        q.append(P[j])                         
                        cluster[P[j]] = c 
        c = c + 1
print(cluster)
