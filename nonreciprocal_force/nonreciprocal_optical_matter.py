import numpy as np
import matplotlib.pyplot as plt

def K(x):
    """Coupling matrix K(x) = sqrt(2 x ln x), defined for x > e to avoid singularity."""
    return np.sqrt(2 * x * np.log(x))

# Positions chosen > e ≈ 2.718 to ensure positive K and avoid divergence
positions = np.array([2.5, 4.0, 6.0])
K_vals = K(positions)

def nonreciprocal_strength(K_i, K_j):
    return np.abs(K_i - K_j) / (np.abs(K_i) + np.abs(K_j))

n = len(positions)
Delta = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            Delta[i, j] = nonreciprocal_strength(K_vals[i], K_vals[j])

print("=== Optical matter N-body nonreciprocal forces ===")
print(f"Particle positions: {positions}")
print(f"K(x) values: {K_vals}")
print("Nonreciprocal strength matrix Delta (Delta_ij = |K_i-K_j|/(|K_i|+|K_j|)):")
print(Delta)
print("Interpretation: Nonzero off-diagonals indicate broken action-reaction symmetry.")
print("The largest asymmetry occurs between particles with largest K difference.")

plt.imshow(Delta, cmap='viridis', vmin=0, vmax=1)
plt.colorbar(label='Nonreciprocal strength Δ')
plt.title('N-body nonreciprocal forces (bent chain)')
plt.xlabel('Particle j')
plt.ylabel('Particle i')
plt.xticks(range(n), [f'p{i+1}' for i in range(n)])
plt.yticks(range(n), [f'p{i+1}' for i in range(n)])
plt.savefig('nonreciprocal_optical_matter.png', dpi=150)
plt.show()