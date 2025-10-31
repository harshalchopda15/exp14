# Quantum Algorithm and Computational Methods
# Program: Deutsch–Jozsa Algorithm (n=2) for Constant and Balanced Functions

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

# ----------------------------------------------
# Constant Function: f(x) = 0
# ----------------------------------------------
def deutsch_jozsa_constant(n=2, shots=1024):
    qc = QuantumCircuit(n + 1, n)

    # Step 1: Initialize ancilla in |1⟩
    qc.x(n)

    # Step 2: Apply Hadamard to all qubits
    qc.h(range(n + 1))

    # --- Oracle for f(x) = 0 ---
    # Do nothing (constant function)
    # --- End Oracle ---

    # Step 3: Apply Hadamard to input qubits
    qc.h(range(n))

    # Step 4: Measure input qubits
    qc.measure(range(n), range(n))

    # Simulate
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    print("\nDeutsch–Jozsa Algorithm (Constant Function f(x)=0)")
    display(qc.draw('mpl'))
    display(plot_histogram(counts))
    print("Expected Output: Only '00' → Oracle is constant.")
    print(counts)

# ----------------------------------------------
# Balanced Function: f(x) = x0 ⊕ x1
# ----------------------------------------------
def deutsch_jozsa_balanced(n=2, shots=1024):
    qc = QuantumCircuit(n + 1, n)

    # Step 1: Initialize ancilla in |1⟩
    qc.x(n)

    # Step 2: Apply Hadamard to all qubits
    qc.h(range(n + 1))

    # --- Oracle for f(x) = x0 XOR x1 ---
    qc.cx(0, n)
    qc.cx(1, n)
    # --- End Oracle ---

    # Step 3: Apply Hadamard to input qubits
    qc.h(range(n))

    # Step 4: Measure input qubits
    qc.measure(range(n), range(n))

    # Simulate
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    print("\nDeutsch–Jozsa Algorithm (Balanced Function f(x)=x0⊕x1)")
    display(qc.draw('mpl'))
    display(plot_histogram(counts))
    print("Expected Output: Multiple results (not all '00') → Oracle is balanced.")
    print(counts)

# Run both versions
deutsch_jozsa_constant()
deutsch_jozsa_balanced()

