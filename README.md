# SpritePro

`SpritePro` — это модуль для работы с 2D-спрайтами в Pygame, который предоставляет классы для создания и управления спрайтами с поддержкой физики, анимации и взаимодействия с окружением.

## Классы

### GameSprite

Класс `GameSprite` является базовым классом для создания спрайтов. Он предоставляет основные функции для загрузки изображений, управления состоянием спрайта и обработки столкновений.

#### Конструктор

```python
GameSprite(sprite: str, size: tuple = (50, 50), pos: tuple = (0, 0), speed: float = 0, health: int = 100)
```

- `sprite`: Путь к изображению спрайта или имя ресурса.
- `size`: Размер спрайта (ширина, высота) по умолчанию (50, 50).
- `pos`: Начальная позиция спрайта (x, y) по умолчанию (0, 0).
- `speed`: Скорость движения спрайта по умолчанию 0.
- `health`: Здоровье спрайта по умолчанию 100.

#### Методы

- `update(window: pygame.Surface)`: Обновляет состояние спрайта и отрисовывает его на переданной поверхности.
- `move(dx: float, dy: float)`: Перемещает спрайт на заданное расстояние.
- `handle_keyboard_input(keys=None, ...)`: Обрабатывает ввод с клавиатуры для движения спрайта.
- `collide_with(other_sprite)`: Проверяет столкновение с другим спрайтом.
- `set_velocity(vx: float, vy: float)`: Устанавливает скорость спрайта.
- `set_state(state: str)`: Устанавливает состояние спрайта, если оно допустимо.
- `is_in_state(state: str)`: Проверяет, находится ли спрайт в заданном состоянии.
- `fade_by(amount: int, min_alpha: int = 0, max_alpha: int = 255)`: Изменяет прозрачность спрайта на заданное количество с ограничениями.
- `scale_by(amount: float, min_scale: float = 0.0, max_scale: float = 2.0)`: Изменяет масштаб спрайта на заданное количество с ограничениями.
- `on_collision_event(callback: Callable)`: Устанавливает функцию обратного вызова для событий столкновения.
- `on_death_event(callback: Callable)`: Устанавливает функцию обратного вызова для событий смерти.

### PhysicalSprite

Класс `PhysicalSprite` наследует от `GameSprite` и добавляет поддержку физики, включая гравитацию и возможность отскока.

#### Конструктор

```python
PhysicalSprite(sprite: str, size: tuple = (50, 50), pos: tuple = (0, 0), speed: float = 0, health: int = 100, mass: float = 1.0, gravity: float = 9.81, bounce_enabled: bool = False)
```

- `mass`: Масса спрайта, используемая для расчета физики.
- `gravity`: Ускорение свободного падения, по умолчанию 9.81.
- `bounce_enabled`: Включает или отключает возможность отскока.

#### Методы

- `apply_force(force: pygame.math.Vector2)`: Применяет силу к спрайту.
- `bounce(normal: pygame.math.Vector2)`: Обрабатывает отскок от поверхности с заданной нормалью.
- `update_physics(delta_time: float)`: Обновляет физическое состояние спрайта.
- `limit_movement(bounds: pygame.Rect, ...)`: Ограничивает движение спрайта в пределах заданных границ с учетом отскока.

### Пример использования

```python
import pygame
from spritePro import PhysicalSprite

# Инициализация Pygame
pygame.init()
window = pygame.display.set_mode((800, 600))

# Создание физического спрайта
ball = PhysicalSprite("Sprites/ball.png", size=(50, 50), pos=(100, 100), speed=5, mass=1.0)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.handle_keyboard_input(keys)  # Обработка ввода
    ball.update(window)  # Обновление спрайта
    ball.limit_movement(window.get_rect())  # Ограничение движения

    pygame.display.flip()

pygame.quit()
```

## Заключение

Модуль `spritePro.py` предоставляет мощные инструменты для работы с 2D-спрайтами в Pygame, включая поддержку физики, анимации и взаимодействия с окружением. Вы можете использовать его для создания интерактивных игр и приложений. 

