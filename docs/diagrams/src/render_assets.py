"""Generate dependency-free SVG portfolio graphics. Run from any directory."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)
BG, PANEL, INK, MUTED = '#0b1220', '#142136', '#eef5ff', '#b8c9de'
CYAN, GREEN, AMBER = '#67d9ef', '#85e4b5', '#ffd18a'


def text(x, y, value, size=18, color=INK, weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}">{escape(value)}</text>'


def rect(x, y, w, h, color=PANEL, stroke='#2c405b'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{color}" stroke="{stroke}"/>'


def save(name, height, title, desc, content):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{height}" viewBox="0 0 1120 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<rect width="1120" height="{height}" rx="20" fill="{BG}"/>
<g font-family="Arial, Helvetica, sans-serif">{content}</g></svg>\n'''
    (OUT / name).write_text(svg, encoding='utf-8')


s = text(44, 48, 'HOMELAB / ENGINEERING PORTFOLIO', 16, CYAN, 700)
s += text(44, 108, 'AI Platform Engineering', 46, INK, 700)
s += text(44, 149, 'From infrastructure operations to automated AI systems.', 23, MUTED)
for x, label in [(44, 'PROXMOX'), (241, 'K3S'), (438, 'LOCAL INFERENCE')]:
    s += rect(x, 183, 180 if x < 400 else 234, 42)
    s += text(x + 18, 210, label, 15, CYAN, 700)
s += text(44, 263, 'LEARN DELIBERATELY   /   BUILD IN PUBLIC   /   DOCUMENT THE EVIDENCE', 15, MUTED)
s += '<circle cx="956" cy="104" r="52" fill="none" stroke="#2c405b" stroke-width="2"/>'
s += '<path d="M914 104h84M956 62v84" stroke="#67d9ef" stroke-width="2"/>'
for x, y in [(914,104),(998,104),(956,62),(956,146)]:
    s += f'<circle cx="{x}" cy="{y}" r="7" fill="{CYAN}"/>'
save('banner.svg', 298, 'AI Platform Engineering', 'A learning portfolio for Proxmox, K3s and local inference.', s)

s = text(36, 42, '01 / PLATFORM TOPOLOGY', 16, CYAN, 700)
s += text(36, 81, 'Virtualised compute. Dedicated inference.', 32, INK, 700)
s += text(36, 111, 'Existing Proxmox / K3s baseline with intended GPU VM placement', 18, MUTED)
s += rect(32, 140, 1056, 449)
s += text(56, 176, 'PROXMOX HOST 1 · COMPUTE', 20, CYAN, 700)
s += text(56, 204, '16 cores / 32 threads  ·  128 GB RAM  ·  2 TB NVMe', 17, MUTED)
s += rect(54, 227, 628, 266, BG)
s += text(76, 260, 'K3s cluster / existing VM topology', 20, INK, 700)
s += rect(214, 279, 310, 58)
s += text(252, 315, 'k3s-control', 21, GREEN, 700)
s += '<path d="M369 337v24H214v25M369 361h155v25" stroke="#85e4b5" fill="none" stroke-width="2"/>'
for x, name in [(76,'k3s-worker-1'),(386,'k3s-worker-2')]:
    s += rect(x, 389, 272, 72)
    s += text(x + 22, 432, name, 20, GREEN, 700)
s += rect(704, 227, 362, 266, BG, '#806444')
s += text(726, 260, 'GPU backend / intended VM', 20, AMBER, 700)
s += text(726, 302, 'llama.cpp inference server', 19)
s += text(726, 339, 'PCIe passthrough', 17, MUTED)
s += rect(726, 365, 318, 62)
s += text(744, 403, 'RTX 3060 · 12 GB VRAM', 20, AMBER, 700)
s += text(726, 465, 'Outside the K3s worker pool', 17, MUTED)
s += text(56, 535, 'Other homelab services remain outside the AI migration scope.', 19, MUTED)
s += text(56, 564, 'One physical compute host; no high-availability claim.', 17, AMBER)
s += rect(32, 609, 1056, 110)
s += text(56, 644, 'PROXMOX HOST 2 · INDEPENDENT STORAGE', 20, CYAN, 700)
s += text(56, 677, 'Network shares  ·  2 × 8 TB disks  ·  K3s storage integration unspecified', 19, MUTED)
s += text(36, 752, 'Hosting boundaries only. Runtime placement and connectivity are not live-verified.', 17, MUTED)
save('platform.svg', 780, 'Proxmox and K3s hosting topology', 'Compute host contains a K3s control plane, two workers and intended GPU VM. A separate storage host serves network shares. No high availability or Kubernetes storage integration is claimed.', s)

s = text(36, 43, '02 / LEARNING ROADMAP', 16, CYAN, 700)
s += text(36, 83, 'Build foundations. Apply them to the platform.', 31, INK, 700)
s += text(36, 115, 'Learning sequence, not a completed technology stack', 19, MUTED)
cards = [
    ('01', 'Foundations', 'ACTIVE LEARNING', CYAN, ['Git & GitHub · Python', '5 / 15 beginner chapters complete', 'Original infrastructure exercises']),
    ('02', 'Systems', 'LEARNING GOALS', AMBER, ['Linux · Docker', 'Services, networking and containers', 'Core checklist items remain open']),
    ('03', 'Automation', 'PLANNED', AMBER, ['Terraform · Ansible', 'Provision and configure the lab', 'Implementation directories scaffolded']),
    ('04', 'Platform & AI', 'LEARNING GOALS', AMBER, ['Kubernetes · Model APIs', 'Existing K3s lab, fundamentals ahead', 'Serving, GPU workloads and tooling']),
    ('05', 'Delivery & cloud', 'PLANNED', AMBER, ['CI/CD · GitOps concepts', 'Cloud platform to be selected', 'Azure or AWS under consideration']),
]
for i, (number, title, status, color, lines) in enumerate(cards):
    y = 144 + i * 146
    s += rect(32, y, 1056, 128)
    s += text(54, y + 45, number, 27, color, 700)
    s += text(111, y + 42, title, 25, INK, 700)
    s += text(111, y + 78, status, 14, color, 700)
    for j, line in enumerate(lines):
        s += text(475, y + 32 + j * 30, line, 18, MUTED)
s += text(36, 906, 'Checklist status is preserved. Running infrastructure does not imply skill mastery.', 18, MUTED)
save('roadmap.svg', 934, 'Learning roadmap', 'Git and Python are active learning. Five of fifteen beginner Python chapters are complete. Linux, Docker, Terraform, Ansible, Kubernetes, AI tooling, CI/CD and cloud remain learning goals.', s)
print('Generated 3 SVG assets')
