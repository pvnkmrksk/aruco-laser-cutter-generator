#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "opencv-python>=4.8.0",
#     "numpy>=1.24.0",
#     "reportlab>=4.0.0",
# ]
# ///
"""
ArUco Marker Generator for Laser Cutting/Engraving
===================================================

Generates ArUco markers optimized for laser cutters with color-coded layers:
- Blue filled squares = Engraving layer (the marker pattern)
- Red outline = Cutting layer (the border)

The markers are generated at the logical grid level (e.g., 6x6 cells for 4x4 markers)
for clean, simple vector output that works perfectly with Lightburn and other laser software.

Usage with uv (recommended - auto-installs dependencies):
    uv run generate_aruco_laser.py --dict 4X4_50 -r 0 9
    uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels
    
Usage with python (requires manual dependency installation):
    python generate_aruco_laser.py --dict 4X4_50 -r 0 9

Examples:
    # Generate all markers from a dictionary
    uv run generate_aruco_laser.py --dict 4X4_50
    
    # Generate specific marker IDs
    uv run generate_aruco_laser.py --dict 4X4_100 -i 0 5 10 15
    
    # Generate a range with custom sizing
    uv run generate_aruco_laser.py -r 0 20 -s 15 -b 1 --spacing 25
    
    # Generate without ID labels
    uv run generate_aruco_laser.py -i 0 1 2 3 --no-labels
    
    # Compact 3mm markers with 2mm spacing (dense array)
    uv run generate_aruco_laser.py -s 3 --spacing 2 --no-labels
    
    # Explicit grid layout: 5 rows × 4 columns
    uv run generate_aruco_laser.py --dict 4X4_50 --nrows 5 --ncols 4

Author: Pavan Kumar Kaushik
License: MIT
"""

import cv2
import numpy as np
import argparse
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# Available ArUco dictionaries with their marker counts
ARUCO_DICTS = {
    '4X4_50': (cv2.aruco.DICT_4X4_50, 50),
    '4X4_100': (cv2.aruco.DICT_4X4_100, 100),
    '4X4_250': (cv2.aruco.DICT_4X4_250, 250),
    '4X4_1000': (cv2.aruco.DICT_4X4_1000, 1000),
    '5X5_50': (cv2.aruco.DICT_5X5_50, 50),
    '5X5_100': (cv2.aruco.DICT_5X5_100, 100),
    '5X5_250': (cv2.aruco.DICT_5X5_250, 250),
    '5X5_1000': (cv2.aruco.DICT_5X5_1000, 1000),
    '6X6_50': (cv2.aruco.DICT_6X6_50, 50),
    '6X6_100': (cv2.aruco.DICT_6X6_100, 100),
    '6X6_250': (cv2.aruco.DICT_6X6_250, 250),
    '6X6_1000': (cv2.aruco.DICT_6X6_1000, 1000),
    '7X7_50': (cv2.aruco.DICT_7X7_50, 50),
    '7X7_100': (cv2.aruco.DICT_7X7_100, 100),
    '7X7_250': (cv2.aruco.DICT_7X7_250, 250),
    '7X7_1000': (cv2.aruco.DICT_7X7_1000, 1000),
}


def generate_aruco_laser_pdf(marker_ids, aruco_dict_name='4X4_50', output_file="aruco_markers.pdf", 
                              marker_size_mm=3, border_mm=0.5, spacing_mm=20,
                              page_size=A4, markers_per_page=20, nrows=None, ncols=None, show_labels=True):
    """
    Generate ArUco markers optimized for laser cutting.
    
    Args:
        marker_ids (list): List of marker IDs to generate
        aruco_dict_name (str): ArUco dictionary name (e.g., '4X4_50', '5X5_100')
        output_file (str): Output PDF filename
        marker_size_mm (float): Size of the marker in millimeters
        border_mm (float): White border around marker in millimeters
        spacing_mm (float): Space between markers in millimeters
        page_size (tuple): Page size (A4 or letter)
        markers_per_page (int): How many markers per page (used if nrows/ncols not specified)
        nrows (int, optional): Explicit number of rows per page (overrides markers_per_page)
        ncols (int, optional): Explicit number of columns per page (overrides markers_per_page)
        show_labels (bool): Whether to show marker ID labels below each marker
    
    Returns:
        None (saves PDF to output_file)
    """
    
    # Get ArUco dictionary
    dict_id, max_markers = ARUCO_DICTS[aruco_dict_name]
    aruco_dict = cv2.aruco.getPredefinedDictionary(dict_id)
    
    # Determine grid size based on dictionary (4x4 -> 6x6, 5x5 -> 7x7, etc.)
    dict_grid = int(aruco_dict_name.split('X')[0])
    grid_size = dict_grid + 2  # Add 2 for border
    
    # Create PDF canvas
    c = canvas.Canvas(output_file, pagesize=page_size)
    page_width, page_height = page_size
    
    # Calculate layout - use explicit nrows/ncols if provided, otherwise calculate from markers_per_page
    if nrows is not None and ncols is not None:
        # Both explicitly specified
        markers_per_row = ncols
        markers_per_col = nrows
        markers_per_page = nrows * ncols
    elif nrows is not None:
        # Only nrows specified, calculate ncols from markers_per_page
        markers_per_col = nrows
        markers_per_row = markers_per_page // nrows
        markers_per_page = nrows * markers_per_row
    elif ncols is not None:
        # Only ncols specified, calculate nrows from markers_per_page
        markers_per_row = ncols
        markers_per_col = markers_per_page // ncols
        markers_per_page = markers_per_col * ncols
    else:
        # Neither specified, calculate square grid from markers_per_page
        markers_per_row = int(np.sqrt(markers_per_page))
        markers_per_col = markers_per_page // markers_per_row
        markers_per_page = markers_per_row * markers_per_col
    
    spacing = spacing_mm * mm
    
    marker_count = 0
    
    for marker_id in marker_ids:
        # Generate ArUco marker at grid resolution (clean, simple output)
        marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, grid_size)
        
        # Calculate position on page
        row = (marker_count % markers_per_page) // markers_per_row
        col = (marker_count % markers_per_page) % markers_per_row
        
        # Center the grid on page
        total_width = markers_per_row * (marker_size_mm * mm + border_mm * 2 * mm) + (markers_per_row - 1) * spacing
        total_height = markers_per_col * (marker_size_mm * mm + border_mm * 2 * mm) + (markers_per_col - 1) * spacing
        
        start_x = (page_width - total_width) / 2
        start_y = (page_height - total_height) / 2
        
        x = start_x + col * (marker_size_mm * mm + border_mm * 2 * mm + spacing)
        y = page_height - (start_y + row * (marker_size_mm * mm + border_mm * 2 * mm + spacing))
        
        # Draw the marker
        draw_marker_for_laser(c, marker_img, x, y, marker_size_mm * mm, border_mm * mm, 
                            marker_id, show_labels)
        
        marker_count += 1
        
        # New page if needed
        if marker_count % markers_per_page == 0 and marker_count < len(marker_ids):
            c.showPage()
    
    # Save PDF
    c.save()
    print(f"✓ Generated {len(marker_ids)} markers in {output_file}")


def draw_marker_for_laser(c, marker_img, x, y, size, border, marker_id, show_labels=True):
    """
    Draw a single ArUco marker with laser-cutter color coding.
    
    Color coding for laser cutters:
    - Blue (RGB: 0,0,255) = Engraving layer with filled squares
    - Red (RGB: 255,0,0) = Cutting layer for outer border
    
    Args:
        c: ReportLab canvas object
        marker_img: ArUco marker image array (grid_size x grid_size)
        x (float): X position in PDF points
        y (float): Y position in PDF points
        size (float): Marker size in PDF points
        border (float): Border width in PDF points
        marker_id (int): Marker ID number
        show_labels (bool): Whether to show marker ID label
    """
    
    grid_size = marker_img.shape[0]
    cell_size = size / grid_size
    
    # Draw blue filled squares for black cells (engraving layer)
    c.setStrokeColorRGB(0, 0, 1)  # Blue stroke
    c.setFillColorRGB(0, 0, 1)  # Blue fill
    c.setLineWidth(0.1)
    
    for i in range(grid_size):
        for j in range(grid_size):
            if marker_img[i, j] == 0:  # Black cell in ArUco marker
                # Calculate position (PDF coordinates start from bottom-left)
                cell_x = x + j * cell_size + border
                cell_y = y - (i + 1) * cell_size - border
                
                # Draw blue filled square
                c.rect(cell_x, cell_y, cell_size, cell_size, fill=1, stroke=1)
    
    # Draw red cutting outline (outer square - cutting layer)
    c.setStrokeColorRGB(1, 0, 0)  # Red
    c.setLineWidth(0.1)
    total_size = size + 2 * border
    c.rect(x, y - total_size, total_size, total_size, fill=0, stroke=1)
    
    # Add marker ID text below (optional, in black)
    if show_labels:
        c.setFillColorRGB(0, 0, 0)
        c.setFont("Helvetica", 6)
        text_width = c.stringWidth(f"{marker_id}", "Helvetica", 6)
        c.drawString(x + (total_size - text_width) / 2, y - total_size - 8, f"{marker_id}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate ArUco markers for laser cutting (Blue=engrave, Red=cut)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --dict 4X4_50                    # Generate all 50 markers from 4X4_50 dictionary
  %(prog)s --dict 5X5_100 -i 0 5 10 15      # Generate specific marker IDs
  %(prog)s -r 0 20 -s 15 -b 1               # Generate IDs 0-20 with custom sizing
  %(prog)s -i 0 1 2 3 --spacing 30          # Custom spacing between markers
  %(prog)s -r 0 10 --no-labels              # Generate without ID labels
  %(prog)s --dict 4X4_50 --nrows 5 --ncols 4  # Explicit 5×4 grid layout

Available dictionaries:
  4X4_50, 4X4_100, 4X4_250, 4X4_1000
  5X5_50, 5X5_100, 5X5_250, 5X5_1000
  6X6_50, 6X6_100, 6X6_250, 6X6_1000
  7X7_50, 7X7_100, 7X7_250, 7X7_1000
        """
    )
    
    parser.add_argument('--dict', '--dictionary',
                        dest='dictionary',
                        choices=list(ARUCO_DICTS.keys()),
                        default='4X4_50',
                        help='ArUco dictionary to use (default: 4X4_50)')
    
    parser.add_argument('-o', '--output', 
                        default='aruco_markers.pdf',
                        help='Output PDF filename (default: aruco_markers.pdf)')
    
    parser.add_argument('-s', '--size', 
                        type=float, 
                        default=10.0,
                        help='Marker size in millimeters (default: 10.0)')
    
    parser.add_argument('-b', '--border', 
                        type=float, 
                        default=0.5,
                        help='Border width in millimeters (default: 0.5)')
    
    parser.add_argument('--spacing',
                        type=float,
                        default=20.0,
                        help='Space between markers in millimeters (default: 20.0)')
    
    parser.add_argument('-i', '--ids', 
                        nargs='+',
                        type=int,
                        help='Specific marker IDs to generate. If not specified, generates all markers from dictionary')
    
    parser.add_argument('-r', '--range',
                        nargs=2,
                        type=int,
                        metavar=('START', 'END'),
                        help='Generate markers from START to END (inclusive)')
    
    parser.add_argument('-p', '--per-page',
                        type=int,
                        default=20,
                        help='Number of markers per page (default: 20, ignored if --nrows/--ncols specified)')
    
    parser.add_argument('--nrows',
                        type=int,
                        default=None,
                        help='Explicit number of rows per page (overrides markers_per_page calculation)')
    
    parser.add_argument('--ncols',
                        type=int,
                        default=None,
                        help='Explicit number of columns per page (overrides markers_per_page calculation)')
    
    parser.add_argument('--page-size',
                        choices=['A4', 'letter'],
                        default='A4',
                        help='Page size (default: A4)')
    
    parser.add_argument('--no-labels',
                        action='store_true',
                        help='Do not show marker ID labels below markers')
    
    args = parser.parse_args()
    
    # Get dictionary info
    dict_id, max_markers = ARUCO_DICTS[args.dictionary]
    
    # Determine which markers to generate
    if args.ids:
        marker_ids = args.ids
    elif args.range:
        marker_ids = list(range(args.range[0], args.range[1] + 1))
    else:
        marker_ids = list(range(max_markers))  # All markers in dictionary
    
    # Validate marker IDs
    if any(mid < 0 or mid >= max_markers for mid in marker_ids):
        print(f"Error: Marker IDs must be between 0 and {max_markers-1} for {args.dictionary}")
        return 1
    
    # Set page size
    page_size = A4 if args.page_size == 'A4' else letter
    
    # Print generation info
    print(f"\nGenerating ArUco Markers")
    print(f"{'='*50}")
    print(f"Dictionary:       {args.dictionary}")
    print(f"Marker count:     {len(marker_ids)}")
    print(f"Marker size:      {args.size}mm × {args.size}mm")
    print(f"Border:           {args.border}mm")
    print(f"Spacing:          {args.spacing}mm")
    print(f"Page size:        {args.page_size}")
    if args.nrows is not None and args.ncols is not None:
        print(f"Layout:           {args.nrows} rows × {args.ncols} cols ({args.nrows * args.ncols} markers per page)")
    elif args.nrows is not None:
        ncols = args.per_page // args.nrows
        print(f"Layout:           {args.nrows} rows × {ncols} cols ({args.nrows * ncols} markers per page)")
    elif args.ncols is not None:
        nrows = args.per_page // args.ncols
        print(f"Layout:           {nrows} rows × {args.ncols} cols ({nrows * args.ncols} markers per page)")
    else:
        print(f"Markers per page: {args.per_page}")
    print(f"Show labels:      {'No' if args.no_labels else 'Yes'}")
    print(f"Output:           {args.output}")
    if len(marker_ids) <= 20:
        print(f"IDs:              {marker_ids}")
    else:
        print(f"IDs:              {marker_ids[:10]}...{marker_ids[-10:]}")
    print(f"{'='*50}\n")
    
    # Generate PDF
    generate_aruco_laser_pdf(
        marker_ids=marker_ids,
        aruco_dict_name=args.dictionary,
        output_file=args.output,
        marker_size_mm=args.size,
        border_mm=args.border,
        spacing_mm=args.spacing,
        page_size=page_size,
        markers_per_page=args.per_page,
        nrows=args.nrows,
        ncols=args.ncols,
        show_labels=not args.no_labels
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
