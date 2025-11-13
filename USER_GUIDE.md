# User Guide

Complete guide to generating ArUco markers for laser cutting and engraving.

## Table of Contents
- [Understanding the Output](#understanding-the-output)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [Dictionary Selection Guide](#dictionary-selection-guide)
- [Sizing Guidelines](#sizing-guidelines)
- [Laser Cutter Setup](#laser-cutter-setup)
- [Real-World Examples](#real-world-examples)
- [Best Practices](#best-practices)

---

## Understanding the Output

### Color Coding

The generated PDF uses colors to indicate different laser operations:

| Color | RGB Values | Laser Operation | Purpose |
|-------|-----------|-----------------|---------|
| Blue | (0, 0, 255) | Engraving/Filling | The marker pattern squares |
| Red | (255, 0, 0) | Cutting | The outer border |
| Black | (0, 0, 0) | Reference only | Marker ID labels (optional) |

### File Structure

Each PDF page contains:
- A centered grid of markers
- Configurable spacing between markers
- Optional ID labels below each marker
- Clean vector graphics (no rasterization)

---

## Basic Usage

### Generate a Single Marker

```bash
python generate_aruco_laser.py -i 0
```

This creates `aruco_markers.pdf` with marker ID 0.

### Generate Multiple Specific Markers

```bash
python generate_aruco_laser.py -i 0 5 10 15 20
```

Generates markers with IDs 0, 5, 10, 15, and 20.

### Generate a Range of Markers

```bash
python generate_aruco_laser.py -r 0 9
```

Generates markers 0 through 9 (inclusive).

### Generate All Markers from Dictionary

```bash
python generate_aruco_laser.py
```

Generates all 50 markers from the default 4X4_50 dictionary.

---

## Advanced Usage

### Custom Marker Size

```bash
python generate_aruco_laser.py -s 15 -r 0 10
```

Creates 15mm × 15mm markers.

**Size recommendations:**
- **3mm**: Dense arrays, requires precise laser
- **5mm**: Compact, general purpose
- **10mm**: Standard size (default)
- **15mm**: Easy to detect, good for testing
- **20mm+**: Long-distance detection

### Adjust Spacing

```bash
python generate_aruco_laser.py --spacing 30 -r 0 20
```

Sets 30mm spacing between markers (default is 20mm).

**When to adjust:**
- **Small spacing (2-10mm)**: Maximize markers per page
- **Medium spacing (15-25mm)**: Standard use
- **Large spacing (30mm+)**: Easier cutting/handling

### Custom Border Width

```bash
python generate_aruco_laser.py -b 2 -s 20
```

Sets 2mm white border around each marker (default is 0.5mm).

**Border recommendations:**
- **0.5mm**: Minimal, space-efficient
- **1-2mm**: Recommended for clarity
- **3mm+**: High contrast, easier detection

### Remove ID Labels

```bash
python generate_aruco_laser.py --no-labels -r 0 10
```

Generates markers without ID numbers below them.

**When to use:**
- Cleaner appearance
- You're tracking IDs separately
- Limited space for labels

### Select Different Dictionary

```bash
python generate_aruco_laser.py --dict 5X5_100 -r 0 50
```

Uses 5×5 dictionary instead of default 4×4.

### Custom Output Filename

```bash
python generate_aruco_laser.py -o my_project_markers.pdf
```

### Page Size Options

```bash
python generate_aruco_laser.py --page-size letter
```

Choose between A4 (default) or letter size.

### Markers Per Page

```bash
python generate_aruco_laser.py -p 12 -s 20
```

Places 12 markers per page (default is 20). Useful for larger markers.

### Combine Options

```bash
python generate_aruco_laser.py \
  --dict 6X6_250 \
  -r 0 100 \
  -s 15 \
  -b 1.5 \
  --spacing 25 \
  --no-labels \
  --page-size A4 \
  -o production_batch_001.pdf
```

---

## Dictionary Selection Guide

### What Are ArUco Dictionaries?

ArUco dictionaries are sets of unique marker patterns. The naming convention is `{GRID_SIZE}X{GRID_SIZE}_{COUNT}`.

### Available Dictionaries

| Dictionary | Grid Size | Marker Count | Best For |
|------------|-----------|--------------|----------|
| **4X4_50** | 4×4 | 50 | Small projects, testing |
| **4X4_100** | 4×4 | 100 | Medium projects |
| **4X4_250** | 4×4 | 250 | Large projects |
| **4X4_1000** | 4×4 | 1000 | Very large projects |
| **5X5_50** | 5×5 | 50 | Better detection |
| **5X5_100** | 5×5 | 100 | Balanced choice |
| **5X5_250** | 5×5 | 250 | Production use |
| **5X5_1000** | 5×5 | 1000 | Industrial applications |
| **6X6_50** | 6×6 | 50 | Most robust detection |
| **6X6_100** | 6×6 | 100 | High reliability |
| **6X6_250** | 6×6 | 250 | Professional use |
| **6X6_1000** | 6×6 | 1000 | Maximum options |
| **7X7_50** | 7×7 | 50 | Maximum robustness |
| **7X7_100-1000** | 7×7 | 100-1000 | Extreme conditions |

### How to Choose

**Grid Size Considerations:**
- **4×4**: Smallest, fastest detection but less error correction
- **5×5**: Good balance of size and robustness
- **6×6**: Better error correction, slightly larger
- **7×7**: Maximum error correction, largest markers

**Marker Count Considerations:**
- **50**: Perfect for small projects, prototypes
- **100**: Good for most applications
- **250**: Large installations, multiple zones
- **1000**: Tracking many objects, scalability

**Example Scenarios:**

| Use Case | Recommended Dictionary |
|----------|----------------------|
| Robotics testing | 4X4_50 or 5X5_50 |
| Warehouse tracking | 5X5_250 or 6X6_250 |
| AR/VR calibration | 6X6_100 |
| Small parts identification | 4X4_100 |
| Outdoor use | 6X6_100 or 7X7_50 |
| Mass production | 5X5_1000 or 6X6_1000 |

---

## Sizing Guidelines

### Marker Size vs. Detection Distance

Detection distance is approximately **marker size × 50-100**.

| Marker Size | Detection Range | Best Use |
|-------------|----------------|----------|
| 3mm | 15-30cm | Tiny parts, dense arrays |
| 5mm | 25-50cm | Small objects |
| 10mm | 0.5-1m | Standard applications |
| 15mm | 0.75-1.5m | Robot navigation |
| 20mm | 1-2m | Room-scale tracking |
| 30mm | 1.5-3m | Large spaces |
| 50mm+ | 2.5m+ | Outdoor, far distances |

### Material Considerations

| Material | Recommendations |
|----------|----------------|
| **Acrylic** | 5-15mm, 1mm border |
| **Wood** | 10-20mm, 1.5mm border |
| **Metal** | 8-15mm, 1mm border |
| **Cardboard** | 10-30mm, 2mm border |
| **Paper** | 5-20mm, 0.5-1mm border |

### Density vs. Page Count

Calculate markers per page:
- Default: 20 markers per page (approximately)
- Larger markers = fewer per page
- Adjust with `-p` flag if needed

**Example:**
```bash
# 50mm markers won't fit 20 per page, reduce to 6
python generate_aruco_laser.py -s 50 -p 6 -r 0 20
```

---

## Laser Cutter Setup

### Lightburn Setup (Recommended)

1. **Import PDF**
   ```
   File → Import → Select your PDF
   ```

2. **Layer Assignment**
   - Lightburn will automatically separate colors into layers
   - Blue shapes → Layer 1 (engraving)
   - Red outlines → Layer 2 (cutting)

3. **Configure Blue Layer (Engraving)**
   ```
   Mode: Fill
   Speed: 300-500 mm/s (adjust for material)
   Power: 20-40% (adjust for material)
   Interval: 0.1mm (line spacing)
   ```

4. **Configure Red Layer (Cutting)**
   ```
   Mode: Line
   Speed: 10-20 mm/s (adjust for material)
   Power: 80-100% (adjust for material)
   Passes: 1-3 (depending on material thickness)
   ```

5. **Test Settings**
   - Always run a test on scrap material first
   - Fine-tune power and speed
   - Check focus is correct

### RDWorks Setup

1. Import PDF
2. Assign layers by color
3. Set engraving parameters (blue)
4. Set cutting parameters (red)
5. Preview and run test

### Other Laser Software

Most laser software supports:
- PDF import
- Color-based layer separation
- Fill/Line mode selection

If your software doesn't auto-detect colors:
- Manually select blue shapes → Set to Fill/Engrave
- Manually select red outlines → Set to Line/Cut

---

## Real-World Examples

### Example 1: Robot Navigation Markers

**Requirement:** 20 markers for robot waypoints, 15mm size

```bash
python generate_aruco_laser.py \
  --dict 5X5_100 \
  -r 0 19 \
  -s 15 \
  -b 1 \
  --spacing 25 \
  -o robot_waypoints.pdf
```

### Example 2: Inventory Tracking

**Requirement:** 100 unique markers, 10mm, no labels (using barcode scanner)

```bash
python generate_aruco_laser.py \
  --dict 6X6_250 \
  -r 0 99 \
  -s 10 \
  --no-labels \
  -o inventory_markers.pdf
```

### Example 3: AR Calibration Targets

**Requirement:** 10 large markers for camera calibration, 30mm

```bash
python generate_aruco_laser.py \
  --dict 4X4_50 \
  -i 0 1 2 3 4 5 6 7 8 9 \
  -s 30 \
  -b 2 \
  --spacing 40 \
  -p 6 \
  -o ar_calibration.pdf
```

### Example 4: Tiny Part Identification

**Requirement:** Dense sheet of 50 small markers, 3mm

```bash
python generate_aruco_laser.py \
  --dict 4X4_50 \
  -s 3 \
  -b 0.5 \
  --spacing 2 \
  --no-labels \
  -o small_parts.pdf
```

### Example 5: Outdoor Event Tracking

**Requirement:** Large, robust markers for outdoor use

```bash
python generate_aruco_laser.py \
  --dict 7X7_50 \
  -r 0 30 \
  -s 50 \
  -b 3 \
  --spacing 60 \
  -p 4 \
  --page-size A4 \
  -o outdoor_event.pdf
```

---

## Best Practices

### Design Phase

1. **Determine Use Case**
   - What are you tracking/detecting?
   - What distances will you detect from?
   - Indoor or outdoor use?

2. **Choose Dictionary**
   - Match marker count to your needs
   - Larger grid = more robust detection
   - Use higher error correction for difficult conditions

3. **Calculate Size**
   - Detection distance = marker size × 50-100
   - Ensure visibility at your working distance

### Production Phase

1. **Test First**
   - Generate 2-3 test markers
   - Cut on scrap material
   - Verify detection with your camera/software

2. **Material Prep**
   - Clean material surface
   - Ensure flat surface for even cutting
   - Use masking tape to prevent burn marks (optional)

3. **Laser Settings**
   - Start with conservative settings
   - Gradually increase power/decrease speed
   - Focus should be exact

### Quality Control

1. **Visual Inspection**
   - Check engraving is clean and visible
   - Ensure cut is complete
   - No burnt edges obscuring pattern

2. **Detection Test**
   - Use camera to detect marker
   - Test at intended distance
   - Verify ID is correctly read

3. **Durability**
   - Test under actual use conditions
   - Check wear resistance
   - Consider protective coating if needed

### Troubleshooting Common Issues

| Problem | Solution |
|---------|----------|
| Markers won't detect | Increase size, improve contrast, check focus |
| Engraving too light | Increase laser power, decrease speed |
| Engraving too dark | Decrease power, increase speed |
| Cut not complete | Increase power, decrease speed, multiple passes |
| Burn marks | Reduce power, increase speed, use masking tape |
| Wrong ID detected | Check orientation, improve engraving quality |

---

## Command Reference

### Complete Command Format

```bash
python generate_aruco_laser.py \
  [--dict DICTIONARY] \
  [-o OUTPUT_FILE] \
  [-s SIZE] \
  [-b BORDER] \
  [--spacing SPACING] \
  [-i ID [ID ...] | -r START END] \
  [-p MARKERS_PER_PAGE] \
  [--page-size {A4,letter}] \
  [--no-labels]
```

### Common Shortcuts

```bash
# Quick test
python generate_aruco_laser.py -i 0

# Small batch
python generate_aruco_laser.py -r 0 9

# Production
python generate_aruco_laser.py --dict 5X5_250 -r 0 100 -s 15 -o batch_001.pdf

# Dense sheet
python generate_aruco_laser.py -s 3 --spacing 2 --no-labels

# Large markers
python generate_aruco_laser.py -s 30 -b 2 --spacing 40 -p 6
```

---

## Tips & Tricks

1. **Batch Production**: Generate multiple PDFs with different size ranges for organization
2. **Version Control**: Include version/date in output filename: `markers_v1_20240101.pdf`
3. **Backup**: Keep your original generated PDFs as references
4. **Testing**: Always test a few markers before cutting a full batch
5. **Documentation**: Take photos of marker placement for future reference
6. **Calibration**: Use the same markers for calibration as for actual use
7. **Wear Protection**: Consider laminating or coating for outdoor/heavy use

---

## FAQ

**Q: Can I use these with any ArUco detection library?**  
A: Yes! These are standard ArUco markers compatible with OpenCV and other libraries.

**Q: What's the smallest usable size?**  
A: 3mm works well with precise lasers. Smaller may work but detection becomes difficult.

**Q: Can I change the colors?**  
A: Yes, but you'll need to modify the script. Blue/red is standard for Lightburn.

**Q: Do I need labels?**  
A: No, use `--no-labels` if you're tracking IDs separately or want cleaner appearance.

**Q: Can I mix different dictionaries?**  
A: No, use one dictionary per detection session. Different dictionaries may have overlapping patterns.

**Q: How many markers can I generate at once?**  
A: Limited by your dictionary. 4X4_1000 allows 1000 unique markers.

---

## Additional Resources

- **OpenCV ArUco Documentation**: https://docs.opencv.org/master/d5/dae/tutorial_aruco_detection.html
- **Lightburn Software**: https://lightburnsoftware.com/
- **ArUco Theory**: Search for "ArUco markers detection" papers

---

## Support

For issues with:
- **Installation**: See [INSTALL.md](INSTALL.md)
- **Quick Start**: See [QUICKSTART.md](QUICKSTART.md)
- **Script Issues**: Check error messages, verify dependencies
- **Laser Settings**: Consult your laser cutter manual

Enjoy generating markers! 🎯
