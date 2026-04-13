# Pokémon Route

A university AI course project that builds an autonomous Pokémon route game, using Prolog, Python and Fuzzy logic to reach the project goal.

## About

This project was developed as part of the Artificial Intelligence course at the University ISCTE-IUL.

The game simulates a Pokémon exploring a 5x5 grid, autonomously deciding which Pokémon to battle next, using **Fuzzy logic** System, the knowledge base is stored in **Prolog**, while the game engine and GUI are built in **Python**.

The game only ends if the starter Pokémon **loses a battle** or **completes the entire route**.

## Technologies Used
| Technology | Purpose |
|---|---|
| **Python 3.11** | Game engine, GUI, Fuzzy Logic |
| **SWI-Prolog 10** | Knowledge base (route, Pokémon info, attack effects) |
| **pyswip** | Python ↔ Prolog bridge |
| **scikit-fuzzy** | Fuzzy Logic system |
| **tkinter** | GUI |
| **Pillow** | Image handling |
 
---
 
## Project Structure
 
```
pokemon_route/
├── main.py                     # Entry point
├── game/
│   ├── pokemon_game.py         # Game engine
│   └── pokemon_fuzzy.py        # Fuzzy Logic system
├── gui/
│   ├── pokemon_gui.py          # Route GUI
│   └── starter_gui.py          # Starter selection GUI
├── prolog/
│   ├── pokemon_game.pl         # Game rules (next_rooms)
│   ├── pokemon_route.pl        # Route facts (5x5 matrix)
│   ├── pokemon_info_attacks.pl # Attack effectiveness facts
│   └── pokemon_list.pl         # 150 Pokémon facts
├── images/                     # Pokémon sprites
├── requirements.txt
├── README.mp #  Text file for installing the requirments
└── README.md

```
 
---
 
## How It Works
 
### 1. Prolog Knowledge Base
The route is stored as a 5x5 matrix of `(Id, Level)` pairs. The `next_rooms(X, Y, Rooms)` predicate finds all valid neighbouring Pokémon (up, down, left, right) and returns their full info.
 
### 2. Fuzzy Logic Decision System
For each neighbour, the system calculates:
- **`level_input`** → difference between player level and enemy level (-9 to 9)
- **`effect_input`** → best attack effectiveness (0 to 4, considering type multiplications)
 
These inputs feed into a **Fuzzy Logic system** with:
- Membership functions for `weak`, `equal`, `strong` (level) and `immune`, `low`, `normal`, `effective`, `super_effective` (effect)
- 15 IF-THEN rules combining both inputs
- Centroid defuzzification to produce a win probability (0 to 1)
 
### 3. Battle System
The Pokémon moves to the neighbour with the **highest win probability**. A turn-based battle is simulated with:
- Random first-mover advantage
- 5% miss chance
- 5% critical hit chance (2x damage)
- Level update on victory
 
---
 
## 🚀 How to Run
 
### Prerequisites
```bash
# Install SWI-Prolog
brew install swi-prolog
 
# Install tkinter for Python 3.11
brew install python-tk@3.11
```
 
### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd pokemon_route
 
# Create virtual environment with Python 3.11
python3.11 -m venv .venv
source .venv/bin/activate
 
# Install dependencies
pip install -r requirements.txt
```
 
### Run
```bash
python main.py
```
 
---
 
## Gameplay
 
1. Choose your starter Pokémon (Bulbasaur, Charmander, or Squirtle)
2. Watch your Pokémon autonomously navigate the route
3. The Fuzzy Logic system picks the best battle at each step
4. Win all 25 battles to complete the route!
 
---
 
## Author
 
> Developed as a solo project for AI course 2025/26 at ISCTE-IUL.
> *(David Galvão 122602)*
 
---
 
## ⚠️ Notes
 
- Requires **Python 3.11** specifically (3.9 too old, 3.13+ too new for dependencies)
- Tested on **macOS 26 (Tahoe)** with **SWI-Prolog 10.0.2**
- This is a **coursework project** — transparency about its academic origins is intentional
- This project was built to accept more Pokémons and routes. 
 