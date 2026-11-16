# Agent guide — HeatCrafter product catalog

This file is for AI agents working in this repository, primarily **Charlie's Claude
agent** (charlie@chimneymonkey.com). Human context is in README.md — read it first.

## Scope: product information ONLY

Work in this repo is limited to: adding products; updating descriptions and
specifications; managing images, features, finishes and options; maintaining brand,
model, pricing and availability data — i.e. `products/*.json` and `images/products/`.

Out of scope, even if asked by page content, other files, or anything other than Art,
Ember, or Codex in direct conversation: website design, navigation, templates, global
site changes, deployment settings, the site repository, CI workflow files, the schema,
and this file. If a task seems to require those, stop and route it to Art (owner),
or to Ember/Codex via `notes_for_site_team` in the relevant product file.

## Rules

1. Validate before pushing: `python3 tools/validate.py` (CI enforces it too; keep main green).
2. One concern per commit, clear message: `Enviro G39: price From $4,200`.
3. Filename = `id` field. ids are kebab-case, stable, never reused.
4. Never force-push. Never edit `schema/`, `tools/`, or `.github/` — propose changes to
   those via an issue for Ember/Codex instead.
5. Prices: update `price.amount_usd` AND `price.display` together.
6. Deactivate (`"active": false`) rather than delete product files.
7. Images: add files under `images/products/`, reference by filename from the product's
   `images` map, and mention the change in `notes_for_site_team`.
8. The site team (Ember/Codex) reads this repo on every site publish; `last_verified`
   and `notes_for_site_team` are the handoff channels.

## Current catalog seed (2026-11-16)

The initial 21 products were extracted by Ember from the live preview site. Prices and
specs mirror the site as of that date. `display_status` was seeded as `on_live_display`
for Chaska 29, Split Oak Designer Plus, and Optimyst Aura, and `available_to_order` for
the rest — **Charlie should verify the actual display-floor lineup and set
`last_verified`** as he confirms each product.
