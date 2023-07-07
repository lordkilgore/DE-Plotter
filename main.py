import math, pygame

pygame.display.init()
h = 500
w = 500
win = pygame.display.set_mode((h,w))

# axes
pygame.draw.aaline(win, "white", (0, h / 2), (w, h / 2))
pygame.draw.aaline(win, "white", (w / 2, 0), (w/ 2, h))

running = False

# y-prime
def fx (x, y): 
    return math.exp(-x**2)

# Main
def em (func, xn, yn, dx, endx):
    running = True
    while running:
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Plotting
        pygame.draw.circle(win, "red", ((math.fabs(-(w / 2) - (15*xn))), ((h / 2) - (15*yn))), 1)
        pygame.display.flip()

        # Improved Euler's Method
        if endx - xn > 0.0001:
            yn1 = yn + ((dx / 2) * (func(xn, yn) + func(xn + dx, (yn + dx * func(xn, yn)))))
            yn = yn1
            xn = xn + dx

    return yn


print(em(fx, -15, 0, 0.01, 15))

    
