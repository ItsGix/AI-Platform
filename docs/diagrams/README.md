# Diagram sources and assets

All portfolio visuals live here. SVGs use a fixed dark palette, system fonts and
text labels so status remains understandable without colour. No external images,
fonts, scripts or HTML `foreignObject` elements are required by the SVG assets.

## Files

| Source | Display location / generated asset | Purpose |
| --- | --- | --- |
| [`src/platform.mmd`](src/platform.mmd) | Architecture page Mermaid block | Proxmox hosting boundaries and K3s topology |
| [`src/inference.mmd`](src/inference.mmd) | Root README and architecture page Mermaid blocks | Proposed application request flow |
| [`src/render_assets.py`](src/render_assets.py) | [`assets/banner.svg`](assets/banner.svg) | Portfolio identity |
| [`src/render_assets.py`](src/render_assets.py) | [`assets/platform.svg`](assets/platform.svg) | Designed overview of the hosting topology |
| [`src/render_assets.py`](src/render_assets.py) | [`assets/roadmap.svg`](assets/roadmap.svg) | Learning areas and current chapter progress |

The Python generator is the source for the designed SVGs; they are not Mermaid
exports. The Mermaid files are the editable topology sources, copied into fenced
`mermaid` blocks because GitHub renders those blocks inline, rather than `.mmd`
file links. Keep both representations consistent when changing the architecture.

## Regenerate SVGs

From the repository root, using Python 3 (standard library only):

```bash
python3 docs/diagrams/src/render_assets.py
```

The roadmap's chapter count is a snapshot of the root README. Update the generator
when the learning record changes. Do not infer completion from deployed services.

## Validate and preview

Render both Mermaid files with Mermaid CLI (validated with version 11.12.0):

```bash
npx --yes --package @mermaid-js/mermaid-cli@11.12.0 mmdc -i docs/diagrams/src/platform.mmd -o /tmp/platform-preview.svg
npx --yes --package @mermaid-js/mermaid-cli@11.12.0 mmdc -i docs/diagrams/src/inference.mmd -o /tmp/inference-preview.svg
```

Mermaid CLI requires a compatible Chromium installation. Local SVG previews are
validation outputs, not additional source files to commit.

When editing, check that Mermaid blocks match their source files, relative links
resolve, SVG text fits its cards, and the README has balanced code fences. Preview
the README on GitHub before merging to check GitHub's current Mermaid renderer.

## Status conventions

- **Existing:** owner-reported homelab baseline; not a live health check.
- **Active learning:** recorded learning is underway; not overall mastery.
- **Intended / target / planned:** design or future work, not verified deployment.

The root README retains the authoritative course table and checklist. See the
[architecture notes](../architecture/README.md) for evidence and limitations.
