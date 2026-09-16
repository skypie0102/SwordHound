# Reprocessing workspace

This directory contains generated and review-support artifacts for canonical reprocessing.

## Source inventory

- `source-inventory-001-125.json` — canonical Korean/source chapter inventory with recovered-MTL witness alignment stored separately.
- `SOURCE-INVENTORY.md` — human-readable source coverage summary.
- `production-baselines-0014-0125.json` — historical production-branch evidence inventory.

## Sanitation review

Broad and strict scans are **diagnostic only**; they are not findings by themselves.

- `SANITIZATION-CANDIDATES-0014-0054.md` / JSON — broad Korean→MTL candidate queue.
- `SANITIZATION-SHORTLIST-0014-0054.md` / JSON — smaller broad-source shortlist.
- `STAGED-SANITIZATION-SCAN-0014-0054.md` — staging-aware broad diagnostic.
- `STRICT-SANITIZATION-SCAN-0014-0054.md` — staging-aware exact-sensitive-term diagnostic.

The authoritative adjudicated result is outside this generated workspace:

- `editorial/reviews/sanitization-audit-0014-0054.md`
- `editorial/reviews/sanitization-corrections-0014-0054.json`

For canonical Chapters 14–54, the sanitation-focused review confirms source-intensity loss in Chapters **22, 24, 28, 34, 35, 39, 43, 45, 46, 48, 49, 52, 53, and 54**. These corrections are mandatory reconstruction inputs. Historical staged text must not be reused verbatim where the correction manifest identifies sanitation.
