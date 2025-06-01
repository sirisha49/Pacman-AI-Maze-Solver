
# 🟡 Pacman: AI Maze Solver

> Teaching Pacman how to think — one search algorithm at a time.

**Pacman** is more than just a classic arcade game in this project — it's a playful and powerful environment for exploring the fundamentals of artificial intelligence. Using the UC Berkeley CS188 framework, I implemented four cornerstone search algorithms — Depth-First Search (DFS), Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search — to enable an intelligent agent (Pacman) to navigate complex mazes and reach its goal efficiently.

Each algorithm demonstrates a different planning strategy, from exploring deeply without regard for cost (DFS), to methodical level-by-level traversal (BFS), to cost-sensitive exploration (UCS), and finally to heuristic-driven optimal search (A*). These approaches bring to life key AI concepts such as state space exploration, graph vs. tree search, cost accumulation, and heuristic design — all in a visual and interactive format.

Whether dodging ghosts, collecting pellets, or simply finding the fastest way out, **Pacman** showcases how even a classic game can become a compelling tool for understanding intelligent decision-making in dynamic environments.

---

## Features

- **Implements Four Search Algorithms**
  - **DFS** – Explores deep paths first using a stack-based fringe
  - **BFS** – Finds the shortest path in terms of steps using a queue
  - **UCS** – Expands paths based on cumulative cost with a priority queue
  - **A\*** – Combines path cost and heuristics for efficient and optimal search

- **Interactive Pacman Simulation**
  - Visualizes agent behavior in real-time using `pacman.py`
  - Test your algorithms in mazes of varying difficulty

- **Graph Search (not Tree Search)**
  - Avoids revisiting states using a closed set
  - Efficient and scalable even in larger mazes

- **Uses Custom Data Structures**
  - Stack, Queue, and PriorityQueue implemented in `util.py`
  - All logic written from scratch (no third-party search libraries)

- **Supports Heuristics in A\***
  - Easily plug in different heuristic functions like `manhattanHeuristic`
  - Modular design allows experimentation with new strategies

---
## How to Run

### Requirements
- Python 3.x (recommended: 3.6+)
- Optional: `tkinter` (for GUI display; not required if using autograder)

> 💡 If you're on Windows, use Command Prompt (CMD) or Git Bash instead of PowerShell for better compatibility.

---

### ▶Running the Search Agents

After cloning the repo, navigate to the `py/` directory and run any of the following commands:

```bash
# Depth-First Search
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

# Breadth-First Search
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Uniform Cost Search
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

# A* Search with Manhattan Heuristic
python3 py/pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

```
---



### What I Learned

This project deepened my understanding of foundational AI concepts and search algorithms, especially in real-world planning scenarios. Some key takeaways include:

### Search Strategy Trade-offs
- **DFS** is memory-efficient but not optimal; can get stuck in deep paths.
- **BFS** guarantees the shortest path in terms of steps but may use more memory.
- **UCS** finds the lowest-cost path and adapts to cost-sensitive environments.
- **A\*** combines the strengths of UCS with domain-specific knowledge via heuristics.

### Graph Search vs Tree Search
- I implemented a **graph search** strategy that tracks visited nodes using a *closed set*, preventing infinite loops.
- This is crucial in real-world applications where the same state may be reachable through multiple paths.

### Technical Skill Growth
- Worked with **custom data structures** (Stack, Queue, PriorityQueue) from `util.py` to simulate real-world resource planning.
- Designed modular and reusable logic that integrates with the Pacman game engine.
- Implemented and tested heuristic functions like `manhattanHeuristic` to guide search intelligently.

### Testing & Debugging
- Visualized Pacman’s movements to understand fringe behavior and detect errors in search logic.
- Used both GUI testing (`pacman.py`) and automated testing (`autograder.py`) for validation.
  
---

## 📂 Project Structure
```bash
Pathman/
├── py/ # Main Python codebase
│ ├── search.py # Your DFS, BFS, UCS, and A* implementations
│ ├── searchAgents.py # Pacman agent logic using search
│ ├── util.py # Custom data structures: Stack, Queue, PriorityQueue
│ ├── pacman.py # Main runner and game loop
│ ├── layout.py # Maze layout file parser
│ ├── game.py # Core game logic (agents, actions, walls)
│ ├── graphicsDisplay.py # GUI-based game rendering
│ ├── graphicsUtils.py # GUI support functions
│ ├── ghostAgents.py # Ghost behaviors (not needed for search)
│ ├── keyboardAgents.py # Manual control of Pacman (optional)
│ ├── autograder.py # Script to grade your search algorithms
│ ├── testClasses.py # Base classes for test cases
│ ├── searchTestClasses.py # Unit tests for search algorithms
│ └── ... # (Other support files from CS188)
│
├── layouts/ # Maze layout files (.lay)
│ ├── mediumMaze.lay # Standard maze for algorithm testing
│ ├── bigSearch.lay # Large map for cost-based algorithms
│ ├── contestClassic.lay # Competitive layout
│ └── ... # Over 30+ layout files of varying complexity
│
├── test_cases/
│ ├── q1/ - q8/ # Unit test folders per question/task
│ └── CONFIG # Config file for autograder logic
│
├── images/ # Game and UI graphic assets (optional)
├── commands.txt # Sample CLI commands to run Pacman with your agents
├── requirements.txt # (Optional) Python dependencies (if needed)
└── README.md # Project documentation

```
---

## Conclusion

Building this project was more than just guiding Pacman through mazes — it was about learning how intelligent agents plan, make decisions, and optimize their paths in complex environments. Implementing foundational search algorithms like DFS, BFS, UCS, and A* gave me a hands-on understanding of key AI principles, trade-offs in algorithm design, and the importance of structuring code for clarity and reusability.

This assignment laid the groundwork for deeper explorations into AI, from adversarial search and reinforcement learning to real-world applications like route planning, game development, and robotics.

> In the end, Pacman didn’t just find the goal — I did too.

---

## Acknowledgements

- Based on the [UC Berkeley CS188: Introduction to Artificial Intelligence](http://inst.eecs.berkeley.edu/~cs188/) project framework.
- This project is used for educational purposes and is not intended for distribution or commercial use.

---

## 🏷️ Tags

`#AI` `#SearchAlgorithms` `#Pacman` `#DFS` `#BFS` `#UCS` `#AStar`  
`#GraphSearch` `#Pathfinding` `#Python` `#CS188` `#Heuristics`

---



