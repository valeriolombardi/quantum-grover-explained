# Quantum Grover Explained

This repository contains a **reproducible, executable, and educational demonstration**
of **Groverâ€™s algorithm**, implemented in Python using **Qiskit**.

The goal is not to publish a research paper, but to show â€” **honestly and concretely** â€”
what changes when we move from a **classical search** to a **quantum search**.

Everything you see here:
- runs locally
- shows the actual code being executed
- avoids misleading metaphors
- separates physics from simplification

---

## ðŸ” The Problem (Explained for Everyone)

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
1011  â† this is the correct one
```

The task is very simple:

> **Find the correct combination (`1011`).**

This is the same kind of problem your phone, computer, or router solves every day:
searching for the right value among many possibilities.

---

## ðŸ’» Classical Approach: One Attempt at a Time

A classical computer works **sequentially**.

It checks:
- first combination
- then the next
- then the next
- until it finds the right one

In the worst case, it must check **all 16 combinations**.

If the number of possibilities grows, the time grows **linearly**:
- 16 â†’ fast
- 1,000,000 â†’ slow
- 1,000,000,000 â†’ very slow

This is called **O(N)** complexity.

---

## âš›ï¸ Quantum Approach: Groverâ€™s Algorithm

A quantum computer works in a very different way.

It does **not** try all combinations one by one.
It also does **not** â€œguessâ€.

Instead, it uses three key ideas:

### 1ï¸âƒ£ Superposition
All possible combinations are represented **at the same time** as a single quantum state.

In code, this happens here:

```python
qc.h([0, 1, 2, 3])
```

This is the moment where:
> **the list of 16 combinations becomes one probability wave.**

---

### 2ï¸âƒ£ Oracle (Marking the Correct Answer)

The **Oracle** is a quantum operation that:
- does NOT reveal the correct answer
- only **marks it** by flipping its phase

Think of it as:
> â€œI donâ€™t know where the solution is, but I know how to recognize it.â€

In the code, this is done using a **multi-controlled gate (`mcx`)**.

This step is **essential**.
Without it, the algorithm would just return a random result.

---

### 3ï¸âƒ£ Diffuser (Amplitude Amplification)

The **Diffuser** takes the small phase difference introduced by the Oracle and:
- amplifies the probability of the correct answer
- suppresses the wrong ones

This is where **quantum interference** happens:
wrong paths cancel out, the right one survives.

---

## ðŸ“ˆ Why This Is Faster

For **16 possibilities**:

- Classical search: up to **16 checks**
- Groverâ€™s algorithm: about **âˆš16 â‰ˆ 4 iterations**

This is not a constant-time miracle,
but a **quadratic speedup**, which becomes dramatic at scale.

Example:
- 1,000,000 possibilities  
  - Classical: ~1,000,000 checks  
  - Quantum: ~1,000 iterations  

This is what people mean by **â€œscale of changeâ€**.

---

## â–¶ï¸ Running the Experiment

### 1ï¸âƒ£ Install dependencies
```bash
pip install -r requirements.txt
```

### 2ï¸âƒ£ Run the demo
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

## ðŸŽ¥ Video Walkthrough

A full explanation of:
- the problem
- the classical code
- the quantum code
- the physics behind the algorithm

ðŸ‘‰ Medium article:
https://medium.com/@valeriolombardi.com/cercare-lago-nel-pagliaio-il-test-quantistico-spiegato-passo-passo-c7a1a875a45f

---

## ðŸŽ¯ What This Project Is (and Is Not)

âœ… It **is**:
- educational
- reproducible
- scientifically honest
- based on real quantum logic

âŒ It is **not**:
- a claim of quantum supremacy
- a hardware benchmark
- a replacement for academic literature

If you are a physicist, engineer, or researcher and spot an imprecision,
feedback and discussion are welcome.

---

## ðŸ“„ License

MIT License â€” free to use, modify, and share with attribution.
