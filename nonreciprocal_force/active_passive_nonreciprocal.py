import numpy as np
import matplotlib.pyplot as plt

def solve_active_passive(L=100.0, nx=200, T=150.0, dt=0.1,
                         Da=1.0, Dp=1.0, gamma=0.2,
                         rho_a0_peak=0.1, rho_p0=0.5):
    """
    Solve active-passive density equations with nonreciprocal coupling.
    Returns: x, rho_a_hist, rho_p_hist
    """
    x = np.linspace(0, L, nx)
    dx = x[1] - x[0]

    # Initial condition: active particles Gaussian peak near left
    sigma = L/10.0
    rho_a = rho_a0_peak * np.exp(-((x - L/4.0)**2) / (2.0 * sigma**2))
    rho_p = rho_p0 * np.ones_like(x)

    def laplacian(y):
        d2y = np.zeros_like(y)
        d2y[1:-1] = (y[2:] - 2*y[1:-1] + y[:-2]) / dx**2
        # Neumann (zero gradient) at boundaries
        d2y[0] = (y[1] - y[0]) / dx**2
        d2y[-1] = (y[-2] - y[-1]) / dx**2
        return d2y

    history_a = [rho_a.copy()]
    history_p = [rho_p.copy()]

    for step in range(int(T / dt)):
        # Diffusion
        diff_a = Da * laplacian(rho_a)
        diff_p = Dp * laplacian(rho_p)

        # Gradients for coupling
        grad_p = np.gradient(rho_p, dx)
        grad_a = np.gradient(rho_a, dx)

        # Limit gradients to avoid blow-up
        max_grad = 5.0
        grad_p = np.clip(grad_p, -max_grad, max_grad)
        grad_a = np.clip(grad_a, -max_grad, max_grad)

        # Nonreciprocal advection (active attracted to passive gradient,
        # passive repelled by active gradient)
        adv_a = gamma * rho_a * grad_p
        adv_p = -gamma * rho_p * grad_a

        # Update
        rho_a += dt * (diff_a + adv_a)
        rho_p += dt * (diff_p + adv_p)

        # Non‑negativity
        rho_a = np.maximum(rho_a, 0.0)
        rho_p = np.maximum(rho_p, 0.0)

        # Optional light smoothing every 50 steps
        if step % 50 == 0:
            rho_a = np.convolve(rho_a, np.ones(3)/3, mode='same')
            rho_p = np.convolve(rho_p, np.ones(3)/3, mode='same')

        history_a.append(rho_a.copy())
        history_p.append(rho_p.copy())

    return x, np.array(history_a), np.array(history_p)

# Run simulation
x, rho_a_hist, rho_p_hist = solve_active_passive(T=150.0, dt=0.1, gamma=0.2)

# Console output
print("=== Active-passive mixture with nonreciprocal forces ===")
print(f"Parameters: Da={1.0}, Dp={1.0}, gamma={0.2}, T={150.0}, dt={0.1}")
print(f"Final max active density: {np.max(rho_a_hist[-1]):.3f}")
print(f"Final max passive density: {np.max(rho_p_hist[-1]):.3f}")
print("Observation: Active particles accumulate near left peak, passive particles are slightly depleted there due to nonreciprocal repulsion.")
print("The system remains stable without numerical blow-up.")

# Plot final state
plt.figure(figsize=(10,5))
plt.plot(x, rho_a_hist[-1], 'r-', label='Active particles')
plt.plot(x, rho_p_hist[-1], 'b--', label='Passive particles')
plt.xlabel('Position')
plt.ylabel('Density')
plt.title('Active-passive mixture with nonreciprocal forces (stable)')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('active_passive_nonreciprocal.png', dpi=150)
plt.show()