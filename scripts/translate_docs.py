"""
Traduit automatiquement les README.md et INSIGHT.md du repo en version bilingue FR/EN.

Usage :
    python scripts/translate_docs.py                     # traduit tous les README/INSIGHT du repo
    python scripts/translate_docs.py task01_student_score_prediction/README.md   # un seul fichier

Ne touche jamais au contenu français existant : ajoute une section "## English"
à la suite, avec un lien de bascule en haut du fichier. Idempotent : si le fichier
a déjà une section anglaise, il est ignoré (sauf --force).

Dépendance : pip install deep-translator
"""
import argparse
import re
import sys
from pathlib import Path

from deep_translator import GoogleTranslator

REPO_ROOT = Path(__file__).resolve().parent.parent
TOGGLE_LINE = "[🇫🇷 Français](#français) | [🇬🇧 English](#english)"
FR_HEADER = "## Français"
EN_HEADER = "## English"


def find_target_files(explicit_paths):
    """Retourne la liste des README.md / INSIGHT.md à traiter."""
    if explicit_paths:
        return [Path(p) for p in explicit_paths]
    return sorted(
        list(REPO_ROOT.glob("*/README.md"))
        + list(REPO_ROOT.glob("*/INSIGHT.md"))
        + [REPO_ROOT / "README.md"]  # le README racine aussi
    )


def already_translated(content: str) -> bool:
    return EN_HEADER in content


def split_code_blocks(text: str):
    """
    Découpe le texte en segments (type, contenu) où type est 'code' ou 'text'.
    Les blocs ```...``` ne sont jamais envoyés à la traduction (code, chemins, commandes).
    """
    parts = re.split(r"(```.*?```)", text, flags=re.DOTALL)
    segments = []
    for part in parts:
        if part.startswith("```"):
            segments.append(("code", part))
        elif part.strip():
            segments.append(("text", part))
        elif part:
            segments.append(("text", part))  # espaces/newlines à préserver
    return segments


def translate_text_segment(segment: str, translator: GoogleTranslator) -> str:
    """
    Traduit un segment texte paragraphe par paragraphe (préserve les sauts de ligne
    et la structure markdown : titres, tableaux, listes).
    """
    lines = segment.split("\n")
    translated_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            translated_lines.append(line)
            continue
        # lignes purement symboliques (séparateurs de tableau markdown "|---|---|", etc.)
        # -> rien à traduire, et Google Translate renvoie parfois None dessus
        if re.fullmatch(r"[|:\-\s]+", stripped):
            translated_lines.append(line)
            continue
        try:
            result = translator.translate(line)
            translated_lines.append(result if result else line)
        except Exception as e:
            print(f"    ⚠️  Ligne non traduite (erreur : {e}) — gardée en français", file=sys.stderr)
            translated_lines.append(line)
    return "\n".join(translated_lines)


def translate_content(content: str) -> str:
    translator = GoogleTranslator(source="fr", target="en")
    segments = split_code_blocks(content)

    translated_parts = []
    for kind, part in segments:
        if kind == "code":
            translated_parts.append(part)  # jamais traduit
        else:
            translated_parts.append(translate_text_segment(part, translator))
    return "".join(translated_parts)


def build_bilingual_file(original_content: str, translated_content: str) -> str:
    return (
        f"{TOGGLE_LINE}\n\n"
        f"{FR_HEADER}\n\n"
        f"{original_content.strip()}\n\n"
        f"{EN_HEADER}\n\n"
        f"{translated_content.strip()}\n"
    )


def process_file(path: Path, force: bool = False):
    if not path.exists():
        print(f"  ⚠️  Introuvable, ignoré : {path}")
        return

    content = path.read_text(encoding="utf-8")

    if already_translated(content) and not force:
        print(f"  ⏭️  Déjà bilingue, ignoré : {path}")
        return

    # si --force sur un fichier déjà bilingue, on repart de la partie FR uniquement
    if already_translated(content):
        match = re.search(
            rf"{re.escape(FR_HEADER)}\n\n(.*?)\n\n{re.escape(EN_HEADER)}",
            content,
            flags=re.DOTALL,
        )
        content = match.group(1) if match else content

    print(f"  🔄 Traduction : {path}")
    translated = translate_content(content)
    bilingual = build_bilingual_file(content, translated)
    path.write_text(bilingual, encoding="utf-8")
    print(f"  ✅ Terminé : {path}")


def main():
    parser = argparse.ArgumentParser(description="Traduit les README/INSIGHT du repo en FR/EN bilingue.")
    parser.add_argument("paths", nargs="*", help="Fichier(s) spécifique(s) à traduire (sinon : tous)")
    parser.add_argument("--force", action="store_true", help="Retraduit même les fichiers déjà bilingues")
    args = parser.parse_args()

    targets = find_target_files(args.paths)
    print(f"{len(targets)} fichier(s) à traiter.\n")

    for path in targets:
        process_file(Path(path), force=args.force)

    print("\nTerminé.")


if __name__ == "__main__":
    main()
