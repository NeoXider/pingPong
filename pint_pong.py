import pygame
import spritePro

pygame.init()

"""КОНСТАНТЫ"""
# размеры экрана
WIDTH, HEIGHT = 800, 600
FPS = 60

"""КЛАССЫ"""


class Cat:
    pass


"""ФУНКЦИИ"""


def clamp(value, min_value, max_value):
    """
    Ограничивает значение в заданном диапазоне [min_value, max_value].
    """
    return max(min_value, min(value, max_value))


def create_window(WIDTH, HEIGHT):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping pong", "Sprite/ball.jpg")
    return screen


"""СЛУЖЕБНЫЕ ПЕРЕМЕННЫЕ"""
screen = create_window(WIDTH, HEIGHT)

"""ПОЛУЧАЕМ КАРТИНКИ"""
bg_image = pygame.transform.scale(pygame.image.load("Sprites/bg.jpg"), (WIDTH, HEIGHT))

clock = pygame.time.Clock()

player1 = spritePro.GameSprite("Sprites/platforma.png", (150, 50), (50, 250), 4)
player1.rotate_to(-90)

player2 = spritePro.GameSprite("Sprites/platforma.png", (150, 50), (750, 250), 4)
player2.rotate_to(90)

ball = spritePro.GameSprite("Sprites/ball.jpg", (50, 50), (400, 300), 3)

speed_x = 1
speed_y = 1

speed = 1
add_speed_frame = 0.005

lose_frames = 0

pygame.font.init()
font_label = pygame.font.Font(None, 36)
text = font_label.render("lol", True, (255, 255, 255))

ball1 = spritePro.PhysicalSprite("Sprites/ball.jpg",(50,50),(200,200), 3)
ball1.bounce_enabled = True

"""ИГРОВОЙ ЦИКЛ"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg_image, (0, 0))
    ball.speed += add_speed_frame
    player1.handle_keyboard_input(
        up_key=pygame.K_w, down_key=pygame.K_s, left_key=None, right_key=None
    )
    ball1.handle_keyboard_input()

    ball1.update(screen)
    ball1.limit_movement(screen.get_rect())

    player1.update(screen)
    player1.limit_movement(bg_image.get_rect())

    player2.handle_keyboard_input(
        up_key=pygame.K_UP, down_key=pygame.K_DOWN, left_key=None, right_key=None
    )

    player2.update(screen)
    player2.limit_movement(bg_image.get_rect())

    ball.update(screen)
    ball.move(speed_x, speed_y)

    if ball.rect.bottom > HEIGHT or ball.rect.top < 0:
        speed_y *= -1

    if ball.collide_with(player1) or ball.collide_with(player2):
        speed_x *= -1

    if ball.rect.right > WIDTH:
        lose_frames = 30
        ball.position.x, ball.position.y = (400, 300)

    # отрисовка

    if lose_frames > 0:
        screen.blit(text, (350, 150))
        lose_frames -= 1

    pygame.display.update()
    clock.tick(FPS)
