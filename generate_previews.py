#!/usr/bin/env python3
"""
Generate preview images from example PDFs.
Requires: pdf2image (pip install pdf2image) and poppler-utils
"""

import os
from pathlib import Path

try:
    from pdf2image import convert_from_path
    PDF2IMAGE_AVAILABLE = True
except ImportError:
    PDF2IMAGE_AVAILABLE = False
    print("Warning: pdf2image not available. Install with: pip install pdf2image")
    print("Also requires poppler-utils: brew install poppler (macOS) or apt-get install poppler-utils (Linux)")

def generate_preview(pdf_path, output_dir="examples/previews", dpi=150, max_size=(800, 600)):
    """Generate a preview image from a PDF file."""
    if not PDF2IMAGE_AVAILABLE:
        return None
    
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_name = Path(pdf_path).stem
    output_path = os.path.join(output_dir, f"{pdf_name}_preview.png")
    
    try:
        # Convert first page of PDF to image
        images = convert_from_path(pdf_path, dpi=dpi, first_page=1, last_page=1)
        
        if images:
            img = images[0]
            
            # Resize if too large
            if img.width > max_size[0] or img.height > max_size[1]:
                img.thumbnail(max_size, resample=3)  # 3 = LANCZOS
            
            img.save(output_path, "PNG", optimize=True)
            print(f"  ✓ Generated: {output_path}")
            return output_path
    except Exception as e:
        print(f"  ✗ Failed to generate preview for {pdf_path}: {e}")
        return None

def main():
    examples_dir = Path("examples")
    if not examples_dir.exists():
        print("Examples directory not found. Run generate_examples.py first.")
        return 1
    
    pdf_files = sorted(examples_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in examples directory.")
        return 1
    
    print(f"Generating previews for {len(pdf_files)} PDFs...")
    print("=" * 60)
    
    if not PDF2IMAGE_AVAILABLE:
        print("\nTo generate preview images, install:")
        print("  pip install pdf2image")
        print("  brew install poppler  # macOS")
        print("  # or apt-get install poppler-utils  # Linux")
        return 1
    
    generated = []
    for pdf_file in pdf_files:
        print(f"\nProcessing {pdf_file.name}...")
        preview = generate_preview(str(pdf_file))
        if preview:
            generated.append(preview)
    
    print("\n" + "=" * 60)
    print(f"Generated {len(generated)} preview images")
    print(f"Preview images saved to: examples/previews/")
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())

