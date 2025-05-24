# Chanson Repository

This repository contains Francophone folk songs encoded as **Humdrum `**kern`** files.  
Encoding is *diplomatic* and includes the musical score, poetic text, phonemes, and rhyme analysis.

---

## Table of Contents

- [Encoding Procedure](#encoding-procedure)
  - [General Encoding](#general-encoding)
  - [Text Encoding](#text-encoding)
  - [Music Encoding](#music-encoding)
  - [Text Analysis](#text-analysis)
- [Additional Notes](#additional-notes)

---

## Encoding Procedure

<details>
<summary><h3>General Encoding</h3></summary>

1. **Record comments** (preceding each song):  
   Example from “O Canada!” (note the space after each colon):

   ```
   !!!COM: Lavallée, Calixa
   !!!LYR: Routhier, juge A.-B.
   !!!PTL@@FR: Les 100 plus belles chansons
   !!!OTL@@FR: O Canada, terre de nos aïeux
   !!!PUB: La Bonne Chanson, inc.
   !!!YEM: On ne peut reproduire, enregistrer ou diffuser en tout ou en partie le présent ouvrage, sous quelque procédé que ce soit, électronique, mécanique, photographique, sonore, magnétique ou autre, sans avoir obtenu au préalable l'autorisation écrite de l'éditrice.
   !!!PDT: 2011
   !!!SMA: 2012 Bibliothèque nationale du Québec; Biblothèque nationale du Canada
   !!!AGN-Laforte: Chanson strophique (sans refrain), 8:10(4+6)
   !!!AGN-type: hymne national
   !!!AGN-rime: mixte, aabcbcbc
   ```

2. **Spine structure**:
   - Melody (Spine 1): `*`
   - Verse 1 (Spine 2): `*v:1`
   - Verse 2 (Spine 3): `*v:2`

3. **To add an empty spine** after the first is completed:
   ```
   extract -s 1-$,0
   ```

4. **Preserve visual layout** of original:
   - Insert `!!LO:PB:g=original` above the measure that appears on the next system.
   - Use the alignment button to preserve layout.
   - For longer songs (>4 systems), switch to “continuous” view on the toolbar.

5. **Add editorial comments** (e.g., pitch variants):
   - Place above the relevant line with a `!`:
     ```
     !pitch variant:b
     ```
   - Ensure each spine on the same row includes an exclamation mark.

6. **Encoding completion info**:
   ```
   !!!EED: Ève Poudrier
   !!!EEV: 2025/May/06
   ```

</details>


### Text Encoding

1. **Syllabification**:
   - Prefix all middle and end syllables with a hyphen (`-`).

2. **Line numbering** (across all verses):
   - Use `*pline:n` (e.g., `*pline:1`)
   - Refrains use `*pline:R1`, `*pline:R2`, etc.

3. **Refrain formatting** (italics):
   - Begin: `*italic`
   - End: `*Xitalic`

4. **Syllable spacing**:
   - Prefix with a space.
   - Exception: Mute “e” at the end of a word before a vowel-initial word.

5. **Elisions**:
   - Same spacing rules as above.
   - Exception: mute “e” elision requires no leading space.

6. **Repetitions**:
   - Full: `*bis` and `*Xbis` around the repeated line.
   - Partial: Use suffixes:
     ```
     *pline:1a    ← start
     *pline:1c    ← middle
     *pline:1b    ← end
     ```

---

### Music Encoding

1. **Melodic grouping** (segmentation levels):
   - First: `{...}`
   - Second: `{{...}}`
   - Third: `{{{...}}}`

2. **Segmentation guidance**:
   - Segments = short units, often bounded by rests.
   - Phrases = melodic contour or textual line ends.
   - Periods = ≥2 phrases with cadences and structural relation.

3. **Tempo marking**:
   - Insert under first measure:
     ```
     !!LO:TX:a:t=Majestueux et résolu
     ```

---

### Text Analysis

1. **Rhyme Marking** (after final word of each line):
   - Phoneme (assonance): `*rp:ø`
   - Full rhyme group: `*rf:yø`
   - Structure label: `*rs:a`, `*rs:b`, ...

   > Note: Kern does not differentiate /a/ sounds (e.g., “orage” vs. “naufrage”).  
   > Add editorial comment for clarity.

   - Use [Dictionnaire de rimes](https://www.rimessolides.com) for guidance.

2. **Repeated words**:
   - Surround with `*bis` ... `*Xbis`

---

## Additional Notes

- Ensure consistent use of tabs and columns in spines.
- Avoid use of trailing whitespace unless intentional.
- All metadata records (`!!!key: value`) should have a single space after the colon.



