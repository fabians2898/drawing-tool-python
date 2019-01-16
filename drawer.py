# drawer.py
import click


class Drawer:

    def __init__(self):
        self.only_canvas = []

    def create_canvas(self, height, width):
        self.only_canvas = [[' ' for x in range(height)] for y in range(width)]
        for index,row in enumerate(self.only_canvas):
            if index == 0 or index == len(self.only_canvas)-1:
                self.only_canvas[index] = ['-' for x in self.only_canvas[index]]
            row[0], row[-1] = '|', '|'

    def paint_line(self, x1, x2, y1, y2):
        if len(self.only_canvas) > 0:
            if x1 != y1 and x2 != y2:
                print('positions doesn\'t work for a horizontal/vertical line')
                exit()

            try:
                if x2 == y2: # checking if positions are for horizontal line
                    temp = x1
                    while temp <= y1:
                        self.only_canvas[x2][temp] = 'x'
                        temp += 1

                elif x1 == y1: # checking if positions are for vertical line
                    temp = x2
                    while temp <= y2:
                        self.only_canvas[temp][x1] = 'x'
                        temp += 1
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

    def write_canvas_file(self, canvas):
        f = open('output.txt','a+') # Not using 'with' just to simplify the example REPL session
        for row in canvas:
            f.write(' '.join(row) + '\n')
        f.write('\n')
        f.close()


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
            drawer.write_canvas_file(drawer.only_canvas)
        elif line[0] == 'L':
            x1, x2, y1, y2 = [int(s) for s in line.split() if s.isdigit()]
            drawer.paint_line(x1, x2, y1, y2)
            drawer.write_canvas_file(drawer.only_canvas)

if __name__ == "__main__":
    main()