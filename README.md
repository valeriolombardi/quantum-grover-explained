# Quantum Grover Explained

This repository contains a **reproducible, executable, and educational demonstration**
of **Grover’s algorithm**, implemented in Python using **Qiskit**.

The goal is not to publish a research paper, but to show — **honestly and concretely** —
what changes when we move from a **classical search** to a **quantum search**.

Everything you see here:
- runs locally
- shows the actual code being executed
- avoids misleading metaphors
- separates physics from simplification

---

## 🔍 The Problem (Explained for Everyone)

Imagine a lock made of **4 small switches**.

Each switch can be:
- ON (1)
- OFF (0)

So we have **16 possible combinations**, for example:

```
0000
0001
0010
...
1011  ← this is the correct one
```

The task is very simple:

> **Find the correct combination (`1011`).**

This is the same kind of problem your phone, computer, or router solves every day:
searching for the right value among many possibilities.

---

## 💻 Classical Approach: One Attempt at a Time

A classical computer works **sequentially**.

It checks:
- first combination
- then the next
- then the next
- until it finds the right one

In the worst case, it must check **all 16 combinations**.

If the number of possibilities grows, the time grows **linearly**:
- 16 → fast
- 1,000,000 → slow
- 1,000,000,000 → very slow

This is called **O(N)** complexity.

---

## ⚛️ Quantum Approach: Grover’s Algorithm

A quantum computer works in a very different way.

It does **not** try all combinations one by one.
It also does **not** “guess”.

Instead, it uses three key ideas:

### 1️⃣ Superposition
All possible combinations are represented **at the same time** as a single quantum state.

In code, this happens here:

```python
qc.h([0, 1, 2, 3])
```

This is the moment where:
> **the list of 16 combinations becomes one probability wave.**

---

### 2️⃣ Oracle (Marking the Correct Answer)

The **Oracle** is a quantum operation that:
- does NOT reveal the correct answer
- only **marks it** by flipping its phase

Think of it as:
> “I don’t know where the solution is, but I know how to recognize it.”

In the code, this is done using a **multi-controlled gate (`mcx`)**.

This step is **essential**.
Without it, the algorithm would just return a random result.

---

### 3️⃣ Diffuser (Amplitude Amplification)

The **Diffuser** takes the small phase difference introduced by the Oracle and:
- amplifies the probability of the correct answer
- suppresses the wrong ones

This is where **quantum interference** happens:
wrong paths cancel out, the right one survives.

---

## 📈 Why This Is Faster

For **16 possibilities**:

- Classical search: up to **16 checks**
- Grover’s algorithm: about **√16 ≈ 4 iterations**

This is not a constant-time miracle,
but a **quadratic speedup**, which becomes dramatic at scale.

Example:
- 1,000,000 possibilities  
  - Classical: ~1,000,000 checks  
  - Quantum: ~1,000 iterations  

This is what people mean by **“scale of change”**.

---

## ▶️ Running the Experiment

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the demo
```bash
python grover_demo.py
```

You will see:
- the **classical search**, step by step
- the **quantum circuit**, explained while it is built
- the **measurement result**
- a **final comparison plot**

Everything shown in the terminal is real execution, not animation.

---

## 🎥 Video Walkthrough

A full explanation of:
- the problem
- the classical code
- the quantum code
- the physics behind the algorithm

👉 Medium article:
https://medium.com/@valeriolombardi.com/cercare-lago-nel-pagliaio-il-test-quantistico-spiegato-passo-passo-c7a1a875a45f

---

## 🎯 What This Project Is (and Is Not)

✅ It **is**:
- educational
- reproducible
- scientifically honest
- based on real quantum logic

❌ It is **not**:
- a claim of quantum supremacy
- a hardware benchmark
- a replacement for academic literature

If you are a physicist, engineer, or researcher and spot an imprecision,
feedback and discussion are welcome.

---

## 📄 License

MIT License — free to use, modify, and share with attribution.
