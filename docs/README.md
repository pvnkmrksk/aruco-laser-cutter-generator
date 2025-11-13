# GitHub Pages Documentation

This directory contains the GitHub Pages documentation for the ArUco Marker Generator.

## Setup

To enable GitHub Pages for this repository:

1. Go to your repository settings on GitHub
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select "Deploy from a branch"
4. Choose the `main` branch and `/ (root)` folder
5. Click "Save"

The documentation will be automatically deployed when you push changes to the main branch (via the GitHub Actions workflow).

## Manual Deployment

If you prefer to deploy manually:

1. Install Jekyll: `gem install bundler jekyll`
2. Build the site: `jekyll build`
3. Serve locally: `jekyll serve`

## Documentation Structure

The main documentation files are in the repository root:
- `README.md` - Project overview
- `INSTALL.md` - Installation guide
- `QUICKSTART.md` - Quick start guide
- `USER_GUIDE.md` - Complete user manual
- `DOCS_INDEX.md` - Documentation index

This `docs/` directory contains:
- `index.md` - GitHub Pages homepage
- `_config.yml` - Jekyll configuration

## Customization

Edit `_config.yml` to customize the GitHub Pages site:
- Change the theme
- Add Google Analytics
- Customize navigation
- Update site metadata

