"""House style v5 - cream "big type" list carousel renderer (1080x1350).

Cream ground (#FBF8EC), small header (avatar, name, badge, title), yellow
highlighter (#FCE883) behind the key word, huge bold type, one idea per slide,
"Save for later" row and n/N on every slide. Built for numbered lists ("7 ...").

Usage:
    exec(open('renderer_v5_bigtype.py').read())
    paths = render(spec, outdir); print(qa())

spec = {
  "name": "Brand Owner", "title": "Founder @Brand", "verified": True,
  "avatar": "/mnt/files/photos/owner.jpg", "initials": "BO",
  "font": "/mnt/files/fonts/Figtree.ttf",
  "slides": [
    {"kind": "cover", "head": "7 Japanese ideas that quietly change how you work",
     "highlight": "quietly change", "sub": "Save this. Free guide at the end →"},
    {"kind": "item", "num": 1, "word": "Kaizen", "meaning": "Small steps, every day.",
     "body": "Improve one tiny thing daily. ...", "watermark": "改善"},   # watermark optional
    {"kind": "recap", "head": "Screenshot this", "lines": ["1. Kaizen - small steps", "..."]},
    {"kind": "cta", "head": "Comment JAPAN", "body": "and I'll DM you the free guide.\nSend this to someone you care about."}
  ]
}
Watermarks in non-Latin scripts need a font that has the glyphs (e.g. Noto Sans JP at
spec["watermark_font"]); if missing, the watermark is skipped.
"""
import math, os
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 90
CREAM = (251, 248, 236); INK = (22, 22, 22); MUTED = (106, 101, 90); HL = (252, 232, 131); BADGE = (0, 149, 246)
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
        p = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if weight >= 700 else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
        return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()


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


def _header(im, d, spec):
    size = 72; x, y = M, 70
    p = spec.get('avatar')
    if p and os.path.exists(p):
        av = Image.open(p).convert('RGB').resize((size, size), Image.LANCZOS)
        mk = Image.new('L', (size * 4, size * 4), 0); ImageDraw.Draw(mk).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
        im.paste(av, (x, y), mk.resize((size, size), Image.LANCZOS))
    else:
        d.ellipse((x, y, x + size, y + size), fill=INK)
        f = _fig(26, 800); t = spec.get('initials', spec['name'][:2].upper())
        d.text((x + size / 2 - d.textlength(t, font=f) / 2, y + 22), t, font=f, fill=CREAM)
    nf = _fig(30, 700); tf = _fig(22, 400)
    d.text((x + size + 18, y + 8), spec['name'], font=nf, fill=INK)
    if spec.get('verified'):
        r = 13; bx = x + size + 18 + d.textlength(spec['name'], font=nf) + 10; by = y + 12
        cx, cy = bx + r, by + r
        pts = [(cx + (r if k % 2 == 0 else r * .86) * math.cos(math.pi * 2 * k / 32 - math.pi / 2),
                cy + (r if k % 2 == 0 else r * .86) * math.sin(math.pi * 2 * k / 32 - math.pi / 2)) for k in range(32)]
        d.polygon(pts, fill=BADGE)
        d.line((cx - r * .42, cy, cx - r * .1, cy + r * .32, cx + r * .45, cy - r * .3), fill=(255, 255, 255), width=4)
    d.text((x + size + 18, y + 46), spec['title'], font=tf, fill=MUTED)


def _footer(d, i, n, save=True):
    f = _fig(24, 600)
    if save:
        bx, by = M, H - 104
        d.polygon([(bx, by), (bx + 22, by), (bx + 22, by + 30), (bx + 11, by + 22), (bx, by + 30)], fill=INK)
        d.text((bx + 34, by + 1), 'Save for later', font=f, fill=INK)
    t = f"{i}/{n}"; d.text((W - M - d.textlength(t, font=f), H - 103), t, font=f, fill=MUTED)


def _hl_text(d, x, y, text, font, hl_words=None):
    """Draw text; draw a highlighter block behind the whole line (or the words in hl_words)."""
    tw = d.textlength(text, font=font)
    if hl_words is None or any(w.lower() in text.lower() for w in hl_words):
        d.rectangle((x - 8, y + font.size * 0.42, x + tw + 8, y + font.size * 1.08), fill=HL)
    d.text((x, y), text, font=font, fill=INK)
    return tw


def render(spec, outdir):
    global _FONT
    _FONT = spec.get('font', _FONT)
    os.makedirs(outdir, exist_ok=True); n = len(spec['slides']); paths = []; LOG.clear()
    for i, s in enumerate(spec['slides'], 1):
        im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
        _header(im, d, spec)
        kind = s.get('kind', 'item'); y = 250
        if kind == 'cover':
            hf = _fig(s.get('size', 96), 800)
            lines = _wrap(d, s['head'], hf, W - 2 * M)
            y = max(240, int(H * 0.45 - len(lines) * hf.size * 1.12 / 2))
            hlw = s['highlight'].split() if s.get('highlight') else []   # any line holding a highlight word gets the block
            for ln in lines:
                hit = any(w.lower() in ln.lower() for w in hlw) if hlw else False
                if hit:
                    _hl_text(d, M, y, ln, hf)
                else:
                    d.text((M, y), ln, font=hf, fill=INK)
                LOG.append(('w', d.textlength(ln, font=hf), W - 2 * M, i)); y += int(hf.size * 1.12)
            if s.get('sub'):
                y += 30; sf = _fig(36, 600)
                for ln in _wrap(d, s['sub'], sf, W - 2 * M):
                    d.text((M, y), ln, font=sf, fill=MUTED); y += 50
            f = _fig(30, 700); t = 'Swipe  →'; d.text((W - M - d.textlength(t, font=f), H - 104), t, font=f, fill=INK)
        elif kind == 'item':
            if s.get('watermark') and spec.get('watermark_font') and os.path.exists(spec['watermark_font']):
                wf = ImageFont.truetype(spec['watermark_font'], 420)
                d.text((W - M - d.textlength(s['watermark'], font=wf), 330), s['watermark'], font=wf, fill=(240, 235, 214))
            # number disc
            r = 42; d.ellipse((M, y, M + 2 * r, y + 2 * r), fill=HL)
            nfnt = _fig(44, 900); t = str(s.get('num', i - 1))
            d.text((M + r - d.textlength(t, font=nfnt) / 2, y + 14), t, font=nfnt, fill=INK)
            y += 2 * r + 40
            wf = _fig(s.get('size', 110), 800)
            for ln in _wrap(d, s['word'], wf, W - 2 * M):
                _hl_text(d, M, y, ln, wf); LOG.append(('w', d.textlength(ln, font=wf), W - 2 * M, i)); y += int(wf.size * 1.1)
            y += 24
            if s.get('meaning'):
                mf = _fig(46, 800)
                for ln in _wrap(d, s['meaning'], mf, W - 2 * M):
                    d.text((M, y), ln, font=mf, fill=INK); LOG.append(('w', d.textlength(ln, font=mf), W - 2 * M, i)); y += 60
                y += 20
            if s.get('body'):
                bf = _fig(38, 400)
                for ln in _wrap(d, s['body'], bf, W - 2 * M):
                    d.text((M, y), ln, font=bf, fill=INK); LOG.append(('w', d.textlength(ln, font=bf), W - 2 * M, i)); y += 54
        elif kind == 'recap':
            hf = _fig(70, 800); _hl_text(d, M, y, s['head'], hf); y += 120
            lf = _fig(38, 600)
            for item in s.get('lines', []):
                for ln in _wrap(d, item, lf, W - 2 * M):
                    d.text((M, y), ln, font=lf, fill=INK); LOG.append(('w', d.textlength(ln, font=lf), W - 2 * M, i)); y += 56
                y += 8
        elif kind == 'cta':
            y = 380; hf = _fig(100, 800)
            for ln in _wrap(d, s['head'], hf, W - 2 * M):
                _hl_text(d, M, y, ln, hf); LOG.append(('w', d.textlength(ln, font=hf), W - 2 * M, i)); y += 120
            y += 30; bf = _fig(44, 600)
            for ln in _wrap(d, s.get('body', ''), bf, W - 2 * M):
                d.text((M, y), ln, font=bf, fill=INK); y += 62
        LOG.append(('y', y, 1220, i))
        if kind != 'cover':
            _footer(d, i, n)
        p = f"{outdir}/slide_{i:02d}.jpg"; im.save(p, 'JPEG', quality=92); paths.append(p)
    return paths


def qa():
    bad = []
    for e in LOG:
        if e[0] == 'w' and e[1] > e[2]:
            bad.append(f"slide {e[3]}: line too wide ({int(e[1])}>{e[2]})")
        if e[0] == 'y' and e[1] > e[2]:
            bad.append(f"slide {e[3]}: text runs to y={int(e[1])} (max {e[2]})")
    return bad
