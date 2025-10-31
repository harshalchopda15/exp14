# Quantum Algorithm and Computational Methods
# Program: Deutsch–Jozsa Algorithm (n=4) for a constant function f(x)=0

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

def deutsch_jozsa_constant(n=4, shots=1024):
    """
    Implements the Deutsch–Jozsa algorithm for n input qubits
    with a constant oracle (f(x) = 0)
    """
    # Total qubits = n input + 1 ancilla
    qc = QuantumCircuit(n + 1, n)

    # Step 1: Initialize the ancilla qubit in |1⟩
    qc.x(n)

    # Step 2: Apply Hadamard to all qubits (inputs + ancilla)
    qc.h(range(n + 1))

    # --- Oracle for f(x) = 0 ---
    # Do nothing (oracle leaves ancilla unchanged)
    # --- End Oracle ---

    # Step 3: Apply Hadamard to input qubits
    qc.h(range(n))

    # Step 4: Measure the input qubits
    qc.measure(range(n), range(n))

    # Simulation
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    # Display output
    print(f"Deutsch–Jozsa Algorithm for Constant Function (n={n})")
    display(qc.draw('mpl'))
    display(plot_histogram(counts))

    # Interpretation
    print("\nMeasurement counts (input qubits):")
    print(counts)
    print("\nExpected Result: Only '0000' → Oracle is constant.")

# Run the algorithm
deutsch_jozsa_constant(n=4, shots=1024)

