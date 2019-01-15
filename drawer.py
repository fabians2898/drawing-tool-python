# drawer.py
import click
import re


class Drawer:

    def __init__(self):
        self.only_canvas = []
        self.regexs = {
            'canvas': r'C\s\d+\s\d+',
            'line': r'L\s\d+\s\d+\s\d+\s\d+'
        }

    def paint_empty_canvas(self, height, width):
        print('height: {}, width: {}'.format(height, width))
        self.only_canvas = [[0 for x in range(width)] for y in range(height)]

    def paint_line(self, x1, x2, y1, y2):
        if len(self.only_canvas) > 0:
            if x1 != y1 or x2 != y2:
                print('coordinate position is not for a straight line')

            if x1 == y1:
                diff = x2 - y2
            elif x2 == y2:
                diff = x1 - y1
            self.only_canvas[x1][x2] = 'L'
            self.only_canvas[y1][y2] = 'L'
        else:
            print('There is no canvas')
            exit()

    def write_file(self, new_line):
        f = open('output.txt','a+') # Not using 'with' just to simplify the example REPL session
        f.write(new_line + '\n')
        f.close()

@click.command()
@click.option('--file', '-f')
def main(file):
    drawer = Drawer()
    r_file = open(file, 'r')
    lines = r_file.readlines()
    for line in lines:
        if line[0] == 'C':
            p = [int(s) for s in line.split() if s.isdigit()]
            drawer.paint_empty_canvas(p[0], p[1])
            print(drawer.only_canvas)
        elif line[0] == 'L':
            x1, x2, y1, y2 = [int(s) for s in line.split() if s.isdigit()]
            drawer.paint_line(x1, x2, y1, y2)
            print(drawer.only_canvas)


if __name__ == "__main__":
    main()