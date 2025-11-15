---
layout: default
title: Home
nav_order: 1
---

# ArUco Marker Generator for Laser Cutting

<div align="center">

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17613883.svg)](https://doi.org/10.5281/zenodo.17613883)

**Generate clean, optimized ArUco markers specifically designed for laser cutting and engraving**

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

## Documentation

### Getting Started
- **[Installation Guide](../INSTALL.md)** - Set up the tool on your system
- **[Quick Start Guide](../QUICKSTART.md)** - Get up and running in 5 minutes
- **[User Guide](../USER_GUIDE.md)** - Complete reference manual

### Examples & Reference
- **[Example Outputs](../examples/)** - 25 comprehensive example PDFs
- **[Documentation Index](../DOCS_INDEX.md)** - Complete documentation map

---

## Example Outputs

The repository includes **25 comprehensive example PDFs** demonstrating:
- Different marker sizes (3mm to 50mm)
- Various border widths (0.5mm to 3mm)
- Different spacing options (2mm to 40mm)
- All dictionary types (4×4, 5×5, 6×6, 7×7)
- Custom grid layouts
- Page size variations (A4 and Letter)

View all examples in the [`examples/`](../examples/) directory.

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
