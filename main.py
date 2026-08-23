#!/usr/bin/env python3
import time
import shutil
import os
import json
import colors
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import ANSI

zeilen = []
zeilen_for_open = []
columns = shutil.get_terminal_size().columns


def restart():
    import sys
    os.execv(sys.executable, [sys.executable] + sys.argv)


Logo = r'''
███████╗██████╗ ███╗   ███╗██████╗ 
██╔════╝██╔══██╗████╗ ████║██╔══██╗
█████╗  ██║  ██║██╔████╔██║██║  ██║
██╔══╝  ██║  ██║██║╚██╔╝██║██║  ██║
███████╗██████╔╝██║ ╚═╝ ██║██████╔╝
╚══════╝╚═════╝ ╚═╝     ╚═╝╚═════╝ 
'''

for line in Logo.splitlines():
    print(colors.LOGO_COLOR + line.center(columns) + colors.RESET)

time.sleep(0.5)


print(colors.INFO_COLOR + "[Use :help to see all commands]" + colors.RESET)

warning_status = 0  # 0 für Wahrnungen anzeigen, 1 für nicht anzeigen
if warning_status == 1:
    print(colors.WARNING_COLOR + "Warnungen sind ausgestellt." + colors.RESET)

programm_ordner = os.path.dirname(os.path.abspath(__file__))
config_datei = os.path.join(programm_ordner, "data.json")

try:
    with open(config_datei, 'r', encoding="utf-8") as f:
        pfad = json.load(f)
except FileNotFoundError:
    if warning_status == 0:
        print(colors.WARNING_COLOR +
              "Kein Pfad gefunden, normaler Pfad wird genutzt." + colors.RESET)
    pfad = programm_ordner
except json.JSONDecodeError:
    if warning_status == 0:
        print(colors.ERROR_COLOR +
              "Fehlerhafter Pfad in JSon-Datei, normaler Pfad wird genutzt." + colors.RESET)
    pfad = programm_ordner


while True:
    number_zeilen = len(zeilen) + 1
    zeile = input(colors.LINE_NUMBER_COLOR + str(number_zeilen) +
                  colors.RESET + colors.PROMPT_COLOR + "> " + colors.RESET)

    if zeile == ":help":
        print(f'''\n\n{colors.INFO_COLOR}Aktuelle Commands:{colors.RESET}
                {colors.COMMAND_COLOR}:save{colors.RESET} (Speichert das Dokument)
                {colors.COMMAND_COLOR}:exit{colors.RESET} (Bricht das Programm ab)
                {colors.COMMAND_COLOR}:new{colors.RESET} (Startet eine Neue Datei !!!Alte wird geloescht!!!)
                {colors.COMMAND_COLOR}:open{colors.RESET} (Öffnet eine Datei)
                {colors.COMMAND_COLOR}:edit{colors.RESET} (editiert eine Zeile)
                {colors.COMMAND_COLOR}:delete{colors.RESET} (löscht die ausgewälte Zeile)
                {colors.COMMAND_COLOR}:pfad{colors.RESET} (setzt den Pfad wo alle md Dateien gespeichert werden sollen)
                    {colors.INFO_COLOR}->{colors.RESET} Es muss sich um einen Ordner handeln
                {colors.COMMAND_COLOR}:show{colors.RESET} (zeigt die aktuelle Datei)
                {colors.COMMAND_COLOR}:warnings{colors.RESET} (stellt Fehlermeldungen aus oder an)''')
        continue

    if zeile == ":save":
        dateiname = input(colors.PROMPT_COLOR + "Name: " + colors.RESET)

        while dateiname.strip() == "":
            if warning_status == 0:
                print(colors.ERROR_COLOR + "Ungültiger Pfad!" + colors.RESET)
            dateiname = input(colors.PROMPT_COLOR + "Name: " + colors.RESET)

        dateiname = pfad + "/" + dateiname + ".md"

        if os.path.exists(dateiname):
            if input(colors.WARNING_COLOR + "Die Datei existiert bereits. Trotzdem sichern? (y/n): " + colors.RESET).strip().lower() == "y":
                pass
            else:
                print(colors.INFO_COLOR +
                      "Der Vorgang wurde abgebrochen." + colors.RESET)
                continue

        with open(dateiname, "w", encoding="utf-8") as datei:
            datei.write("\n".join(zeilen))

        print(colors.SUCCESS_COLOR +
              "Die Datei wurde erfolgreich gespeichert." + colors.RESET)
        continue

    if zeile == ":exit":
        if input(colors.WARNING_COLOR + "Nicht gespeicherte Änderungen gehen verloren. Trotzdem beenden? (y/n): " + colors.RESET).strip().lower() == "y":
            print(colors.INFO_COLOR + "Progamm beendet" + colors.RESET)
            exit()
        else:
            continue

    if zeile == ":new":
        if input(colors.WARNING_COLOR + "Die Jetzige Datei wird verworfen, wollen sie fortfahren? (y/n)" + colors.RESET).strip().lower() == "y":
            zeilen = []
            restart()
        else:
            print(colors.INFO_COLOR + "Abgebrochen." + colors.RESET)
            continue

    if zeile == ":open":
        file_open_pfad = input(
            colors.PROMPT_COLOR + "Bitte den Pfad zum öffnen eingeben: " + colors.RESET).strip()

        if (file_open_pfad.startswith("'") and file_open_pfad.endswith("'")) or (
                file_open_pfad.startswith('"') and file_open_pfad.endswith('"')):
            file_open_pfad = file_open_pfad[1:-1]

        if os.path.isfile(file_open_pfad):
            pass
        else:
            if warning_status == 0:
                print(
                    colors.ERROR_COLOR + "Es handelt sich nicht um eine gültige Datei oder der Pfad existiert nicht." + colors.RESET)
                continue

        if input(colors.WARNING_COLOR + "Möchtest du die Datei bearbeiten. (Wird zu deinen aktuellen Zeilen hinzugefügt, neues Dokument dafür empfohlen.) (y/n)" + colors.RESET).strip().lower() == "y":
            which_list_for_open = zeilen
        else:
            which_list_for_open = zeilen_for_open

        try:
            with open(file_open_pfad, "r", encoding="utf-8") as f:
                which_list_for_open.extend(f.read().splitlines())
                for nummer, inhalt in enumerate(which_list_for_open, start=1):
                    print(
                        f"{colors.LINE_NUMBER_COLOR}{nummer}{colors.RESET}{colors.PROMPT_COLOR}> {colors.RESET}{inhalt}")
                zeilen_for_open = []
                if which_list_for_open == zeilen:
                    print(colors.INFO_COLOR +
                        "Hier kannst du weiter Arbeiten:)" + colors.RESET)
                else:
                    print(colors.INFO_COLOR +
                        "Datei erfolgreich zum Anschauen geöffnet." + colors.RESET)
                continue
        except FileNotFoundError:
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Die Datei existiert nicht oder der Pfad ist Falsch." + colors.RESET)
        except PermissionError:
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Die Datei kann nicht geöffnet werden, da die Berechtigungen fehlen." + colors.RESET)
        except UnicodeDecodeError:
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Die Datei kann nicht geöffnet werden, da sie nicht im UTF-8 Format ist." + colors.RESET)
            continue

    if zeile == ":edit":
        try:
            which_zeile_to_edit = int(
                input(colors.PROMPT_COLOR + "Welche zeile soll geändert werden: " + colors.RESET))
        except:
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Die Eingabe ist nicht erlaubt. Muss sich um eine Nummer handeln." + colors.RESET)
            continue

        if which_zeile_to_edit < 1 or which_zeile_to_edit > len(zeilen):
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Darf nicht länger als die Zeilen sein und/oder kleiner als 1." + colors.RESET)
            continue

        which_zeile_to_edit = which_zeile_to_edit - 1
        alter_inhalt = zeilen[which_zeile_to_edit]

        new_content = prompt(
            ANSI(
                colors.PROMPT_COLOR
                + "Was soll in die Zeile: "
                + colors.RESET
            ),
            default=alter_inhalt
        )

        zeilen[which_zeile_to_edit] = new_content
        print(colors.SUCCESS_COLOR + "Zeile wurde gespeichert:)" + colors.RESET)
        continue

    if zeile == ":delete":
        try:
            which_zeile_to_delete = int(
                input(colors.PROMPT_COLOR + "Welche zeile soll gelöscht werden: " + colors.RESET))
        except:
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Die Eingabe ist nicht erlaubt. Muss sich um eine Nummer handeln." + colors.RESET)
            continue

        if which_zeile_to_delete < 1 or which_zeile_to_delete > len(zeilen):
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Darf nicht länger als die Zeilen sein und/oder kleiner als 1." + colors.RESET)
            continue

        which_zeile_to_delete = which_zeile_to_delete - 1
        if input(colors.WARNING_COLOR + "Wollen sie die Zeile wirklich löschen? (y/n): " + colors.RESET).strip().lower() == "y":
            zeilen.pop(which_zeile_to_delete)
            print(colors.SUCCESS_COLOR +
                  f"Die Zeile {which_zeile_to_delete + 1} wurde gelöscht:)" + colors.RESET)
            continue
        else:
            print("")
            continue

    if zeile == ":show":
        for nummer, inhalt in enumerate(zeilen, start=1):
            print(
                f"{colors.LINE_NUMBER_COLOR}{nummer}{colors.RESET}{colors.PROMPT_COLOR}> {colors.RESET}{inhalt}")
        continue

    if zeile == ":pfad":
        pfad = input(colors.PROMPT_COLOR + "Pfad eingeben:" + colors.RESET)

        if (pfad.startswith("'") and pfad.endswith("'")) or (
                pfad.startswith('"') and pfad.endswith('"')):
            pfad = pfad[1:-1]

        if os.path.isdir(pfad):
            with open(config_datei, 'w', encoding="utf-8") as f:
                json.dump(pfad, f)
            print(colors.SUCCESS_COLOR + "Pfad wurde übernommen" + colors.RESET)
            continue
        else:
            if warning_status == 0:
                print(colors.ERROR_COLOR +
                      "Der Pfad ist Ungültig (:help für Problemlösung)" + colors.RESET)
            continue

    if zeile == ":warnings":
        print(colors.WARNING_COLOR + "Selten empfohlen!" + colors.RESET)
        if input(colors.WARNING_COLOR + "Möchten sie Fehlermeldungen ausstellen? (y/n)" + colors.RESET).strip().lower() == "y":
            warning_status = 1
        else:
            warning_status = 0
        continue

    if zeile == ":insert":
        pass

    zeilen.append(zeile)
