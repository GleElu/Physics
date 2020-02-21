import pygame
import config as con
from object import *


class Game:
    def __init__(self, caption, width, height, back_image_filename, frame_rate):
        self.background_image = pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        #pygame.mixer.init(44100, -16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        """print(caption)"""
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)


class Dots(Game):
    def __init__(self):
        Game.__init__(self, "Physics", 600, 600, con.FULL_PATH, 60)
        self.create_objects()

    def create_objects(self):
        self.create_circle(200, 200, [255, 0, 0], 5, 5)
        self.create_circle(500, 300, [0, 255, 251], -5, 0)

    def create_circle(self, x, y, color, speed_x, speed_y):
        circle = Circle(x, y, color, speed_x, speed_y)
        self.objects.append(circle)


    def update(self):
        def crushing(object_1, object_2):
            vector_first_x = -(object_2.center[0] - object_1.center[0])
            vector_first_y = -(object_2.center[1] - object_1.center[0])
            vector_second_x = -(object_1.center[0] - object_2.center[0])
            vector_second_y = -(object_1.center[1] - object_2.center[1])

            object_1.speed[0] = vector_first_x / abs(vector_first_x)
            object_2.speed[0] = vector_second
            object_1.speed[1] =
            object_2.speed[1] =

        def handle_collision(self):
            if self.objects[0].bounds.colliderect(self.objects[1].bounds):
                crushing(self.objects[0], self.objects[1])
        for object in self.objects:
            if object.center[0] > con.SCREEN_WIDTH:
                object.speed[0] = -object.speed[0]

            if object.center[1] > con.SCREEN_HEIGHT:
                object.speed[1] = -object.speed[1]

            if object.center[0] < 0:
                object.speed[0] = -object.speed[0]

            if object.center[1] < 0:
                object.speed[1] = -object.speed[1]

        handle_collision(self)
        super().update()