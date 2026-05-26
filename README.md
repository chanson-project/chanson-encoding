# Chanson Repository

This repository contains Francophone folk songs encoded as **Humdrum `**kern`** files.  
Initial encoding is *diplomatic* and includes the musical score, poetic text, phonemes, and rhyme analysis. Editorial policies are being developed through the initial stage of encoding BC100 and EG104 datasets.

Both collections are also integrated into Verovio Humdrum View as "Monophonic Songs" under the "Scores" menu, as well as on the website https://folklore-vivant.humdrum.org, from which they can be viewed locally, downloaded from github, and exported to VHV.

Metadata for all encoded materials can be accessed at: https://docs.google.com/spreadsheets/d/16E5ZaTv--7Ketd5Lpgcbk11aKRj9T2hDjjRUiRHiAOY/edit?usp=sharing


## Encoding Procedure
<details>
<summary><h3>General Encoding</h3></summary>

1. **Reference Records**:  
   Work information, authorship information, and imprint information (including copyrights, if any) are encoded preceding each song.
   
   Example from “O Canada!” (note the space after each colon); for page numbers, add "t" for songs that end on a second page and are followed by another song on the same page; add "b" for songs that are preceded by the end of a song on the same page.

   ```
   !!!id: BC001
   !!!page: 4-5
   !!!COM: Lavallée, Calixa
   !!!LYR: Routhier, juge A.-B.
   !!!OTL@@FR: O Canada, terre de nos aïeux
   !!!PTL@@FR: Les 100 plus belles chansons
   !!!PUB: La Bonne Chanson, inc.
   !!!YEM: On ne peut reproduire, enregistrer ou diffuser en tout ou en partie le présent ouvrage, sous quelque procédé que ce soit, électronique, mécanique, photographique, sonore, magnétique ou autre, sans avoir obtenu au préalable l'autorisation écrite de l'éditrice.
   !!!PDT: 2011
   !!!SMA: 2012 Bibliothèque nationale du Québec; Biblothèque nationale du Canada
   ```
Representation information, electronic editing information are encoded below the **kern and **text encoding. Analysis information is collected on the master spreadsheet, from which they will be exported to kern files upon completion.

For a list of the different types of record comments, consult: https://www.humdrum.org/reference-records

To view the current master spreadsheet, see: https://docs.google.com/spreadsheets/d/16E5ZaTv--7Ketd5Lpgcbk11aKRj9T2hDjjRUiRHiAOY/edit?usp=sharing


2. **Spine structure**:
   - We use three types of spines:
     
   `**kern` = melody and rhythm, including slurs, ties, and accents; tempo and structure markings can be encoded above the note where they appear using `!!LO:TX:a:t=text` (for italics, add `i:`; for boldface, add `B:`).
   
   `**dynam` = dynamic markings, such as crescendi (`<`...`]`) and decrescendi (`>`...`]`).
   
   `**text` = lyrics
   
   - To add an empty spine** after the first is completed:
   
   ```
   extract -s 1-$,0
   ```
   This will add a `**blank` spine. To encode dynamics, change to `**dynam`; to encode text, change to `**text`

   - Text can be viewed above or below the graphic representation in the right pane as you are encoding. Use the filter `text` for the default view below the score; adding the filter option `-a` will show it above.

    NOTE: Make sure to double-check whether there are dynamics that require a `**dynam` spine before adding text. Adding a **dynam spine after text has been entered requires manual editing that is very time consuming!
   
3. **Preserving visual layout** of original:
   - Insert `!!LO:PB:g=original` above the measure that appears on the next system.
   - Use the alignment button to preserve layout.
   - For longer songs (>4 systems), you may wish to switch to “continuous” view on the toolbar.

4. **Add editorial comments** (e.g., pitch variants):
   - Place above the relevant line with a `!`:
     ```
     !pitch variant:b
     ```
   Ensure each spine on the same row includes an exclamation mark.

5. **Encoding completion info**:
   - Use the format "First Last" for name.
   - Use the format "year/mm/dd" for date of completion.
   ```
   !!!EED: Ève Poudrier
   !!!EEV: 2025/05/06
   ```
   Multiple editors are shows as `!!!EED1`, `!!!EED2`, etc.
   
   NOTE: This information should also be updated on the master metadata spreadsheet.
   
6. **Encoding editorial comments**:
   ```
   !!!RNB (Representation note) can be used to encode any modifications to the representation of the score. For example, replacing dal segno symbols by repeats.

   !!!RNB-original` for editor's comments on the original score.

   !!!RWG (Representation warning) can be use to point out an unusual representation in the poriginal score. For example the use of two double barlines at the end of eg003_cest-la-belle-francoise_p8-9.
   ```
NOTE: Tese should alsop be entered in the corresponding columns in the master netadata spreadsheet on Google Drive until metadata collection is completed. Additional notes should be recorded in the master spreadsheet in column AQ: `Notes`.

</details>

<details>
<summary><h3>Text Encoding</h3></summary>

1. **Syllabification**:
   - Prefix all middle and end syllables with a hyphen (`-`).
   - Words separated by a hyphen (e.g., "voulez-vous") require a double dash at the end of the first word, and no dash preceding the second word (e.g., `vou-` `lez--` `vous`). (In some rare cases, the double-dash may need to be added before the second word instead of after the first word.)
  
     NOTE: Syllabification can be reviewed withb the filter option `-y` on VHV.

2. **Line numbering** (across all verses):
   - Use `*pline:n` (e.g., `*pline:1`)
   - Stand-alone refrain lines are labeled `*rline:R1`, `*rline:R2`, etc.
   - Integrated refrains are labeled using `*pline:` format
  
     NOTE: Refrains can be reviewed using the filter option `-refrains` on VHV. If the refrain does not appear, the line encoding may need to be edited (i.e., changing *pline: for *rline:).

3. **Refrain formatting** (italics):
   - All refrain types (stand-alone and integrated) are encoded with the interpretations *refrain and *italic before the first refrain syllable and the interpretations *Xitalic and *Xrefrain after the last refrain syllable.
   - Refrain lines may be initial, medial, and final based on their position within the song.
   - Text of initial and final refrains that are repeated in alternation with verses are encoded only once and further identified with `*>Refrain` markings.

     NOTE: Implementation of automatic italics with *refrain to be added.

4. **Elisions**:
   - Final "e" (/ə/) that are elided and not replaced by an apostrophe in the original should be put in square brackets. For example: If the word group "danse avec moi" is set to three notes, with "danse" set to a single note, the final "e" is elided and th word should be encoded as "dans[e]".
   - Use the same procedures for plural endings, such as "es" and "ent" that are sounded as /ə/.

5. **Repetitions**:
   - Full line repetition should be numbered as original with the suffix "r", e.g., *pline:1r
   - Partial line repetitions should be labeled with the following suffixes:
     ```
     *pline:1a    ← start (add last repeated syllable number)
     *pline:1c    ← middle (add first and last repeated syllables numbers)
     *pline:1b    ← end (add first repeated syllable number)
     ```
   - Repetitions that are not accommodated by the above rules (e.g., single word repetitions or adjacent repetitions within the same line) should be preceded by *bis and followed by *Xbis interpretations.
  
     ```
     tour-
     -ne
     ma
     rou-
     -let-
     -te,
     vi-
     -re,
     *bis
     vi-
     -re,
     vi-
     -re,
     *Xbis
     ```
6. **Text filter options**:
   There are several ways to view the song lyrics; these are very helpful for review and editing as well as to create a .txt file with the raw text:

    ```
   filter option | meaning |
   |------------| --------  |
   | -a | show text above score |
   | -y | show hyphenation |
   | --no-repeats | hide repeated lines |
   | --refrains| show only lines labeled `*rline:` |
   | --verse | show only lines labeled `*pline:` | 
   ```

   
</details>

<details>
<summary><h3>Music Encoding</h3></summary>

1. **Melodic grouping** (segmentation levels):
   - First: `{...}`
   - Second: `{{...}}`
   - Third: `{{{...}}}`
  
     NOTE: We are only using first level segmentation in tbhis round of encoding. If you see multip[le levels, delete the higher levels.
     
2. **Segmentation guidance**:
   Segmentation is based on the following criteria:
     - rest
     - longer duration
     - repetition
       
   Different levels tend to use different markers:
   - Segments = short units, often bounded by rests or in-line repetition
   - Phrases = melodic contour, textual line ends, or longer duration
   - Periods = ≥2 phrases that are related, the second of which ends with a melodic cadence (SD 2-1 and SD 5-1 seems to be the most common)

4. **Tempo marking**:
   - Insert under first measure:
     ```
     !!LO:TX:a:t=Majestueux et résolu
     ```
     NOTE: If tempo changes, the new tempo must precede the first pitch of the new sectional tempo in order to appear.
     
5. **Accidentals**:
   - To hide an accidental, add "y" to the pitch encoding.
</details>

<details>
<summary><h3>Text Analysis</h3></summary>

1. **Rhyme Marking** (after final word of each line):
    - Line endings with rhymes are marked with three interpretations, i.e., `*rp:`, `*rf:`, and `*rs`.
    ```
    *rp:ø
    *rf:jø
    *rs:a
   ```
   These are to be interpreted as follows:
   ```
   interpretation | meaning | examples |
   |------------| --------  | ---------|
   | rp | phoneme | vowel of rhyme |
   | rf | phoneme group | full rhyme |
   | rs | lowercase letter | structure label |  
   ```
 
   - Note that structure label is based on the rhyming vowel or combination of consonant(s) and vowel sound; in cases where the rhyme is simple, same vowel will typically be used with a variety of consonants (same or different); in these cases, `*rs:` is given a suffix number corresponding to each vowel/consonant combination. For example:
```
ending | rhyme vowel | full rhyme | label |
|------| -------------| ------------| -----------|
| vent | *rp:ɑ̃ | *rf:vɑ̃ | *rs:a1 |
| gens | *rp:ɑ̃ | *rf:ʒɑ̃ | *rs:a2 |
```
   - Mute "e" are added to the full rhyme and set apart from full rhyme by a comma. These are not counted in the metre.

   - Use [Dictionnaire de rimes](https://www.rimessolides.com) for guidance.

      NOTE: Kern does not differentiate /a/ sounds (e.g., “orage” vs. “naufrage”).

## Additional Notes

<details>
<summary><h3>Formatting</h3></summary>

- Ensure consistent use of tabs and columns in spines.
- Avoid use of trailing whitespace unless intentional.
- All mreference records (`!!!key: value`) should have a single space after the colon.
</details>



