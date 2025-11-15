# Example Outputs

This directory contains **25 comprehensive example PDF files** demonstrating all parameters and use cases for the ArUco Marker Generator.

## 📋 Example Categories

### Standard Configurations (01-02)
- **01_standard_10mm_with_labels.pdf** - All 50 markers with ID labels (25 per page)
- **02_standard_10mm_no_labels.pdf** - All 50 markers without labels (clean production look)

### Page Size Variations (03-04)
- **03_letter_page_size.pdf** - Letter page size (8.5" × 11"), 30 markers per page
- **04_a4_page_size.pdf** - A4 page size (210mm × 297mm), 25 markers per page

### Marker Size Variations (05-07)
- **05_compact_3mm_dense.pdf** - 3mm markers, maximum density (50 per page)
- **06_medium_15mm_standard.pdf** - 15mm markers, standard production size (16 per page)
- **07_large_25mm_high_visibility.pdf** - 25mm markers, high visibility (9 per page)

### Border Width Variations (08-10)
- **08_minimal_border_0.5mm.pdf** - 0.5mm border, most compact
- **09_standard_border_1mm.pdf** - 1mm border, recommended for best definition
- **10_thick_border_3mm.pdf** - 3mm border, high contrast, easy detection

### Spacing Variations (11-13)
- **11_tight_spacing_5mm.pdf** - 5mm spacing, maximum density (30 per page)
- **12_standard_spacing_20mm.pdf** - 20mm spacing, easy cutting (20 per page)
- **13_generous_spacing_40mm.pdf** - 40mm spacing, easy handling (9 per page)

### Dictionary Types (14-17)
- **14_4x4_dictionary_50_markers.pdf** - 4×4 dictionary, 50 markers (compact)
- **15_5x5_dictionary_100_markers.pdf** - 5×5 dictionary, 100 markers (better reliability)
- **16_6x6_dictionary_250_markers.pdf** - 6×6 dictionary, 100 markers shown (maximum reliability)
- **17_7x7_dictionary_sample.pdf** - 7×7 dictionary, 25 markers (extreme conditions)

### Custom Grid Layouts (18-21)
- **18_custom_grid_5x5.pdf** - Custom 5×5 grid layout (25 markers)
- **19_custom_grid_4x6.pdf** - Custom 4×6 grid layout (24 markers)
- **20_custom_grid_10x2.pdf** - Custom 10×2 grid layout (20 markers, vertical strip)
- **21_custom_grid_2x10.pdf** - Custom 2×10 grid layout (20 markers, horizontal strip)

### Special Use Cases (22-25)
- **22_specific_markers_selected.pdf** - Specific marker IDs selected (12 markers)
- **23_single_marker_large.pdf** - Single large marker (50mm) for testing/calibration
- **24_production_standard.pdf** - Production standard (12mm, 1.5mm border, 25mm spacing)
- **25_production_compact.pdf** - Production compact (8mm, optimized for space)

## 🎯 Parameter Coverage

These examples demonstrate all available parameters:

| Parameter | Examples | Values Shown |
|-----------|----------|--------------|
| **Page Size** | 03, 04 | A4, Letter |
| **Marker Size** | 05, 06, 07 | 3mm, 15mm, 25mm |
| **Border Width** | 08, 09, 10 | 0.5mm, 1mm, 3mm |
| **Spacing** | 11, 12, 13 | 5mm, 20mm, 40mm |
| **Dictionary** | 14, 15, 16, 17 | 4×4, 5×5, 6×6, 7×7 |
| **Grid Layout** | 18, 19, 20, 21 | Various nrows×ncols |
| **Labels** | 01, 02 | With/without labels |
| **Marker Selection** | 22, 23 | Specific IDs, single marker |

## 🔄 Regenerating Examples

To regenerate all examples with the latest script version:

```bash
# From the repository root
python scripts/generate_examples.py
```

This will recreate all 25 example PDFs with the current script version.

## 📝 Notes

- All examples use appropriate marker counts and page layouts
- Examples are dense (many markers per page) to show practical usage
- Color coding: Blue (RGB: 0,0,255) = Engraving, Red (RGB: 255,0,0) = Cutting
- File sizes are optimized for vector output (typically 50-500 KB per PDF)
- Each example demonstrates a specific parameter or use case

## 💡 Usage Tips

1. **Browse** - Click any PDF to view it directly in GitHub
2. **Compare** - Compare examples to see parameter effects
3. **Download** - Download the PDF that matches your needs
4. **Customize** - Use the command patterns shown in the main README to generate your own version
