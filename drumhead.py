import pygame
import wave

GRAY = (25, 33, 40)


class DrumHead:
    def __init__(self, name, screen, hit_keys, sound_filename, down_color=(255, 255, 255), raw_pos=(0, 0), radius=20):
        """
        :param raw_pos: This is the center position of the drumhead. It can be a float to be a percent of the screen
        size, or an int to be a raw pixel value.
        """
        self.name = name
        self.screen = screen
        self.screen_dimensions = self.screen_width, self.screen_height = self.screen.get_size()
        self.down_color = down_color
        self.is_down = False
        self.hit_keys = [eval(f"pygame.K_{hit_key}") for hit_key in hit_keys]
        self.sound_filename = sound_filename
        self.radius = radius
        self.raw_pos = raw_pos
        self.left_top = self._parse_raw_pos()
        self.rect = pygame.Rect(self.left_top[0], self.left_top[1], self.radius*2, self.radius*2)

    def _parse_raw_pos(self):
        left_top = []
        for index in range(len(self.raw_pos)):
            pos_value = self.raw_pos[index]
            screen_dimension = self.screen_dimensions[index]
            if -1 < pos_value < 1:
                left_top.append(pos_value*screen_dimension-self.radius)
            else:
                left_top.append(pos_value-self.radius)
        return tuple(left_top)

    def draw(self):
        if self.is_down:
            pygame.draw.ellipse(self.screen, self.down_color, self.rect)
        else:
            pygame.draw.ellipse(self.screen, GRAY, self.rect)

    def down(self):
        self.is_down = True

    def hit(self):
        self.down()
        hit_sound = pygame.mixer.Sound(self.sound_filename)
        pygame.mixer.Sound.play(hit_sound)

    def up(self):
        self.is_down = False
