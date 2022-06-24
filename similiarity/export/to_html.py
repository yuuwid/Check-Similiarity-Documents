from similiarity.export.template.bottomview import footer_html
from similiarity.export.template.tableview import table_row_html
from similiarity.export.template.topview import head_html

def bulk_score_(results):

    sum_score = 0
    n_score = 0

    for result in results[1]:
        sum_score += result[-1]
        n_score += 1

    return sum_score / n_score

def conclusion_(score, tolerance):
    if score > tolerance:
        return "PLAGIARISM DETECTED"
    else:
        return "UNIQUE"

def get_filename(pathfile):
    return pathfile.split('\\')[-1]

def c_html(data, tolerance):
    
    html = []

    for results in data:
        filename = get_filename(results[0])
        pathfile = results[0]

        chars = results[-1]
        words = results[-2]

        percentage = bulk_score_(results)
        percentage = ("%.2f" % percentage)

        temp_head_html = head_html(filename, pathfile, chars, words, percentage)

        temp_table_row_html = ''

        for res in results[1]:
            filename2 = get_filename(res[0])
            score = res[-1]

            score = ("%.2f" % score)

            conclusion = conclusion_(float(score), tolerance)

            temp_row = table_row_html(filename2, score, conclusion)

            temp_table_row_html += temp_row

        temp_footer_html = footer_html()

        html = temp_head_html + temp_table_row_html + temp_footer_html

        export_temp = 'export/' + filename + '.html'
        file_temp = open(export_temp, 'w')
        file_temp.write(html)
