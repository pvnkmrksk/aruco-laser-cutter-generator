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

The repository includes **25 comprehensive example PDFs** demonstrating all parameters and use cases. All examples are located in the [`examples/`](examples/) directory.

### Quick Preview by Category

<details>
<summary><b>Click to view all example categories</b></summary>

#### Standard Configurations
- **[01_standard_10mm_with_labels.pdf](examples/01_standard_10mm_with_labels.pdf)** - All 50 markers with ID labels (25 per page)
- **[02_standard_10mm_no_labels.pdf](examples/02_standard_10mm_no_labels.pdf)** - All 50 markers without labels

#### Page Size Variations
- **[03_letter_page_size.pdf](examples/03_letter_page_size.pdf)** - Letter page size, 30 markers per page
- **[04_a4_page_size.pdf](examples/04_a4_page_size.pdf)** - A4 page size, 25 markers per page

#### Marker Size Variations
- **[05_compact_3mm_dense.pdf](examples/05_compact_3mm_dense.pdf)** - 3mm markers, maximum density (50 per page)
- **[06_medium_15mm_standard.pdf](examples/06_medium_15mm_standard.pdf)** - 15mm markers, standard production
- **[07_large_25mm_high_visibility.pdf](examples/07_large_25mm_high_visibility.pdf)** - 25mm markers, long-range detection

#### Border Width Variations
- **[08_minimal_border_0.5mm.pdf](examples/08_minimal_border_0.5mm.pdf)** - 0.5mm border, most compact
- **[09_standard_border_1mm.pdf](examples/09_standard_border_1mm.pdf)** - 1mm border, recommended
- **[10_thick_border_3mm.pdf](examples/10_thick_border_3mm.pdf)** - 3mm border, high contrast

#### Spacing Variations
- **[11_tight_spacing_5mm.pdf](examples/11_tight_spacing_5mm.pdf)** - 5mm spacing, maximum density
- **[12_standard_spacing_20mm.pdf](examples/12_standard_spacing_20mm.pdf)** - 20mm spacing, easy cutting
- **[13_generous_spacing_40mm.pdf](examples/13_generous_spacing_40mm.pdf)** - 40mm spacing, easy handling

#### Dictionary Types
- **[14_4x4_dictionary_50_markers.pdf](examples/14_4x4_dictionary_50_markers.pdf)** - 4×4 dictionary, 50 markers
- **[15_5x5_dictionary_100_markers.pdf](examples/15_5x5_dictionary_100_markers.pdf)** - 5×5 dictionary, 100 markers
- **[16_6x6_dictionary_250_markers.pdf](examples/16_6x6_dictionary_250_markers.pdf)** - 6×6 dictionary, maximum reliability
- **[17_7x7_dictionary_sample.pdf](examples/17_7x7_dictionary_sample.pdf)** - 7×7 dictionary, extreme conditions

#### Custom Grid Layouts
- **[18_custom_grid_5x5.pdf](examples/18_custom_grid_5x5.pdf)** - 5×5 grid layout
- **[19_custom_grid_4x6.pdf](examples/19_custom_grid_4x6.pdf)** - 4×6 grid layout
- **[20_custom_grid_10x2.pdf](examples/20_custom_grid_10x2.pdf)** - 10×2 vertical strip
- **[21_custom_grid_2x10.pdf](examples/21_custom_grid_2x10.pdf)** - 2×10 horizontal strip

#### Special Use Cases
- **[22_specific_markers_selected.pdf](examples/22_specific_markers_selected.pdf)** - Specific marker IDs selected
- **[23_single_marker_large.pdf](examples/23_single_marker_large.pdf)** - Single 50mm marker for testing
- **[24_production_standard.pdf](examples/24_production_standard.pdf)** - Production standard configuration
- **[25_production_compact.pdf](examples/25_production_compact.pdf)** - Production compact configuration

</details>

### Complete Example Reference

| # | Example | Key Parameters | Use Case |
|---|---------|----------------|----------|
| 01 | [standard_10mm_with_labels.pdf](examples/01_standard_10mm_with_labels.pdf) | 10mm, labels, 25/page | Learning, identification |
| 02 | [standard_10mm_no_labels.pdf](examples/02_standard_10mm_no_labels.pdf) | 10mm, no labels, 25/page | Clean production |
| 03 | [letter_page_size.pdf](examples/03_letter_page_size.pdf) | Letter page, 30/page | US paper size |
| 04 | [a4_page_size.pdf](examples/04_a4_page_size.pdf) | A4 page, 25/page | International standard |
| 05 | [compact_3mm_dense.pdf](examples/05_compact_3mm_dense.pdf) | 3mm, 50/page, dense | Maximum density |
| 06 | [medium_15mm_standard.pdf](examples/06_medium_15mm_standard.pdf) | 15mm, 16/page | Standard production |
| 07 | [large_25mm_high_visibility.pdf](examples/07_large_25mm_high_visibility.pdf) | 25mm, 9/page | Long-range detection |
| 08 | [minimal_border_0.5mm.pdf](examples/08_minimal_border_0.5mm.pdf) | 0.5mm border | Most compact |
| 09 | [standard_border_1mm.pdf](examples/09_standard_border_1mm.pdf) | 1mm border | Recommended |
| 10 | [thick_border_3mm.pdf](examples/10_thick_border_3mm.pdf) | 3mm border | High contrast |
| 11 | [tight_spacing_5mm.pdf](examples/11_tight_spacing_5mm.pdf) | 5mm spacing | Maximum density |
| 12 | [standard_spacing_20mm.pdf](examples/12_standard_spacing_20mm.pdf) | 20mm spacing | Easy cutting |
| 13 | [generous_spacing_40mm.pdf](examples/13_generous_spacing_40mm.pdf) | 40mm spacing | Easy handling |
| 14 | [4x4_dictionary_50_markers.pdf](examples/14_4x4_dictionary_50_markers.pdf) | 4×4 dict, 50 markers | Compact markers |
| 15 | [5x5_dictionary_100_markers.pdf](examples/15_5x5_dictionary_100_markers.pdf) | 5×5 dict, 100 markers | Better reliability |
| 16 | [6x6_dictionary_250_markers.pdf](examples/16_6x6_dictionary_250_markers.pdf) | 6×6 dict, 100 shown | Maximum reliability |
| 17 | [7x7_dictionary_sample.pdf](examples/17_7x7_dictionary_sample.pdf) | 7×7 dict, 25 markers | Extreme conditions |
| 18 | [custom_grid_5x5.pdf](examples/18_custom_grid_5x5.pdf) | 5×5 grid layout | Square grid |
| 19 | [custom_grid_4x6.pdf](examples/19_custom_grid_4x6.pdf) | 4×6 grid layout | Wide grid |
| 20 | [custom_grid_10x2.pdf](examples/20_custom_grid_10x2.pdf) | 10×2 grid layout | Vertical strip |
| 21 | [custom_grid_2x10.pdf](examples/21_custom_grid_2x10.pdf) | 2×10 grid layout | Horizontal strip |
| 22 | [specific_markers_selected.pdf](examples/22_specific_markers_selected.pdf) | Selected IDs | Specific markers |
| 23 | [single_marker_large.pdf](examples/23_single_marker_large.pdf) | Single 50mm marker | Testing/calibration |
| 24 | [production_standard.pdf](examples/24_production_standard.pdf) | 12mm, 1.5mm border | Production ready |
| 25 | [production_compact.pdf](examples/25_production_compact.pdf) | 8mm, optimized | Space optimized |

> **💡 Tip:** Click any PDF link above to view it directly in GitHub. All examples demonstrate the clean vector output with color-coded layers (Blue=engraving, Red=cutting).

### Output Features

All generated PDFs include:
- ✅ **Clean vector graphics** - No pixelation, perfect for laser cutting
- ✅ **Color-coded layers** - Blue (RGB: 0,0,255) for engraving, Red (RGB: 255,0,0) for cutting
- ✅ **Precise spacing** - Consistent gaps between markers for easy cutting
- ✅ **Optional labels** - Marker IDs can be shown or hidden
- ✅ **Multiple dictionaries** - Support for 4×4, 5×5, 6×6, and 7×7 ArUco dictionaries

### Regenerating Examples

To regenerate all examples with the latest script:

```bash
python generate_examples.py
```

This will create all example PDFs in the `examples/` directory with consistent naming.

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
├── generate_examples.py       # Script to regenerate all examples
├── generate_previews.py       # Script to generate preview images (optional)
├── requirements.txt            # Dependencies
├── pyproject.toml             # Package configuration
├── CITATION.cff               # Citation file for academic use
│
├── README.md                   # Project overview (this file)
├── INSTALL.md                 # Installation guide
├── QUICKSTART.md              # Quick start guide
├── USER_GUIDE.md              # Complete user manual
├── DOCS_INDEX.md              # Documentation index
│
├── examples/                   # Example PDFs
│   ├── README.md              # Example descriptions
│   ├── 01_standard_10mm_with_labels.pdf
│   ├── 02_standard_10mm_no_labels.pdf
│   ├── 03_compact_3mm_all50.pdf
│   └── ... (10 total examples)
│
└── docs/                      # GitHub Pages documentation
    ├── index.md               # GitHub Pages homepage
    └── _config.yml            # Jekyll configuration
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

## 📚 Documentation

Comprehensive documentation is available:

- **[Installation Guide](INSTALL.md)** - Detailed setup instructions
- **[Quick Start Guide](QUICKSTART.md)** - Get started in 5 minutes
- **[User Guide](USER_GUIDE.md)** - Complete reference manual
- **[Documentation Index](DOCS_INDEX.md)** - Navigate all documentation
- **[Examples](examples/)** - View all example outputs

### GitHub Pages

Documentation is also available via GitHub Pages (if enabled):
- Visit your repository's GitHub Pages URL (e.g., `https://yourusername.github.io/aruco-laser-generator/`)
- Or view the docs locally in the [`docs/`](docs/) directory

---

## 🔗 External Links

- **uv documentation**: https://docs.astral.sh/uv/
- **OpenCV ArUco**: https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html
- **Lightburn**: https://lightburnsoftware.com/

---

**Need help?** Run `uv run generate_aruco_laser.py --help` for all options!
