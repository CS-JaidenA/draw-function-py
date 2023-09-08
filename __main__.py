#!/usr/bin/env python

import pygame
pygame.init()

done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Target")

def draw_target(x: int, y: int, width: int, height: int, ring_count: int, ext_clr: tuple, int_clr: tuple):
	w_decrease: int = int(2 * width  / (ring_count * 2 - 1))
	h_decrease: int = int(2 * height / (ring_count * 2 - 1))

	calculated_w = width
	calculated_h = height

	for i in range(ring_count):
		color: tuple = int_clr if i % 2 == 0 else ext_clr

		pygame.draw.ellipse(screen, color, (
			x + (100 - calculated_w) / 2,
			y + (100 - calculated_h) / 2, 
			calculated_w,
			calculated_h,
		), 0)

		calculated_w -= w_decrease
		calculated_h -= h_decrease

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	screen.fill((255, 255, 255))
	draw_target(100, 100, 200, 100, 5, (255, 0, 0), (255, 255, 255))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
