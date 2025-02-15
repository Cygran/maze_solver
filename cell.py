from window import Point, Line

class Cell:
    def __init__(self, window, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

    def draw(self):
        if self.has_left_wall:
            self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_top_wall:
            self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_right_wall:
            self._window.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))

    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "darkgray"
        center = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        to_center = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        self._window.draw_line(Line(center, to_center), fill_color=color)