# Order form pages (systeme.io)

Page code for the four order forms and the thank-you page. Each file goes into a **Raw HTML** element. The order form itself (contact fields, payment, order summary, button) is made of systeme.io's own order form elements, placed between the two Raw HTML blocks.

All links are relative (`/lmp-pro`), so every page must be on the same domain as the tool page.

## Slugs

| Page | Slug | Code |
|---|---|---|
| The tool (Raw HTML widget) | `lead-magnet-pro` | `frontend/widget.html` (later, pinned) |
| Starter order form | `lmp-starter` | `lmp-starter.html` + `below-form.html` |
| Pro order form | `lmp-pro` | `lmp-pro.html` + `below-form.html` |
| Scale order form | `lmp-scale` | `lmp-scale.html` + `below-form.html` |
| 100-credit pack order form | `lmp-credits` | `lmp-credits.html` + `below-form.html` |
| Thank-you page (after payment) | `lmp-welcome` | `lmp-welcome.html` |
| Terms and conditions | `lmp-terms` | your own terms page (or change the two `/lmp-terms` links) |

## Layout of each order form page

1. **Section 1**: full width, no padding, white. Raw HTML with the plan file (`lmp-pro.html` etc.). It ends with the grey "Secure your … plan" heading.
2. **Section 2**: background `#F5F6F9`, top padding 0, content width about 720 px. The systeme.io order form elements. Suggested button color `#2F54EB`, corner radius 10 px.
3. **Section 3**: full width, no padding. Raw HTML with `below-form.html` (trust line, terms line, footer).

The thank-you page is one full-width section with `lmp-welcome.html`.

## Automation rules (one per order form)

Replace SECRET with `BILLING_SECRET`. The address must end exactly at the last word (no dot, no space).

| Order form | Trigger | Webhook address |
|---|---|---|
| `lmp-starter` | New sale | `https://n8n.team-sio.com/webhook/lmg-pro-billing/event?secret=SECRET&type=subscribe&plan=starter` |
| `lmp-pro` | New sale | `...&type=subscribe&plan=pro` |
| `lmp-scale` | New sale | `...&type=subscribe&plan=scale` |
| `lmp-credits` | New sale | `...&type=pack&plan=pack100` |
| each plan | Subscription cancelled | `...&type=cancel` |
| each plan | Subscription ended / refunded | `...&type=ended` |
| each plan | Payment failed | `...&type=payment-failed` |

## Editing the text

The code is generated, so the four plan pages stay consistent. To change a sentence everywhere, edit `scripts/gen_order_forms.py` and run `python3 scripts/gen_order_forms.py`; or edit the HTML files directly for a one-off change.
