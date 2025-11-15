---
layout: default
title: ArUco Marker Generator for Laser Cutting
---

<div style="text-align: center; margin: 2rem 0;">

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17613883.svg)](https://doi.org/10.5281/zenodo.17613883)

<h2 style="font-weight: 300; color: #666; margin-top: 1rem;">Generate clean, optimized ArUco markers specifically designed for laser cutting and engraving</h2>

</div>

---

## Overview

A Python tool that generates ArUco markers optimized for laser cutting with color-coded layers:
- **Blue (RGB: 0,0,255)** - Engraving layer (filled squares)
- **Red (RGB: 255,0,0)** - Cutting layer (outer border)

Perfect for use with Lightburn, RDWorks, and other laser cutting software.

---

## Quick Start

### With UV (Recommended)

```bash
# Install UV (one-time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Generate markers
uv run generate_aruco_laser.py -r 0 9
```

### With pip

```bash
pip install opencv-python numpy reportlab
python generate_aruco_laser.py -r 0 9
```

---

## Key Features

- ✅ **Clean Vector Output** - Logical grid level generation (no pixelation)
- ✅ **Color-Coded Layers** - Automatic layer assignment for laser software
- ✅ **Multiple Dictionaries** - Support for 4×4, 5×5, 6×6, and 7×7 ArUco dictionaries
- ✅ **Flexible Configuration** - Customize size, spacing, borders, page size, and grid layout
- ✅ **Batch Generation** - Generate specific IDs, ranges, or entire dictionaries
- ✅ **Optional Labels** - Toggle marker ID labels on/off

---

## Example Outputs

The repository includes **25 comprehensive example PDFs** demonstrating all parameters and use cases.

### Preview

<div style="text-align: center; margin: 2rem 0;">

<table style="margin: 0 auto; border: none; width: 100%; max-width: 900px;">
<tr style="border: none;">
<td style="border: none; padding: 15px; text-align: center; vertical-align: top;">
<a href="../examples/01_standard_10mm_with_labels.pdf">
<img src="{{ '/assets/previews/01_standard_10mm_with_labels_preview.png' | relative_url }}" width="200" alt="Standard 10mm markers" style="border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.2s;">
</a><br/>
<strong style="display: block; margin-top: 10px;">Standard 10mm</strong>
<small style="color: #666;">With labels</small>
</td>
<td style="border: none; padding: 15px; text-align: center; vertical-align: top;">
<a href="../examples/05_compact_3mm_dense.pdf">
<img src="{{ '/assets/previews/05_compact_3mm_dense_preview.png' | relative_url }}" width="200" alt="Compact 3mm markers" style="border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.2s;">
</a><br/>
<strong style="display: block; margin-top: 10px;">Compact 3mm</strong>
<small style="color: #666;">Dense layout</small>
</td>
<td style="border: none; padding: 15px; text-align: center; vertical-align: top;">
<a href="../examples/18_custom_grid_5x5.pdf">
<img src="{{ '/assets/previews/18_custom_grid_5x5_preview.png' | relative_url }}" width="200" alt="Custom grid layout" style="border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.2s;">
</a><br/>
<strong style="display: block; margin-top: 10px;">Custom 5×5</strong>
<small style="color: #666;">Grid layout</small>
</td>
<td style="border: none; padding: 15px; text-align: center; vertical-align: top;">
<a href="../examples/24_production_standard.pdf">
<img src="{{ '/assets/previews/24_production_standard_preview.png' | relative_url }}" width="200" alt="Production standard" style="border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); transition: transform 0.2s;">
</a><br/>
<strong style="display: block; margin-top: 10px;">Production</strong>
<small style="color: #666;">12mm standard</small>
</td>
</tr>
</table>

<p style="margin-top: 1.5rem; color: #666; font-style: italic;">Click images to view full PDF examples</p>

</div>

**All examples demonstrate:**
- Different marker sizes (3mm to 50mm)
- Various border widths (0.5mm to 3mm)
- Different spacing options (2mm to 40mm)
- All dictionary types (4×4, 5×5, 6×6, 7×7)
- Custom grid layouts
- Page size variations (A4 and Letter)

View all examples in the [`examples/`](../examples/) directory.

---

## Documentation

### Getting Started
- **[Installation Guide](../INSTALL.md)** - Set up the tool on your system
- **[Quick Start Guide](../QUICKSTART.md)** - Get up and running in 5 minutes
- **[User Guide](../USER_GUIDE.md)** - Complete reference manual

### Examples & Reference
- **[Example Outputs](../examples/)** - 25 comprehensive example PDFs
- **[Documentation Index](../DOCS_INDEX.md)** - Complete documentation map

---

## Usage Examples

```bash
# Generate standard 10mm markers
uv run generate_aruco_laser.py -r 0 9 -s 10

# Generate compact 3mm markers, dense layout
uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels

# Custom grid layout
uv run generate_aruco_laser.py --nrows 5 --ncols 4 -r 0 19

# Different dictionary
uv run generate_aruco_laser.py --dict 5X5_100 -r 0 20
```

---

## Citation

**DOI:** [10.5281/zenodo.17613883](https://doi.org/10.5281/zenodo.17613883)

If you use this software in your research, please cite it:

```bibtex
@software{kaushik2024aruco,
  author = {Kaushik, Pavan Kumar},
  title = {ArUco Marker Generator for Laser Cutting},
  version = {1.0.0},
  year = {2024},
  doi = {10.5281/zenodo.17613883},
  url = {https://github.com/pavankaushik/aruco-laser-generator}
}
```

---

## Requirements

- Python 3.8 or higher
- opencv-python >= 4.8.0
- numpy >= 1.24.0
- reportlab >= 4.0.0

---

## License

MIT License - Free to use and modify for your projects!

---

## Links

- **Repository**: [GitHub](https://github.com/pavankaushik/aruco-laser-generator)
- **DOI**: [10.5281/zenodo.17613883](https://doi.org/10.5281/zenodo.17613883)
- **OpenCV ArUco**: [Documentation](https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html)
