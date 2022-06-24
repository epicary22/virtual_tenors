import pygame
import sys
import copy
import json
from drumhead import DrumHead
from scipy.io import wavfile

# samplerate, data = wavfile.read("short-reverb-tom-sample-e-key-24-Wqi.wav")

pygame.init()

screen_size = screen_width, screen_height = 540, 260
screen = pygame.display.set_mode(screen_size)


def parse_drumhead_data(drumhead_data):
    down_color = tuple(drumhead_data["down_color"])
    raw_pos = tuple(drumhead_data["raw_pos"])
    radius = drumhead_data["radius"]
    hit_keys = tuple(drumhead_data["hit_keys"])
    return down_color, raw_pos, radius, hit_keys


def get_drumheads():
    with open("drumhead_data.json", "r") as file:
        data = json.load(file)
    drumheads_ = []
    for drumhead_name, drumhead_data in data.items():
        down_color, raw_pos, radius, hit_keys = parse_drumhead_data(drumhead_data)
        drumheads_.append(
            DrumHead(
                name=drumhead_name,
                screen=screen,
                hit_keys=hit_keys,
                down_color=down_color,
                raw_pos=raw_pos,
                radius=radius,
            )
        )
    return drumheads_


drumheads = get_drumheads()
while 1:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for drumhead in drumheads:
                print(pygame.key.get_pressed(), drumhead.hit_keys)
                if pygame.key.get_pressed() in drumhead.hit_keys: # bTODO Fix this line!
                    drumhead.hit()
        elif event.type == pygame.KEYUP:
            pass

    # Draw
    for drumhead in drumheads:
        drumhead.draw()

    # Advance Frame
    pygame.display.flip()
