import pygame


def main():
    # Initialize pygame
    pygame.init()

    # Set screen dimensions and create screen
    screen_width, screen_height = 600, 400
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set ball properties
    ball_color = (255, 0, 0)
    ball = {
        "radius": 20,
        "position": [50, 50],
        "velocity": [20, 200],
    }
    gravity = 500

    # Set frame rate and create clock
    fps = 30
    clock = pygame.time.Clock()

    # Create ball size slider
    slider_rect = pygame.Rect(
        screen_width // 2 - 100, screen_height - 40, 200, 20
    )
    dragging = False
    initial_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        initial_pos = draw_slider(
            screen, slider_rect, ball, dragging, initial_pos
        )

        update_ball_position(fps, gravity, screen_width, screen_height, ball)
        screen.fill((255, 255, 255))
        draw_ball(screen, ball_color, ball)

        # Update the display and limit the frame rate
        pygame.display.update()
        clock.tick(fps)


def update_ball_position(fps, gravity, screen_width, screen_height, ball):
    dt = 1 / fps
    ball["position"][1] += ball["velocity"][1] * dt
    ball["velocity"][1] += gravity * dt

    if (
        not ball["radius"]
        <= ball["position"][0]
        <= screen_width - ball["radius"]
    ):
        ball["velocity"][0] *= -1
        ball["position"][0] = max(
            ball["radius"],
            min(screen_width - ball["radius"], ball["position"][0]),
        )

    if (
        not ball["radius"]
        <= ball["position"][1]
        <= screen_height - ball["radius"]
    ):
        ball["velocity"][1] *= (
            -0.8
            if ball["position"][1] > screen_height - ball["radius"]
            else -1
        )
        ball["velocity"][0] *= (
            0.8 if ball["position"][1] > screen_height - ball["radius"] else 1
        )
        ball["position"][1] = max(
            ball["radius"],
            min(screen_height - ball["radius"], ball["position"][1]),
        )


def draw_ball(screen, ball_color, ball):
    pygame.draw.circle(
        screen,
        ball_color,
        (int(ball["position"][0]), int(ball["position"][1])),
        ball["radius"],
    )


def draw_slider(screen, slider_rect, ball, dragging, initial_pos):
    pygame.draw.rect(screen, (0, 0, 0), slider_rect, 1)

    if dragging:
        rel_x, _ = pygame.mouse.get_rel()
        ball["radius"] = max(10, min(200, ball["radius"] + rel_x))
    else:
        initial_pos = None

    if pygame.mouse.get_pressed()[0] and slider_rect.collidepoint(
        pygame.mouse.get_pos()
    ):
        initial_pos = pygame.mouse.get_pos()

    return initial_pos


if __name__ == "__main__":
    main()
