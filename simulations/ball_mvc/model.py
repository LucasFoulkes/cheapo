class Ball:
    def __init__(self, x, y, dx, dy, radius, gravity):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.gravity = gravity

    def update(self, dt, screen_width, screen_height):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.dy += self.gravity * dt

        if self.x > screen_width - self.radius or self.x < self.radius:
            self.dx *= -1
            self.x = max(self.radius, min(screen_width - self.radius, self.x))

        if self.y > screen_height - self.radius or self.y < self.radius:
            self.dy *= -0.8 if self.y > screen_height - self.radius else -1
            self.dx *= 0.8 if self.y > screen_height - self.radius else 1
            self.y = max(self.radius, min(screen_height - self.radius, self.y))
