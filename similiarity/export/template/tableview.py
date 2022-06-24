
def table_row_html(filename, score, conclusion):
    return """
        <tr>
            <td>{filename}</td>
            <td>{score} %</td>
            <td>{conclusion}</td>
        </tr>
    """.format(filename=filename, score=score, conclusion=conclusion)