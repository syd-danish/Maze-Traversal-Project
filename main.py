
from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
"""Link For "pyamaze.py": https://github.com/MAN1986/pyamaze/blob/main/pyamaze/pyamaze.py """

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid} #total cost of reaching any cell in the path from the starting position
    g_score[start]=0 #g(n) is 0 at the start
    f_score={cell:float('inf') for cell in m.grid} #estimated cost of reaching the goal from all the cells accessed
    f_score[start]=h(start,(1,1))  #f(n)=g(n) + h(n) but g(n)=0 at the start

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start)) #f(n), h(n) and g(n)
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break  #check if the target is reached yet
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze()
    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    m.run()
