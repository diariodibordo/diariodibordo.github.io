import sys
import re


def replace_words_in_md_file(file_path):
    # Dizionario con le coppie chiave-valore per la sostituzione
    replacements = {
        "incantesimi'": '[**incantesimi**](/rules/incantesimi)',
        "incantesimo'": '[**incantesimo**](/rules/incantesimi)',
        "riposo lungo'": '[**riposo lungo**](/avventura/riposo-lungo)',
        "lungo'": '[**lungo**](/avventura/riposo-lungo)',
        "riposo breve'": '[**riposo breve**](/avventura/riposo-breve)',
        "bonus di competenza'": '[**bonus di competenza**](/rules/punteggi-caratteristica#bonus-di-competenza)',
        "tiro salvezza'": '[**tiro salvezza**](/rules/combattimento#tiro-salvezza)',
        "tiri salvezza'": '[**tiri salvezza**](/rules/combattimento#tiro-salvezza)',
        "Tiri salvezza'": '[**Tiri salvezza**](/rules/combattimento#tiro-salvezza)',
        "Tiri Salvezza'": '[**Tiri Salvezza**](/rules/combattimento#tiro-salvezza)',
        "tiro per colpire'": '[**tiro per colpire**](/rules/combattimento#tiro-per-colpire)',
        "tiri per colpire'": '[**tiri per colpire**](/rules/combattimento#tiro-per-colpire)',
        "rituale'": '[**rituale**](/rules/incantesimo#rituale)',
        "Saggezza'": '[**Saggezza**](/rules/punteggi-caratteristica/#saggezza)',
        "Intelligenza'": '[**Intelligenza**](/rules/punteggi-caratteristica/#intelligenza)',
        "saggezza'": '[**Saggezza**](/rules/punteggi-caratteristica/#saggezza)',
        "intelligenza'": '[**Intelligenza**](/rules/punteggi-caratteristica/#intelligenza)',
        "reazioni'": '[**reazioni**](/rules/combattimento#reazioni)',
        "Scatto'": '[**Scatto**](/rules/combattimento#scatto)',
        "Schivata'": '[**Schivata**](/rules/combattimento#schivata)',
        "punteggio di caratteristica'": '[**punteggio di caratteristica**](/rules/punteggi-caratteristica)',
        "Grado di Sfida'": '[**Grado di Sfida**](/rules/mostri#sfida)',
        "grado di sfida'": '[**grado di sfida**](/rules/mostri#sfida)',
        "azione'": '[**azione**](/rules/combattimento#azione)',
        "prova di caratteristica'": '[**prova di caratteristica**](/rules/punteggi-caratteristica/#prove-di-caratteristica)',
        "Attacco'": '[**Attacco**](/rules/combattimento#attacco)',
        "attacca'": '[**attacca**](/rules/combattimento#attacco)',
        "azione bonus'": '[**azione bonus**](/rules/combattimento#azione-bonus)',
        "resistenza'": '[**resistenza**](/rules/combattimento#resistenza)',
        "Destrezza'": '[**Destrezza**](/rules/punteggi-caratteristica/#destrezza)',
        "trucchetto'": '[**trucchetto**](/rules/trucchetto)',
        "Costituzione'": '[**Costituzione**](/rules/punteggi-caratteristica/#costituzione)',
        "costituzione'": '[**Costituzione**](/rules/punteggi-caratteristica/#costituzione)',
        "druido'": '[**druido**](/classi/druido)',
        "druidi'": '[**druidi**](/classi/druido)',
        "affascinato'": '[**affascinato**](/rules/condizioni)',
        "taglia'": '[**taglia**](/rules/mostri#taglia)',
        "volare'": '[**volare**](/rules/avventura#movimento)',
        "punti ferita'": '[**punti ferita**](/rules/mostri#punti-ferita)',
        "Punti ferita'": '[**Punti ferita**](/rules/mostri#punti-ferita)',
        "Punti Ferita'": '[**Punti Ferita**](/rules/mostri#punti-ferita)'
    }

    # Apri il file .md in modalità lettura
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Sostituisci le parole con il loro valore nel dizionario
    for word, replacement in replacements.items():
        file_content = file_content.replace(word, replacement)

    # Scrivi il contenuto modificato nel file .md
    with open(file_path, 'w') as file:
        file.write(file_content)


# Verifica se è stato fornito un argomento da linea di comando
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_md_file>")
        sys.exit(1)

    md_file_path = sys.argv[1]
    replace_words_in_md_file(md_file_path)
