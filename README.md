# Chanson Repository

This repository contains Francophone folk songs encoded as **Humdrum `**kern`** files.  
Encoding is *diplomatic* and includes the musical score, poetic text, phonemes, and rhyme analysis.


## Encoding Procedure

<summary><h3>General Encoding</h3></summary>

1. **Record comments** (preceding each song):  
   Example from “O Canada!” (note the space after each colon); for page numbers, add "t" for songs that end on a second page and are followed by another song on the same page; add "b" for songs that are preceded by the end of a song on the same page.

   ```
   !!!id: BC001
   !!!page: 4-5
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
 
For a list of the different types of record comments, consult: https://www.humdrum.org/reference-records

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
   - Use the format "First Last" for name.
   - Use the format "year/mm/dd" for date of completion.
   ```
   !!!EED: Ève Poudrier
   !!!EEV: 2025/05/06
   ```
8. **Encoding editorial comments**:
   ```
   !!!RNB (Representation note) can be used to encode any modifications to the representation of the score. For example, replacing dal segno symbols by repeats.
   !!!RWG (Representation warning) can be use to point out an unusual representation in the poriginal score. For example the use of two double barlines at the end of eg003_cest-la-belle-francoise_p8-9.
   ```

<summary><h3>Text Encoding</h3></summary>

1. **Syllabification**:
   - Prefix all middle and end syllables with a hyphen (`-`).

2. **Line numbering** (across all verses):
   - Use `*pline:n` (e.g., `*pline:1`)
   - Refrains use `*pline:R1`, `*pline:R2`, etc.

3. **Refrain formatting** (italics):
   - All refrains are encoded with the interpretations *refrain and *italic before the first refrain syllable and and the interpretations *Xitalic and *Xrefrain after the last refrain syllable.
   - Refrain lines may be initial, inserted, and final based on their position within the song.
   - Text of initial and final refrains that are repeated in alternation with verses are encoded only once and further identified with *>Refrain markings.
   - NOTE: Implementation of automatic italics with *refrain to be added.

7. **Joint syllables**:
   - Notes that are set with two or more joined syllables (e.g., "il y  a" formulated as "ya") should be set with a space to add a slur joining the two syllables. 

8. **Elisions**:
   - Final "e" (/ə/) that are elided and not replaced by an apostrophe in the original should be put in square brackets. For example: If the word group "danse avec moi" is set to three notes, with "danse" set to a single note, the final "e" is elided and th word should be encoded as "dans[e]".
   - Use the same procedures for plural endings, such as "es" and "ent", which are pronounced as /ə/.

9. **Repetitions**:
   - Full line repetition should be numbered as original with the suffix "r", e.g., *pline:1r
   - Partial line repetitions should be labeled with the following suffixes:
     ```
     *pline:1a    ← start (add last repeated syllable number)
     *pline:1c    ← middle (add first and last repeated syllables numbers)
     *pline:1b    ← end (add first repeated syllable number)
     ```
   - Repetitions that are not accommodated by the above rules (e.g., single word repeitions) should be preceded by *bis and followed by *Xbis interpretations.
  
10. **Text analysis
    - Line endings are marked with three interpretations, i.e., *r:, *rf, and *rs.
    ```
    *rp:ø
    *rf:jø
    *rs:a
   ```
   - These are to be interpreted as follows:
   ```
   interpretation | meaning | examples |
   |------------| --------  | ---------|
   | rp | phoneme | vowel of rhyme |
   | rf | phoneme group | full rhyme |
   | rs | lowercase letter | structure label |  
   ```
   - Note that structure label is based on the rhyming vowel; in cases where the same vowel is used with a different consonants, the rhythm is given a suffix number corresponding to each vowel/consonant combination. For example:
```
ending | rhyme vowel | full rhyme | label |
|------| -------------| ------------| -----------|
| vent | *rp:ɑ̃ | *rf:vɑ̃ | *rs:a1 |
| gens | *rp:ɑ̃ | *rf:ʒɑ̃ | *rs:a2 |
| ange | *rp:ɑ̃ | *rf:ɑ̃ʒ,ə | *rs:a3 |
```
- Mute "e" are added to the full rhyme and set apart from full rhyme by a comma.

<summary><h3>Music Encoding</h3></summary>

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
4. To hide an accidental, add "y".

</details>

<summary><h3>Text Analysis</h3></summary>

1. **Rhyme Marking** (after final word of each line):
   - Phoneme (assonance): `*rp:ø`
   - Full rhyme group: `*rf:yø`
   - Structure label: `*rs:a`, `*rs:b`, ...

   > Note: Kern does not differentiate /a/ sounds (e.g., “orage” vs. “naufrage”).  
   > Add editorial comment for clarity.

   - Use [Dictionnaire de rimes](https://www.rimessolides.com) for guidance.

2. **Repeated words**:
   - Surround with `*bis` ... `*Xbis`


## Additional Notes


<summary><h3>Formatting</h3></summary>

- Ensure consistent use of tabs and columns in spines.
- Avoid use of trailing whitespace unless intentional.
- All metadata records (`!!!key: value`) should have a single space after the colon.



