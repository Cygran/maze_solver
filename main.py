from window import MazeWindow, Point, Line
from cell import Cell

def main():
    win = MazeWindow(800, 600)
    
    cell1 = Cell(win, 100, 100, 200, 200)
    cell1.draw()
    
    cell2 = Cell(win, 200, 100, 300, 200)
    cell2.has_right_wall = False
    cell2.draw()

    cell3 = Cell(win, 300, 100, 400, 200)
    cell3.has_top_wall = False
    cell3.has_bottom_wall = False
    cell3.draw()
    
    cell4 = Cell(win, 400, 100, 500, 200)
    cell4.has_left_wall = False
    cell4.has_right_wall = False
    cell4.draw()
    
    win.wait_for_close()

if __name__ == '__main__':
    main()