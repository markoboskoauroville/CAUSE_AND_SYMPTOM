# Uzrok i simptom · Cause and Symptom

### A study of one pattern, repeating: in the body, in the field, in the river, at the border, and in war

**Read it:** https://markoboskoauroville.github.io/CAUSE_AND_SYMPTOM/

Bilingual, Croatian and English, with an instant toggle — both versions are
decrypted together and held in memory, so switching languages is immediate.

## The thesis

> It is better to treat the cause than the symptom. But when the symptom is
> overwhelming, the cause cannot be reached — the symptom must first be made
> survivable. Only then does cause-work become possible.

Sixteen chapters in four parts, each ending in a bottom line: the principle and the
triage rule; medicine, and the mechanisms by which cause-work actually operates; the
same structure in agriculture, river engineering, migration and war; and the pattern
itself. See `ROADMAP.md` for page count and expansion slots.

## Files

| | |
|---|---|
| `EN.md` | English manuscript |
| `HR.md` | Croatian manuscript |
| `ILLUSTRATIONS.md` | Nano Banana prompt book — character sheets and chapter frames |
| `docs/index.html` | the built site: both languages, encrypted, behind a passphrase |
| `docs/img/` | illustrations, dropped in as they are generated |
| `ROADMAP.md` | page count, expansion slots, rules for each round |
| `build_site.py` | rebuilds the site from the two manuscripts |
| `page_template.html` | the reading page shell |

## Illustration method

Two registers in one continuous frame, as in *The Brain Brake*: a graphite pencil
register carrying the **cause** — the principle, the mechanism, the invisible part
— and a photoreal register carrying the **symptom**, the visible surface everyone
argues about. Character sheets are generated first and fed back as reference so the
visual language stays continuous across chapters. `ILLUSTRATIONS.md` holds every
prompt and a slot for each finished image.

## Rebuilding

```
BOOK_PASS='passphrase' python3 build_site.py
```

Requires `markdown` and `cryptography`. Strips the `<cite>` bookkeeping tags,
renders both manuscripts, encrypts them together with AES-256-GCM under a key
derived by PBKDF2-SHA256 at 300,000 iterations, and writes `docs/index.html`.
Neither the manuscripts nor the passphrase appear in the built page.

## A note on the gate

The passphrase is short, which is a deliberate trade-off for a working draft: it
keeps the text out of search engines and out of casual reach while it is revised.
Anyone who downloads the page can attack a short passphrase offline. Use a longer
phrase before this is treated as published.

## Honest limits

The evidence is mixed in places and the book says so rather than smoothing it over:
lifestyle intervention beat pharmacology on diabetes incidence but did not move
cardiovascular events over twenty-one years; crop diversification reduces pest
pressure but field size does not consistently predict pest damage; the resource
curse is real as a pattern and contested as a law; Schauberger's ecological
intuition about flowing water was sound while his energy claims were never
validated; and causes in war are disputed rather than measured, which is why the
book states plainly that root-cause language is itself a standard justification for
aggression.
