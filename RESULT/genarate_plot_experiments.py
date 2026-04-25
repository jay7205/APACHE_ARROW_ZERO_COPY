import matplotlib.pyplot as plt
import os

os.makedirs("RESULT", exist_ok=True)

# -----------------------------
# GLOBAL STYLE (consistent look)
# -----------------------------
plt.rcParams.update({
    "figure.figsize": (7, 4),
    "axes.grid": True,
    "grid.alpha": 0.3,
    "font.size": 10
})


# -----------------------------
# 1. Zero-copy vs Copy (FIXED)
# -----------------------------
def plot_zero_copy_vs_copy():
    sizes = [1_000_000, 5_000_000, 10_000_000]

    zero_copy = [0.000014, 0.000014, 0.000014]
    copy = [2.3, 6.5, 11.5]

    plt.figure()
    plt.plot(sizes, zero_copy, marker='o', linewidth=2, label='Zero-copy')
    plt.plot(sizes, copy, marker='o', linewidth=2, label='Copy')

    plt.yscale('log')  # IMPORTANT FIX

    plt.xlabel("Data Size")
    plt.ylabel("Time (seconds, log scale)")
    plt.title("Zero-Copy vs Copy Performance")
    plt.legend()

    plt.savefig("RESULT/zero_copy_vs_copy_plot.png", bbox_inches='tight')
    plt.close()


# -----------------------------
# 2. Scaling Behavior (FIXED)
# -----------------------------
def plot_scaling():
    sizes = [1_000_000, 5_000_000, 10_000_000, 50_000_000]
    times = [0.089, 0.0011, 0.0023, 0.015]

    plt.figure()
    plt.plot(sizes, times, marker='o', linewidth=2)

    plt.xscale('log')  # FIX
    plt.yscale('log')  # FIX

    plt.xlabel("Data Size (log scale)")
    plt.ylabel("Time (seconds, log scale)")
    plt.title("Scaling Behavior (Log-Log View)")

    plt.savefig("RESULT/scaling_plot.png", bbox_inches='tight')
    plt.close()


# -----------------------------
# 3. Memory Pool (FIXED)
# -----------------------------
def plot_memory_pool():
    stages = ["Initial", "After arr1", "After arr2", "After delete"]
    memory = [0, 80, 160, 80]

    plt.figure()
    plt.plot(stages, memory, marker='o', linewidth=2)

    plt.ylabel("Memory (MB)")
    plt.title("Memory Pool Behavior")

    plt.savefig("RESULT/memory_pool_plot.png", bbox_inches='tight')
    plt.close()


# -----------------------------
# 4. Null Bitmap (FIXED)
# -----------------------------
def plot_null_bitmap():
    labels = ["No Nulls", "With Nulls"]
    times = [1.02, 0.48]

    plt.figure()
    plt.bar(labels, times)

    plt.ylabel("Time (seconds)")
    plt.title("Null Bitmap Impact")

    # ADD EXPLANATION TEXT ON GRAPH
    plt.text(0.5, max(times)*0.9,
             "Result affected by Python overhead / noise",
             ha='center', fontsize=8)

    plt.savefig("RESULT/null_bitmap_plot.png", bbox_inches='tight')
    plt.close()


# -----------------------------
# 5. Break Zero-Copy (FIXED)
# -----------------------------
def plot_break_zero_copy():
    cases = ["Slice", "Python List", "NumPy"]
    times = [0.000014, 11.5, 0.000014]

    plt.figure()
    plt.bar(cases, times)

    plt.yscale('log')  # IMPORTANT FIX

    plt.ylabel("Time (seconds, log scale)")
    plt.title("Zero-Copy vs Breaking Conditions")

    plt.savefig("RESULT/break_zero_copy_plot.png", bbox_inches='tight')
    plt.close()


# -----------------------------
# RUN ALL
# -----------------------------
plot_zero_copy_vs_copy()
plot_scaling()
plot_memory_pool()
plot_null_bitmap()
plot_break_zero_copy()

print("All fixed plots generated successfully.")