def akordi_info(akord):
    akord = akord.strip().lower()

    if akord in akordi:
        ime, noti = akordi[akord]
        return ime, noti
    else:
        return None, None
    
akordi = {
    "c": ("C Major", ["C", "E", "G"]), "cm": ("C Minor", ["C", "D#", "G"]), "c7": ("C7", ["C", "E", "G", "A#"]),
    "c#": ("C# Major", ["C#", "F", "G#"]), "c#m": ("C# Minor", ["C#", "E", "G#"]), "c#7": ("C#7", ["C#", "F", "G#", "B"]),
    "d": ("D Major", ["D", "F#", "A"]), "dm": ("D Minor", ["D", "F", "A"]), "d7": ("D7", ["D", "F#", "A", "C"]),
    "d#": ("D# Major", ["D#", "G", "A#"]), "d#m": ("D# Minor", ["D#", "F#", "A#"]), "d#7": ("D#7", ["D#", "G", "A#", "C#"]),
    "e": ("E Major", ["E", "G#", "B"]), "em": ("E Minor", ["E", "G", "B"]), "e7": ("E7", ["E", "G#", "B", "D"]),
    "f": ("F Major", ["F", "A", "C"]), "fm": ("F Minor", ["F", "G#", "C"]), "f7": ("F7", ["F", "A", "C", "D#"]),
    "f#": ("F# Major", ["F#", "A#", "C#"]), "f#m": ("F# Minor", ["F#", "A", "C#"]), "f#7": ("F#7", ["F#", "A#", "C#", "E"]),
    "g": ("G Major", ["G", "B", "D"]), "gm": ("G Minor", ["G", "A#", "D"]), "g7": ("G7", ["G", "B", "D", "F"]),
    "g#": ("G# Major", ["G#", "C", "D#"]), "g#m": ("G# Minor", ["G#", "B", "D#"]), "g#7": ("G#7", ["G#", "C", "D#", "F#"]),
    "a": ("A Major", ["A", "C#", "E"]), "am": ("A Minor", ["A", "C", "E"]), "a7": ("A7", ["A", "C#", "E", "G"]),
    "a#": ("A# Major", ["A#", "D", "F"]), "a#m": ("A# Minor", ["A#", "C#", "F"]), "a#7": ("A#7", ["A#", "D", "F", "G#"]),
    "b": ("B Major", ["B", "D#", "F#"]), "bm": ("B Minor", ["B", "D", "F#"]), "b7": ("B7", ["B", "D#", "F#", "A"])
}

popularnost = {
    "c": "64.3%", "cm": "36.7%", "c7": "11.2%",
    "c#": "5.4%", "c#m": "3.1%", "c#7": "1.0%",
    "d": "52.8%", "dm": "31.5%", "d7": "8.9%",
    "d#": "4.3%", "d#m": "2.2%", "d#7": "0.9%",
    "e": "57.6%", "em": "34.1%", "e7": "9.5%",
    "f": "46.7%", "fm": "28.4%", "f7": "7.3%",
    "f#": "21.2%", "f#m": "15.6%", "f#7": "5.0%",
    "g": "65.4%", "gm": "40.3%", "g7": "12.1%",
    "g#": "8.1%", "g#m": "4.2%", "g#7": "2.0%",
    "a": "58.3%", "am": "38.2%", "a7": "11.4%",
    "a#": "6.2%", "a#m": "3.3%", "a#7": "1.1%",
    "b": "25.7%", "bm": "20.5%", "b7": "5.3%"
}

trudnost = {
    "c":   "2/10",  "cm":  "3/10",  "c7":  "3/10",
    "c#":  "8/10",  "c#m": "8/10",  "c#7": "7/10",
    "d":   "3/10",  "dm":  "4/10",  "d7":  "4/10",
    "d#":  "8/10",  "d#m": "8/10",  "d#7": "7/10",
    "e":   "2/10",  "em":  "2/10",  "e7":  "3/10",
    "f":   "8/10",  "fm":  "8/10",  "f7":  "7/10",
    "f#":  "8/10",  "f#m": "8/10",  "f#7": "7/10",
    "g":   "3/10",  "gm":  "5/10",  "g7":  "4/10",
    "g#":  "8/10",  "g#m": "8/10",  "g#7": "7/10",
    "a":   "2/10",  "am":  "3/10",  "a7":  "3/10",
    "a#":  "7/10",  "a#m": "8/10",  "a#7": "6/10",
    "b":   "7/10",  "bm":  "7/10",  "b7":  "5/10"
}

trudnost_prichini = {
    "c":   "open major chord — no barre, minimal finger stretch; beginner-friendly.",
    "cm":  "open-ish minor requires finger pressure and awkward finger placement for some players.",
    "c7":  "open dominant 7th voicing — small extra fingering but still accessible.",
    "c#":  "sharp-key major usually needs a barre or movable shape — requires finger strength and precise muting.",
    "c#m": "barre minor shape in a sharp key — demands hand strength and clean ringing.",
    "c#7": "dominant 7th in a sharp key; often played as a barre variant — tricky for beginners.",
    "d":   "open major — simple; low barrier for beginners.",
    "dm":  "open minor with more finger stretch on high strings — intermediate-easy.",
    "d7":  "open dominant 7th — requires finger placement but no full barre.",
    "d#":  "requires barre or odd finger placement — less common, higher technical demand.",
    "d#m": "barre minor — high finger strength and clean fretting needed.",
    "d#7": "sharp-key 7th that usually uses partial barre — tricky to keep strings ringing.",
    "e":   "open major — extremely beginner-friendly with open strings.",
    "em":  "one of the easiest chords (two fingers) — ideal for beginners.",
    "e7":  "open dominant 7th — simple alteration from E major.",
    "f":   "full barre at 1st fret or tricky partial shapes — many beginners struggle with clean tone.",
    "fm":  "full barre minor — needs finger strength and good fretting technique.",
    "f7":  "barre + 7th finger stretch — coordination and pressure required.",
    "f#":  "barre/movable shape high on neck — requires pressure and muting control.",
    "f#m": "barre minor at higher fret — stamina and accuracy needed.",
    "f#7": "movable 7th shape; easier than full barre but still demanding.",
    "g":   "open major — common beginner chord, comfortable shape.",
    "gm":  "minor G often needs barre or awkward fingering — moderate difficulty.",
    "g7":  "open dominant 7th — easy to moderate; slight stretching.",
    "g#":  "sharp major with barre or odd shapes — technically demanding.",
    "g#m": "barre minor in high position — needs accuracy and strength.",
    "g#7": "sharp-key 7th — complex fingering and muting control.",
    "a":   "open major — very beginner friendly, easy finger positions.",
    "am":  "open minor — easy but requires slightly different finger pressure.",
    "a7":  "open dominant 7th — simple and useful for progressions.",
    "a#":  "often a barre at 1–2 frets; less friendly for new players.",
    "a#m": "barre minor — higher difficulty due to pressure and hand positioning.",
    "a#7": "dominant 7th variant can be played as partial barre — moderate difficulty.",
    "b":   "full barre chord on 2nd fret for major — challenging for beginners.",
    "bm":  "barre minor at 2nd fret — needs clean fretting and pressure.",
    "b7":  "partial 7th voicing of B — easier than full barre but needs accuracy."
}

progresii = {
    "bright": [
        ["C", "F", "G", "C"],
        ["G", "C", "D", "G"],
        ["A", "D", "E", "A"],
        ["D", "G", "A", "D"],
        ["F", "C", "G", "F"],
        ["C", "G", "Am", "F"],
        ["G", "D", "Em", "C"]
    ],
    "sad": [
        ["Am", "Em", "Dm", "Am"],
        ["Dm", "Gm", "Am", "Dm"],
        ["Em", "Bm", "C", "Em"],
        ["Cm", "Gm", "Fm", "Cm"],
        ["Fm", "Cm", "D#", "Fm"],
        ["Am", "Dm", "E7", "Am"],
        ["Em", "Am", "Bm", "Em"]
    ],
    "suspenseful": [
        ["Cm", "G#", "F", "Cm"],
        ["D#m", "A#", "F#", "D#m"],
        ["Fm", "C#", "G#", "Fm"],
        ["Gm", "D#", "A#", "Gm"],
        ["C#m", "G#", "F#", "C#m"],
        ["Am", "F", "E7", "Am"]
    ],
    "dreamy": [
        ["F", "G", "Am", "F"],
        ["C", "Em", "F", "G"],
        ["Dm", "G", "C", "Am"],
        ["Am", "F", "C", "G"],
        ["C", "F", "Dm", "G"],
        ["Em", "Am", "F", "G"],
        ["F", "Dm", "G", "C"]
    ],
    "romantic": [
        ["C", "Am", "F", "G"],
        ["G", "Em", "C", "D"],
        ["F", "Dm", "Gm", "C"],
        ["Am", "F", "C", "G"],
        ["Dm", "G", "C", "Am"],
        ["C", "G", "Am", "Em"],
        ["F", "C", "Dm", "G"]
    ],
    "raw & aggressive": [
        ["E", "G", "A", "B"],
        ["F#", "B", "C#", "F#"],
        ["G#", "D#", "A#", "G#"],
        ["C", "G", "F", "C"],
        ["D", "A", "G", "D"],
        ["A", "E", "D", "A"],
        ["B", "F#", "E", "B"]
    ],
    "dramatic": [
        ["Cm", "G", "A#", "Fm"],
        ["D#m", "A#", "C#", "G#"],
        ["Fm", "C", "D#", "G#"],
        ["Am", "F", "G", "Em"],
        ["Em", "C", "D", "Bm"],
        ["Gm", "D#", "A#", "F"],
        ["C#m", "A", "B", "E"]
    ]
}