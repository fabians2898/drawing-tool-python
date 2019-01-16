# drawer.py
import click


class Drawer:

    def __init__(self):
        self.only_canvas = []

    def create_canvas(self, height, width):
        self.only_canvas = [['' for x in range(height)] for y in range(width)]
        for index,row in enumerate(self.only_canvas):
            if index == 0 or index == len(self.only_canvas)-1:
                self.only_canvas[index] = ['#' for x in self.only_canvas[index]]
            row[0], row[-1] = '#', '#'

    def paint_line(self, x1, x2, y1, y2):
        if len(self.only_canvas) > 0:
            if x1 != y1 and x2 != y2:
                print('positions doesn\'t work for a straight line')
                exit()

            try:
                self.only_canvas[x2][x1] = 'L'
            except Exception as err:
                print('Line cannot be painted')
                exit()

            try:
                self.only_canvas[y2][y1] = 'L'
            except Exception as err:
                print('Line cannot be painted')
                exit()

        else:
            print('There is no canvas')
            exit()

    def write_file(self, new_line):
        f = open('output.txt','a+') # Not using 'with' just to simplify the example REPL session
        f.write(new_line + '\n')
        f.close()

    def print_canvas(canvas):
        print([''.join(map(str, x)) for x in canvas])

@click.command()
@click.option('--file', '-f')
def main(file):
    drawer = Drawer()
    r_file = open(file, 'r')
    lines = r_file.readlines()
    for line in lines:
        if line[0] == 'C':
            p = [int(s)+2 for s in line.split() if s.isdigit()]
            drawer.create_canvas(p[0], p[1])
            for row in drawer.only_canvas:
                print(row)
        elif line[0] == 'L':
            x1, x2, y1, y2 = [int(s) for s in line.split() if s.isdigit()]
            print(x1, x2, y1, y2)
            drawer.paint_line(x1, x2, y1, y2)
            for row in drawer.only_canvas:
                print(row)

if __name__ == "__main__":
    main()