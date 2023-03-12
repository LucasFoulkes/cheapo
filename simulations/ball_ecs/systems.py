class BallSystem:
    def __init__(self, entities, dt, screen_width, screen_height):
        self.entities = entities
        self.dt = dt
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        for entity in self.entities:
            ball = entity.ball
            ball.x += ball.dx * self.dt
            ball.y += ball.dy * self.dt
            ball.dy += ball.gravity * self.dt

            if (
                ball.x > self.screen_width - ball.radius
                or ball.x < ball.radius
            ):
                ball.dx *= -1
                ball.x = max(
                    ball.radius, min(self.screen_width - ball.radius, ball.x)
                )

            if (
                ball.y > self.screen_height - ball.radius
                or ball.y < ball.radius
            ):
                ball.dy *= (
                    -0.8 if ball.y > self.screen_height - ball.radius else -1
                )
                ball.dx *= (
                    0.8 if ball.y > self.screen_height - ball.radius else 1
                )
                ball.y = max(
                    ball.radius, min(self.screen_height - ball.radius, ball.y)
                )
