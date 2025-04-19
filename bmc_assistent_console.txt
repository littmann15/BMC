
def erklaerung_und_eingabe(feldname, erklaerung):
    print(f"\n=== {feldname} ===")
    print(f"Erklärung: {erklaerung}")
    eingabe = input(f"Bitte geben Sie Ihre Idee für '{feldname}' ein:\n> ")
    return eingabe

def generiere_vorschlaege(bmc):
    print("\n🔍 Vorschläge für nächste Schritte basierend auf Ihren Eingaben:")
    
    if not bmc["Kundensegmente"]:
        print("- Definieren Sie klar, für wen Sie Mehrwert schaffen möchten.")
    if not bmc["Wertangebote"]:
        print("- Entwickeln Sie ein konkretes Wertangebot basierend auf den Bedürfnissen Ihrer Kunden.")
    if bmc["Kanäle"]:
        print("- Überprüfen Sie, ob Ihre Vertriebskanäle effizient sind und zur Zielgruppe passen.")
    if not bmc["Einnahmequellen"]:
        print("- Planen Sie, wie genau Sie Einnahmen generieren wollen.")
    if not bmc["Kostenstruktur"]:
        print("- Kalkulieren Sie die Kosten für Ihr Geschäftsmodell realistisch.")
    if not bmc["Schlüsselaktivitäten"]:
        print("- Identifizieren Sie die wichtigsten Aufgaben zur Umsetzung Ihres Angebots.")
    if bmc["Partnerschaften"]:
        print("- Stellen Sie sicher, dass Ihre Partnerschaften echten Mehrwert liefern.")

    print("\n📌 Allgemeiner Tipp: Erstellen Sie aus dieser Canvas-Version ein Pitch-Deck oder Businessplan.")


def main():
    print("🚀 Willkommen zum interaktiven Business Model Canvas Assistenten!\n")
    print("Sie werden durch alle 9 Bausteine des Canvas geführt. Geben Sie Ihre Antworten sorgfältig ein.")

    bmc = {}

    bmc["Kundensegmente"] = erklaerung_und_eingabe(
        "Kundensegmente",
        "Für wen schaffen Sie Wert? Wer sind Ihre wichtigsten Kunden(gruppen)?"
    )

    bmc["Wertangebote"] = erklaerung_und_eingabe(
        "Wertangebote",
        "Welche Probleme lösen Sie? Welchen Nutzen bieten Sie?"
    )

    bmc["Kanäle"] = erklaerung_und_eingabe(
        "Kanäle",
        "Wie erreichen Sie Ihre Kunden? Über welche Kanäle kommunizieren und liefern Sie Ihr Angebot?"
    )

    bmc["Kundenbeziehungen"] = erklaerung_und_eingabe(
        "Kundenbeziehungen",
        "Welche Art von Beziehung erwarten Ihre Kunden von Ihnen? (z.B. persönlich, automatisiert, Self-Service)"
    )

    bmc["Einnahmequellen"] = erklaerung_und_eingabe(
        "Einnahmequellen",
        "Wofür sind Ihre Kunden bereit zu zahlen? Wie generieren Sie Einnahmen?"
    )

    bmc["Schlüsselressourcen"] = erklaerung_und_eingabe(
        "Schlüsselressourcen",
        "Welche Ressourcen sind unerlässlich für Ihr Geschäftsmodell? (z.B. Personal, Technik, Wissen)"
    )

    bmc["Schlüsselaktivitäten"] = erklaerung_und_eingabe(
        "Schlüsselaktivitäten",
        "Welche Tätigkeiten sind zentral für die Erbringung Ihres Angebots?"
    )

    bmc["Partnerschaften"] = erklaerung_und_eingabe(
        "Partnerschaften",
        "Wer sind Ihre wichtigsten Partner? Welche Leistungen erbringen diese?"
    )

    bmc["Kostenstruktur"] = erklaerung_und_eingabe(
        "Kostenstruktur",
        "Welche sind die wichtigsten Kostenfaktoren Ihres Geschäftsmodells?"
    )

    print("\n🎯 Ihre Business Model Canvas Zusammenfassung:\n")
    for schluessel, wert in bmc.items():
        print(f"{schluessel}: {wert}")

    generiere_vorschlaege(bmc)


if __name__ == "__main__":
    main()
