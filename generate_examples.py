#!/usr/bin/env python3
"""
Script to generate all example PDFs for the repository.
Run this to regenerate all example files with clean, systematic names.
Each example demonstrates different parameters and use cases.
"""

import subprocess
import sys
import os

# Ensure examples directory exists
os.makedirs("examples", exist_ok=True)

# Define all examples to generate - comprehensive coverage of all parameters
examples = [
    # Standard configurations with labels
    {
        "name": "01_standard_10mm_with_labels.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/01_standard_10mm_with_labels.pdf", 
                 "-s", "10", "--spacing", "15", "-p", "25"],
        "desc": "Standard 10mm markers with labels - all 50 markers, 25 per page"
    },
    {
        "name": "02_standard_10mm_no_labels.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/02_standard_10mm_no_labels.pdf", 
                 "-s", "10", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "Standard 10mm markers without labels - clean production look"
    },
    
    # Page size variations
    {
        "name": "03_letter_page_size.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/03_letter_page_size.pdf", 
                 "-s", "10", "--spacing", "15", "--page-size", "letter", "-p", "30", "--no-labels"],
        "desc": "Letter page size - 30 markers per page"
    },
    {
        "name": "04_a4_page_size.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/04_a4_page_size.pdf", 
                 "-s", "10", "--spacing", "15", "--page-size", "A4", "-p", "25", "--no-labels"],
        "desc": "A4 page size - 25 markers per page (default)"
    },
    
    # Marker size variations
    {
        "name": "05_compact_3mm_dense.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/05_compact_3mm_dense.pdf", 
                 "-s", "3", "--spacing", "2", "--no-labels", "-p", "50"],
        "desc": "Compact 3mm markers - maximum density, 50 per page"
    },
    {
        "name": "06_medium_15mm_standard.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/06_medium_15mm_standard.pdf", 
                 "-s", "15", "--spacing", "20", "--no-labels", "-p", "16"],
        "desc": "Medium 15mm markers - standard production size"
    },
    {
        "name": "07_large_25mm_high_visibility.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "24", "-o", "examples/07_large_25mm_high_visibility.pdf", 
                 "-s", "25", "--spacing", "30", "-p", "9", "--no-labels"],
        "desc": "Large 25mm markers - high visibility, long-range detection"
    },
    
    # Border width variations
    {
        "name": "08_minimal_border_0.5mm.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/08_minimal_border_0.5mm.pdf", 
                 "-s", "10", "-b", "0.5", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "Minimal 0.5mm border - most compact"
    },
    {
        "name": "09_standard_border_1mm.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/09_standard_border_1mm.pdf", 
                 "-s", "10", "-b", "1.0", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "Standard 1mm border - recommended"
    },
    {
        "name": "10_thick_border_3mm.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "24", "-o", "examples/10_thick_border_3mm.pdf", 
                 "-s", "15", "-b", "3.0", "--spacing", "25", "--no-labels", "-p", "12"],
        "desc": "Thick 3mm border - high contrast, easy detection"
    },
    
    # Spacing variations
    {
        "name": "11_tight_spacing_5mm.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/11_tight_spacing_5mm.pdf", 
                 "-s", "10", "--spacing", "5", "--no-labels", "-p", "30"],
        "desc": "Tight 5mm spacing - maximum density"
    },
    {
        "name": "12_standard_spacing_20mm.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/12_standard_spacing_20mm.pdf", 
                 "-s", "10", "--spacing", "20", "--no-labels", "-p", "20"],
        "desc": "Standard 20mm spacing - easy cutting"
    },
    {
        "name": "13_generous_spacing_40mm.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "24", "-o", "examples/13_generous_spacing_40mm.pdf", 
                 "-s", "12", "--spacing", "40", "--no-labels", "-p", "9"],
        "desc": "Generous 40mm spacing - large markers, easy handling"
    },
    
    # Dictionary variations
    {
        "name": "14_4x4_dictionary_50_markers.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/14_4x4_dictionary_50_markers.pdf", 
                 "-s", "10", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "4×4 dictionary - 50 markers, compact"
    },
    {
        "name": "15_5x5_dictionary_100_markers.pdf",
        "args": ["--dict", "5X5_100", "-r", "0", "99", "-o", "examples/15_5x5_dictionary_100_markers.pdf", 
                 "-s", "10", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "5×5 dictionary - 100 markers, better reliability"
    },
    {
        "name": "16_6x6_dictionary_250_markers.pdf",
        "args": ["--dict", "6X6_250", "-r", "0", "99", "-o", "examples/16_6x6_dictionary_250_markers.pdf", 
                 "-s", "10", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "6×6 dictionary - maximum reliability, 100 markers shown"
    },
    {
        "name": "17_7x7_dictionary_sample.pdf",
        "args": ["--dict", "7X7_1000", "-r", "0", "24", "-o", "examples/17_7x7_dictionary_sample.pdf", 
                 "-s", "10", "--spacing", "15", "--no-labels", "-p", "25"],
        "desc": "7×7 dictionary - extreme conditions, 25 markers"
    },
    
    # Custom grid layouts (nrows/ncols)
    {
        "name": "18_custom_grid_5x5.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "24", "-o", "examples/18_custom_grid_5x5.pdf", 
                 "--nrows", "5", "--ncols", "5", "-s", "10", "--spacing", "15", "--no-labels"],
        "desc": "Custom 5×5 grid layout - 25 markers"
    },
    {
        "name": "19_custom_grid_4x6.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "23", "-o", "examples/19_custom_grid_4x6.pdf", 
                 "--nrows", "4", "--ncols", "6", "-s", "10", "--spacing", "15", "--no-labels"],
        "desc": "Custom 4×6 grid layout - 24 markers"
    },
    {
        "name": "20_custom_grid_10x2.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "19", "-o", "examples/20_custom_grid_10x2.pdf", 
                 "--nrows", "10", "--ncols", "2", "-s", "10", "--spacing", "15", "--no-labels"],
        "desc": "Custom 10×2 grid layout - 20 markers, vertical strip"
    },
    {
        "name": "21_custom_grid_2x10.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "19", "-o", "examples/21_custom_grid_2x10.pdf", 
                 "--nrows", "2", "--ncols", "10", "-s", "10", "--spacing", "15", "--no-labels"],
        "desc": "Custom 2×10 grid layout - 20 markers, horizontal strip"
    },
    
    # Specific marker selection
    {
        "name": "22_specific_markers_selected.pdf",
        "args": ["--dict", "4X4_50", "-i", "0", "5", "10", "15", "20", "25", "30", "35", "40", "45", 
                 "-o", "examples/22_specific_markers_selected.pdf", 
                 "-s", "12", "--spacing", "20", "-p", "12"],
        "desc": "Specific marker IDs selected - 12 markers"
    },
    {
        "name": "23_single_marker_large.pdf",
        "args": ["-i", "0", "-o", "examples/23_single_marker_large.pdf", 
                 "-s", "50", "-b", "3", "--spacing", "10"],
        "desc": "Single large marker - 50mm, for testing/calibration"
    },
    
    # Production-ready combinations
    {
        "name": "24_production_standard.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/24_production_standard.pdf", 
                 "-s", "12", "-b", "1.5", "--spacing", "25", "--no-labels", "-p", "20"],
        "desc": "Production standard - 12mm markers, 1.5mm border, 25mm spacing"
    },
    {
        "name": "25_production_compact.pdf",
        "args": ["--dict", "4X4_50", "-r", "0", "49", "-o", "examples/25_production_compact.pdf", 
                 "-s", "8", "-b", "1.0", "--spacing", "12", "--no-labels", "-p", "30"],
        "desc": "Production compact - 8mm markers, optimized for space"
    },
]

def main():
    print("Generating comprehensive example PDFs...")
    print("=" * 70)
    print(f"Total examples to generate: {len(examples)}")
    print("=" * 70)
    
    success_count = 0
    failed = []
    
    for i, example in enumerate(examples, 1):
        print(f"\n[{i}/{len(examples)}] Generating {example['name']}...")
        print(f"  Description: {example['desc']}")
        
        # Try with uv run first, fall back to python
        cmd = ["uv", "run", "generate_aruco_laser.py"] + example["args"]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"  ✓ Success")
            success_count += 1
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fall back to python
            cmd = ["python", "generate_aruco_laser.py"] + example["args"]
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                print(f"  ✓ Success")
                success_count += 1
            except subprocess.CalledProcessError as e:
                print(f"  ✗ Failed: {e}")
                if e.stderr:
                    print(f"    Error: {e.stderr[:200]}")
                failed.append(example['name'])
            except FileNotFoundError:
                print(f"  ✗ Failed: Python not found. Please install dependencies first.")
                failed.append(example['name'])
    
    print("\n" + "=" * 70)
    print(f"Generation complete: {success_count}/{len(examples)} successful")
    
    if failed:
        print(f"\nFailed files ({len(failed)}):")
        for f in failed:
            print(f"  - {f}")
        return 1
    
    print("\n✓ All examples generated successfully!")
    print(f"  Total files: {len(examples)}")
    print(f"  Location: examples/")
    return 0

if __name__ == "__main__":
    sys.exit(main())
