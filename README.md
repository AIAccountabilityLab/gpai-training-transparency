# GPAI Training Transparency
Assessing the quality of AI Act's Article 53(1)(d) public summaries 

> [https://aial.ie/research/gpai-training-transparency](https://aial.ie/research/gpai-training-transparency)

> Cite as: Blankvoort, D. A. H., Pandit, H. J., & Gahntz, M. (2026). _*Quality Assessment of Public Summary of Training Content for GPAI models required by AI Act Article 53(1)(d)*_ (preprint). 9th ACM Conference on Fairness, Accountability, and Transparency (FAccT), Montreal, Canada. Zenodo. DOI:10.5281/zenodo.18803975 [DOI:10.5281/zenodo.18803975](https://doi.org/10.5281/zenodo.18803975) (to be presented)

## Dev Branch Workflow

### Making modifications to the website

Use `main.py`

```bash
$> uv run main.py --help

usage: main.py [-h] [-D] [-H] [-O] [-C] [-R] [-M] [-E] [-A]

options:
  -h, --help            show this help message and exit
  -D, --debug           enable debug logging
  -H, --home            generate home page
  -O, --overview        generate overview page
  -C, --contact         generate contact page
  -R, --recommendations
                        generate recommendations page
  -M, --methodology     generate methodology page
  -E, --evaluations     generate methodology page
  -A, --all             generate all pages
```

### Score a new public summary

Use the checklist: TODO

### Update scores for existing public summary

Use the checklist: TODO

### Publish to main branch / public site

```bash
# assuming your dev branch has the work in commits
$> git switch main
$> git checkout dev -- public
$> git commit  # add your commit message
```

Remember to acknowledge authors at the end of the commit message, e.g.

```
Co-authored-by: Dick Blankvoort <dahblankvoort@gmail.com>
Co-authored-by: Harshvardhan Pandit <me@harshp.com>
```