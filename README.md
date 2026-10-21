# 2D Physics Collision Simulator

## Overview
Simulating elastic and inelastic particle collisions requires tracking momentum conservation and dynamic velocity updates across discrete time steps. This repository implements a two-dimensional physics simulation model that computes kinematic trajectories, processes object boundary collisions, and evaluates momentum transfer and surface friction between colliding masses using command-line arguments.

## CLI Usage

### Installation
```bash
# Clone the repository
git clone https://github.com/eved1018/collision-simulator
cd collision-simulator
```

### Basic Usage
```bash
python3 semester_project.py [OPTIONS]
```

### Options
| Option | Description |
| :--- | :--- |
| `-h`, `--help` | Show usage information and exit |
| `--m1 <value>` | Mass of the first body (kg) |
| `--v1 <value>` | Initial motion velocity of the first body |
| `--m2 <value>` | Mass of the second body (kg) |
| `--v2 <value>` | Initial motion velocity of the second body |
| `--e <value>` | Coefficient of restitution governing kinetic energy retention during impact |
| `--f <value>` | Surface friction coefficient applied continuously over time steps |

### Example Execution
```bash
python3 semester_project.py --m1 10 --v1 50 --m2 20 --v2 30 --e 8 --f 1
```

## Repository Structure
- `semester_project.py` — Primary Python script containing terminal parameter parsing (`argparse`), kinematic updates, and collision detection logic.
- `Draw.py` — Custom graphics module used for rendering the visual simulation canvas and particle interactions.

## Technical Background
The simulation computes real-time kinematic interactions across discrete delta-time intervals:
- **Momentum Transfer:** Evaluates collision vectors based on object mass ratios and coefficient of restitution.
- **Friction Dissipation:** Continuously decelerates moving bodies based on surface friction values.
- **Boundary Box Calculations:** Detects spatial overlaps and reverses velocity vectors when colliding with canvas borders.

## References
1. Classical Mechanics: Conservation of Linear Momentum
2. Elastic and Inelastic Collisions in 2D
3. Python argparse Module Documentation
