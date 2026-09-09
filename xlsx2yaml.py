# Get xlsx file passed as argument

import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Spreadsheet downloaded should be passed as argument")
    sys.exit(-1)
INPUT_XLSX = Path(sys.argv[1])
print(f"{INPUT_XLSX=}")
import openpyxl
import yaml

workbook = openpyxl.load_workbook(INPUT_XLSX, data_only=True)

# TODO replace sheet extraction criteria with list in Public_summaries
sheet_names_skip_extraction = (
    'README', 'Metrics', 'CoP_signees', 'Models', 'Public_summaries',
    'Eval_template', 'methodology_v2', 'Evaluations -- full data',
    'Field-Level Questions',
    # SKIP additional sheets
    'SwissAI_Apertus'
)

sheet_all = workbook.sheetnames
sheet_selected = [
    sheet for sheet in sheet_all
    if sheet not in sheet_names_skip_extraction ]

TEST_SCHEMA = {
    "A1": "Eval Metadata",
    # "B5": "DONE", # STATUS
    "A9": "Model details",
    "A15": "Public Summary details",
    "A23": "ID",
    # TODO: More tests for schema
    "A336": "F3.3.a.3",
}

DATA_SCHEMA = {
    "metadata": {
        "model_name": "B10",
        "model_link": "B11",
        "organization": "B12",
        "org_link": "B13",
        "evaluation_date": "B3",
        "public_summary_link": "B16",
        "public_summary_date": "B17",
        "public_summary_location": "B18",
        "model_publication_date": "B19",
        "category": "B20",
        "archive_file_name": "B21",
        # "general_notes": "B433", # handle as special case - multiple lines
        # TODO: previous_versions is an array calculated from files
    },
    "scores": {
        "S1": {
            "D1": {
                "score": "C376",
                "max_score": "D376",
                "note": "E376",
            },
            "D2": {
                "score": "C377",
                "max_score": "D377",
                "note": "E377",
            },
            "D3": {
                "score": "C378",
                "max_score": "D378",
                "note": "E378",
            },
            "D4": {
                "score": "C379",
                "max_score": "D379",
                "note": "E379",
            },
            "D5": {
                "score": "C380",
                "max_score": "D380",
                "note": "E380",
            },
            "D6": {
                "score": "C381",
                "max_score": "D381",
                "note": "E381",
            },
        },
        "S2": {
            "D1": {
                "score": "C383",
                "max_score": "D383",
                "note": "E383",
            },
            "D2": {
                "score": "C384",
                "max_score": "D384",
                "note": "E384",
            },
            "D3": {
                "score": "C385",
                "max_score": "D385",
                "note": "E385",
            },
            "D4": {
                "score": "C386",
                "max_score": "D386",
                "note": "E386",
            },
            "D5": {
                "score": "C387",
                "max_score": "D387",
                "note": "E387",
            },
            "D6": {
                "score": "C388",
                "max_score": "D388",
                "note": "E388",
            },
        },
        "S3": {
            "D1": {
                "score": "C390",
                "max_score": "D390",
                "note": "E390",
            },
            "D2": {
                "score": "C391",
                "max_score": "D391",
                "note": "E391",
            },
            "D3": {
                "score": "C392",
                "max_score": "D392",
                "note": "E392",
            },
            "D4": {
                "score": "C393",
                "max_score": "D393",
                "note": "E393",
            },
            "D5": {
                "score": "C394",
                "max_score": "D394",
                "note": "E394",
            },
            "D6": {
                "score": "C395",
                "max_score": "D395",
                "note": "E395",
            },
        },
        "S4": {
            "D1": {
                "score": "C397",
                "max_score": "D397",
                "note": "E397",
            },
            "D2": {
                "score": "C398",
                "max_score": "D398",
                "note": "E398",
            },
            "D3": {
                "score": "C399",
                "max_score": "D399",
                "note": "E399",
            },
            "D4": {
                "score": "C400",
                "max_score": "D400",
                "note": "E400",
            },
            "D5": {
                "score": "C401",
                "max_score": "D401",
                "note": "E401",
            },
            "D6": {
                "score": "C402",
                "max_score": "D402",
                "note": "E402",
            },
        },
        "S5": {
            "D1": {
                "score": "C404",
                "max_score": "D404",
                "note": "E404",
            },
            "D2": {
                "score": "C405",
                "max_score": "D405",
                "note": "E405",
            },
            "D3": {
                "score": "C406",
                "max_score": "D406",
                "note": "E406",
            },
            "D4": {
                "score": "C407",
                "max_score": "D407",
                "note": "E407",
            },
            "D5": {
                "score": "C408",
                "max_score": "D408",
                "note": "E408",
            },
            "D6": {
                "score": "C409",
                "max_score": "D409",
                "note": "E409",
            },
        },
        "S6": {
            "D1": {
                "score": "C411",
                "max_score": "D411",
                "note": "E411",
            },
            "D2": {
                "score": "C412",
                "max_score": "D412",
                "note": "E412",
            },
            "D3": {
                "score": "C413",
                "max_score": "D413",
                "note": "E413",
            },
            "D4": {
                "score": "C414",
                "max_score": "D414",
                "note": "E414",
            },
            "D5": {
                "score": "C415",
                "max_score": "D415",
                "note": "E415",
            },
            "D6": {
                "score": "C416",
                "max_score": "D416",
                "note": "E416",
            },
        },
        "S7": {
            "D1": {
                "score": "C418",
                "max_score": "D418",
                "note": "E418",
            },
            "D2": {
                "score": "C419",
                "max_score": "D419",
                "note": "E419",
            },
            "D3": {
                "score": "C420",
                "max_score": "D420",
                "note": "E420",
            },
            "D4": {
                "score": "C421",
                "max_score": "D421",
                "note": "E421",
            },
            "D5": {
                "score": "C422",
                "max_score": "D422",
                "note": "E422",
            },
            "D6": {
                "score": "C423",
                "max_score": "D423",
                "note": "E423",
            },
        },
        "S8": {
            "D1": {
                "score": "C425",
                "max_score": "D425",
                "note": "E425",
            },
            "D2": {
                "score": "C426",
                "max_score": "D426",
                "note": "E426",
            },
            "D3": {
                "score": "C427",
                "max_score": "D427",
                "note": "E427",
            },
            "D4": {
                "score": "C428",
                "max_score": "D428",
                "note": "E428",
            },
            "D5": {
                "score": "C429",
                "max_score": "D429",
                "note": "E429",
            },
            "D6": {
                "score": "C430",
                "max_score": "D430",
                "note": "E430",
            },
        },
    },
}

for sheet in sheet_selected:
    print('-'*78)
    print(f"working with {sheet=}")
    sheet = workbook[sheet]

    # --- Validation checks ---
    if sheet['B5'].value != 'DONE': # Status
        print(f"skipping sheet as status is NOT DONE")
        continue
    TEST_SCHEMA_PASS = True
    for cell, expected in TEST_SCHEMA.items():
        actual = sheet[cell].value
        try:
            assert(actual == expected)
        except AssertionError as E:
            print(f"failed assertion {cell=} {expected=} {actual=}")
            TEST_SCHEMA_PASS = False
            break
    if not TEST_SCHEMA_PASS:
        print(f"skipped sheet due to assertion failures")
        continue

    # --- data extraction ---
    data = {}
    for fieldname, cell in DATA_SCHEMA['metadata'].items():
        value = str(sheet[cell].value).strip()
        try:
            assert(value)
        except AssertionError as E:
            print(f"Error: empty value for {fieldname=} in {cell=}")
            # TODO: fix errors
            print(f"Treating as null...")
            value = ""
        data[fieldname] = value
    for section, sectionscells in DATA_SCHEMA['scores'].items():
        sectiondata = {}
        for metric, metriccells in sectionscells.items():
            sectiondata[metric] = {
                'score': sheet[metriccells['score']].value,
                'max_score': sheet[metriccells['max_score']].value,
                'notes': sheet[metriccells['note']].value or "",
            }
        data[section] = sectiondata

    # --- export ---

    filename = sheet['B6'].value
    
    with open(f"evals/{filename}.yaml", "w", encoding="utf-8") as fd:
        yaml.safe_dump(
            data,
            fd,
            allow_unicode=True,
            sort_keys=False,
            )
    print(f"wrote data to {filename=}.yaml")