from array import *
from numpy import *
end_point = 105
rows, cols = (250, 250)
dx = array([1,0,0,-1])
dy = array([0,1,-1,0])
Direction = array(['e','n','s','w'])
sta = [0] * 30
num = array([0,3])

def check_direction(x, y, pos):
    global ans, result
    if(pos == n+1):
        if(x == end_point and y == end_point):
            ans = ans + 1
            result += Direction[sta[1]]
            for i in range(2,n+1):
                result += Direction[sta[i]]
                
def is_visited(xx, yy):
    return vis[xx][yy]

def mark_as_visited(xx, yy):
    vis[xx][yy] = True

def mark_as_unvisited(xx, yy):
   vis[xx][yy] = False
   
def dfs(x, y, pos, path):
    check_direction(x, y, pos)
    step = 0
    for i in range(pos, n+1):
        step += i
    if (abs(x-end_point) + abs(y-end_point)) > step :
        return
    if(path == -1):
            for i in range(0,4):
                xx = x + pos*dx[i]
                yy = y + pos*dy[i] 
                if is_visited(xx, yy):
                   continue
                k = 0
                if(1 <= i and i < 3):
                    for k in range(min(y, yy),max(y, yy)+2):
                        if(gra[xx][k]):
                            break
                    if(k == max(y, yy) + 1): 
                        sta[pos] = i
                        mark_as_visited(xx, yy)
                        dfs(xx, yy, pos+1, 1)
                        mark_as_unvisited(xx, yy)
                else:
                    for k in range(min(x, xx),max(x, xx)+2):
                        if(gra[k][yy]):
                            break
                    if(k == max(x, xx) + 1):
                        sta[pos] = i
                        mark_as_visited(xx, yy)
                        dfs(xx, yy, pos+1, 0)
                        mark_as_unvisited(xx, yy)
    else:
            if(path == 0):
                for i  in range(1,3):
                    xx = x + pos*dx[i]
                    yy = y + pos*dy[i]
                    if is_visited(xx, yy):
                        continue
                    k = 0
                    for k in range(min(y, yy), max(y, yy)+2):
                        if(gra[xx][k]):
                           break
                    if(k == max(y, yy) + 1):
                        sta[pos] = i
                        mark_as_visited(xx,yy)
                        dfs(xx, yy, pos+1, 1)
                        mark_as_unvisited(xx, yy)
            elif(path == 1):
                for j  in range(0,2):
                    i = num[j]
                    xx = x + pos*dx[i]
                    yy = y + pos*dy[i]
                    if is_visited(xx, yy):
                       continue
                    k = 0
                    for k in range(min(x, xx), max(x, xx)+2):
                        if(gra[k][yy]):
                           break						
                    if(k == max(x, xx) + 1):
                        sta[pos] = i
                        mark_as_visited(xx, yy)
                        dfs(xx, yy, pos+1, 0)
                        mark_as_unvisited(xx, yy)
    return ans

def create_grid():
    a = [0] * 62500
    return reshape(a, ( 250, 250))

def create_visited_grid():
    b = [False] * 62500
    return reshape(b, (250, 250))

test_cases = 2
l1 = [-2, 0, 6, -2]
l2 = [2, 1, -2, 0]
while test_cases :
    ans = 0
    result = ""
    gra = create_grid()
    vis = create_visited_grid()
    n = 8
    k = 2
    if test_cases == 2 :
           for i in range(0,k):
                if i == 0 :
                     x, y = l1[0], l1[1]          
                else :
                     x, y = l1[2], l1[3]
                if(abs(x) > end_point or abs(y) > end_point):
                   continue  
                gra [end_point + x][end_point + y] = 1
    else :
           for i in range(0, k):
               if i == 0 :
                   x, y = l2[0], l2[1]          
               else :
                  x, y = l2[2], l2[3]
               if(abs(x) > end_point or abs(y) > end_point):
                  continue  
               gra [end_point + x][end_point + y] = 1       
    m = dfs(end_point, end_point, 1, -1)
    print("%s\n"%result)
    print("Found %d golygon(s)."%m)
    test_cases -= 1
