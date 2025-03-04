# CHIP-8 Emulator

This is a simple CHIP-8 emulator written in Python using the Pygame library. The emulator can load and run CHIP-8 ROMs, rendering the graphics and handling input using a keyboard.

## Features
- Loads and executes CHIP-8 ROMs
- Implements the core CHIP-8 instructions
- Keyboard input mapping for CHIP-8 keys
- Basic display rendering using Pygame
- Emulates delay and sound timers

## Installation
1. Install Python (>=3.6) if not already installed.
2. Install dependencies:
   sh
   pip install pygame
   
3. Clone the repository or download the script.

## How to Use
1. Place a CHIP-8 ROM (e.g., Soccer.ch8) in the same directory as game.py.
2. Run the emulator:
   sh
   python game.py
   
3. Use the following keyboard mappings for CHIP-8 input:
   
   | CHIP-8 Key | Keyboard Key |
   |-----------|--------------|
   | 1 | 1 |
   | 2 | 2 |
   | 3 | 3 |
   | C | 4 |
   | 4 | Q |
   | 5 | W |
   | 6 | E |
   | D | R |
   | 7 | A |
   | 8 | S |
   | 9 | D |
   | E | F |
   | A | Z |
   | 0 | X |
   | B | C |
   | F | V |

4. The emulator will run the ROM and render the game.

## What Could Be Improved with More Time
- *Sound Emulation*: Implement proper sound support for the sound_timer.
- *Configurable Key Mapping*: Allow users to set custom key bindings.
- *Better Performance Optimization*: Improve execution speed for smoother emulation.
- *Save States*: Implement a feature to save and load game states.
- *GUI for ROM Selection*: Create a graphical user interface to select ROMs before running the emulator.
- *SuperCHIP Support*: Add support for extended instructions from the SuperCHIP-8 specification.
