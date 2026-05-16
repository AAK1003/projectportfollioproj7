from music21 import stream, chord, note, meter, key, tempo

s = stream.Score()
p = stream.Part()

# set key and tempo
p.append(key.KeySignature(1))  # G major (1 sharp)
p.append(tempo.MetronomeMark(number=85))
p.append(meter.TimeSignature('4/4'))

# add chords to match progression
chords_prog = [
    (["G3","B3","D4"], 4),   # G chord, whole note
    (["C4","E4","G4"], 4),
    (["D4","F#4","A4"], 4),
    (["G3","B3","D4"], 4),
]

for pitches, dur in chords_prog:
    c = chord.Chord(pitches)
    c.quarterLength = dur
    p.append(c)

s.append(p)
s.show("musicxml")  # opens in MuseScore or another notation program
