def solution(n):
    num = 1
    length = n
    ans = [ [0]*n for _ in range(n)]
    
    stopAt = 0
    for i in range(n+1): stopAt += i
    
    idx = 0
    while num <= stopAt:
        # down
        for i in range(idx*2, length):
            if num <= stopAt and ans[i][idx] == 0: 
                ans[i][idx] = num
                num += 1
            else : break
            
        # right
        for i in range(idx+1,length):
            if num <= stopAt and ans[n-idx-1][i] == 0 : 
                ans[n-idx-1][i] = num
                num += 1
            else : break
            
        # left up
        for i in range(0, length):
            if num <= stopAt and ans[n-(idx+2)-i][n-(idx*2+2)-i] == 0: 
                ans[n-(idx+2)-i][n-(idx*2+2)-i] = num
                num += 1
            else : break
        idx += 1
        
    result = []
    for a in ans:
        for i in a:
            if i != 0 : result.append(i)
        
    return result