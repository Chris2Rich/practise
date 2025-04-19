import numpy as np
import matplotlib.pyplot as plt
import sympy

scale = 100

fig, ax = plt.subplots()
ax.set_xlim(-scale, scale)
ax.set_ylim(-scale, scale)
ax.set_aspect("equal")

ax.spines["left"].set_position("center")
ax.spines["bottom"].set_position("center")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xticks([i for i in np.arange(-scale, scale + 1, scale / 5) if i != 0])
ax.set_yticks([i for i in np.arange(-scale, scale + 1, scale / 5) if i != 0])

ax.text(scale * 1.1, 0, "ℝ", fontsize=12, ha="center", va="center")
ax.text(0, scale * 1.1, "𝕀", fontsize=12, ha="center", va="center")

plt.grid(True, alpha=0.35)

points = []
colors = []

def gaussian_primes():
    for i in range(1, scale)[::-1]:
        res = set()
        for a in range(i + 1):
            for b in range(a, i + 1):
                if a == 0 and b == 0:
                    continue
                if a == 0 or b == 0:
                    if ((a % 4) == 3 and sympy.isprime(a)) or ((b % 4) == 3 and sympy.isprime(b)):
                        res.add((a,b))
                        res.add((-a,b))
                        res.add((a,-b))
                        res.add((-a,-b))
                        res.add((b,a))
                        res.add((-b,a))
                        res.add((b,-a))
                        res.add((-b,-a))
                norm = a**2 + b**2
                if sympy.isprime(norm):
                    res.add((a, b))
                    res.add((-a,b))
                    res.add((a,-b))
                    res.add((-a,-b))
                    res.add((b,a))
                    res.add((-b,a))
                    res.add((b,-a))
                    res.add((-b,-a))


        gaussians = set(map(tuple, np.vstack(tuple(map(np.ravel, np.meshgrid(np.arange(-i, i + 1), np.arange(-i, i + 1))))).T))
        freq = len(gaussians & res) / len(gaussians)
        print(f"{freq * 100}% of points covered.")

        res = np.array(list(res))
        points.extend(res)
        colors.extend([i] * len(res))

gaussian_primes()

points = np.array(points)
colors = np.array(colors)
scatter = ax.scatter(points[:, 0], points[:, 1], c=colors, cmap="jet", s=10, alpha=0.5)
plt.colorbar(scatter, ax=ax)
plt.show()