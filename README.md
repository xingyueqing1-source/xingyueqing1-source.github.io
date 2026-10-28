# Yueqing Xing — personal homepage

A lightweight personal and academic homepage designed for GitHub Pages. It uses plain HTML, CSS, and JavaScript: no package manager, framework, build step, or paid service is required.

## Preview locally

Open `index.html` directly, or serve the folder with any static web server. For example:

```powershell
python -m http.server 4173
```

Then visit `http://localhost:4173`.

## Routine updates

Most updates only require editing `site-content.js`:

- `profile`: name, affiliation, avatar, contact links, CV, and research interests
- `about`: introductory paragraphs
- `work`: papers and projects
- `news`: dated updates
- `awards` and `services`: optional sections; empty arrays are hidden automatically
- `footer.lastUpdated`: visible maintenance date

Keep downloadable files such as a CV in an `assets/` folder and use a relative path, for example `assets/Yueqing-Xing-CV.pdf`.

The English CV is generated from `scripts/build_cv.py`. From the repository root, run:

```powershell
python scripts/build_cv.py
```

The generated PDF is written to `output/pdf/Yueqing-Xing-CV-English.pdf`, which is also linked from the homepage.

## Publish on GitHub Pages

1. Create a public repository named `xingyueqing1-source.github.io` in the `xingyueqing1-source` account.
2. Push the files in this folder to the repository's `main` branch.
3. In **Settings → Pages**, choose **Deploy from a branch**, then select `main` and `/ (root)`.
4. The site will be available at `https://xingyueqing1-source.github.io/` after GitHub finishes deployment.

## Files

- `index.html` — semantic page shell and metadata
- `site-content.js` — editable personal content
- `styles.css` — visual design and responsive behavior
- `app.js` — rendering, navigation, theme, and reveal interactions
- `assets/github-avatar-circle-500.png` — upload-ready GitHub and homepage avatar
- `scripts/build_cv.py` — English CV build entry point
- `scripts/build_cv_v2.py` — current two-column academic CV layout and content
- `output/pdf/Yueqing-Xing-CV-English.pdf` — generated English CV
- `favicon.svg` — browser-tab icon
- `.nojekyll` — tells GitHub Pages to serve the files directly

## Content verification

The initial version uses only information visible on the public GitHub profile and C1B-MC repository. Review and replace the introductory copy before publication, then add affiliation, email, CV, publications, news, awards, and service records as appropriate.
