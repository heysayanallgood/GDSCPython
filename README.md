<p align="center">
  <img src="https://media.giphy.com/media/3ohs4CacylzFaHjMM8/giphy.gif" width="450">
</p>

<!-- =======================
     CHIP-8 EMULATOR README
     Supersonic Gaming Edition
     ======================= -->

<p align="center">
  <img src="https://media.giphy.com/media/26BRuo6sLetdllPAQ/giphy.gif" width="100%">
</p>

<h1 align="center">🎮 CHIP-8 Emulator</h1>
<h3 align="center">A Retro Virtual Machine — Rebuilt at Supersonic Speed ⚡</h3>
<p align="center">
  <img src="https://media.giphy.com/media/xT0GqssRweIhlz209i/giphy.gif" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Pygame-Graphics-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Emulator-Retro%20Gaming-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/GDSC-First%20Project-purple?style=for-the-badge">
</p>

---

## 🚀 Project Overview

<p align="center">
  <img src="https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif" width="600">
</p>

> *“Old hardware. New power.”*

This is a **fully functional CHIP-8 emulator** written in **Python using Pygame**, capable of loading and running classic CHIP-8 ROMs with real-time graphics and keyboard input.

This project was built as my **first project for GDSC**, focusing on:
- Emulator architecture
- Low-level instruction decoding
- Graphics rendering
- Timing & input handling

---

## 🧠 What is CHIP-8?

<p align="center">
  <img src="https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif" width="500">
</p>

CHIP-8 is a **virtual machine** designed in the 1970s to run simple games.  
It features:
- 4KB memory
- 16 registers
- 64×32 monochrome display
- Stack-based subroutines
- Hexadecimal keypad

This emulator recreates all of that — in software.

---

## ✨ Features

<p align="center">
  <img src="https://media.giphy.com/media/3o7TKy2eMXG8hZ0C0o/giphy.gif" width="450">
</p>

✔ Loads and executes CHIP-8 ROMs  
✔ Implements core CHIP-8 instruction set  
✔ Real-time graphics rendering (64×32)  
✔ Keyboard input mapping  
✔ Delay & sound timer emulation  
✔ Fast execution loop for smooth gameplay  

---

## ⌨️ Keyboard Mapping

<p align="center">
  <img src="https://media.giphy.com/media/3o7TKp5V9PZ9DgBq4E/giphy.gif" width="400">
</p>

| CHIP-8 Key | Keyboard |
|----------|----------|
| 1 2 3 C | 1 2 3 4 |
| 4 5 6 D | Q W E R |
| 7 8 9 E | A S D F |
| A 0 B F | Z X C V |

---

## 🧩 Emulator Architecture

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="600">
</p>

```text
ROM (.ch8)
   ↓
Memory Load @ 0x200
   ↓
Fetch Opcode
   ↓
Decode & Execute
   ↓
Update Timers (60Hz)
   ↓
Render Display (Pygame)
🛠 Tech Stack
<p align="center"> <img src="https://media.giphy.com/media/3ohs4CacylzFaHjMM8/giphy.gif" width="450"> </p>

🐍 Python 3.6+

🎮 Pygame

🧠 Emulator Logic

⏱ Timer Synchronization

🎨 Pixel-Perfect Rendering⚙️ Installation
pip install pygame

▶️ How to Run
<p align="center"> <img src="https://media.giphy.com/media/xUPGcEliCc7bETyfO8/giphy.gif" width="450"> </p>

Place a CHIP-8 ROM (e.g. Soccer.ch8) in the same directory

Run the emulator:

python game.py


Enjoy retro gaming 🚀

🔮 What Can Be Improved
<p align="center"> <img src="https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif" width="400"> </p>

🔊 Proper sound emulation

🎛 Configurable key mapping

💾 Save / Load game states

🖥 GUI-based ROM selector

⚡ Performance optimizations

🧩 SuperCHIP-8 instruction support

👨‍💻 About
<p align="center"> <img src="https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif" width="500"> </p>

This is my first project for GDSC, built to explore:

Low-level systems

Emulator design

Game rendering loops

Real-time input processing

⭐ Final Note
<p align="center"> <img src="https://media.giphy.com/media/26BRuo6sLetdllPAQ/giphy.gif" width="100%"> </p> <p align="center"> <b>“From pixels to processors — emulation at supersonic speed.”</b> </p> ```
<p align="center">
  <img src="https://media.giphy.com/media/26BRuo6sLetdllPAQ/giphy.gif" width="100%">
</p>

<p align="center">
  <b>“Retro hardware. Modern speed. Supersonic execution.”</b>
</p>
