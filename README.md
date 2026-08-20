# Python lernen, indem ein Spiel wächst

**Ein Tutorial in 30 Etappen. Du baust ein textbasiertes Rollenspiel — und eine KI begleitet dich dabei als Mentor, der dir nicht die Lösung verrät.**

> 🇬🇧 **English:** This is a German-language Python curriculum. You learn Python by building a text-based RPG over 29 stages, guided by an AI mentor that is explicitly instructed never to write the code for you. All materials are in German — an English version does not exist yet.

**Status:** In Arbeit. Der Lehrplan steht vollständig, die ausführlichen Guides entstehen Etappe für Etappe.

---

## Was das hier ist

Die meisten Python-Kurse lassen dich Übungsaufgaben lösen, die du nach zwei Wochen vergessen hast. Dieses Tutorial macht etwas anderes: **Jede gelernte Fähigkeit landet noch am selben Tag in einem Spiel, das dir gehört und das jeden Tag ein Stück größer wird.**

Du lernst Listen – und baust ein Inventar. Du lernst Dictionaries – und baust eine Landkarte. Du lernst Klassen – und deine Dorfbewohner bekommen ein Eigenleben. Schon früh kannst du mit deinem eigenen Spiel etwas ausprobieren und sehen, was dein neuer Code bewirkt – und über die Monate wächst daraus Schritt für Schritt eine echte Spielwelt.

Und das Besondere: **Du arbeitest nicht allein, sondern mit einer KI als Mentor.** Aber nicht so, wie du es vielleicht kennst. Die KI bekommt eine Anweisungsdatei, die ihr ausdrücklich verbietet, dir den Code zu schreiben. Sie stellt Rückfragen, gibt Hinweise, prüft dein Verständnis — und lässt dich jede Zeile selbst tippen.

---

## Für wen das gedacht ist

**Gut geeignet, wenn du…**
- Python lernen willst, aber bei abstrakten Übungsaufgaben die Motivation verlierst
- bereits mit KI-generiertem Code arbeitest und aufhören willst, ihm blind zu vertrauen
- 20–30 Minuten am Tag hast und einen langen Atem
- Freude daran hast, wenn eine Welt entsteht

**Nicht geeignet, wenn du…**
- in zwei Wochen einen Job als Entwickler brauchst
- eine reine Syntax-Referenz suchst (das hier ist die *Anwendung*, nicht die Einführung)
- schnell ein fertiges Spiel willst — dann nimm eine Engine, nicht dieses Tutorial

**Ausdrücklich auch geeignet, wenn du technisch versiert bist, aber nicht programmieren kannst.** Das Tutorial behandelt dich nicht wie einen Computer-Anfänger. Terminal, Editor und Dateisystem werden vorausgesetzt.

---

## Die Prämisse

> Du wachst an einem Morgen auf. Das Dorf ist leer. Drei Menschen sind noch da. Alle anderen sind fort — keine Kampfspuren, keine Abschiedsbriefe, nur kalte Herdstellen und ein Frühstück, das jemand nicht mehr zu Ende gegessen hat.
>
> Vor dem Dorf liegt eine Wiese. Weiter draußen der Eingang zu einer alten Mine, die niemand mehr betreten hat.

Drei verbliebene Figuren sind kein Zufall. Bei zwölf Verdächtigen ist niemand verdächtig — bei dreien ist es jeder. Und technisch bleibt ein System mit drei Figuren überschaubar genug, dass du es wirklich verstehst.

Später kehren Dorfbewohner zurück. Das ist deine Belohnungswährung — und gleichzeitig der Punkt, an dem du dein System erweiterst, weil dein Code bereit dafür ist.

---

## Wie es funktioniert

Das hier ist der Kern, und er unterscheidet dieses Tutorial von allem anderen.

**1. Du gibst einer KI die Mentor-Anweisung.**

Lade das Repo herunter und gib der KI deiner Wahl (Claude, ChatGPT, Gemini …) diese drei Dateien:

- `MENTOR.md` — die Regeln, nach denen sie dich begleitet
- `RPG_Lehrplan.md` — der Überblick über alle 30 Etappen
- `BOGEN.md` — das Register aller Querverweise

Bei Claude legst du sie als Projektdateien ab, bei anderen Anbietern als Anweisung oder angehängtes Dokument. Dann schreibst du einfach:

> „Begleite mich durch dieses Tutorial. Ich fange bei Etappe 0 an."

**2. Die KI hält sich zurück — und das ist Absicht.**

`MENTOR.md` verbietet ihr, Code für dein Spiel zu schreiben. Stattdessen arbeitet sie eine Hinweis-Leiter ab: erst Rückfragen, dann auf die Stelle zeigen, dann das Konzept an einem *fremden* Beispiel erklären. Die Lösung bekommst du nicht.

Das ist unbequem. Es ist auch der einzige Weg, auf dem etwas hängen bleibt.

**3. Du arbeitest Etappe für Etappe.**

Jede Etappe hat denselben Aufbau: ein Konzept lernen, es im Spiel anwenden, eine kleine Übung außerhalb des Spiels, absichtlich etwas kaputtmachen — und am Ende erklären, was du verstanden hast. Erst dann gilt sie als abgeschlossen.

**4. Die KI prüft dich.**

Wenn du sagst „fertig", stellt sie dir die Lernziel-Fragen der Etappe. Nicht als Prüfung — das Erklären *ist* der Lernvorgang. Wer eine Sache in eigenen Worten erklären kann, hat sie verstanden. Wer sie nur benutzen kann, erinnert sich an seinen eigenen Code.

---

## Schnellstart

```bash
git clone https://github.com/Moe-Joe86/Python-Tutorial.git
```

1. **Lies** `RPG_Lehrplan.md` — einmal ganz, damit du den Bogen kennst.
2. **Übergib** `MENTOR.md`, `RPG_Lehrplan.md` und `BOGEN.md` an deine KI.
3. **Leg dein eigenes Repo an** — das Spiel gehört dir, nicht hierher.
4. **Starte mit Etappe 0.** Ein Abend, kein Python: Repo, `README.md`, `GELERNT.md`, `.gitignore`, virtuelle Umgebung.
5. **Dann Etappe 1.** Am Ende des Abends existiert dein Spiel.

Die ausführlichen Etappen-Guides gibst du der KI einzeln dazu, wenn du sie erreichst. Das hält den Kontext schlank.

---

## Was du brauchst

| | |
|---|---|
| **Python 3.10+** | Installiert und im Terminal aufrufbar |
| **Ein Editor** | VS Code empfohlen, aber beliebig |
| **Git & GitHub** | Ein kostenloses Konto reicht |
| **Eine KI** | Claude, ChatGPT, Gemini o. ä. |
| **Zeit** | 20–30 Minuten am Tag, über Monate |

**Empfohlen zusätzlich:** eine strukturierte Syntax-Quelle. Der Lehrplan ist auf [Boot.dev](https://boot.dev) abgestimmt, funktioniert aber mit jeder Quelle, die dieselben Themen in ähnlicher Reihenfolge behandelt — auch mit kostenlosen wie freeCodeCamp. Dieses Tutorial ersetzt keine Syntax-Einführung. Es ist die Anwendung dazu.

---

## Aufbau des Repos

```
├── README.md              ← du bist hier
├── RPG_Lehrplan.md        ← alle 30 Etappen im Überblick
├── MENTOR.md              ← Anweisungen für die begleitende KI
├── BOGEN.md               ← Register aller Vorausverweise
├── PROMPT.md              ← fertige Startprompts zum Kopieren
└── de/
    ├── etappe-01-der-erste-morgen.md
    ├── etappe-02-die-erste-begegnung.md
    └── …
```

**Die drei Kerndateien:**

**`RPG_Lehrplan.md`** — die Landkarte. Alle 30 Etappen, in vier Blöcken: Fundament, Objekte und Zeit, Die Welt reagiert, Grafik. Dazu die Arbeitsregeln und der Zeitrahmen.

**`MENTOR.md`** — die Anweisung an die KI. Enthält die Hinweis-Leiter, die Regeln für Code-Reviews, das Bug-Jagd-Ritual und eine Ehrlichkeitszusage. Lies sie ruhig selbst: Zu wissen, warum dir jemand die Lösung vorenthält, macht es erträglicher.

**`BOGEN.md`** — die Buchführung. Etappe 1 legt eine Variable an, die erst in Etappe 17 gebraucht wird. Solche Versprechen gehen über vier Monate verloren — auch der KI, die dich begleitet. Diese Datei hält sie fest, damit niemand aus dem Gedächtnis raten muss.

---

## Die Grundsätze

**Kein Vibe Coding.** Du schreibst jede Zeile selbst. Wenn du feststeckst, formulierst du es so: *„Ich will X, habe Y probiert, es passiert Z — woran könnte es liegen?"* Nicht: *„Schreib mir das."*

**Erst kaputt machen, dann fragen.** Wenn etwas funktioniert, änderst du absichtlich etwas und schaust zu. „So schreibt man es" ist Auswendiglernen. „Warum muss es so sein" ist Verstehen.

**Am Ende steht eine Leseprobe.** In Etappe 27 nimmst du ein echtes, fremdes Repository und beschreibst seine Architektur — ohne Hilfe. Das ist die Probe auf das eigentliche Ziel: fremden Code lesen und beurteilen können.

**Grafik kommt zum Schluss.** Das leere Dorf, die Zeitabläufe, das Verschwinden — alles reine Logik, kein Pixel nötig. Wer mit Sprites anfängt, kämpft ein halbes Jahr mit Kollisionsabfragen und baut nie das, was ihn eigentlich interessiert hat. Pygame kommt ab Etappe 28.

**Das Spiel läuft ab Etappe 1.** Erst hässlich und textbasiert, aber spielbar. Jede Etappe macht es größer, nicht hübscher.

**Erweitern, ohne zu zerstören.** Ab Block 2 der Maßstab für alles. Programmieren heißt nicht nur, neuen Code zu schreiben — sondern bestehenden zu verstehen und vorsichtig zu verändern.

---

## Zeitrahmen — ehrlich

| Block | Etappen | Dauer |
|---|---|---|
| Werkzeug | 0 | 1 Abend |
| Fundament | 1–8 | 6–8 Wochen |
| Objekte und Zeit | 9–16 | 9–12 Wochen |
| Die Welt reagiert | 17–27 | 13–17 Wochen |
| Grafik (optional) | 28–30 | offen |

Bei 20–30 Minuten am Tag. Das ist kein Wochenendprojekt.

Der Punkt, an dem es *richtig* Spaß macht, liegt bei Etappe 12–13: Dort bekommt dein Dorf einen Takt, die Figuren gehen eigenen Tagesabläufen nach, und Pflanzen wachsen, während du woanders bist. Bis dahin durchhalten.

---

## Was am Ende dasteht

Ein spielbares Rollenspiel: ein leeres Dorf, drei Überlebende, eine Mine voller Hinweise, eine Wiese, auf der Dinge wachsen, während du weg bist, Entscheidungen mit Nachhall — und ein Verschwinden, das nicht gescriptet ist, sondern passiert.

Dazu ein öffentliches Repo mit hunderten Commits über Monate. Das ist ein besserer Nachweis für Durchhaltevermögen als jedes Kurszertifikat.

Und der eigentliche Punkt: **Du wirst fremden Python-Code lesen und beurteilen können, statt ihm zu vertrauen.**

---

## Ehrliche Einschränkungen

**Es ist noch nicht fertig.** Der Lehrplan steht, die ausführlichen Etappen-Guides entstehen nach und nach. Bis dahin trägt der Lehrplan die späteren Etappen — knapper, aber vollständig.

**Es hängt an der KI.** Die Qualität der Begleitung schwankt je nach Modell. `MENTOR.md` ist so geschrieben, dass es robust sein sollte, aber keine KI hält sich perfekt an Anweisungen. Wenn deine KI anfängt, dir Lösungen hinzuschreiben, erinnere sie an `MENTOR.md`.

**Es ersetzt keinen Kurs.** Die Syntax lernst du woanders. Hier lernst du, sie zu benutzen.

**Es ist ein Lernprojekt, kein Spieleentwicklungs-Tutorial.** Wenn du ein kommerzielles Spiel bauen willst, ist eine Engine der schnellere Weg.

---

## Mitwirken

Wenn du das Tutorial durchläufst und über eine unklare Stelle stolperst, ist ein Issue hilfreich. Besonders wertvoll: Stellen, an denen du feststeckst und der Guide dir nicht weiterhilft — das sind die Lücken, die man von innen nicht sieht.

---

## Lizenz

MIT — siehe [LICENSE](LICENSE). Nutz es, verändere es, gib es weiter.
