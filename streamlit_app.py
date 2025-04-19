
import streamlit as st

st.set_page_config(page_title="Business Model Canvas Assistent", layout="centered")

st.title("🚀 Business Model Canvas Assistent")

st.markdown("Dieser Assistent hilft Ihnen dabei, ein vollständiges Geschäftsmodell zu entwickeln.")

def feld_eingabe(name, erklaerung):
    return st.text_area(f"📌 {name}", f"💬 {erklaerung}")

bmc = {}

bmc["Kundensegmente"] = feld_eingabe(
    "Kundensegmente",
    "Für wen schaffen Sie Wert? Wer sind Ihre wichtigsten Kunden(gruppen)?"
)

bmc["Wertangebote"] = feld_eingabe(
    "Wertangebote",
    "Welche Probleme lösen Sie? Welchen Nutzen bieten Sie?"
)

bmc["Kanäle"] = feld_eingabe(
    "Kanäle",
    "Wie erreichen Sie Ihre Kunden? Über welche Kanäle kommunizieren und liefern Sie Ihr Angebot?"
)

bmc["Kundenbeziehungen"] = feld_eingabe(
    "Kundenbeziehungen",
    "Welche Art von Beziehung erwarten Ihre Kunden von Ihnen? (z.B. persönlich, automatisiert, Self-Service)"
)

bmc["Einnahmequellen"] = feld_eingabe(
    "Einnahmequellen",
    "Wofür sind Ihre Kunden bereit zu zahlen? Wie generieren Sie Einnahmen?"
)

bmc["Schlüsselressourcen"] = feld_eingabe(
    "Schlüsselressourcen",
    "Welche Ressourcen sind unerlässlich für Ihr Geschäftsmodell? (z.B. Personal, Technik, Wissen)"
)

bmc["Schlüsselaktivitäten"] = feld_eingabe(
    "Schlüsselaktivitäten",
    "Welche Tätigkeiten sind zentral für die Erbringung Ihres Angebots?"
)

bmc["Partnerschaften"] = feld_eingabe(
    "Partnerschaften",
    "Wer sind Ihre wichtigsten Partner? Welche Leistungen erbringen diese?"
)

bmc["Kostenstruktur"] = feld_eingabe(
    "Kostenstruktur",
    "Welche sind die wichtigsten Kostenfaktoren Ihres Geschäftsmodells?"
)

if st.button("Canvas auswerten"):
    st.subheader("🎯 Ihre Business Model Canvas Zusammenfassung")
    for key, value in bmc.items():
        st.markdown(f"**{key}:** {value}")

    st.subheader("🔍 Vorschläge für nächste Schritte")
    if not bmc["Kundensegmente"].strip():
        st.markdown("- Definieren Sie klar, für wen Sie Mehrwert schaffen möchten.")
    if not bmc["Wertangebote"].strip():
        st.markdown("- Entwickeln Sie ein konkretes Wertangebot basierend auf den Bedürfnissen Ihrer Kunden.")
    if bmc["Kanäle"].strip():
        st.markdown("- Überprüfen Sie, ob Ihre Vertriebskanäle effizient sind und zur Zielgruppe passen.")
    if not bmc["Einnahmequellen"].strip():
        st.markdown("- Planen Sie, wie genau Sie Einnahmen generieren wollen.")
    if not bmc["Kostenstruktur"].strip():
        st.markdown("- Kalkulieren Sie die Kosten für Ihr Geschäftsmodell realistisch.")
    if not bmc["Schlüsselaktivitäten"].strip():
        st.markdown("- Identifizieren Sie die wichtigsten Aufgaben zur Umsetzung Ihres Angebots.")
    if bmc["Partnerschaften"].strip():
        st.markdown("- Stellen Sie sicher, dass Ihre Partnerschaften echten Mehrwert liefern.")
    
    st.markdown("📌 *Tipp: Nutzen Sie dieses Canvas als Grundlage für Ihren Businessplan oder Pitch!*")
