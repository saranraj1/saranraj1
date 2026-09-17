# Setup

## 1. Create the GitHub profile repository

Create a **public repository named exactly `saranraj1`** under the `saranraj1` account. GitHub recognizes this as the special profile repository.

Copy the contents of this package into that repository and push `main`.

## 2. Check the profile

Open `https://github.com/saranraj1`. GitHub should render `README.md` as the profile page.

## 3. Regenerate assets locally

To regenerate the profile animations and SVGs:

```bash
python generator/make_gifs.py
python generator/make_map.py
python generator/make_systems.py
```

Or via npm:

```bash
npm run generate
```

## Notes

- The hero and failure lab animations are pre-rendered lightweight GIFs (<180 KB) for 100% reliable rendering on GitHub.
- The research map and systems plates are static SVGs for crisp vector rendering across all displays.
- The README uses direct repository links for the flagship projects and failure lab experiments so visitors can inspect actual implementations.
