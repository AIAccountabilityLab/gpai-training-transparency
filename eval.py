from datetime import datetime
from os import listdir, remove, system, makedirs
import json
from pprint import pformat
from yaml import safe_load

import log

ID_TO_NAME_MAPPING = {
    'S1': 'Document',
    'S2': 'General information',
    'S3': 'Public Data Sources',
    'S4': 'Private Data Sources',
    'S5': 'Scraped/Crawled Data',
    'S6': 'User Data',
    'S7': 'Synthetic/Other Data',
    'S8': 'Data Processing',
    'D1': 'Clarity',
    'D2': 'Completeness',
    'D3': 'Consistency',
    'D4': 'Correctness',
    'D5': 'Accessibility',
    'D6': 'Comprehension',
}

def calc_percents(template_info):
    percs = {}
    sum_scores = 6*[0]
    sum_max_scores = 6*[0]
    sum_notes = 6*[""]
    for k1 in template_info.keys():
        if k1.startswith('S'):
            section_percs = {}
            t_score = 0
            t_max_score = 0
            t_notes = ""
            u_score = 0
            u_max_score = 0
            u_notes = ""

            for k2 in template_info[k1].keys():
                if k2.startswith('D'):
                    score = template_info[k1][k2]['score']
                    if score == None:
                        score = 0
                    max_score = template_info[k1][k2]['max_score']
                    if max_score == None:
                        max_score = 0
                    notes = template_info[k1][k2]['notes']

                    if score == None:
                        score = 0

                    if int(k2[1]) <= 4:
                        t_score += score
                        t_max_score += max_score
                        t_notes += notes + '\n'
                    else:
                        u_score += score
                        u_max_score += max_score
                        u_notes += notes + '\n'
                    
                    sum_scores[int(k2[1])-1] += score
                    sum_max_scores[int(k2[1])-1] += max_score
                    sum_notes[int(k2[1])-1] += notes

                    if max_score == 0:
                        section_percs[ID_TO_NAME_MAPPING[k2]] = {'score': 'N/A', 'notes': notes}
                    else:
                        section_percs[ID_TO_NAME_MAPPING[k2]] = {'score': round(score/max_score*100, 2), 'notes': notes}
            
            if t_max_score == 0:
                section_percs['Transparency'] = {'score': 'N/A', 'notes': t_notes}
            else:
                section_percs['Transparency'] = {'score': round(t_score/t_max_score*100, 2), 'notes': t_notes}

            if u_max_score == 0:
                section_percs['Usefulness'] = {'score': 'N/A', 'notes': u_notes}
            else:
                section_percs['Usefulness'] = {'score': round(u_score/u_max_score*100, 2), 'notes': u_notes}

            percs[ID_TO_NAME_MAPPING[k1]] = section_percs

    percs['Sum'] = {}
    for i in range(len(sum_scores)):
        if sum_max_scores[i] == 0:
            percs['Sum'][ID_TO_NAME_MAPPING['D'+str(i+1)]] = {'score': 'N/A', 'notes': sum_notes[i]}
        else:
            percs['Sum'][ID_TO_NAME_MAPPING['D'+str(i+1)]] = {'score': round(sum_scores[i]/sum_max_scores[i]*100, 2), 'notes': sum_notes[i]}
    
    if sum(sum_max_scores[:4]) == 0:
        percs['Sum']['Transparency'] = {'score': 'N/A', 'notes': '\n'.join(sum_notes[:4])}
    else:
        percs['Sum']['Transparency'] = {'score': round(sum(sum_scores[:4])/sum(sum_max_scores[:4])*100, 2), 'notes': '\n'.join(sum_notes[:4])}

    if sum(sum_max_scores[4:]) == 0:
        percs['Sum']['Usefulness'] = {'score': 'N/A', 'notes': '\n'.join(sum_notes[4:])}
    else:
        percs['Sum']['Usefulness'] = {'score': round(sum(sum_scores[4:])/sum(sum_max_scores[4:])*100, 2), 'notes': '\n'.join(sum_notes[4:])}
    
    return percs

def scores_to_eval(scores, group):    
    perc_score = scores['Sum'][group]

    if perc_score['score'] == 'N/A':
        return ("N/A", perc_score['notes'])
    elif perc_score['score'] >= 95:
        return ("A+", perc_score['notes'])
    elif perc_score['score'] >= 90:
        return ("A", perc_score['notes'])
    elif perc_score['score'] >= 80:
        return ("B+", perc_score['notes'])
    elif perc_score['score'] >= 75:
        return ("B", perc_score['notes'])
    elif perc_score['score'] >= 60:
        return ("C+", perc_score['notes'])
    elif perc_score['score'] >= 50:
        return ("C", perc_score['notes'])
    elif perc_score['score'] >= 40:
        return ("D+", perc_score['notes'])
    elif perc_score['score'] >= 25:
        return ("D", perc_score['notes'])
    elif perc_score['score'] >= 0:
        return ("F", perc_score['notes'])
    else:
        return ValueError()

def grade_to_col(grade):
    if grade == 'N/A':
        return 'na'
    elif grade.startswith('A') or grade.startswith('B'):
        return "open"
    elif grade.startswith('C'):
        return "partial"
    elif grade.startswith('D') or grade.startswith('F'):
        return "closed"
    else:
        return ValueError()

def percent_to_col(score):
    # log.DEBUG(f"{score=}")
    returndict = { "val": score['score'], "notes": score['notes'] }
    if score['score'] == 'N/A':
        returndict["col"] = "na"
    elif score['score'] >= 75:
        returndict["col"] = "open"
    elif score['score'] >= 50:
        returndict["col"] = "partial"
    elif score['score'] >= 0:
        returndict["col"] = "closed"
    else:
        raise ValueError(f"{score['score']=} is an invalid score")

    return returndict


def round_scores(scores):
    out = []
    for score in scores:
        if score['val'] == 'N/A':
            out.append(score)
        else:
            out.append({'col': score['col'], 'val': int(score['val'])})
    return out


def calculate():
    log.DEBUG('-' * 25)
    log.DEBUG(f"Calculating evaluations")
    log.DEBUG('-' * 25)
    # Get miscellaneous data for variables
    curr_date = datetime.today().strftime('%Y-%m-%d')
    # TODO: move section names to global static data (tuple)
    section_names = ['Document', 'General information', 'Public Data Sources', 'Private Data Sources', 'Scraped/Crawled Data', 'User Data', 'Synthetic & Other Data', 'Data Processing', 'Overall']

    page_names = []
    eval_data = {}
    
    for file in listdir('./evals'):
        if not file.endswith('.yaml'):
            raise ValueError("Non-YAML files in evals directory")
        
        with open('./evals/'+file, 'r') as yml_file:
            template_info = safe_load(yml_file)
            # log.DEBUG(f"{template_info.keys()=}")
            # log.DEBUG(f"{template_info['S1']=}")

        file_name = file[:-5]
        log.DEBUG(f"Target: {file_name}")
        page_names.append(file_name)
        perc_scores = calc_percents(template_info)
        # log.DEBUG(perc_scores)
        # log.DEBUG(f"score: {perc_scores['Sum']}")

        t_grade, t_notes = scores_to_eval(perc_scores, "Transparency")
        # log.DEBUG(t_notes)
        u_grade, u_notes = scores_to_eval(perc_scores, "Usefulness")

        t_col = grade_to_col(t_grade)
        u_col = grade_to_col(u_grade)
        colored_tu_scores = [percent_to_col(score) for sect in perc_scores.values() for key, score in sect.items() if key == "Transparency" or key == "Usefulness"]
        colored_full_scores = [
            {
                'name': name, 
                'scores': [percent_to_col(score) for score in sect.values()],
            } for name, sect in perc_scores.items() ]
        # log.DEBUG(colored_full_scores)
        detailed_overview_scores = round_scores(colored_tu_scores[-2:] + colored_tu_scores[2:-2] + colored_tu_scores[0:2])
        t_score = perc_scores['Sum']['Transparency']['score']
        u_score = perc_scores['Sum']['Usefulness']['score']
        
        if t_score == 'N/A':
            t_score = 0
        if u_score == 'N/A':
            u_score = 0
        summed_score = (t_score + u_score)
        
        # log.DEBUG(f"graded as: T: {t_score}% {t_grade}; U: {u_score}% {u_grade}; total: {summed_score:.2f}%")

        log.DEBUG('-' * 55)

        page_data = {
            'model_page': file_name,
            'model_name': template_info['model_name'],
            'model_link': template_info['model_link'],
            'model_publication_date': template_info['model_publication_date'], 
            'model_category': template_info['category'],
            'summary_last_update': template_info['public_summary_date'], 
            'summary_link': template_info['public_summary_link'],
            'summary_location': template_info['public_summary_location'], 
            'summary_archive': 'archive/'+template_info['archive_file_name'],
            'org_name': template_info['organization'],
            'org_link': template_info['org_link'],
            'eval_date': template_info['evaluation_date'],
            't_col': t_col, 
            't_grade': t_grade, 
            't_notes': t_notes, 
            'u_col': u_col, 
            'u_grade': u_grade, 
            'u_notes': u_notes,
            'summed_score': summed_score,
            'detailed_scores': detailed_overview_scores,
            'colored_scores': colored_full_scores,
            'general_notes': template_info['general_notes'],
            'improvements': identify_improvements(colored_full_scores),
            'previous_versions': template_info.get('previous_versions', [])
        }
        # log.DEBUG(pformat(page_data))
        eval_data[file_name] = page_data

    log.DEBUG(f"completed {len(eval_data)} evaluations")
    return eval_data


def identify_improvements(scores):
    with open('conf/config.json') as fd:
        data_config = json.load(fd)

    # log.DEBUG(pformat(scores))
    deficiencies = {}
    for section in scores:
        name = section['name']
        section_deficiencies = []
        for index in range(0,6): # 6 metrics
            field = section['scores'][index]
            score = field['val']
            col = field['col']
            message = field['notes'].strip()
            if not message:
                message = data_config['metrics'][f'M{index+1}']['description']
            if col == 'open':
                severity = 'low'
            elif col == 'partial':
                severity = 'medium'
            elif col == 'closed':
                severity = 'high'
            elif col == 'na':
                pass
            else:
                raise ValueError(f"{col} is an invalid severity")
            if type(score) is not str and score < 100.0:
                section_deficiencies.append({
                    'metric': f'M{index+1}',
                    'message': message,
                    'severity': severity,
                    'col': col,
                    })
        if section_deficiencies:
            deficiencies[name] = section_deficiencies

    # log.DEBUG(pformat(deficiencies))

    return deficiencies