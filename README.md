# GUITARVERSE — Interactive Guitar Theory & Ear Training CLI Tool

GUITARVERSE is a Python-based command-line application designed to help guitar players learn chords, understand music theory, practice ear-training, and explore chord progressions based on mood.  
It includes chord identification, chord lookup, mood-based progression generation, chord difficulty and popularity metrics, chord quizzes, and a fretboard note trainer.

---

## Features

### 1. Chord Information Lookup
Enter a chord (for example: `am`, `g7`, `c#m`) and the program displays:
- The full chord name
- The notes that build the chord

### 2. Reverse Chord Finder
Enter notes separated by spaces, and the program checks for any matching chord.

### 3. Mood-Based Chord Progressions
Choose a mood such as:
- bright
- sad
- suspenseful
- dreamy
- romantic
- raw & aggressive
- dramatic

The program displays multiple chord progressions that match your selected mood.

### 4. Chord Popularity
Shows how commonly a chord is used in guitar songs, based on estimated percentages.

### 5. Chord Difficulty Ratings
Displays:
- Difficulty level (1–10)
- A brief text explanation of why the chord is rated that way

### 6. Guess the Chord (Quiz Game)
A chord-guessing game that:
- Shows shuffled notes from a random chord
- Lets you choose from options A, B, or C
- Tracks your score until you make a mistake or exit

### 7. Guess the Note (Fretboard Trainer)
A fretboard-note quiz:
- The program gives a random string number and fret number
- You guess the resulting note
- Score increases until a wrong answer or exit

---

## Installation

1. Clone the repository:
git clone https://github.com/denisgeorgievv/Guitarverse.git


2. Enter the project directory:
python osn.py

---

## Project Structure

GuitarVerse/
│
├── osn.py # Main file — menu UI and game logic
│
└── komponenti/
└── akordi_info.py # Databases for chords, progressions, popularity, difficulty

---

## How It Works

- `akordi_info.py` contains chord definitions, difficulty ratings, popularity data, and mood-based progressions
- `osn.py` handles user input, menu navigation, and the quiz systems
- Uses Python’s built-in `random` module for generating quiz questions

---

## Example Usage

Start the program:
python osn.py

Main menu:
1. get info about a chord
2. you give us the notes, we give you the chord
3. search chord progressions by the mood you're going for
4. how popular is your chord?
5. how difficult is your chord?
6. guess the chord!
7. guess the note!
8. exit

---

## Requirements

- Python 3.7 or newer
- No external libraries required

---

## Future Improvements

- Sound playback for chords and notes
- Extended chord types (sus, dim, aug, add9, etc.)
- Scale and mode calculators
- Fretboard diagrams
- User statistics and score tracking
- Export chord progressions or quiz results

---

## License

Free to use, modify, and extend.

---

## Author

Created to help guitar players learn theory and strengthen ear-training through interactive practice.
