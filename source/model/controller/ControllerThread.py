import pygame
from pygame import JOYBUTTONDOWN, JOYAXISMOTION, JOYHATMOTION


class ControllerThread:
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == JOYBUTTONDOWN:
                    self.controller.on_button_pressed(event.button)
                if event.type == JOYAXISMOTION:
                    self.controller.on_joystick_move(event.axis, event.value)
                if event.type == JOYHATMOTION:
                    self.controller.on_hat_push(event.value[0], event.value[1])