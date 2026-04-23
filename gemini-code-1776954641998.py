import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculateur Echafaudage Pro", layout="centered")

st.title("🏗️ Calculateur de Charges Échafaudage")

# Abas/Tabs
tab1, tab2 = st.tabs(["Pont de Service", "Échafaudage de Façade"])

# --- TAB 1: PONT DE SERVICE ---
with tab1:
    st.header("Pont de Service")
    nom_projet1 = st.text_input("Nom du Projet", key="p1")
    poids_mat1 = st.number_input("Poids du Matériel (kg)", min_value=0.0, step=1.0)
    charge_utile1 = st.number_input("Charge Utile (kg)", min_value=0.0, step=1.0)
    nb_pieds1 = st.selectbox("Nombre de pieds ao solo", [4, 6])

    charge_totale1 = poids_mat1 + charge_utile1
    
    if st.button("Générer Rapport Pont"):
        st.subheader("Résultats")
        st.error("⚠️ STOCKAGE INTERDIT SUR LE PONT")
        
        if nb_pieds1 == 4:
            par_pied = round(charge_totale1 / 4)
            res = f"Charge par pied: {par_pied} kg"
        else:
            central = round(charge_totale1 * 0.25)
            coin = round(charge_totale1 * 0.125)
            res = f"Pieds Centraux: {central} kg | Pieds de Coin: {coin} kg"
        
        st.write(f"**Total: {charge_totale1} kg**")
        st.info(res)
        
        # Bloco para copiar
        report = f"Rapport: {nom_projet1}\nType: Pont de Service\nPoids Matériel: {poids_mat1}kg\nCharge Utile: {charge_utile1}kg\n{res}\nSTOCKAGE INTERDIT"
        st.text_area("Copier pour WhatsApp:", report)

# --- TAB 2: ECHAFAUDAGE DE FAÇADE ---
with tab2:
    st.header("Échafaudage de Façade")
    nom_projet2 = st.text_input("Nom du Projet", key="p2")
    classe = st.selectbox("Classe de charge", [200, 300, "Personnalisé"])
    if classe == "Personnalisé":
        val_classe = st.number_input("Valeur (kg/m²)", value=200)
    else:
        val_classe = classe
        
    larg = st.number_input("Largeur de la trame (m) - ex: 0.73", value=0.73)
    long = st.selectbox("Longueur de la trame (m)", [1.20, 1.50, 1.80, 2.00, 2.50, 3.00, 3.60])
    poids_mat2 = st.number_input("Poids total du matériel façade (kg)", min_value=0.0)
    nb_pieds2 = st.number_input("Nombre total de pieds au sol", min_value=2, value=2)

    if st.button("Générer Rapport Façade"):
        g_pied = round(poids_mat2 / nb_pieds2)
        q_pied = round((long * larg * val_classe) / 2)
        total_pied = g_pied + q_pied
        
        st.subheader("Résultats par pied")
        st.write(f"Carga Permanente (G): {g_pied} kg")
        st.write(f"Carga Utile (Q): {q_pied} kg")
        st.success(f"**Charge Maximale par Pied: {total_pied} kg**")
        
        report_f = f"Rapport: {nom_projet2}\nType: Façade\nTrame: {long}x{larg}m\nCharge G: {g_pied}kg\nCharge Q: {q_pied}kg\nTOTAL MAX: {total_pied}kg"
        st.text_area("Copier pour WhatsApp:", report_f)

st.divider()
st.caption("Note : Ce calcul est indicatif. La résistance du sol doit être validée avant installation. Cales obligatoires.")