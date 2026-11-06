# Lead Magnet Pro (frontend)

The paid version of the AI Lead Magnet Generator: customers buy a subscription or a credit pack, receive an access key by email, and spend credits to create ebooks, guides and checklists as PDFs.

This repo is **public** and holds only what the browser needs and nothing secret: the page code (served by jsDelivr), the document schema and the PDF actor. The prompts, the n8n workflows and the billing logic live in a separate **private** backend repo.

The free tool is a separate project. Nothing here changes it.

## Status

Phase 1c: the page now asks for an access key, shows the credit balance, charges up front (`/start`) and writes sections with the ticket it gets back. The Turnstile check is gone. The pricing section holds **placeholder prices**, so the page must not be published until phase 2c.

## Repo structure

```
frontend/   app.js, app.css (the tool), page.template.html (page source), widget.html (generated, never edit by hand)
schema/     document.schema.json (shared document shape) and two examples
apify/      lead-magnet-pro-pdf: private actor that turns the print-ready HTML into a PDF
scripts/    build_widget.py: builds the pinned systeme.io snippet
```

## Differences from the free tool (so far)

| | Free tool | Pro (this repo) |
|---|---|---|
| App version | `0.5.2` | `0.2.0` (restarted for the fork) |
| Access | none (human check) | access key + credits; key kept in this browser (`lmp:key`) |
| Saved work | `lmg:v1` | `lmp:v1` (separate key, same site) |
| API base (`data-api`) | `.../webhook/lead-magnet` | `.../webhook/lmg-pro` (not live until phase 1b) |
| Apify actor | `lead-magnet-pdf` | `lead-magnet-pro-pdf` (new, separate) |
| Schema `$id` | free repo | this repo |

## Build the page locally

```
python3 scripts/build_widget.py --local out.html
```

Builds a test page that uses mock answers and no AI calls. Open `out.html` in a browser and enter the demo key `lmp_demo` (170 credits).

```
python3 scripts/build_widget.py --live out-live.html
```

Builds a page that talks to the real API (`data-api`). Open it from your computer and enter your own access key.

## Releasing a new version

1. Change `frontend/app.js`, `app.css` or `page.template.html` and bump `VERSION` in `app.js`. Keep `app.js` ASCII (escape other characters as `\uXXXX`).
2. Commit and push, then run `python3 scripts/build_widget.py <full commit sha>` to pin `frontend/widget.html` to that commit with integrity hashes.
3. Commit and push `widget.html`, paste it into the systeme.io Raw HTML element and republish.

## Coming next

- Phase 2a: billing workflow and `/resend-key` (the key screen links to it).
- Phase 2c: real prices and order-form links in the pricing section, then publish.
