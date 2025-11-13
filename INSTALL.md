# Installation & Setup Guide

This guide covers installation using UV (recommended) and traditional pip methods.

## Table of Contents
- [Quick Install with UV](#quick-install-with-uv)
- [Traditional Install with pip](#traditional-install-with-pip)
- [Verify Installation](#verify-installation)
- [First Run](#first-run)
- [Troubleshooting](#troubleshooting)

---

## Quick Install with UV

[UV](https://github.com/astral-sh/uv) is a blazingly fast Python package installer and resolver. It's the recommended way to install this tool.

### 1. Install UV

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (with pip):**
```bash
pip install uv
```

### 2. Create Project Directory

```bash
mkdir aruco-laser-generator
cd aruco-laser-generator
```

### 3. Copy Files

Place these files in your directory:
- `generate_aruco_laser.py`
- `pyproject.toml`

### 4. Install Dependencies with UV

```bash
# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

Or install dependencies directly from pyproject.toml:
```bash
uv pip install -e .
```

### 5. Run the Generator

```bash
python generate_aruco_laser.py --help
```

---

## Traditional Install with pip

If you prefer using pip instead of UV:

### 1. Ensure Python 3.8+ is Installed

```bash
python3 --version
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install opencv-python numpy reportlab
```

Or using requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Run the Generator

```bash
python generate_aruco_laser.py --help
```

---

## Verify Installation

Test that everything is working:

```bash
# Generate a test marker
python generate_aruco_laser.py -i 0 -o test.pdf

# Check that test.pdf was created
ls -lh test.pdf  # On Windows: dir test.pdf
```

You should see a `test.pdf` file created with one ArUco marker.

---

## First Run

Generate your first set of markers:

```bash
# Generate 10 markers for testing
python generate_aruco_laser.py -r 0 9 -s 10 -o my_first_markers.pdf
```

Open `my_first_markers.pdf` to see your markers!

**What you should see:**
- Blue filled squares (engraving areas)
- Red outer borders (cutting lines)
- Marker IDs labeled below each marker

---

## Common Commands

### Generate All 50 Markers (4X4_50 Dictionary)
```bash
python generate_aruco_laser.py --dict 4X4_50 -o all_markers.pdf
```

### Generate with Custom Size (3mm)
```bash
python generate_aruco_laser.py -s 3 --spacing 2 --no-labels -o small_markers.pdf
```

### Generate Specific IDs
```bash
python generate_aruco_laser.py -i 0 5 10 15 20 -o specific_markers.pdf
```

### Use Different Dictionary
```bash
python generate_aruco_laser.py --dict 5X5_100 -r 0 50 -o 5x5_markers.pdf
```

---

## Troubleshooting

### ImportError: No module named 'cv2'

**Problem:** OpenCV is not installed.

**Solution:**
```bash
# With UV
uv pip install opencv-python

# With pip
pip install opencv-python
```

### Command not found: python

**Problem:** Python is not in your PATH or it's called `python3`.

**Solution:**
Try using `python3` instead:
```bash
python3 generate_aruco_laser.py --help
```

### Virtual Environment Issues

**Problem:** Can't activate virtual environment.

**Solution:**

**Linux/macOS:**
```bash
source venv/bin/activate  # or .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

If PowerShell gives an error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### UV Not Found After Installation

**Problem:** UV command not found after installation.

**Solution:**
Restart your terminal or run:
```bash
source ~/.bashrc  # or ~/.zshrc on macOS
```

### PDF Output Issues

**Problem:** PDF is created but looks wrong.

**Solution:**
1. Check that you're using the correct command-line options
2. Try different marker sizes: `-s 10` or `-s 15`
3. Ensure you're opening the PDF with a proper PDF viewer (not a text editor)

### Permission Denied

**Problem:** Can't write output file.

**Solution:**
```bash
# Check write permissions in current directory
ls -la

# Or specify a different output directory
python generate_aruco_laser.py -o ~/Desktop/markers.pdf
```

---

## System Requirements

- **Python:** 3.8 or higher
- **Operating System:** Windows, macOS, Linux
- **RAM:** 512 MB minimum
- **Disk Space:** 100 MB for dependencies

---

## Dependencies

This project requires:

| Package | Version | Purpose |
|---------|---------|---------|
| opencv-python | ≥4.5.0 | ArUco marker generation |
| numpy | ≥1.19.0 | Array operations |
| reportlab | ≥3.6.0 | PDF generation |

---

## Next Steps

Once installed, check out:

1. **[QUICKSTART.md](QUICKSTART.md)** - Common usage patterns
2. **[README.md](README.md)** - Complete documentation
3. **[USER_GUIDE.md](USER_GUIDE.md)** - Detailed usage guide

---

## Getting Help

If you encounter issues not covered here:

1. Check that all dependencies are installed: `uv pip list` or `pip list`
2. Verify Python version: `python --version` (should be 3.8+)
3. Try running with verbose output: `python -v generate_aruco_laser.py`
4. Review the error message carefully

---

## Updating

### With UV
```bash
uv pip install --upgrade opencv-python numpy reportlab
```

### With pip
```bash
pip install --upgrade opencv-python numpy reportlab
```
