# generate_pacman.py
import os

os.makedirs("dist", exist_ok=True)

# Create simple SVG
svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="120">
  <text x="20" y="60" font-size="50">😋 • • • • •</text>
</svg>
"""

with open("dist/github-contribution-grid-pacman.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

# Optional dark version
svg_content_dark = """
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="120" style="background:black">
  <text x="20" y="60" font-size="50" fill="yellow">😋 • • • • •</text>
</svg>
"""

with open("dist/github-contribution-grid-pacman-dark.svg", "w", encoding="utf-8") as f:
    f.write(svg_content_dark)

print("✅ Pac-Man SVGs generated in dist/")
