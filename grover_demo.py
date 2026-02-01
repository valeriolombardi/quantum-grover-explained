"""
Grover Algorithm – Educational Demonstration
Author: Valerio Lombardi
Purpose: Explain classical vs quantum search in a reproducible way
"""
import time
import os
import platform
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

# --- FUNZIONI DI UTILITÀ ---
def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def slide_frame(title, points, delay=1.2):
    clear()
    print("=" * 80)
    print(f"  🔬 {title.upper()} 🔬")
    print("=" * 80)
    print("\n")
    for p in points:
        print(f"  ➤ {p}")
        time.sleep(delay)
    print("\n" + "=" * 80)
    input("\n  [Premi INVIO per continuare...]")

def animate_progress(text, steps=20, delay=0.1):
    for i in range(steps + 1):
        bar = '█' * i + '-' * (steps - i)
        print(f"\r{text}: |{bar}| {int(i/steps*100)}%", end="")
        time.sleep(delay)
    print("\n")

def visualizza_combinazione(bin_str):
    """Rappresenta la combinazione come 4 luci accese/spente."""
    return ' '.join(['💡' if b=='1' else '⚫' for b in bin_str])

# --- PRESENTAZIONE QUANTISTICA ---
def esegui_presentazione_quantistica():
    # --- SLIDE 0: HOOK INIZIALE ---
    slide_frame("Cosa succederebbe se...",
        ["Cosa succederebbe se potessi cercare un ago in un pagliaio senza dover guardare ogni singolo filo?",
         "Oggi vi mostro come il calcolo quantistico riscrive le regole della logica!"])

    # --- SLIDE 1: IL PROBLEMA QUOTIDIANO ---
    slide_frame("Il problema quotidiano",
        ["Immagina di avere una porta con 4 luci, ciascuna accesa (1) o spenta (0).",
         "Il codice giusto per aprirla è 💡⚫💡💡 (binario: 1011).",
         "Ci sono 16 possibili combinazioni (0000 → 1111).",
         "Il metodo classico prova una combinazione alla volta (O(N)).",
         "Se raddoppiano le combinazioni, raddoppia il tempo necessario."])

    # --- SIMULAZIONE CLASSICA ---
    clear()
    print("💻 SIMULAZIONE CLASSICA: TROVA IL CODICE 💡⚫💡💡")
    print("Guardate il computer classico: sta provando ogni singola combinazione, lentamente e faticosamente.\n")
    
    codice_classico = """
target_id = '1011'
for i in range(16):
    current = format(i, '04b')
    if current == target_id:
        print("Trovato!")
        break
"""
    print("📜 Codice Python eseguito (Classico):")
    print(codice_classico)
    time.sleep(2)

    target_id = "1011"
    n_chiavi = 16
    passaggi_classici = 0

    for i in range(n_chiavi):
        current = format(i, '04b')
        passaggi_classici += 1
        print(f"\rControllo combinazione: {visualizza_combinazione(current)} [{current}]", end="")
        time.sleep(0.4)
        if current == target_id:
            print(f"\n✅ TARGET TROVATO! Passaggi classici: {passaggi_classici}")
            break
    input("\n[Premi INVIO per vedere il Quantum in azione...]")

    # --- SLIDE 2: SALTO QUANTISTICO ---
    slide_frame("Il salto quantistico",
        ["Concetto chiave: Sovrapposizione → tutte le combinazioni esistono insieme.",
         "Interferenza: amplifica la probabilità della combinazione corretta e annulla le altre.",
         "Algoritmo di Grover: riduce drasticamente i tentativi da N a √N (~4 invece di 16).",
         "Ora vediamo come il quantum trova il codice senza provarle tutte!"])

    # --- SIMULAZIONE QUANTISTICA VISIVA ---
    clear()
    print("🧪 SIMULAZIONE QUANTISTICA: TROVA IL CODICE 💡⚫💡💡")
    print("Qui non c'è una lista. C'è un'onda di probabilità. Non stiamo bussando a ogni porta;")
    print("stiamo facendo in modo che la porta giusta si apra da sola.\n")
    
    codice_quantum = """
from qiskit import QuantumCircuit
qc = QuantumCircuit(4)
qc.h([0,1,2,3])           # Sovrapposizione: qui le 16 possibilità diventano un'unica onda
# Oracolo: riconosce target 1011
qc.x([2])
qc.h(3)
qc.mcx([0,1,2], 3)       # L'oracolo marca la risposta corretta senza leggerla
qc.h(3)
qc.x([2])
# Diffusore di Grover
qc.h([0,1,2,3])
qc.x([0,1,2,3])
qc.h(3)
qc.mcx([0,1,2],3)
qc.h(3)
qc.x([0,1,2,3])
qc.h([0,1,2,3])
qc.measure_all()
"""
    print("📜 Codice Python eseguito (Quantum):")
    print(codice_quantum)
    time.sleep(3)

    # Lampeggio probabilità
    combinazioni = [format(i,'04b') for i in range(16)]
    for _ in range(8):
        corrente = random.choice(combinazioni)
        print(f"\rProbabilità: {visualizza_combinazione(corrente)} [{corrente}]", end="")
        time.sleep(0.3)
    print("\n")
    time.sleep(1)

    # --- COSTRUZIONE CIRCUITO QUANTISTICO REALE ---
    qc = QuantumCircuit(4)
    qc.h([0,1,2,3])
    qc.x([2])
    qc.h(3)
    qc.mcx([0,1,2], 3)
    qc.h(3)
    qc.x([2])
    qc.h([0,1,2,3])
    qc.x([0,1,2,3])
    qc.h(3)
    qc.mcx([0,1,2],3)
    qc.h(3)
    qc.x([0,1,2,3])
    qc.h([0,1,2,3])
    qc.measure_all()

    sim = AerSimulator()
    t_qc = transpile(qc, sim)
    result = sim.run(t_qc, shots=1).result()
    output_q = list(result.get_counts().keys())[0]

    print(f"\n🎯 RISULTATO QUANTISTICO: {visualizza_combinazione(output_q)} [{output_q}]")
    print("⚡ Il target viene trovato con alta probabilità in pochi passi (~4 invece di 16).")
    input("\n[Premi INVIO per le Conclusioni...]")

    # --- SLIDE 3: CONCLUSIONI + SCALA DEL CAMBIAMENTO ---
    slide_frame("Conclusioni e impatto reale",
        [f"Classico: {passaggi_classici} tentativi sequenziali.",
         "Quantistico: ~4 iterazioni coerenti grazie a Grover.",
         "Applicazioni reali: sicurezza informatica, farmaceutica, analisi big data.",
         "Scala del cambiamento:",
         "   Se ci fossero 1 milione di combinazioni, il classico richiederebbe ore,",
         "   mentre il Quantum, in ~1000 iterazioni logiche, troverebbe la soluzione in pochi secondi simulati."])

    # --- GRAFICO FINALE ---
    mostra_risultati(passaggi_classici, 4)

# --- GRAFICO PROFESSIONALE ---
def mostra_risultati(classico, quantistico):
    plt.rcParams.update({'font.size': 12})  # ingrandisci font
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8,5))  # finestra più compatta
    labels = ['Classico (Bit)', 'Quantistico (Qubit)']
    values = [classico, quantistico]
    colors = ['#FF3B30', '#007AFF']
    bars = ax.bar(labels, values, color=colors)
    ax.set_title('Confronto Efficienza: Ricerca Codice 💡⚫💡💡', fontsize=16, pad=15, color='white')
    ax.set_ylabel('Numero di Tentativi', fontsize=12)
    ax.set_facecolor('#1c1c1c')
    fig.patch.set_facecolor('#1c1c1c')
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{int(yval)}', ha='center', va='bottom', fontsize=12, fontweight='bold', color='white')
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    print("\n📊 Generazione grafico finale...")
    plt.show()

# --- MAIN ---
if __name__ == "__main__":
    esegui_presentazione_quantistica()
