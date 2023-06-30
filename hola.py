import pygame

class pelota:
    def __init__(self, ventana, x, y):
        self.ventana = ventana
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

    def mover(self):
        self.x += self.vx
        self.y += self.vy

class tubo:
    def __init__(self, ventana):
        self.tamano = 80
        self.x = 600/2 - self.tamano/2
        self.y = 380
        self.centro = self.x + self.tamano/2
        self.ventana = ventana
        self.izq = False
        self.der = False

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, self.tamano, 10))

    def mover(self):
        if self.izq: self.x -=10
        if self.der: self.x +=10
        self.x = 0 if self.x < 0 else 600 - self.tamano if self.x + self.tamano > 600 else self.x


def refrescar(ventana):
    ventana.fill((0, 0, 0))
    bola.dibujar()
    cosa.dibujar()

def main():
    global bola, golpes, font, cosa
    ventana = pygame.display.set_mode((600, 400))
    ventana.fill((0, 0, 0))
    bola = pelota(ventana, 50, 100)
    bola.vx = 5
    bola.vy = 5
    golpes = 0
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)
    jugar = True
    cosa = tubo(ventana)
    clock = pygame.time.Clock()
    while jugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugar = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cosa.izq = True
                if event.key == pygame.K_RIGHT:
                    cosa.der = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    cosa.izq = False
                if event.key == pygame.K_RIGHT:
                    cosa.der = False
        bola.mover()
        cosa.mover()
        if bola.x >= 590:
            bola.vx *= -1
            bola.x = 590

        if bola.x <= 0:
            bola.vx *= -1
            bola.x = 0

        if bola.y + 10 > cosa.y:
            if (cosa.x < bola.x < cosa.x + cosa.tamano) or (cosa.x < bola.x + 10 < cosa.x + cosa.tamano):
                bola.vy *= -1
                golpes += 1

        if bola.y >= 390:
            print("you lose")
            print(golpes)
            jugar = False

        if bola.y <= 0:
            bola.vy *= -1
            bola.y = 0
        refrescar(ventana)
        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()


    