import pygame
import random


def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_horizontal = 0
        mole_vertical = 0
        mole_width, mole_height = mole_image.get_size()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x , click_y = event.pos
                    if mole_horizontal <= click_x < mole_horizontal + 31 and mole_vertical <= click_y < mole_vertical + 31:
                        mole_horizontal = random.randrange(0,640,32)
                        mole_vertical = random.randrange(0, 512, 32)

            screen.fill("light blue")
            #mole png
            screen.blit(mole_image, (mole_horizontal, mole_vertical))
            #vertical lines (20)
            pygame.draw.line(screen, color="Black", start_pos=(0, 0), end_pos=(0, 512))
            pygame.draw.line(screen, color= "Black", start_pos=(32,0), end_pos=(32,512))
            pygame.draw.line(screen, color="Black", start_pos=(64, 0), end_pos=(64, 512))
            pygame.draw.line(screen, color="Black", start_pos=(96, 0), end_pos=(96, 512))
            pygame.draw.line(screen, color="Black", start_pos=(128, 0), end_pos=(128, 512))
            pygame.draw.line(screen, color="Black", start_pos=(160, 0), end_pos=(160, 512))
            pygame.draw.line(screen, color="Black", start_pos=(192, 0), end_pos=(192, 512))
            pygame.draw.line(screen, color="Black", start_pos=(224, 0), end_pos=(224, 512))
            pygame.draw.line(screen, color="Black", start_pos=(256, 0), end_pos=(256, 512))
            pygame.draw.line(screen, color="Black", start_pos=(288, 0), end_pos=(288, 512))
            pygame.draw.line(screen, color="Black", start_pos=(320, 0), end_pos=(320, 512))
            pygame.draw.line(screen, color="Black", start_pos=(352, 0), end_pos=(352, 512))
            pygame.draw.line(screen, color="Black", start_pos=(384, 0), end_pos=(384, 512))
            pygame.draw.line(screen, color="Black", start_pos=(416, 0), end_pos=(416, 512))
            pygame.draw.line(screen, color="Black", start_pos=(448, 0), end_pos=(448, 512))
            pygame.draw.line(screen, color="Black", start_pos=(480, 0), end_pos=(480, 512))
            pygame.draw.line(screen, color="Black", start_pos=(512, 0), end_pos=(512, 512))
            pygame.draw.line(screen, color="Black", start_pos=(544, 0), end_pos=(544, 512))
            pygame.draw.line(screen, color="Black", start_pos=(576, 0), end_pos=(576, 512))
            pygame.draw.line(screen, color="Black", start_pos=(608, 0), end_pos=(608, 512))
            pygame.draw.line(screen, color="Black", start_pos=(640, 0), end_pos=(640, 512))
            #horizontal lines (16)
            pygame.draw.line(screen, color="Black", start_pos=(0, 32), end_pos=(640, 32))
            pygame.draw.line(screen, color="Black", start_pos=(0, 64), end_pos=(640, 64))
            pygame.draw.line(screen, color="Black", start_pos=(0, 96), end_pos=(640, 96))
            pygame.draw.line(screen, color="Black", start_pos=(0, 128), end_pos=(640, 128))
            pygame.draw.line(screen, color="Black", start_pos=(0, 160), end_pos=(640, 160))
            pygame.draw.line(screen, color="Black", start_pos=(0, 192), end_pos=(640, 192))
            pygame.draw.line(screen, color="Black", start_pos=(0, 224), end_pos=(640, 224))
            pygame.draw.line(screen, color="Black", start_pos=(0, 256), end_pos=(640, 256))
            pygame.draw.line(screen, color="Black", start_pos=(0, 288), end_pos=(640, 288))
            pygame.draw.line(screen, color="Black", start_pos=(0, 320), end_pos=(640, 320))
            pygame.draw.line(screen, color="Black", start_pos=(0, 352), end_pos=(640, 352))
            pygame.draw.line(screen, color="Black", start_pos=(0, 384), end_pos=(640, 384))
            pygame.draw.line(screen, color="Black", start_pos=(0, 416), end_pos=(640, 416))
            pygame.draw.line(screen, color="Black", start_pos=(0, 448), end_pos=(640, 448))
            pygame.draw.line(screen, color="Black", start_pos=(0, 480), end_pos=(640, 480))
            pygame.draw.line(screen, color="Black", start_pos=(0, 512), end_pos=(640, 512))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
