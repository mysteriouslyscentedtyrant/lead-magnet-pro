import os, html
import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / 'order-forms')
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
<style>
.lmpo{--ink:#181C39;--slate:#5E6075;--soft:#8A8CA0;--band:#F5F6F9;--line:#E2E4EC;--blue:#2F54EB;--lime:#B9F27C;--lime-ink:#1F3D10;
  font-family:Outfit,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased;text-align:left}
.lmpo *,.lmpo *::before,.lmpo *::after{box-sizing:border-box}
:where(.lmpo) :where(h1,h2,h3,p,ul,ol){margin:0;padding:0}
:where(.lmpo) a{color:inherit}
.lmpo-wrap{max-width:1100px;margin:0 auto;padding:0 24px}
.lmpo-switch{display:flex;justify-content:center;gap:6px;flex-wrap:wrap;padding:24px 16px 0}
.lmpo-switch a{padding:8px 16px;border-radius:999px;border:1px solid var(--line);font-size:14px;font-weight:500;text-decoration:none;color:var(--slate);background:#fff}
.lmpo-switch a:hover{border-color:var(--ink);color:var(--ink)}
.lmpo-switch a.is-on{background:var(--ink);border-color:var(--ink);color:#fff}
.lmpo-hero{display:grid;grid-template-columns:1fr 1.15fr;gap:48px;align-items:start;padding-top:48px;padding-bottom:64px}
.lmpo-kicker{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
.lmpo-kicker::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--blue)}
.lmpo h1{margin-top:14px;font-size:48px;line-height:1.08;font-weight:700;letter-spacing:-.02em}
.lmpo-lead{margin-top:18px;font-size:17px;color:var(--slate);max-width:460px}
.lmpo-amount{margin-top:28px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.lmpo-amount strong{font-size:40px;line-height:1;font-weight:700;letter-spacing:-.02em}
.lmpo-amount span{font-size:15px;color:var(--slate)}
.lmpo-note{margin-top:8px;font-size:14px;color:var(--soft)}
.lmpo-card{border:1px solid var(--line);border-radius:14px;padding:22px 24px;background:#fff}
.lmpo-checks{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:10px 24px}
.lmpo-checks li{position:relative;padding-left:26px;font-size:14px}
.lmpo-checks li::before{content:"";position:absolute;left:2px;top:4px;width:12px;height:7px;border-left:2px solid var(--blue);border-bottom:2px solid var(--blue);transform:rotate(-45deg)}
.lmpo-minis{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
.lmpo-mini{background:var(--band);border-radius:12px;padding:14px 16px;font-size:13px;color:var(--slate)}
.lmpo-mini strong{display:flex;align-items:center;gap:8px;margin-bottom:4px;font-size:14px;color:var(--ink);font-weight:600}
.lmpo-mini svg{flex:none;width:18px;height:18px}
.lmpo-band{background:var(--band);padding:72px 0}
.lmpo h2{font-size:36px;line-height:1.15;font-weight:700;letter-spacing:-.015em;text-align:center;max-width:720px;margin:0 auto}
.lmpo-sub{margin:12px auto 0;max-width:600px;text-align:center;color:var(--slate);font-size:16px}
.lmpo-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.lmpo-feat{background:#fff;border-radius:14px;padding:24px}
.lmpo-icon{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:var(--lime);color:var(--lime-ink)}
.lmpo-icon svg{width:18px;height:18px}
.lmpo-feat h3{margin-top:18px;font-size:17px;font-weight:600}
.lmpo-feat p{margin-top:8px;font-size:14px;color:var(--slate)}
.lmpo-credits{padding:72px 24px}
.lmpo-costs{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:36px}
.lmpo-costs li{border:1px solid var(--line);border-radius:14px;padding:20px;text-align:center}
.lmpo-costs b{display:block;font-size:26px;font-weight:700;letter-spacing:-.01em}
.lmpo-costs span{display:block;margin-top:4px;font-size:14px;color:var(--slate)}
.lmpo-costs-note{margin-top:20px;text-align:center;font-size:14px;color:var(--slate)}
.lmpo-costs-note a{color:var(--blue);font-weight:600;text-decoration:none}
.lmpo-costs-note a:hover{text-decoration:underline}
.lmpo-formhead{background:var(--band);padding:64px 24px 28px;text-align:center}
.lmpo-formhead .lmpo-sub{margin-top:10px}
.lmpo-after{background:var(--band);padding:20px 24px 56px;text-align:center;font-size:13px;color:var(--soft)}
.lmpo-after p+p{margin-top:8px}
.lmpo-after a{color:var(--slate)}
.lmpo-trust{display:flex;justify-content:center;gap:10px 28px;flex-wrap:wrap;margin-bottom:22px;font-size:14px;color:var(--slate)}
.lmpo-trust span{display:inline-flex;align-items:center;gap:8px}
.lmpo-trust svg{width:16px;height:16px;color:var(--blue)}
.lmpo-foot{border-top:1px solid var(--line);background:#fff;padding:24px;font-size:13px;color:var(--soft)}
.lmpo-foot .lmpo-wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:0}
.lmpo-foot a{color:var(--slate);text-decoration:none}
.lmpo-foot a:hover{text-decoration:underline}
.lmpo-foot nav{display:flex;gap:20px;flex-wrap:wrap}
.lmpo-welcome{max-width:720px;margin:0 auto;padding:72px 24px 80px;text-align:center}
.lmpo-done{display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;border-radius:50%;background:var(--lime);color:var(--lime-ink)}
.lmpo-done svg{width:30px;height:30px}
.lmpo-welcome h1{font-size:44px}
.lmpo-welcome .lmpo-lead{margin:16px auto 0}
.lmpo-steps{list-style:none;counter-reset:s;display:grid;gap:12px;margin-top:36px;text-align:left}
.lmpo-steps li{counter-increment:s;position:relative;background:var(--band);border-radius:14px;padding:18px 20px 18px 64px}
.lmpo-steps li::before{content:counter(s);position:absolute;left:20px;top:16px;width:30px;height:30px;border-radius:50%;background:var(--ink);color:#fff;font-weight:600;font-size:15px;display:flex;align-items:center;justify-content:center}
.lmpo-steps strong{display:block;font-weight:600}
.lmpo-steps span{display:block;margin-top:2px;font-size:14px;color:var(--slate)}
.lmpo-btn{display:inline-block;margin-top:32px;padding:14px 28px;border-radius:10px;background:var(--blue);color:#fff!important;font-weight:600;font-size:16px;text-decoration:none}
.lmpo-btn:hover{filter:brightness(1.08)}
.lmpo-small{margin-top:24px;font-size:14px;color:var(--slate)}
.lmpo-small+.lmpo-small{margin-top:8px}
.lmpo code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.92em;background:#fff;border:1px solid var(--line);border-radius:6px;padding:1px 6px}
@media (max-width:900px){
  .lmpo-hero{grid-template-columns:1fr;gap:32px;padding-top:36px;padding-bottom:48px}
  .lmpo h1{font-size:38px}
  .lmpo-grid{grid-template-columns:1fr 1fr}
  .lmpo-costs{grid-template-columns:1fr 1fr}
}
@media (max-width:560px){
  .lmpo-wrap{padding-left:16px;padding-right:16px}
  .lmpo h1{font-size:32px}
  .lmpo h2{font-size:28px}
  .lmpo-checks,.lmpo-minis,.lmpo-grid{grid-template-columns:1fr}
  .lmpo-band,.lmpo-credits{padding-top:56px;padding-bottom:56px}
  .lmpo-credits{padding-left:16px;padding-right:16px}
  .lmpo-formhead{padding:48px 16px 24px}
  .lmpo-card{padding:18px}
  .lmpo-welcome h1{font-size:34px}
}
</style>"""

def svg(path, sw=2):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
I = {
  'list': svg('<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6h.01M4 12h.01M4 18h.01"/>'),
  'pen': svg('<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
  'palette': svg('<circle cx="13.5" cy="6.5" r="1"/><circle cx="17.5" cy="10.5" r="1"/><circle cx="8.5" cy="7.5" r="1"/><circle cx="6.5" cy="12.5" r="1"/><path d="M12 2a10 10 0 0 0 0 20c1.1 0 2-.9 2-2 0-.5-.2-1-.5-1.3-.3-.4-.5-.8-.5-1.3 0-1.1.9-2 2-2h2.4A5.6 5.6 0 0 0 22 10c0-4.4-4.5-8-10-8Z"/>'),
  'download': svg('<path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/>'),
  'folder': svg('<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>'),
  'refund': svg('<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/>'),
  'shield': svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>'),
  'x': svg('<circle cx="12" cy="12" r="10"/><path d="m15 9-6 6M9 9l6 6"/>'),
  'mail': svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
  'infinity': svg('<path d="M18.2 8c2.4 0 3.8 1.8 3.8 4s-1.4 4-3.8 4c-3.9 0-8.5-8-12.4-8C3.4 8 2 9.8 2 12s1.4 4 3.8 4c3.9 0 8.5-8 12.4-8Z"/>'),
  'check': svg('<path d="M20 6 9 17l-5-5"/>', 2.5),
}

PLANS = [
  dict(slug='lmp-starter', tab='Starter', kicker='Lead Magnet Pro · Starter plan', name='Starter',
       h1='Your first lead magnets, ready in minutes',
       lead='Turn what you know into ebooks, guides and checklists your audience wants to download. Pick a format, describe your audience, and the AI writes it in your brand.',
       amount='500 credits', per='every month', note='About 50 lead magnets a month.',
       mini2=('x', 'Cancel anytime', 'Your plan stays active until the end of the month you paid for.'),
       head='Secure your Starter plan', headsub='Enter your details below. Your access key arrives by email a minute after payment.',
       more='Monthly credits renew every month and don’t roll over. Need more one month? <a href="/lmp-credits">Add a credit pack</a> or <a href="/lmp-pro">switch to Pro</a>.'),
  dict(slug='lmp-pro', tab='Pro', kicker='Lead Magnet Pro · Pro plan', name='Pro',
       h1='A lead magnet for every offer you sell',
       lead='Give every course, coaching program and product its own ebook, guide or checklist. The AI writes it for your audience; you keep full control of the outline and the design.',
       amount='1,000 credits', per='every month', note='About 100 lead magnets a month.',
       mini2=('x', 'Cancel anytime', 'Your plan stays active until the end of the month you paid for.'),
       head='Secure your Pro plan', headsub='Enter your details below. Your access key arrives by email a minute after payment.',
       more='Monthly credits renew every month and don’t roll over. Need more one month? <a href="/lmp-credits">Add a credit pack</a> or <a href="/lmp-scale">switch to Scale</a>.'),
  dict(slug='lmp-scale', tab='Scale', kicker='Lead Magnet Pro · Scale plan', name='Scale',
       h1='Lead magnets for every client and campaign',
       lead='For agencies, teams and busy creators: produce branded ebooks, guides and checklists for every audience, language and campaign, and keep them all in one place.',
       amount='5,000 credits', per='every month', note='About 500 lead magnets a month.',
       mini2=('x', 'Cancel anytime', 'Your plan stays active until the end of the month you paid for.'),
       head='Secure your Scale plan', headsub='Enter your details below. Your access key arrives by email a minute after payment.',
       more='Monthly credits renew every month and don’t roll over. Need more one month? <a href="/lmp-credits">Add a credit pack</a>.'),
  dict(slug='lmp-credits', tab='Credit pack', kicker='Lead Magnet Pro · Credit pack', name='100-credit pack',
       h1='100 more credits, whenever you need them',
       lead='Top up your balance for a busy month, or try Lead Magnet Pro without a subscription. One payment, no renewal.',
       amount='100 credits', per='one-time payment', note='About 10 lead magnets. Pack credits never expire.',
       mini2=('infinity', 'Never expire', 'Pack credits stay on your balance and are used after any monthly credits.'),
       head='Get your 100-credit pack', headsub='Use the same email as your account to add the credits to your existing key. New here? Your access key arrives by email a minute after payment.',
       more='Pack credits never expire and are used after your monthly credits. Making lead magnets every month? <a href="/lmp-starter">See the monthly plans</a>.'),
]

CHECKS = ['Ebooks, guides and checklists', 'An outline you review first', 'Written in 8 languages', 'Rewrite any section',
          '3 templates, 6 palettes, 5 font pairs', 'Your logo, name and colors', 'Call to action with your link', 'PDF in A4 or US Letter',
          'Word (.docx) download', '25 saved documents', '10 brand kits', 'Balance always visible']
FEATS = [
  ('list', 'An outline you control', 'Pick a format, describe your audience and your offer, then review and edit the outline before a single word is written.'),
  ('pen', 'Written section by section', 'Each section is written for your audience. Not happy with one? Rewrite just that section for 1 credit.'),
  ('palette', 'Your brand on every page', 'Templates, colors, fonts, your logo and your name. Save them as a brand kit and reuse them in one click.'),
  ('download', 'PDF and Word downloads', 'A print-ready PDF in A4 or US Letter, or a Word file to keep editing. Downloads are always free.'),
  ('folder', 'All your work, saved', 'Every lead magnet is saved to My documents. Reopen, duplicate or download it again anytime.'),
  ('refund', 'Fair credits', 'You pay only for AI writing. If a section can’t be written, its credits come back to your balance automatically.'),
]

def switch(active):
    links = ''.join(f'<a href="/{p["slug"]}"' + (' class="is-on" aria-current="page"' if p['slug'] == active else '') + f'>{p["tab"]}</a>' for p in PLANS)
    return f'<nav class="lmpo-switch" aria-label="Plans">{links}</nav>'

def top(p):
    checks = ''.join(f'<li>{html.escape(c)}</li>' for c in CHECKS)
    feats = ''.join(f'<div class="lmpo-feat"><span class="lmpo-icon">{I[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in FEATS)
    m2 = p['mini2']
    return f'''<!-- Lead Magnet Pro order form: {p["name"]} (page slug: {p["slug"]}). Paste into a Raw HTML element ABOVE the order form. -->
{FONT}{CSS}
<div class="lmpo">
  {switch(p["slug"])}
  <section class="lmpo-wrap lmpo-hero">
    <div>
      <p class="lmpo-kicker">{p["kicker"]}</p>
      <h1>{p["h1"]}</h1>
      <p class="lmpo-lead">{p["lead"]}</p>
      <p class="lmpo-amount"><strong>{p["amount"]}</strong><span>{p["per"]}</span></p>
      <p class="lmpo-note">{p["note"]} A typical one uses 8 to 12 credits.</p>
    </div>
    <div>
      <div class="lmpo-card"><ul class="lmpo-checks">{checks}</ul></div>
      <div class="lmpo-minis">
        <div class="lmpo-mini"><strong>{I["refund"]}Credits back if the AI fails</strong>If a section can’t be written, its credits return automatically.</div>
        <div class="lmpo-mini"><strong>{I[m2[0]]}{m2[1]}</strong>{m2[2]}</div>
      </div>
    </div>
  </section>
  <section class="lmpo-band">
    <div class="lmpo-wrap">
      <h2>Everything you need to create, brand and deliver lead magnets</h2>
      <div class="lmpo-grid">{feats}</div>
    </div>
  </section>
  <section class="lmpo-credits">
    <div class="lmpo-wrap">
      <h2>How credits work</h2>
      <p class="lmpo-sub">You see your balance at the top of the tool at all times.</p>
      <ul class="lmpo-costs">
        <li><b>2</b><span>credits for an outline</span></li>
        <li><b>1</b><span>credit per section written or rewritten</span></li>
        <li><b>0</b><span>for edits, design, PDF, Word and saving</span></li>
        <li><b>8–12</b><span>credits for a typical lead magnet</span></li>
      </ul>
      <p class="lmpo-costs-note">{p["more"]}</p>
    </div>
  </section>
  <section class="lmpo-formhead">
    <h2>{p["head"]}</h2>
    <p class="lmpo-sub">{p["headsub"]}</p>
  </section>
</div>
'''

BELOW = f'''<!-- Lead Magnet Pro order forms: paste into a Raw HTML element BELOW the order form (the same code on all four pages). -->
{FONT}{CSS}
<div class="lmpo">
  <section class="lmpo-after">
    <div class="lmpo-trust">
      <span>{I["mail"]}Access key by email right after payment</span>
      <span>{I["shield"]}Secure payment</span>
      <span>{I["refund"]}Credits back if the AI fails</span>
    </div>
    <p>By completing your purchase, you agree to our <a href="/lmp-terms">Terms and Conditions</a>.</p>
    <p>Already have an access key? <a href="/lead-magnet-pro">Open Lead Magnet Pro</a></p>
  </section>
  <footer class="lmpo-foot">
    <div class="lmpo-wrap">
      <span>© 2026 Lead Magnet Pro</span>
      <nav aria-label="More"><a href="/lead-magnet-pro">The tool</a><a href="/lead-magnet-pro#lmp-pricing">Plans</a><a href="/lmp-terms">Terms</a></nav>
    </div>
  </footer>
</div>
'''

WELCOME = f'''<!-- Lead Magnet Pro: thank-you page after payment (page slug: lmp-welcome). Paste into one Raw HTML element. -->
{FONT}{CSS}
<div class="lmpo">
  <section class="lmpo-welcome">
    <span class="lmpo-done">{I["check"]}</span>
    <h1 style="margin-top:22px">You’re in. Check your inbox.</h1>
    <p class="lmpo-lead">Thank you for your purchase. Your access key is on its way to the email you used at checkout.</p>
    <ol class="lmpo-steps">
      <li><strong>Open the email “Here is your access key”</strong><span>It usually arrives within a minute. Check your spam or promotions folder too.</span></li>
      <li><strong>Copy your key</strong><span>It starts with <code>lmp_</code>. Keep the email: it is your login.</span></li>
      <li><strong>Open the tool and paste it</strong><span>Your balance appears at the top, and you can create your first lead magnet right away.</span></li>
    </ol>
    <a class="lmpo-btn" href="/lead-magnet-pro">Open Lead Magnet Pro</a>
    <p class="lmpo-small">Already had a key? It still works: your new credits are already on it.</p>
    <p class="lmpo-small">No email after 5 minutes? On the tool’s key screen, click “Send me a new one” and enter the same email.</p>
  </section>
  <footer class="lmpo-foot">
    <div class="lmpo-wrap">
      <span>© 2026 Lead Magnet Pro</span>
      <nav aria-label="More"><a href="/lead-magnet-pro">The tool</a><a href="/lmp-terms">Terms</a></nav>
    </div>
  </footer>
</div>
'''

def write(name, text):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f: f.write(text)
for p in PLANS: write(p['slug'] + '.html', top(p))
write('below-form.html', BELOW)
write('lmp-welcome.html', WELCOME)

# previews for checking only (not for systeme.io): top + a stand-in form + below
FORM = '<div style="background:#F5F6F9;padding:0 16px"><div style="max-width:720px;margin:0 auto;background:#fff;border:2px dashed #C9CCDA;border-radius:14px;padding:48px 24px;text-align:center;font:500 15px Outfit,sans-serif;color:#8A8CA0">systeme.io order form elements go here<br>(contact fields, payment, order summary, button)</div></div>'
PREV = os.path.join(OUT, 'previews'); os.makedirs(PREV, exist_ok=True)
for p in PLANS:
    open(os.path.join(PREV, p['slug'] + '.html'), 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><body style="margin:0">' + top(p) + FORM + BELOW)
open(os.path.join(PREV, 'lmp-welcome.html'), 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><body style="margin:0">' + WELCOME)
print('ok')
