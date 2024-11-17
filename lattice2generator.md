### **1. Key Features of the Stabilizers**
1. **Stabilizer Dimensions:**
   - Each stabilizer is a \( m \times m \) grid (in this case, \( 3 \times 3 \)).
   - The stabilizer acts on \( m^2 = 9 \) qubits but has **weight 4**, meaning it only "interacts" with 4 qubits per stabilizer.

2. **Dependency of the Top Qubit:**
   - The top qubit of each stabilizer is determined by the lower \( (m-1) \) rows of the stabilizer grid.

3. **Weight-4 Stabilizers:**
   - Each stabilizer only measures parity (e.g., \( X \)-parity or \( Z \)-parity) over 4 specific qubits:
     - For \( m = 3 \), these qubits are labeled \( a, b, c, \text{top} \) as shown in the diagram.
     - The stabilizer acts on \( a, b, c, \text{top} \), where "top" is a function of \( a, b, c \).

---

### **2. Representation as a Generator Matrix**
To represent these stabilizers in a generator matrix, we need to encode:
- **Which qubits each stabilizer acts upon (weight-4 qubits).**
- The interactions of stabilizers with data qubits.

#### **Steps to Build the Stabilizer Matrix**
1. **Label the Qubits:**
   - Assign indices to each data qubit in the lattice. For example:
     - Qubits are organized row by row.
     - For a lattice with dimensions \( L \times L \), label the qubits \( q_0, q_1, q_2, \dots, q_{L^2 - 1} \).

2. **Label the Stabilizers:**
   - Each stabilizer is associated with a square region and is indexed accordingly. For instance:
     - \( S_0, S_1, S_2, \dots \) correspond to stabilizers in order from top-left to bottom-right.

3. **Map Stabilizers to Data Qubits:**
   - For each stabilizer, identify the 4 qubits it acts upon.
     - For \( m = 3 \), the stabilizer acts on the top qubit and the 3 lower qubits (\( a, b, c \)).
   - Assign a \( 1 \) in the generator matrix for each qubit that the stabilizer acts on.

---

### **3. Example**
#### **Small Lattice**
Let’s consider a \( 4 \times 4 \) lattice of qubits:
```
o---o---o---o
|   |   |   |
o---o---o---o
|   |   |   |
o---o---o---o
|   |   |   |
o---o---o---o
```
- Label the qubits from \( q_0 \) to \( q_{15} \) row by row.
- \( 3 \times 3 \) stabilizers overlap, acting on weight-4 qubits.

#### **Stabilizer \( S_0 \) (Top-Left Corner):**
- Acts on qubits \( q_0 \) (top), \( q_4, q_1, q_5 \) (lower rows).

Row in the generator matrix:
\[
S_0 = [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
\]

#### **Stabilizer \( S_1 \) (Shifted to the Right):**
- Acts on \( q_1 \) (top), \( q_5, q_2, q_6 \).

Row in the generator matrix:
\[
S_1 = [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
\]

#### **Generalization:**
For each stabilizer, identify its top qubit and the 3 qubits in the rows below it. Fill the row of the generator matrix with \( 1 \) at the corresponding indices.

---

### **4. General Form of the Generator Matrix**
For a lattice with \( n \) total qubits and \( k \) stabilizers:
- **Rows of the Matrix:** Correspond to stabilizers.
- **Columns of the Matrix:** Correspond to data qubits.
- **Entries (0 or 1):**
  - A \( 1 \) indicates that the stabilizer acts on the corresponding qubit.

---

### **5. Example Matrix for a \( 4 \times 4 \) Lattice**
For the small lattice example with 16 qubits and overlapping \( 3 \times 3 \) stabilizers, the generator matrix might look like:
\[
G_s =
\begin{bmatrix}
1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\  % S_0
0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\  % S_1
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots
\end{bmatrix}
\]
Each row corresponds to one stabilizer, and each column corresponds to a qubit.

---

### **6. Extend to Larger Lattices**
- For larger lattices with periodic boundary conditions:
  - The structure is repeated, but qubits and stabilizers wrap around the edges.
  - This can be automated programmatically by iterating over the lattice grid, identifying stabilizer regions, and filling the generator matrix.

---

