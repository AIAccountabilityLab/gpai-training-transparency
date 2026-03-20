from jinja2 import Environment, FileSystemLoader
from jinja2 import select_autoescape
import json
import os
from pprint import pformat

import log

OUT_DIR = 'public'
OUT_EVAL_DIR = 'evals'
TEMPLATE_PATH = 'templates'

# Set up environment
template_loader = FileSystemLoader(searchpath=f'{TEMPLATE_PATH}')
env = Environment(
    loader=template_loader,
    autoescape=select_autoescape, trim_blocks=True, lstrip_blocks=True)

JINJA2_FILTERS = {
    'pad': lambda s: s + "&nbsp;&nbsp;" if len(s) == 1 else s,
    'prettify': lambda s: pformat(s),
}
env.filters.update(JINJA2_FILTERS)


def about():
    template = env.get_template("about.html")
    with open(f'./{OUT_DIR}/about.html', 'w') as fd:
        fd.write(template.render())
    log.DEBUG('wrote about page')


def detailed_overview(data):
    template = env.get_template("detailed-overview.html")
    with open(f'./{OUT_DIR}/detailed-overview.html', 'w') as fd:
        fd.write(template.render(table_data=data))
    log.DEBUG('wrote detailed overview page')


def evaluation(data):
    template = env.get_template("details-page.html")
    output_path = f"./{OUT_DIR}/{OUT_EVAL_DIR}/{data['model_page']}"
    os.makedirs(output_path, exist_ok=True)
    with open(f"{output_path}/index.html", 'w') as fd:
            fd.write(template.render(page_data=data))
    if data['eval_date']:
        with open(f"{output_path}/version-{data['eval_date']}.html", 'w') as fd:
            fd.write(template.render(page_data=data))
    log.DEBUG(f"wrote evaluation page for {data['model_page']}")


def index(data):
    template = env.get_template("index.html")
    with open(f'./{OUT_DIR}/index.html', 'w') as fd:
        fd.write(template.render(table_data=data))
    log.DEBUG('wrote index/home page')


def methodology():
    template = env.get_template("methodology.html")
    with open(f'./{OUT_DIR}/methodology.html', 'w') as fd:
        fd.write(template.render())
    log.DEBUG('wrote methodology page')


def recommendations():
    template = env.get_template("recommendations.html")
    with open(f'./{OUT_DIR}/recommendations.html', 'w') as fd:
        fd.write(template.render())
    log.DEBUG('wrote recommendations page')