# Mendel's First Law

## OVERVIEW
This program calculates the **probability** that two randomly selected organisms from a population will produce an offspring with a **dominant allele**. It is a solution to the Rosalind problem **"Mendel's First Law" (ID: IPRB)**.

---

## FEATURES
- Reads <u>k, m, n</u> from a text file (rosalind_iprb.txt)
- Calculates <u>all 6 types</u> of ordered pairs (FF×FF, FF×Ff, FF×ff, Ff×Ff, Ff×ff, ff×ff)
- Returns probability <u>rounded to 5 decimal places</u>
- Clean, well-commented code with proper functions

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input txt named rosalind_iprb.txt in the same folder as the code, otherwise you will receive a File Not Found Error!!!**</u>

---

## EXAMPLE
**Input** (rosalind_iprb.txt):
```
2 2 2
```
**Output:**
```
0.78333
```
- <u>k = 2</u> → Homozygous Dominant (FF)
- <u>m = 2</u> → Heterozygous (Ff)
- <u>n = 2</u> → Homozygous Recessive (ff)

---

## HOW IT WORKS
1. Reads <u>k (FF)</u>, <u>m (Ff)</u>, <u>n (ff)</u> from file
2. Calculates total ordered pairs: <u>(k+m+n) × (k+m+n-1)</u>
3. Multiplies each pair type by its dominant offspring probability:
   - FF×FF → **100%**
   - FF×Ff → **100%**
   - FF×ff → **100%**
   - Ff×Ff → **75%**
   - Ff×ff → **50%**
   - ff×ff → **0%**
4. Divides the <u>sum of contributions</u> by total pairs

---

## TECHNOLOGIES USED
- **Python**
- **File I/O** (txt)
