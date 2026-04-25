import matplotlib.pyplot as plt

# -----------------------------
# 1. Execution Flow Diagram
# -----------------------------
def execution_flow():
    fig, ax = plt.subplots(figsize=(6, 8))

    steps = [
        "Python API\npa.array()",
        "array.pxi",
        "ConvertPySequence",
        "Converter->Extend",
        "ArrayData",
        "Buffer (Memory)"
    ]

    y_positions = list(range(len(steps), 0, -1))

    for i, (step, y) in enumerate(zip(steps, y_positions)):
        ax.text(0.5, y, step, ha='center', va='center',
                bbox=dict(boxstyle="round", fc="lightblue"))

        if i < len(steps) - 1:
            ax.arrow(0.5, y-0.3, 0, -0.7,
                     head_width=0.05, head_length=0.1, fc='black')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, len(steps)+1)
    ax.axis('off')

    plt.title("Execution Flow")
    plt.savefig("DIAGRAMS/execution_flow.png", bbox_inches='tight')
    plt.close()

# -----------------------------
# 2. Memory Layout Diagram
# -----------------------------
def memory_layout():
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.text(0.5, 0.8, "ArrayData", ha='center',
            bbox=dict(boxstyle="round", fc="lightgreen"))

    ax.text(0.3, 0.4, "buffers[0]\nNull Bitmap", ha='center',
            bbox=dict(boxstyle="round", fc="lightyellow"))

    ax.text(0.7, 0.4, "buffers[1]\nValues", ha='center',
            bbox=dict(boxstyle="round", fc="lightyellow"))

    ax.annotate('', xy=(0.3, 0.5), xytext=(0.5, 0.75),
                arrowprops=dict(arrowstyle='->'))

    ax.annotate('', xy=(0.7, 0.5), xytext=(0.5, 0.75),
                arrowprops=dict(arrowstyle='->'))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.title("Memory Layout")
    plt.savefig("DIAGRAMS/memory_layout.png", bbox_inches='tight')
    plt.close()
# -----------------------------
# 3. Zero-Copy vs Copy Diagram
# -----------------------------
def zero_copy_vs_copy():
    fig, ax = plt.subplots(figsize=(8, 4))

    # Zero-copy side
    ax.text(0.2, 0.7, "Original Array", ha='center',
            bbox=dict(boxstyle="round", fc="lightblue"))

    ax.text(0.2, 0.3, "Slice Array", ha='center',
            bbox=dict(boxstyle="round", fc="lightblue"))

    ax.text(0.4, 0.5, "Shared Buffer", ha='center',
            bbox=dict(boxstyle="round", fc="lightgreen"))

    ax.annotate('', xy=(0.4, 0.55), xytext=(0.2, 0.7),
                arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xy=(0.4, 0.45), xytext=(0.2, 0.3),
                arrowprops=dict(arrowstyle='->'))

    # Copy side
    ax.text(0.7, 0.7, "Original Array", ha='center',
            bbox=dict(boxstyle="round", fc="lightblue"))

    ax.text(0.7, 0.3, "Copied Array", ha='center',
            bbox=dict(boxstyle="round", fc="lightblue"))

    ax.text(0.9, 0.5, "New Buffer", ha='center',
            bbox=dict(boxstyle="round", fc="salmon"))

    ax.annotate('', xy=(0.9, 0.55), xytext=(0.7, 0.7),
                arrowprops=dict(arrowstyle='->'))
    ax.annotate('', xy=(0.9, 0.45), xytext=(0.7, 0.3),
                arrowprops=dict(arrowstyle='->'))

    ax.axis('off')

    plt.title("Zero-Copy vs Copy")
    plt.savefig("DIAGRAMS/zero_copy_vs_copy.png", bbox_inches='tight')
    plt.close()

# -----------------------------
# Run all
# -----------------------------
execution_flow()
memory_layout()
zero_copy_vs_copy()


print("Diagrams generated successfully in DIAGRAMS/")