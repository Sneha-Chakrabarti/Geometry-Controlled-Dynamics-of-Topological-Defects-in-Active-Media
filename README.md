# Geometry-Controlled-Dynamics-of-Topological-Defects-in-Active-Media
## Overview
This project investigates how geometric confinement and activity influence the dynamics of topological defects in active media. The goal is to understand how boundaries, curvature, and disorder control transport, trapping, and emergent behavior in nonequilibrium systems.

The work combines continuum field models of active nematics with effective particle-based descriptions inspired by active Brownian systems.

---

## Motivation
Active systems, from cytoskeletal networks to synthetic active materials, exhibit rich nonequilibrium behavior, driven by internal energy consumption. In such systems, topological defects play a central role in organizing dynamics and structure. Recent studies of active polymers and particles in porous environments show transitions between smooth transport, trapping, and escape. This project explores whether similar mechanisms govern defect dynamics under confinement.

---

## Objectives
- Simulate active nematic systems using a minimal angle field model
- Identify and track topological defects (+1/2 and -1/2)
- Study the effect of geometry (circular, elliptical, porous) on defect behavior
- Analyze transport properties such as mean squared displacement (MSD)
- Compare defect dynamics with active Brownian particle models

---

## Model Description

### Field Model (Active Nematic)
The system is described by an angle field θ(x, y) evolving as:

∂θ/∂t = K ∇²θ + ζ sin(2θ) + η(x,y,t)

where:
- K is the elastic constant
- ζ represents activity
- η is stochastic noise

Topological defects emerge as singularities in the field.

---

### Particle Model (Effective Description)
Defects are also modeled as effective active particles:

γ dr/dt = -∇V + F_a + ξ(t)

where:
- F_a is a self-propulsion force
- ξ(t) is noise
- V represents interactions or confinement

---

## Key Questions
- How does confinement geometry affect defect motion?
- Do defects exhibit trapping and escape transitions?
- Can defect dynamics be mapped to active Brownian particles?
- How does activity control transitions between localized and mobile regimes?

---

## Methods
- Finite-difference simulation of angle field on a 2D grid
- Defect detection via winding number calculation
- Particle-based simulations using Langevin dynamics
- Statistical analysis of trajectories and spatial distributions

---

## Planned Features
- Defect detection and classification
- Circular and elliptical confinement
- Porous media (random obstacle fields)
- Defect trajectory tracking
- MSD and diffusion analysis

---

## Repository Structure
```
project/
├── README.md
├── src/
│   ├── field_model.py
│   ├── defect_detection.py
│   └── particle_model.py
├── simulations/
├── results/
└── plots/
```
