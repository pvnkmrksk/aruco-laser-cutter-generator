# ArUco Laser Generator - Documentation Index

Complete documentation package for generating ArUco markers for laser cutting.

## 📦 Package Contents

### Core Files
- **`generate_aruco_laser.py`** - Main script for generating ArUco markers
- **`pyproject.toml`** - UV/pip package configuration
- **`requirements.txt`** - Python dependencies list

### Documentation Files

#### Getting Started (Read First!)
1. **[INSTALL.md](INSTALL.md)** - Installation & Setup Guide
   - UV installation (recommended)
   - pip installation (traditional)
   - Troubleshooting
   - System requirements

2. **[QUICKSTART.md](QUICKSTART.md)** - Quick Start Guide
   - Common commands
   - 5-minute getting started
   - Basic examples

#### Complete Reference
3. **[USER_GUIDE.md](USER_GUIDE.md)** - Complete User Guide (⭐ Most Comprehensive)
   - All command-line options
   - Dictionary selection guide
   - Sizing guidelines
   - Laser cutter setup (Lightburn, RDWorks, etc.)
   - Real-world examples
   - Best practices
   - FAQ

4. **[README.md](README.md)** - Project Overview
   - Features overview
   - Quick examples
   - Available dictionaries table
   - Tips and troubleshooting

### Example Outputs
- **`aruco_3mm_all.pdf`** - All 50 markers from 4X4_50 (3mm size, 2mm spacing, no labels)
- **`final_demo.pdf`** - Demo with 10 markers (12mm size, 25mm spacing)
- **`example_5x5_markers.pdf`** - Example using 5X5 dictionary
- **`example_no_labels.pdf`** - Example without ID labels

---

## 📖 Documentation Map

### For New Users
1. Start with **[INSTALL.md](INSTALL.md)** to get set up
2. Try examples from **[QUICKSTART.md](QUICKSTART.md)**
3. Reference **[USER_GUIDE.md](USER_GUIDE.md)** for details

### For Quick Reference
- Command syntax → **[QUICKSTART.md](QUICKSTART.md)**
- Laser setup → **[USER_GUIDE.md](USER_GUIDE.md)** (Laser Cutter Setup section)
- Troubleshooting → **[INSTALL.md](INSTALL.md)** (Troubleshooting section)

### For In-Depth Usage
- Complete options → **[USER_GUIDE.md](USER_GUIDE.md)**
- Best practices → **[USER_GUIDE.md](USER_GUIDE.md)** (Best Practices section)
- Real examples → **[USER_GUIDE.md](USER_GUIDE.md)** (Real-World Examples section)

---

## 🚀 Quick Setup

### With UV (Recommended - Fast!)

```bash
# 1. Install UV (once)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# 2. Generate markers (UV handles dependencies automatically!)
uv run generate_aruco_laser.py -r 0 9
```

### With pip (Traditional)

```bash
# 1. Install dependencies
pip install opencv-python numpy reportlab

# 2. Generate markers
python generate_aruco_laser.py -r 0 9
```

**See [INSTALL.md](INSTALL.md) for detailed instructions**

---

## 📋 Common Use Cases

| What You Want | Command | Documentation |
|---------------|---------|---------------|
| Install the tool | See setup commands above | [INSTALL.md](INSTALL.md) |
| Generate first markers | `python generate_aruco_laser.py -r 0 9` | [QUICKSTART.md](QUICKSTART.md) |
| All 50 markers, 3mm, compact | `python generate_aruco_laser.py -s 3 --spacing 2 --no-labels` | [USER_GUIDE.md](USER_GUIDE.md) |
| Custom size (15mm) | `python generate_aruco_laser.py -s 15 -r 0 20` | [USER_GUIDE.md](USER_GUIDE.md) |
| Different dictionary | `python generate_aruco_laser.py --dict 5X5_100` | [USER_GUIDE.md](USER_GUIDE.md) - Dictionary Guide |
| Setup laser cutter | Configure layers in Lightburn | [USER_GUIDE.md](USER_GUIDE.md) - Laser Setup |
| Fix issues | Check error messages | [INSTALL.md](INSTALL.md) - Troubleshooting |

---

## 🎯 Typical Workflow

### 1. Installation (One Time)
Follow **[INSTALL.md](INSTALL.md)**

### 2. Generate Markers
Choose your command from **[QUICKSTART.md](QUICKSTART.md)** or **[USER_GUIDE.md](USER_GUIDE.md)**

### 3. Import to Laser Software
See **[USER_GUIDE.md](USER_GUIDE.md)** - "Laser Cutter Setup" section

### 4. Cut/Engrave
- Blue = Engraving (Fill mode)
- Red = Cutting (Line mode)

---

## 📚 Documentation Quick Links

### By Task

**Installing:**
→ [INSTALL.md](INSTALL.md)

**Learning the basics:**
→ [QUICKSTART.md](QUICKSTART.md)

**Understanding all options:**
→ [USER_GUIDE.md](USER_GUIDE.md) - Command Reference

**Choosing marker size:**
→ [USER_GUIDE.md](USER_GUIDE.md) - Sizing Guidelines

**Choosing dictionary:**
→ [USER_GUIDE.md](USER_GUIDE.md) - Dictionary Selection Guide

**Setting up Lightburn:**
→ [USER_GUIDE.md](USER_GUIDE.md) - Laser Cutter Setup

**Troubleshooting:**
→ [INSTALL.md](INSTALL.md) - Troubleshooting
→ [USER_GUIDE.md](USER_GUIDE.md) - Best Practices

**Real-world examples:**
→ [USER_GUIDE.md](USER_GUIDE.md) - Real-World Examples

---

## 🆘 Getting Help

### Error Messages
1. Check **[INSTALL.md](INSTALL.md)** - Troubleshooting section
2. Verify dependencies are installed: `uv pip list` or `pip list`
3. Check Python version: `python --version` (needs 3.8+)

### Usage Questions
1. Check **[USER_GUIDE.md](USER_GUIDE.md)** - FAQ section
2. Review examples in **[USER_GUIDE.md](USER_GUIDE.md)** - Real-World Examples
3. Try variations of commands from **[QUICKSTART.md](QUICKSTART.md)**

### Laser Settings
1. See **[USER_GUIDE.md](USER_GUIDE.md)** - Laser Cutter Setup
2. Start with test markers (generate just 1-3 markers)
3. Adjust power/speed based on material

---

## 🔄 Updating

### With UV
```bash
uv pip install --upgrade opencv-python numpy reportlab
```

### With pip
```bash
pip install --upgrade opencv-python numpy reportlab
```

---

## 📊 File Size Reference

| File Type | Description | Typical Size |
|-----------|-------------|--------------|
| Python script | Main generator | ~15 KB |
| PDF (10 markers) | Typical output | ~50-100 KB |
| PDF (50 markers) | Full dictionary | ~200-300 KB |
| Documentation | All .md files | ~100 KB total |

---

## ✅ Complete Documentation Checklist

- [x] Installation guide (UV and pip)
- [x] Quick start examples
- [x] Complete user guide
- [x] Command reference
- [x] Dictionary selection guide
- [x] Sizing guidelines
- [x] Laser cutter setup instructions
- [x] Real-world examples
- [x] Best practices
- [x] Troubleshooting
- [x] FAQ
- [x] Example PDFs

---

## 📝 Version Info

- **Script Version:** 1.0.0
- **Documentation Updated:** 2024
- **Python Required:** 3.8+
- **Dependencies:** opencv-python, numpy, reportlab

---

## 🎉 You're All Set!

Choose where to start:
- **New to this?** → [INSTALL.md](INSTALL.md)
- **Want to start fast?** → [QUICKSTART.md](QUICKSTART.md)
- **Need details?** → [USER_GUIDE.md](USER_GUIDE.md)

Happy laser cutting! 🎯
