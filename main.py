from window import MazeWindow, Point, Line

def main():
    win = MazeWindow(800, 600)
    l = Line(Point(100, 100), Point(200, 200))
    win.draw_line(l, "black")
    
    win.wait_for_close()

if __name__ == '__main__':
    main()