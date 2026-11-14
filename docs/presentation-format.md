# Bolt: Presentation Animation Format

The standard for every Unifist Unum presentation. Slide 1 of the Logical Flow deck is the gold standard. Same is same: anything built twice is generated, never built by hand.

## Slides

Slide = `{ title, kind, beats[] }`. Each kind is one template:

| Kind | Used for |
|---|---|
| `text` | Stacked statements |
| `grid` | Search vs Bucket squares |
| `bars` | Time bars |
| `spine` | Galaxy Mosaic |
| `buckets` | Sparks routed into Bolt Buckets |
| `summary` | Section summaries |

A **beat** is one step on screen. Down goes to the next beat. Up restarts the current beat, or goes to the previous one if pressed within 1 second of the beat starting.

## Text roles

These are the only allowed sizes.

| Role | Style |
|---|---|
| Lead | 48 bold |
| Statement | 40 bold |
| Note | 30 grey |
| Caption | 30, top 186; explains the slide before anything moves |
| Label | 14 caps grey |
| Result | 84 colored number + 26 grey line, top 610 |
| Takeaway | 30 bold, beside the result |

## Timing

- Text fades in over 0.8s and out over 0.6s. Small elements fade over 0.4s.
- Reading time is the longer of 2.5s or 0.3s per word.
- Search lighting runs at double speed (0.175s per square). Everything after it moves earlier by the time saved.
- Arrows trace at 45 px/s (slow) or 120 px/s (fast), with the head riding the line. No SMIL.
- Endless loops never count as beats.

## Layout

- Squares sit on one fixed grid.
- A Bucket snaps to that grid: one empty column from its neighbors, lined up with the top row.
- The gap from a label to a Bucket's border equals the gap from a label to its squares.

## Levels

- **Cumulus:** Buckets hold separate squares, one per item.
- **Lightning:** Buckets are bars, 96px wide, 10px per Scat, count on top, name below.
- **Thunder:** numbers only.

## Color

- Green = creation
- Blue = completion
- Yellow = execution
- Red = construction
- Sparks are red, and turn yellow in a Bolt Bucket.
- Rods are orange triangles pointing up.

## Behavior

- **Explain before doing:** a caption comes before any motion.
- **Constant count:** when items move, the number on screen stays the same.
- **Buckets first:** every Bucket is shown before anything is routed into it.
- **Spine:** pieces stay grey until mentioned, then light white.

## Content

- Text is Gaf's word for word, with only typos fixed.
- Terms are capitalized.
- Nothing invented: no captions, numbers or labels Gaf didn't give or approve.

## Canvas care

These rules come from the editing outage on 2026-11-14.

1. **Never write the canvas layout file (`canvas.json`) from scratch.** Read the editor's own copy and change only the keys needed.
2. **Publish in batches,** not once per tweak, and never over a canvas Gaf is editing without reading it first.
3. **Sync before build.** Gaf's edits in the canvas are the source of truth for text.
4. **If editing breaks, run the template check first** (Claude does this, not Gaf). Make a template canvas and confirm it edits. If the template edits and the deck doesn't, rebuild the deck into a fresh canvas.

## Rod: when something breaks

1. **Exception:** state what's wrong.
2. **Expectation:** find a known-good case.
3. **Compare** one factor at a time.
4. **Act:** apply the fix.

No guessing at fixes without an Expectation to test against.
