"""House style v3 - white "post card" carousel renderer (1080x1350).

Every slide: white ground, round avatar, name + optional blue verified badge,
grey title, bold headline with an accent underline on every line, plain body.
Slide 1 shows "Swipe ->" (and an optional footer such as "Free gift on slide 4 ->"),
other slides show "n/N".

Usage (Composio workbench or any Python with Pillow):
    exec(open('renderer_v3_postcard.py').read())
    paths = render(spec, '/mnt/files/ig_queue/<date>_<keyword>')
    print(qa())   # [] means nothing overflowed

spec = {
  "name": "Brand Owner", "title": "Founder @Brand", "verified": True,
  "avatar": "/mnt/files/photos/owner.jpg",      # optional; falls back to initials
  "initials": "BO",                              # used when no avatar file
  "accent": [98,124,226],                        # underline + footer colour (optional)
  "font": "/mnt/files/fonts/Figtree.ttf",        # variable Figtree (optional)
  "head_size": 54, "body_size": 46,              # optional
  "slides": [ {"head": "...", "body": "...", "footer": "Free gift on slide 4 ->"},
              {"head": "FREE: <doc title>", "body": "- teaser 1\n- teaser 2\n- teaser 3\nComment KEYWORD and I'll send you the doc"},  # slide 4 gift preview
              ... ]
}
Fonts: download Figtree once into /mnt/files/fonts/Figtree.ttf from
https://github.com/google/fonts/raw/main/ofl/figtree/Figtree%5Bwght%5D.ttf
"""
import math, os
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 96
BG = (255, 255, 255); INK = (17, 17, 17); GREY = (120, 120, 120); BADGE = (0, 149, 246)
LOG = []
_FONT = '/mnt/files/fonts/Figtree.ttf'


def _fig(size, weight=400):
    try:
        f = ImageFont.truetype(_FONT, size)
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
        return f
    except Exception:
        for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if weight >= 700 else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',):
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default()


def _wrap(d, text, font, width):
    out = []
    for para in text.split('\n'):
        line = ''
        for w in para.split():
            t = (line + ' ' + w).strip()
            if d.textlength(t, font=font) <= width:
                line = t
            else:
                out.append(line); line = w
        out.append(line)
    return out


def _avatar(im, d, spec, x, y, size):
    p = spec.get('avatar')
    if p and os.path.exists(p):
        av = Image.open(p).convert('RGB').resize((size, size), Image.LANCZOS)
        mk = Image.new('L', (size * 4, size * 4), 0)
        ImageDraw.Draw(mk).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
        im.paste(av, (x, y), mk.resize((size, size), Image.LANCZOS))
    else:
        d.ellipse((x, y, x + size, y + size), fill=INK)
        f = _fig(int(size * 0.36), 800); t = spec.get('initials', spec['name'][:2].upper())
        d.text((x + size / 2 - d.textlength(t, font=f) / 2, y + size * 0.3), t, font=f, fill=BG)


def _badge(d, x, y, r):
    cx, cy = x + r, y + r; pts = []
    for k in range(32):
        a = math.pi * 2 * k / 32 - math.pi / 2; rr = r if k % 2 == 0 else r * 0.86
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=BADGE)
    d.line((cx - r * 0.42, cy + r * 0.02, cx - r * 0.1, cy + r * 0.34, cx + r * 0.45, cy - r * 0.3),
           fill=(255, 255, 255), width=max(3, int(r * 0.24)), joint='curve')


def render(spec, outdir):
    global _FONT
    _FONT = spec.get('font', _FONT)
    accent = tuple(spec.get('accent', (98, 124, 226)))
    os.makedirs(outdir, exist_ok=True); n = len(spec['slides']); paths = []; LOG.clear()
    hf = _fig(spec.get('head_size', 54), 800); bf = _fig(spec.get('body_size', 46), 400)
    nf = _fig(38, 700); tf = _fig(27, 400)
    for i, s in enumerate(spec['slides'], 1):
        im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
        hl = _wrap(d, s['head'], hf, W - 2 * M) if s.get('head') else []
        bl = _wrap(d, s['body'], bf, W - 2 * M) if s.get('body') else []
        hlh = int(hf.size * 1.32); blh = int(bf.size * 1.36)
        block = 150 + 48 + len(hl) * hlh + (40 if bl else 0) + len(bl) * blh
        y = max(150, int(H * 0.53 - block / 2))
        _avatar(im, d, spec, M, y, 150)
        nx = M + 180; ny = y + 34
        d.text((nx, ny), spec['name'], font=nf, fill=INK)
        if spec.get('verified'):
            _badge(d, nx + d.textlength(spec['name'], font=nf) + 12, ny + 6, 18)
        d.text((nx, ny + 56), spec['title'], font=tf, fill=GREY)
        y += 198
        for ln in hl:
            d.text((M, y), ln, font=hf, fill=INK); tw = d.textlength(ln, font=hf); LOG.append(('w', tw, W - 2 * M, i))
            uy = y + int(hf.size * 1.16); d.line((M - 4, uy, M + tw + 16, uy), fill=accent, width=4); y += hlh
        if bl:
            y += 40
        for ln in bl:
            d.text((M, y), ln, font=bf, fill=INK); LOG.append(('w', d.textlength(ln, font=bf), W - 2 * M, i)); y += blh
        LOG.append(('y', y, 1220, i))
        if i == 1 and n > 1:
            t = 'Swipe  →'; f = _fig(30, 600); d.text((W - M - d.textlength(t, font=f), H - 110), t, font=f, fill=GREY)
            if s.get('footer'):
                d.text((M, H - 110), s['footer'], font=_fig(28, 600), fill=accent)
        elif n > 1:
            t = f"{i}/{n}"; f = _fig(26, 500); d.text((W - M - d.textlength(t, font=f), H - 104), t, font=f, fill=(170, 170, 170))
        p = f"{outdir}/slide_{i:02d}.jpg"; im.save(p, 'JPEG', quality=92); paths.append(p)
    return paths


def qa():
    """Return a list of problems. Empty list = pass. Fix by shortening copy, never by shrinking type."""
    bad = []
    for e in LOG:
        if e[0] == 'w' and e[1] > e[2]:
            bad.append(f"slide {e[3]}: line too wide ({int(e[1])}>{e[2]})")
        if e[0] == 'y' and e[1] > e[2]:
            bad.append(f"slide {e[3]}: text runs to y={int(e[1])} (max {e[2]})")
    return bad
