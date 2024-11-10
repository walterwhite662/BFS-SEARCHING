import curses
from curses import wrapper
import queue
import time
maze = [
    ["#", "0", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "x", "#"]
]
def print_maze(maze,stdscr,path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_path(2)

    for i , row in enumerate(maze):
        for j,value in enumerate(row):
            if(i,j)in path:
                stdscr.addstr(i,j*2,value,RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)
def find_start(maze_start):
    for i ,row in enumerate(maze):
        for j , value in enumerate(row):
            if value == start:
                return i,j
    return None        
            
            

def find_path(maze,stdscr):
    start = "0"
    end ="x"
    start_pos = find_start(maze,start)

    q = queue.Queue()
    q.put((start_pos,[start_pos]))
    visited = set()
    while not q.empty():
        current_pos,path=q.get()
        row,col = current_pos
        stdscr.clear()
        print_maze(maze,stdscr)
        stdscr.refresh()
        if maze[row][col]==end:
            return path
        neighbour = find_neighbour(maze,row,col)
        for neighbours in neighbour:
            if neighbours in visited:
                continue
            r,c= neighbours
            if maze[r][c]=="1":
                continue

            new_path = path + [neighbours]
            q.put((neighbours,new_path))
            visited.add(neighbours)
            
        

def find_neighbour(maze,row,col):
    neighbour = []

    if row > 0:
        neighbour.append((row - 1,col))
    if row + 1 < len(maze):
        neighbour.append((row+1,col))
    if col > 0:
        neighbour.append((row,col-1))
    if col + 1 < len(maze[0]):
        neighbour.appen((row,col+1))
        
            
def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    find_path(maze,stdscr)
    
   
    stdscr.getch()

wrapper(main)    
    
