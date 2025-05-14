import streamlit as st
from gurobipy import Model, GRB, quicksum
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Problème de Flot Maximum", layout="wide")

st.title("💧 Résolution du Problème de Flot Maximum avec Gurobi")

# === Entrée des nœuds ===
st.subheader("Étape 1 : Définir les nœuds")
nodes_input = st.text_area("Liste des nœuds (séparés par des virgules)", "A,B,C,D,E")
nodes = [n.strip() for n in nodes_input.split(",") if n.strip()]

source = st.selectbox("Nœud Source", nodes)
sink = st.selectbox("Nœud Puits", [n for n in nodes if n != source])

# === Entrée des arcs ===
st.subheader("Étape 2 : Définir les arcs et leurs capacités")
edges_data = st.text_area(
    "Liste des arcs (format: départ, arrivée, capacité - un par ligne)",
    "A,B,10\nA,C,5\nB,C,15\nB,D,10\nC,E,10\nD,E,10"
)

edges = {}
if st.button("🔍 Résoudre le problème"):
    try:
        for line in edges_data.strip().split("\n"):
            u, v, cap = line.strip().split(",")
            edges[(u.strip(), v.strip())] = float(cap)

        # === Modèle Gurobi ===
        model = Model("Flot_Maximum")
        flow = model.addVars(edges.keys(), name="Flow", lb=0)
        model.setObjective(quicksum(flow[u, v] for (u, v) in edges if v == sink), GRB.MAXIMIZE)

        for (u, v), cap in edges.items():
            model.addConstr(flow[u, v] <= cap)

        for node in nodes:
            if node != source and node != sink:
                inflow = quicksum(flow[u, v] for (u, v) in edges if v == node)
                outflow = quicksum(flow[u, v] for (u, v) in edges if u == node)
                model.addConstr(inflow == outflow)

        model.optimize()

        # === Affichage Résultat ===
        if model.status == GRB.OPTIMAL:
            st.success(f"✅ Flot total maximum : {model.objVal:.2f}")
            st.markdown("### 🔄 Détail des flots :")
            for (u, v) in edges:
                flot = flow[u, v].x
                st.write(f"**{u} → {v}** : {flot:.2f} / {edges[(u, v)]}")

            # === Visualisation ===
            st.subheader("🧭 Visualisation du réseau de flots")
            G = nx.DiGraph()
            edge_colors = []
            edge_labels = {}
            epsilon = 1e-5

            for (u, v), cap in edges.items():
                flot = flow[u, v].x
                G.add_edge(u, v, weight=flot)
                edge_labels[(u, v)] = f"{flot:.1f}/{cap}"
                edge_colors.append("red" if abs(flot - cap) < epsilon else "gray")

            pos = nx.spring_layout(G, seed=42)
            fig, ax = plt.subplots(figsize=(10, 6))
            nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=12, edge_color=edge_colors, width=2, ax=ax)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)
            ax.set_title("Graphe du flot maximum (arcs saturés en rouge)")
            ax.axis('off')
            st.pyplot(fig)
        else:
            st.error("❌ Aucune solution optimale trouvée.")

    except Exception as e:
        st.error(f"Erreur : {e}")
