# HeatCrafter Product Catalog

This repository is the **single source of truth for HeatCrafter product information**
(fireplace showroom, Buffalo Grove IL). It feeds the HeatCrafter website: the site team
(Ember and Codex) pulls this catalog and applies prices, availability, specs, and product
details to the site pages. **Editing here is how product changes reach the website.**

Maintained by **Charlie Dreiske** — product catalog manager.
Owner: Art Kalina (`artiomk`), final decision-maker.

## What lives here

| Path | What it is |
|---|---|
| `products/*.json` | One file per product — name, brand, price, availability, specs, finishes, options, images |
| `images/products/` | Product photos (referenced by filename from the JSON) |
| `schema/product.schema.json` | The required shape of every product file |
| `tools/validate.py` | Checker — run `python3 tools/validate.py` before pushing |

Every push is validated automatically (GitHub Actions). A red ❌ on your commit means a
product file is malformed — open the Actions tab to see exactly what and where.

## How to make a change (Charlie's workflow)

1. Edit the product's file in `products/` (or add a new file for a new product — copy an
   existing one as a template; the filename must match the `id` field).
2. Commit with a clear message, e.g. `Chaska 29: price $11,400` or `Add Mendota D30`.
3. The validation check runs automatically. Green ✓ = the site team picks it up from here.

Field notes:
- **`price.amount_usd`** is the number the site uses; keep `display` consistent with it
  (`"From $4,000"` + `"starting_at": true` for starting prices).
- **`display_status`** is one of: `burning_now`, `on_live_display`, `available_to_order`,
  `special_order`, `discontinued`. This drives the showroom badges on the site.
- **`active: false`** hides a product from the site without deleting its data.
- **`last_verified`**: set to today's date (YYYY-MM-DD) when you've confirmed price and
  availability with the supplier — helps everyone trust the data.
- **`notes_for_site_team`**: anything the site team should know or change that isn't a
  structured field (e.g. "new hero photo in images/products/, please swap").

## Scope

This repo is product information only. Website design, navigation, templates, page
layouts, and deployment live in the site repository and are handled by Ember and Codex.
Product changes committed here do NOT appear on the website instantly — the site team
applies the catalog on each site publish.
