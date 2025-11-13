# Quick Start Guide

## 🚀 Installation (One Command!)

```bash
# Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

That's it! No need to manually install dependencies.

---

## ⚡ Quick Commands

All commands use `uv run` which automatically handles dependencies:

### 1. Generate First 10 Markers (Testing)
```bash
uv run generate_aruco_laser.py -r 0 9
```

### 2. Compact 3mm Markers (Dense Array)
```bash
uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels
```

### 3. Standard 12mm Markers
```bash
uv run generate_aruco_laser.py -r 0 20 -s 12 --spacing 25
```

### 4. Specific Markers for Your Project
```bash
uv run generate_aruco_laser.py -i 0 5 10 15 20
```

### 5. Different Dictionary (More Unique Markers)
```bash
uv run generate_aruco_laser.py --dict 5X5_100 -r 0 50
```

### 6. Without Labels (Cleaner Look)
```bash
uv run generate_aruco_laser.py -r 0 10 --no-labels
```

### 7. Large High-Visibility Markers
```bash
uv run generate_aruco_laser.py -r 0 10 -s 25 -b 2 --spacing 40
```

### 8. Production Run (All Options)
```bash
uv run generate_aruco_laser.py --dict 6X6_250 -r 0 100 -s 20 -b 2 --spacing 30 -o production.pdf
```

---

## 🔥 In Lightburn (Quick Setup)

1. **Import PDF** → Your generated file
2. **Layers auto-assigned by color:**
   - Blue → Engraving (Fill mode)
   - Red → Cutting (Line mode)
3. **Set power/speed** for your material
4. **Test on scrap** first!
5. **Run your job** ✨

---

## 📏 Recommended Starting Settings

| Setting | Value | Why |
|---------|-------|-----|
| Marker Size | 10-15mm | Good balance |
| Border | 0.5-1mm | Clean edges |
| Spacing | 20-30mm | Easy separation |
| Dictionary | 4X4_50 | Enough for most |

---

## 💡 Quick Tips

**Need compact markers?** → Use 3-5mm size, 2-5mm spacing  
**Need high visibility?** → Use 20-30mm size, 40-50mm spacing  
**Need many unique markers?** → Use 5X5_100 or 6X6_250 dictionary  
**Want clean look?** → Add `--no-labels` flag  

---

## 🆘 Need Help?

```bash
# See all options
uv run generate_aruco_laser.py --help

# Check uv is installed
uv --version
```

---

## 🎯 Common Use Cases

**Robot Vision:**
```bash
uv run generate_aruco_laser.py -r 0 24 -s 15 -o robot_markers.pdf
```

**Board Game:**
```bash
uv run generate_aruco_laser.py -r 0 9 -s 5 --spacing 3 --no-labels -o game.pdf
```

**Asset Tracking:**
```bash
uv run generate_aruco_laser.py --dict 5X5_250 -r 0 99 -s 25 -b 2 -o assets.pdf
```

---

**That's it!** Just use `uv run` before any command and it handles everything! 🎉
