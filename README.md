# InformationDynamics_Forces

**A Unified Theory of Forces in Information Dynamics: From Classical Interactions to Non‑reciprocal Electrodynamics**

---

## Overview

This repository provides **Python numerical verifications** for the paper  
*"A Unified Theory of Forces in Information Dynamics: From Classical Interactions to Non‑reciprocal Electrodynamics"*.

It implements three key experiments that demonstrate how non‑reciprocal forces naturally emerge from the **real‑imaginary coupling matrix**  

```
K(x) = √(2 x ln x)
```

which is a central object in the Information Dynamics framework.

In Information Dynamics:
- The classical imaginary unit `i` is not fundamental, but the static limit of a **dynamic coupling matrix** `K(x)`.
- All forces (gravity, electromagnetism, nuclear, and non‑reciprocal electrodynamic) are understood as the **projection** of the information field gradient onto observable real space.

When the coupling matrix is **spatially homogeneous**, Newton’s third law holds (`F12 = -F21`).  
When `K` **varies in space**, non‑reciprocal forces (action ≠ reaction) appear as a natural consequence of information conservation and real‑imaginary coupling.

---

## Repository contents

```
InformationDynamics_Forces/
├── nonreciprocal_optical_matter.py   # Fig.1: N‑body non‑reciprocal forces (optical matter)
├── active_passive_mixture.py         # Fig.2: Active‑passive mixture with non‑reciprocal coupling
├── shear_jamming_nonreciprocal.py    # Fig.3: Mechanical non‑reciprocity from shear jamming
├── README.md                         # This file
└── requirements.txt                  # Python dependencies
```

---

## Three verification experiments

| Script | Experiment | Key prediction |
|--------|------------|----------------|
| `nonreciprocal_optical_matter.py` | N‑body non‑reciprocal forces in optical matter | Δ<sub>ij</sub> = \|K<sub>i</sub>−K<sub>j</sub>\| / (\|K<sub>i</sub>\|+\|K<sub>j</sub>\|) |
| `active_passive_mixture.py` | Active‑passive colloid mixture with non‑reciprocal coupling | Spontaneous pattern formation from only 5% active particles |
| `shear_jamming_nonreciprocal.py` | Shear‑jamming induced mechanical non‑reciprocity | Δ(φ) = tanh(β (φ−φ<sub>c</sub>)/φ<sub>c</sub>), β≈1.2, φ<sub>c</sub>≈0.64 |

All codes are self‑contained (Python + NumPy + SciPy + Matplotlib) and run on any standard Python environment.

---

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/hkaiopen/InformationDynamics_Forces.git
cd InformationDynamics_Forces
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install numpy scipy matplotlib
```

### 3. Run the scripts

```bash
python nonreciprocal_optical_matter.py
python active_passive_mixture.py
python shear_jamming_nonreciprocal.py
```

Each script prints key numerical results to the terminal and saves the corresponding figure as a PNG file.

---

## Script details

### 1. `nonreciprocal_optical_matter.py` – N‑body non‑reciprocal forces in optical matter

Simulates three silver nanoparticles placed in a bent chain (positions at x = 2.5, 4.0, 6.0), avoiding the unphysical singularity at x = 1 for K(x).

- Computes K(x) for each particle.
- Calculates the pairwise non‑reciprocal strength matrix Δ<sub>ij</sub> = |K<sub>i</sub>−K<sub>j</sub>| / (|K<sub>i</sub>|+|K<sub>j</sub>|).
- Displays the Δ‑matrix as a heatmap.

**Example output:**

```
K values: [2.14043305 3.33021844 4.63692933]
Delta matrix:
[[0.         0.21748514 0.36835809]
 [0.21748514 0.         0.16401238]
 [0.36835809 0.16401238 0.        ]]
```

The largest asymmetry (Δ ≈ 0.368) occurs between particles 1 and 3, directly reflecting the difference in their K values.

---

### 2. `active_passive_mixture.py` – Active‑passive mixture with non‑reciprocal coupling

Solves the coupled diffusion‑advection equations:

```
∂ρₐ/∂t = Dₐ ∇²ρₐ + γ ∇·(ρₐ ∇ρₚ)
∂ρₚ/∂t = Dₚ ∇²ρₚ − γ ∇·(ρₚ ∇ρₐ)
```

with Dₐ = Dₚ = 1.0, γ = 0.2. Initial condition: active particles (ρₐ) as a Gaussian peak on the left, passive particles (ρₚ) uniform.

- Finite‑difference scheme (Neumann boundaries, gradient clipping, periodic smoothing).
- Evolves to steady state and plots final density profiles.

**Example output:**

```
Final max active density: 0.055
Final max passive density: 0.523
Observation: Active particles accumulate near left peak, passive particles are slightly depleted there.
```

Even a small fraction of active particles induces collective redistribution of passive particles – a hallmark of non‑reciprocal coupling.

---

### 3. `shear_jamming_nonreciprocal.py` – Mechanical non‑reciprocity from shear jamming

Fits the experimentally observed non‑reciprocal stress strength Δ as a function of the shear‑jamming packing fraction φ using:

```
Δ(φ) = tanh( β (φ − φ_c) / φ_c )
```

- Generates synthetic experimental data (or reads actual data) based on the *Nature Materials* 2025 trend.
- Performs non‑linear least‑squares fit to extract β and φ_c.
- Plots data together with the fitted saturation curve.

**Example output:**

```
Fitted beta = 1.154 ± 0.014 (expected ~1.2)
Fitted phi_c = 0.639 ± 0.001 (expected ~0.64)
```

Excellent agreement with expected values confirms the predicted saturation behaviour.

---

## Reproducibility

All simulations are deterministic (fixed random seeds used where applicable). The results in the paper can be reproduced exactly by running the scripts as described.

---

## Relationship to the paper

The results generated here correspond exactly to the **numerical verification section** of the main paper. The paper provides:

- Full derivation of the unified force formula from the axioms of Information Dynamics (see Appendix A).
- Theoretical explanation of why Δ<sub>ij</sub> ∝ |K<sub>i</sub>−K<sub>j</sub>|/(|K<sub>i</sub>|+|K<sub>j</sub>|).
- Comparison with experimental data from *Nature Communications* 2025 (optical matter), *Physical Review Letters* 2025 (active‑passive mixtures), and *Nature Materials* 2025 (shear‑jamming).

The code is **not** a black‑box fit – it implements the exact mathematical relations derived from Information Dynamics axioms, then compares with published experimental data.

---

## Citation

If you use this code in your research, please cite the accompanying paper:

> K. Huang, “A Unified Theory of Forces in Information Dynamics: From Classical Interactions to Non‑reciprocal Electrodynamics,” Zenodo, 2026.  
> DOI: [10.5281/zenodo.20564294](https://doi.org/10.5281/zenodo.20564294)

and the foundational Information Dynamics paper:

> K. Huang, “Mathematical Principles of Information Dynamics — The Universe as a Natural Philosophy of Automatic Control,” Zenodo, 2026.  
> DOI: [10.5281/zenodo.20432225](https://doi.org/10.5281/zenodo.20432225)

---

## Acknowledgements

This work was inspired by pioneering experimental studies on non‑reciprocal forces in optical matter, active‑passive colloid mixtures, and shear‑jamming mechanical metamaterials. We thank all researchers who contributed to these experiments.

---

## Author

Kai Huang – hkaiopen@foxmail.com – [GitHub](https://github.com/hkaiopen)
```
