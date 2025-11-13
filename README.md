# ArUco Marker Generator for Laser Cutting

A Python script to generate clean, optimized ArUco markers for laser cutting and engraving with color-coded layers that work perfectly with Lightburn and other laser software.

**Author:** Pavan Kumar Kaushik

## Features

✅ **Clean Vector Output** - Generates markers at logical grid level (not pixel level) for simple, clean vectors  
✅ **Color-Coded Layers** - Blue for engraving, Red for cutting  
✅ **Multiple Dictionaries** - Supports 4x4, 5x5, 6x6, 7x7 ArUco dictionaries  
✅ **Flexible Configuration** - Customize size, spacing, borders, and more  
✅ **Batch Generation** - Generate specific IDs, ranges, or entire dictionaries  
✅ **Optional Labels** - Toggle marker ID labels on/off  

## Color Coding

- **Blue (RGB: 0,0,255)** - Filled squares for engraving layer
- **Red (RGB: 255,0,0)** - Outer border for cutting layer

Your laser software (e.g., Lightburn) will recognize these colors and apply appropriate operations.

---

## 🚀 Quick Start (with uv)

### 1. Install uv (if you don't have it)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or visit: https://docs.astral.sh/uv/getting-started/installation/

### 2. Run the Generator (uv handles everything!)

```bash
# Generate all 50 markers from 4X4_50 dictionary
uv run generate_aruco_laser.py

# Generate specific markers with custom settings
uv run generate_aruco_laser.py -r 0 9 -s 10 --spacing 20

# 3mm markers, 2mm spacing, all 50 tags, no labels (compact)
uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels

# Generate from different dictionary
uv run generate_aruco_laser.py --dict 5X5_100 -r 0 20
```

**That's it!** `uv` automatically creates a virtual environment, installs dependencies, and runs the script.

---

## 📦 Alternative: Traditional Installation

If you prefer traditional pip:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python generate_aruco_laser.py
```

---

## 🖼️ Example Outputs

The repository includes several example PDFs demonstrating different configurations:

### Example Files

| File | Description | Command |
|------|-------------|---------|
| [`my_first_markers.pdf`](my_first_markers.pdf) | Standard 10mm markers with labels | `uv run generate_aruco_laser.py -r 0 9` |
| [`aruco_3mm_all.pdf`](aruco_3mm_all.pdf) | Compact 3mm markers, all 50 from 4X4_50 | `uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels` |
| [`example_5x5_markers.pdf`](example_5x5_markers.pdf) | 5×5 dictionary markers | `uv run generate_aruco_laser.py --dict 5X5_100 -r 0 20` |
| [`example_no_labels.pdf`](example_no_labels.pdf) | Clean markers without ID labels | `uv run generate_aruco_laser.py -r 0 15 --no-labels` |
| [`final_demo.pdf`](final_demo.pdf) | Production-ready example | `uv run generate_aruco_laser.py -r 0 25 -s 12 --spacing 25` |
| [`all_markers.pdf`](all_markers.pdf) | All 100 markers in single column layout | `uv run generate_aruco_laser.py --dict 4X4_100 --nrows 25 --ncols 1 -s 2.5 --spacing 1 --no-labels` |

> **Note:** Click on any PDF file above to view it directly in GitHub or download it to see the output quality.

### Visual Preview

The generated PDFs feature:
- **Clean vector graphics** - No pixelation, perfect for laser cutting
- **Color-coded layers** - Blue (engraving) and Red (cutting) automatically recognized by laser software
- **Precise spacing** - Consistent gaps between markers for easy cutting
- **Optional labels** - Marker IDs can be shown or hidden

---

## 📖 Usage Examples

### Quick Examples

```bash
# Generate first 10 markers (great for testing)
uv run generate_aruco_laser.py -r 0 9

# Generate specific marker IDs
uv run generate_aruco_laser.py -i 0 5 10 15 20

# Custom size - 15mm markers with larger spacing
uv run generate_aruco_laser.py -r 0 20 -s 15 --spacing 30

# Use a different dictionary (more unique markers available)
uv run generate_aruco_laser.py --dict 5X5_100 -r 0 50

# Generate without ID labels (cleaner look)
uv run generate_aruco_laser.py -r 0 10 --no-labels

# Production run - custom everything
uv run generate_aruco_laser.py --dict 6X6_250 -r 0 100 -s 20 -b 2 --spacing 30 -o my_markers.pdf
```

### Common Use Cases

**Small Dense Array (like your 3mm request):**
```bash
uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels -o compact_markers.pdf
```

**Medium Standard Markers:**
```bash
uv run generate_aruco_laser.py -r 0 20 -s 12 --spacing 25 -o standard_markers.pdf
```

**Large High-Visibility Markers:**
```bash
uv run generate_aruco_laser.py -r 0 10 -s 25 -b 2 --spacing 40 -o large_markers.pdf
```

---

## ⚙️ Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--dict DICT` | ArUco dictionary (4X4_50, 5X5_100, etc.) | 4X4_50 |
| `-o FILE` | Output PDF filename | aruco_markers.pdf |
| `-s SIZE` | Marker size in millimeters | 10.0 |
| `-b BORDER` | Border width in millimeters | 0.5 |
| `--spacing SIZE` | Space between markers in mm | 20.0 |
| `-i ID [ID ...]` | Specific marker IDs to generate | All markers |
| `-r START END` | Generate range of IDs (inclusive) | - |
| `-p NUM` | Number of markers per page | 20 |
| `--nrows NUM` | Explicit number of rows per page | Auto-calculated |
| `--ncols NUM` | Explicit number of columns per page | Auto-calculated |
| `--page-size SIZE` | Page size (A4 or letter) | A4 |
| `--no-labels` | Don't show marker ID labels | Show labels |

### View All Options

```bash
uv run generate_aruco_laser.py --help
```

---

## 📚 Available Dictionaries

| Dictionary | Marker Count | Grid Size | Best For |
|------------|--------------|-----------|----------|
| **4X4_50** | 50 | 4×4 (6×6 with border) | Small projects, compact markers |
| 4X4_100 | 100 | 4×4 (6×6 with border) | Medium projects |
| 4X4_250 | 250 | 4×4 (6×6 with border) | Large projects |
| 4X4_1000 | 1000 | 4×4 (6×6 with border) | Very large projects |
| **5X5_100** | 100 | 5×5 (7×7 with border) | Better detection reliability |
| 5X5_250 | 250 | 5×5 (7×7 with border) | Large projects with better detection |
| 5X5_1000 | 1000 | 5×5 (7×7 with border) | Very large projects |
| 6X6_250 | 250 | 6×6 (8×8 with border) | Maximum detection reliability |
| 6X6_1000 | 1000 | 6×6 (8×8 with border) | Very large projects, best detection |
| 7X7_1000 | 1000 | 7×7 (9×9 with border) | Extreme conditions |

> **Note:** Larger grid sizes (5×5, 6×6, 7×7) are more robust to detection errors but require more space.

---

## 🔥 Laser Cutting Setup

### In Lightburn

1. **Import the PDF**
   - File → Import → Select your generated PDF

2. **Assign Layers** (Lightburn does this automatically by color)
   - **Blue shapes** → Engraving layer (Fill mode)
   - **Red outlines** → Cutting layer (Line mode)

3. **Configure Layers:**
   
   **Blue Layer (Engraving):**
   - Mode: Fill
   - Speed: 1000-1500 mm/min (adjust for material)
   - Power: 10-20% (adjust for material)
   - Line Interval: 0.1mm
   
   **Red Layer (Cutting):**
   - Mode: Line
   - Speed: 10-20 mm/min (adjust for material)
   - Power: 70-100% (adjust for material)
   - Passes: 1-2

4. **Test on Scrap Material First!**

5. **Run Your Job**

### Material Recommendations

| Material | Blue Power | Blue Speed | Red Power | Red Speed |
|----------|------------|------------|-----------|-----------|
| Cardboard | 15% | 1200 mm/min | 80% | 15 mm/min |
| Wood (3mm) | 20% | 1000 mm/min | 100% | 12 mm/min |
| Acrylic (3mm) | 18% | 1500 mm/min | 90% | 10 mm/min |
| Anodized Aluminum | 40% | 800 mm/min | N/A | N/A |

> ⚠️ **Always test on scrap first!** Settings vary by laser power and material.

---

## 💡 Tips & Best Practices

### Marker Size Guidelines

- **3-5mm**: Ultra-compact, requires precise cutting, detection distance < 30cm
- **10-15mm**: Versatile, good balance, detection distance 30cm-1m
- **20-30mm**: Large format, easy detection, distance 1m-3m+

### Border Width

- **0.5mm**: Minimal border, most compact
- **1-2mm**: Recommended for best marker definition
- **3mm+**: High contrast, easier detection in poor lighting

### Spacing

- **2-5mm**: Maximum density for small markers
- **20-30mm**: Standard spacing, easy to cut individually
- **40-50mm**: Generous spacing for large markers

### Detection Tips

1. **Lighting**: Even, diffuse lighting works best
2. **Contrast**: White or light material with dark engraving
3. **Focus**: Ensure laser is properly focused for sharp engraving
4. **Camera Quality**: Higher resolution cameras detect smaller markers
5. **Multiple Dictionaries**: Mix dictionaries if you need 100+ markers

---

## 🐛 Troubleshooting

### Markers too small/large
```bash
# Adjust size with -s flag
uv run generate_aruco_laser.py -s 15  # 15mm markers
```

### Markers too close together
```bash
# Increase spacing
uv run generate_aruco_laser.py --spacing 30  # 30mm between markers
```

### Border too thin/thick
```bash
# Adjust border width
uv run generate_aruco_laser.py -b 2  # 2mm border
```

### Laser software doesn't recognize colors
- Ensure you're importing as vectors, not rasterizing
- Check color settings: Blue (0,0,255) and Red (255,0,0)
- Some software requires RGB mode, not CMYK

### Engraving not filling properly
- Verify blue layer is set to "Fill" mode
- Check line interval (0.1mm recommended)
- Ensure adequate power for your material

### Script won't run
```bash
# Make sure uv is installed
uv --version

# If using pip, check dependencies
pip list | grep -E 'opencv|numpy|reportlab'
```

---

## 📋 Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
- `opencv-python>=4.8.0` - ArUco marker generation
- `numpy>=1.24.0` - Array operations
- `reportlab>=4.0.0` - PDF generation

All dependencies are automatically installed when using `uv run`.

---

## 📂 File Structure

```
aruco-laser-generator/
├── generate_aruco_laser.py    # Main script
├── requirements.txt            # Dependencies
├── README.md                   # This file
├── QUICKSTART.md              # Quick reference
└── examples/                   # Example outputs
    ├── aruco_3mm_all50.pdf    # Compact 3mm markers
    ├── final_demo.pdf          # Standard demo
    └── example_no_labels.pdf   # No-label example
```

---

## 🎯 Example Workflows

### For Robotics/Computer Vision Projects
```bash
# Generate 25 medium markers with labels for easy identification
uv run generate_aruco_laser.py -r 0 24 -s 15 --spacing 30 -o robot_markers.pdf
```

### For Board Game Pieces
```bash
# Generate 10 small markers without labels for clean look
uv run generate_aruco_laser.py -r 0 9 -s 5 --spacing 3 --no-labels -o game_markers.pdf
```

### For Warehouse/Asset Tracking
```bash
# Generate 100 large durable markers from 5X5 dictionary
uv run generate_aruco_laser.py --dict 5X5_100 -r 0 99 -s 25 -b 2 -o warehouse_markers.pdf
```

### For Drone Landing Pads
```bash
# Generate large high-contrast markers
uv run generate_aruco_laser.py -i 0 -s 200 -b 10 --spacing 50 -o landing_pad.pdf
```

---

## 🤝 Contributing

Suggestions and improvements welcome! This is a practical tool designed for real-world laser cutting workflows.

---

## 📖 Citation

If you use this software in your research or projects, please cite it:

### BibTeX
```bibtex
@software{kaushik2024aruco,
  author = {Kaushik, Pavan Kumar},
  title = {ArUco Marker Generator for Laser Cutting},
  version = {1.0.0},
  year = {2024},
  license = {MIT},
  url = {https://github.com/pavankaushik/aruco-laser-generator},
  abstract = {A Python tool for generating clean, optimized ArUco markers specifically designed for laser cutting and engraving. Produces vector-based PDF output with color-coded layers (blue for engraving, red for cutting) that work seamlessly with laser cutting software like Lightburn.}
}
```

### APA Style
```
Kaushik, P. K. (2024). ArUco Marker Generator for Laser Cutting (Version 1.0.0) [Computer software]. 
https://github.com/pavankaushik/aruco-laser-generator
```

### Citation File Format
A `CITATION.cff` file is included in this repository for automatic citation generation. GitHub and many academic tools can automatically generate citations from this file.

### Getting a DOI (Optional but Recommended)
For better discoverability and citation tracking, consider publishing a release to [Zenodo](https://zenodo.org/):
1. Create a GitHub release
2. Connect your GitHub repository to Zenodo
3. Zenodo will automatically assign a DOI to each release
4. Update the `CITATION.cff` file with your DOI

This makes your work more discoverable in Google Scholar and other academic databases.

---

## 📄 License

MIT License - Free to use and modify for your projects!

---

## ✨ Credits

**Created by:** Pavan Kumar Kaushik

**Why this tool exists:** Online ArUco generators often produce pixelated, bloated files. This generator creates clean vector output at the logical grid level, perfect for laser cutters.

---

## 🔗 Quick Links

- **uv documentation**: https://docs.astral.sh/uv/
- **OpenCV ArUco**: https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html
- **Lightburn**: https://lightburnsoftware.com/

---

**Need help?** Run `uv run generate_aruco_laser.py --help` for all options!
