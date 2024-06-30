import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    p = 2 * dy - dx
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))
        if p < 0:
            p = p + 2 * dy
        else:
            y = y + 1
            p = p + 2 * dy - 2 * dx
    return points
  
def main():
    x1, y1 = map(int, input("Enter starting point (x1 y1): ").split())
    x2, y2 = map(int, input("Enter ending point (x2 y2): ").split())
    points = draw_line(x1, y1, x2, y2)
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bresenham Line Drawing Algorithm')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
