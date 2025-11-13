# ArUco Marker Generator for Laser Cutting

Welcome to the complete documentation for the ArUco Marker Generator.

## 📚 Documentation Overview

This documentation is organized into several sections:

### Getting Started
- **[Installation Guide](../INSTALL.md)** - Set up the tool on your system
- **[Quick Start Guide](../QUICKSTART.md)** - Get up and running in 5 minutes
- **[User Guide](../USER_GUIDE.md)** - Complete reference manual

### Examples
- **[Example Outputs](../examples/)** - View all example PDFs
- **[Example README](../examples/README.md)** - Detailed example descriptions

### Reference
- **[Documentation Index](../DOCS_INDEX.md)** - Complete documentation map
- **[README](../README.md)** - Project overview and features

## 🚀 Quick Start

### Installation (UV - Recommended)

```bash
# Install UV (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Generate your first markers
uv run generate_aruco_laser.py -r 0 9
```

### Installation (Traditional)

```bash
# Install dependencies
pip install opencv-python numpy reportlab

# Generate markers
python generate_aruco_laser.py -r 0 9
```

## 🎯 Common Use Cases

### Generate Standard Markers
```bash
uv run generate_aruco_laser.py -r 0 9 -s 10
```

### Generate Compact Markers
```bash
uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels
```

### Custom Grid Layout
```bash
uv run generate_aruco_laser.py --nrows 5 --ncols 4 -r 0 19
```

## 📖 Documentation Structure

```
aruco-laser-generator/
├── README.md              # Project overview
├── INSTALL.md             # Installation guide
├── QUICKSTART.md          # Quick start guide
├── USER_GUIDE.md          # Complete user manual
├── DOCS_INDEX.md          # Documentation index
├── examples/              # Example PDFs
│   ├── README.md          # Example descriptions
│   └── *.pdf              # Example files
└── docs/                  # GitHub Pages (this directory)
    └── index.md           # This file
```

## 🔗 Quick Links

- **Installation**: [INSTALL.md](../INSTALL.md)
- **Quick Start**: [QUICKSTART.md](../QUICKSTART.md)
- **Full Guide**: [USER_GUIDE.md](../USER_GUIDE.md)
- **Examples**: [examples/](../examples/)
- **Documentation Index**: [DOCS_INDEX.md](../DOCS_INDEX.md)

## 💡 Key Features

- ✅ Clean vector output (no pixelation)
- ✅ Color-coded layers (Blue=engraving, Red=cutting)
- ✅ Multiple ArUco dictionaries (4×4, 5×5, 6×6, 7×7)
- ✅ Flexible sizing and spacing
- ✅ Custom grid layouts
- ✅ Optional ID labels

## 📄 License

MIT License - Free to use and modify for your projects!

## 👤 Author

**Pavan Kumar Kaushik**

For citation information, see the [main README](../README.md#-citation).

---

**Need help?** Check the [Documentation Index](../DOCS_INDEX.md) or [User Guide](../USER_GUIDE.md).

