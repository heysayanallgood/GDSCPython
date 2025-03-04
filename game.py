import pygame
import sys
import random

class Chip8:
    def __init__(self):
        self.memory = bytearray(4096)
        self.V = bytearray(16)
        self.I = 0
        self.PC = 0x200
        self.stack = [0] * 16
        self.SP = 0
        self.delay_timer = 0
        self.sound_timer = 0
        self.display = [[False]*64 for _ in range(32)]
        self.draw_flag = False
        self.keypad = [False] * 16
        self.opcode = 0
        self.waiting_for_key = None
        
        # Load fontset
        font = [
            0xF0, 0x90, 0x90, 0x90, 0xF0, 0x20, 0x60, 0x20, 0x20, 0x70,
            0xF0, 0x10, 0xF0, 0x80, 0xF0, 0xF0, 0x10, 0xF0, 0x10, 0xF0,
            0x90, 0x90, 0xF0, 0x10, 0x10, 0xF0, 0x80, 0xF0, 0x10, 0xF0,
            0xF0, 0x80, 0xF0, 0x90, 0xF0, 0xF0, 0x10, 0x20, 0x40, 0x40,
            0xF0, 0x90, 0xF0, 0x90, 0xF0, 0xF0, 0x90, 0xF0, 0x10, 0xF0,
            0xF0, 0x90, 0xF0, 0x90, 0x90, 0xE0, 0x90, 0xE0, 0x90, 0xE0,
            0xF0, 0x80, 0x80, 0x80, 0xF0, 0xE0, 0x90, 0x90, 0x90, 0xE0,
            0xF0, 0x80, 0xF0, 0x80, 0xF0, 0xF0, 0x80, 0xF0, 0x80, 0x80
        ]
        self.memory[:len(font)] = font

    def load_rom(self, filename):
        with open(filename, 'rb') as f:
            rom = f.read()
        self.memory[0x200:0x200+len(rom)] = rom

    def fetch_opcode(self):
        self.opcode = (self.memory[self.PC] << 8) | self.memory[self.PC+1]
        self.PC += 2

    def decode_execute(self):
        opcode = self.opcode
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        nnn = opcode & 0x0FFF
        kk = opcode & 0x00FF
        n = opcode & 0x000F

        if opcode == 0x00E0:
            self.display = [[False]*64 for _ in range(32)]
            self.draw_flag = True
        elif opcode == 0x00EE:
            self.SP -= 1
            self.PC = self.stack[self.SP]
        elif (opcode & 0xF000) == 0x1000:
            self.PC = nnn
        elif (opcode & 0xF000) == 0x2000:
            self.stack[self.SP] = self.PC
            self.SP += 1
            self.PC = nnn
        elif (opcode & 0xF000) == 0x3000:
            if self.V[x] == kk:
                self.PC += 2
        elif (opcode & 0xF000) == 0x4000:
            if self.V[x] != kk:
                self.PC += 2
        elif (opcode & 0xF000) == 0x5000:
            if self.V[x] == self.V[y]:
                self.PC += 2
        elif (opcode & 0xF000) == 0x6000:
            self.V[x] = kk
        elif (opcode & 0xF000) == 0x7000:
            self.V[x] = (self.V[x] + kk) & 0xFF
        elif (opcode & 0xF00F) == 0x8000:
            self.V[x] = self.V[y]
        elif (opcode & 0xF00F) == 0x8001:
            self.V[x] |= self.V[y]
        elif (opcode & 0xF00F) == 0x8002:
            self.V[x] &= self.V[y]
        elif (opcode & 0xF00F) == 0x8003:
            self.V[x] ^= self.V[y]
        elif (opcode & 0xF00F) == 0x8004:
            sum_val = self.V[x] + self.V[y]
            self.V[0xF] = 1 if sum_val > 0xFF else 0
            self.V[x] = sum_val & 0xFF
        elif (opcode & 0xF00F) == 0x8005:
            self.V[0xF] = 1 if self.V[x] >= self.V[y] else 0
            self.V[x] = (self.V[x] - self.V[y]) & 0xFF
        elif (opcode & 0xF00F) == 0x8006:
            self.V[0xF] = self.V[x] & 0x1
            self.V[x] = (self.V[x] >> 1) & 0xFF
        elif (opcode & 0xF00F) == 0x8007:
            self.V[0xF] = 1 if self.V[y] >= self.V[x] else 0
            self.V[x] = (self.V[y] - self.V[x]) & 0xFF
        elif (opcode & 0xF00F) == 0x800E:
            self.V[0xF] = (self.V[x] & 0x80) >> 7
            self.V[x] = (self.V[x] << 1) & 0xFF
        elif (opcode & 0xF000) == 0x9000:
            if self.V[x] != self.V[y]:
                self.PC += 2
        elif (opcode & 0xF000) == 0xA000:
            self.I = nnn
        elif (opcode & 0xF000) == 0xB000:
            self.PC = nnn + self.V[0]
        elif (opcode & 0xF000) == 0xC000:
            self.V[x] = (random.randint(0, 255) & kk)
        elif (opcode & 0xF000) == 0xD000:
            x_pos = self.V[x] % 64
            y_pos = self.V[y] % 32
            self.V[0xF] = 0
            for row in range(n):
                sprite = self.memory[self.I + row]
                for col in range(8):
                    if sprite & (0x80 >> col):
                        px = (x_pos + col) % 64
                        py = (y_pos + row) % 32
                        if self.display[py][px]:
                            self.V[0xF] = 1
                        self.display[py][px] ^= True
            self.draw_flag = True
        elif (opcode & 0xF0FF) == 0xE09E:
            if self.keypad[self.V[x]]:
                self.PC += 2
        elif (opcode & 0xF0FF) == 0xE0A1:
            if not self.keypad[self.V[x]]:
                self.PC += 2
        elif (opcode & 0xF0FF) == 0xF007:
            self.V[x] = self.delay_timer
        elif (opcode & 0xF0FF) == 0xF00A:
            self.waiting_for_key = x
        elif (opcode & 0xF0FF) == 0xF015:
            self.delay_timer = self.V[x]
        elif (opcode & 0xF0FF) == 0xF018:
            self.sound_timer = self.V[x]
        elif (opcode & 0xF0FF) == 0xF01E:
            self.I = (self.I + self.V[x]) & 0xFFF
        elif (opcode & 0xF0FF) == 0xF029:
            self.I = self.V[x] * 5
        elif (opcode & 0xF0FF) == 0xF033:
            self.memory[self.I] = self.V[x] // 100
            self.memory[self.I+1] = (self.V[x] % 100) // 10
            self.memory[self.I+2] = self.V[x] % 10
        elif (opcode & 0xF0FF) == 0xF055:
            for i in range(x+1):
                self.memory[self.I+i] = self.V[i]
        elif (opcode & 0xF0FF) == 0xF065:
            for i in range(x+1):
                self.V[i] = self.memory[self.I+i]
        else:
            print(f"Unimplemented opcode: {hex(opcode)}")

    def update_timers(self):
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1
            if self.sound_timer == 0:
                print("\a", end='', flush=True)  # System beep

    def handle_input(self, event):
        key_map = {
            pygame.K_1: 0x1, pygame.K_2: 0x2, pygame.K_3: 0x3, pygame.K_4: 0xC,
            pygame.K_q: 0x4, pygame.K_w: 0x5, pygame.K_e: 0x6, pygame.K_r: 0xD,
            pygame.K_a: 0x7, pygame.K_s: 0x8, pygame.K_d: 0x9, pygame.K_f: 0xE,
            pygame.K_z: 0xA, pygame.K_x: 0x0, pygame.K_c: 0xB, pygame.K_v: 0xF
        }
        if event.type == pygame.KEYDOWN:
            if event.key in key_map:
                key = key_map[event.key]
                self.keypad[key] = True
                if self.waiting_for_key is not None:
                    self.V[self.waiting_for_key] = key
                    self.waiting_for_key = None
        elif event.type == pygame.KEYUP:
            if event.key in key_map:
                key = key_map[event.key]
                self.keypad[key] = False

def main():
    pygame.init()
    scale = 10
    screen = pygame.display.set_mode((64*scale, 32*scale))
    pygame.display.set_caption("CHIP-8 Emulator")
    clock = pygame.time.Clock()
    
    emu = Chip8()
    emu.load_rom("Soccer.ch8")
    
    running = True
    last_timer = pygame.time.get_ticks()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                emu.handle_input(event)
        
        emu.fetch_opcode()
        emu.decode_execute()
        
        # Update timers at 60Hz
        now = pygame.time.get_ticks()
        if now - last_timer > 16:
            emu.update_timers()
            last_timer = now
        
        # Update display
        if emu.draw_flag:
            screen.fill((0, 0, 0))
            for y in range(32):
                for x in range(64):
                    if emu.display[y][x]:
                        pygame.draw.rect(screen, (255,255,255),
                                       (x*scale, y*scale, scale, scale))
            pygame.display.flip()
            emu.draw_flag = False
        
        clock.tick(500)  # Fast execution speed
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()