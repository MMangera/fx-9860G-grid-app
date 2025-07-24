import pygame as pg
import os
pg.font.init()
class Pixel:
    def __init__(self, pos, app):
        self.app = app
        self.pos = pos
        self.rect = pg.Rect(pos[0] * 10, pos[1] * 10, 9, 9)
        self.colour = (100, 100, 100)
    def event_handling(self):
        if pg.mouse.get_pressed()[0]:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    if self.app.mode:
                        self.colour = (255, 255, 0)
                    else:
                        self.colour = (100, 100, 100)
class App:
    def __init__(self):
        path = os.path.abspath(__file__)
        try:
            f = open(path[:-10]+"lastsave.txt", "x")
            f.close()
        except FileExistsError:
            pass
        f = open(path[:-10]+"lastsave.txt", "r")
        read = f.readlines()
        f.close()
        if read == []:
            f = open(path[:-10]+"lastsave.txt", "w")
            f.write("[]")
            f.close()
        self.last_save_time = 0
        self.tabhalt = False
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 40)
        self.mode = True
        self.run = True
        self.pixels: list[Pixel] = []
        for i in range(128):
            for j in range(64):
                self.pixels.append(Pixel([i, j], self))
    def event_handling(self):
        for pixel in self.pixels:
            pixel.event_handling()
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.run = False
        if keys[pg.K_TAB]:
            if not self.tabhalt:
                self.mode = not self.mode
            self.tabhalt = True
        else:
            self.tabhalt = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
    def render(self):
        modes = {True: "Mode: Draw", False: "Mode: Erase"}
        if self.last_save_time < 180:
            saved = self.font.render("Saved!", True, (0, 255, 0))
            saved_rect = saved.get_rect(center=(500, 700))
        surface = self.font.render(modes[self.mode], True, (255, 0, 0))
        surface_rect = surface.get_rect(center=(100, 700))
        print(modes[self.mode])
        self.screen.fill((255, 255, 255))
        for pixel in self.pixels:
            pg.draw.rect(self.screen, pixel.colour, pixel.rect)
        if self.last_save_time < 180:
            self.screen.blit(saved, saved_rect)
        self.screen.blit(surface, surface_rect)
        pg.display.update()
    def tick(self):
        self.event_handling()
        self.render()
    def end(self):
        returner = [i.pos for i in self.pixels if i.colour == (255, 255, 0)]
        return returner
    def activate(self):
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        while self.run:
            self.tick()
            self.last_save_time += 1
            if self.last_save_time > 2700:
                self.save()
            self.clock.tick(60)
        self.save()
        pg.quit()
        return self.end()
    def save(self):
        path = os.path.abspath(__file__)
        f = open(path[:-10]+"lastsave.txt", "w")
        f.write(str([i.pos for i in self.pixels if i.colour == (255, 255, 0)]))
        self.last_save_time = 0
    def load(self, load = None):
        if load == None:
            path = os.path.abspath(__file__)
            f = open(path[:-10]+"lastsave.txt", "r")
            load = eval(f.readlines()[0])
        else:
            pass
        self.__init__()
        for i in self.pixels:
            i.colour = (100, 100, 100) if i.pos not in load else (255, 255, 0)
def main(load = None):
    app = App()
    if load == None:
        ans = input("Load last save? (y/n):").upper()
        if ans == "Y":
            app.load()
        elif ans == "N":
            pass
        else:
            raise Exception("Invalid answer")
    else:
        app.load(load)
    pixels = app.activate()
    s = ""
    for pixel in pixels:
        s += f"set_pixel({pixel[0]}, {pixel[1]})\n"
    path = os.path.abspath(__file__)
    try:
        f = open(path[:-10]+"gridapp.txt", "x")
        f.close()
    except FileExistsError:
            pass
    f = open(path[:-10]+"gridapp.txt", "w")
    f.write("from casioplot import *\n")
    f.write(s)
    f.write("show_screen()")
    f.close()
    ans = input("Split into files for graphics calculator? (y/n)").upper()
    if ans == "Y":
        try:
            os.mkdir(path[:-10]+"APPANS")
        except FileExistsError:
            raise FileExistsError("'APPANS' has not been moved onto your graphics calculator. Try moving the file onto your graphics calculator, then rerunning the app pressing SPACE immediately upon entering.")
        f  = open(path[:-10]+"gridapp.txt", "r")
        read = f.readlines()
        f.close()
        idx = 1
        while read != []:
            f = open(path[:-10]+f"APPANS/file{idx}.py", "x")
            f.close()
            f = open(path[:-10]+f"APPANS/file{idx}.py", "w")
            f.writelines([f"from appans.file{idx-1} import *"]+read[:149])
            f.close
            read = read[149:]
            idx += 1
    elif ans == "N":
        pass
    else:
        raise Exception("Invalid answer")
if __name__ == '__main__':
    main()
