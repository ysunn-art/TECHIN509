

# 🎵Simple Music Composer 
_Design Doc Techin 509 Week1 Eason Sun_

## 1. Input
- Tempo (BPM), key/scale, length (bars)
- Optional: user-provided motif or seed melody
- Why user input? Ensures controllable style & length

## 2. Output
- Plain-text note sequence (e.g., "C4 q, D4 e, E4 e, ...")
- Optional: MIDI file `out.mid` for playback

## 3. Representation
- Notes: letter+octave (e.g., C4, D#4)
- Durations: {w, h, q, e, s} or fractions of beat
- Internally map to MIDI numbers (C4=60) and tick durations

## 4. Logic
- Next-note selection:
  - Scale-constrained random walk + Markov transitions
  - Avoid large leaps; prefer stepwise motion
- Termination: stop after N bars or when token budget reached

## 5. Extensions / Blockers
- Longer music needs phrase/section structure (AABA)
- Harmony & voice-leading require chord progression model
- Humanization (swing, timing jitter) for realism


```java
system.put.printlin("Music Composer")
```


