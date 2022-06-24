
def head_html(filename, pathfile, chars, words, percentage):
    color = ''
    if (float(percentage) <= 33):
        color = 'green'
    elif (float(percentage) > 33 or float(percentage) <= 66):
        color = 'orange'
    else:
        color = 'red'


    html = """
    <!DOCTYPE html>
    <html lang=\"en\">

    <head>
        <meta charset=\"UTF-8\" />
        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />

        <style>
            body {
                padding: 10px;
            }

            header {
                padding-top: 60px;
                padding-bottom: 60px;
                padding-left: 10px;
                background-color: dodgerblue;
                color: white;
            }

            .head-title {
                font-size: 30px;
                font-weight: bold;
                font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;
                margin-top: 0px;
                margin: 0px;
            }

            h1,
            h2,
            h3,
            h4,
            h5,
            h6,
            p {
                margin: 0px;
            }

            .container {
                border: solid 0.2px;
                padding: 10px;
            }

            .grid-container {
                display: grid;
                grid-template-columns: auto auto auto;
                gap: 10px;
            }

            .mt-2 {
                margin-top: 14px;
            }

            .mt-4 {
                margin-top: 28px;
            }

            .text-center {
                text-align: center;
            }

            .text-normal {
                font-weight: normal;
            }

            .item-left-1 {
                grid-column-start: 1;
                grid-column-end: 2;
            }

            .item-left-2 {
                grid-column-start: 1;
                grid-column-end: 3;
            }

            .table-borderless {
                border: none;
                overflow-x: auto;
                width: auto;
            }

            .box {
                --v: calc(((18/5) * var(--p) - 90)*1deg);

                width: 100px;
                height: 100px;
                display: inline-block;
                border-radius: 50%;
                padding: 10px;
                place-content: center;
                font-size: 25px;
                font-weight: bold;
                font-family: sans-serif;
                position: relative;
                display: inline-grid;

                background:
                    linear-gradient(#fff, #fff) content-box,
                    linear-gradient(var(--v), #f2f2f2 50%, transparent 0) 0/min(100%, (50 - var(--p))*100%),
                    linear-gradient(var(--v), transparent 50%, var(--c) 0) 0/min(100%, (var(--p) - 50)*100%),
                    linear-gradient(to right, #f2f2f2 50%, var(--c) 0);
            }

            .detail-table {
                font-family: Arial, Helvetica, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            .detail-table th {
                border: 1px solid #ddd;
                padding: 8px;
            }
            .detail-table td {
                border: 1px solid #ddd;
                padding: 4px;
                padding-left: 8px;
                padding-right: 8px;
            }

            .detail-table tr:nth-child(even) {
                background-color: #f2f2f2;
            }

            .detail-table tr:hover {
                background-color: #ddd;
            }

            .detail-table th {
                text-align: left;
                background-color: dodgerblue;
                color: white;
            }
        </style>
    </head>

    <body>
        <header>
            <h1 class=\"head-title\">Check Similiarity Documents</h1>
        </header>

        <div class=\"container\">
            <div class=\"grid-container\">
                <div class=\"item-left-2\">

                    <div class=\"grid-container\">
                        <div class=\"item-left-1\">
                            <h3><b>File Name</b></h3>
                        </div>
                        <div class=\"grid-item\">
                            <h3 class=\"text-normal\">
                                <p>""" + filename + """</p>
                            </h3>
                        </div>
                        <div class=\"item-left-1\">
                            <h3><b>Path Name</b></h3>
                        </div>
                        <div class=\"grid-item\">
                            <h3 class=\"text-normal\">
                                <p>""" + pathfile + """</p>
                            </h3>
                        </div>



                        <div class=\"item-left-1 mt-2\">
                            <h3><b>Number of words</b></h3>
                        </div>
                        <div class=\"grid-item mt-2\">
                            <h3 class=\"text-normal\">
                                <p>""" + str(words) + """</p>
                            </h3>
                        </div>
                        <div class=\"item-left-1\">
                            <h3><b>Number of characters</b></h3>
                        </div>
                        <div class=\"grid-item\">
                            <h3 class=\"text-normal\">
                                <p>""" + str(chars) + """</p>
                            </h3>
                        </div>
                    </div>

                </div>
                <div class=\"grid-item\">
                    <h3>Result</h3>

                    <div class=\"text-center mt-2\">
                        <div class=\"box\" style=\"--p:""" + str(percentage) + """; --c:""" + color + """ \">""" + str(percentage) + """%</div>
                    </div>
                </div>
            </div>
            
            <div class=\"mt-4\">
                <h4>Details</h4>

                <table class=\"detail-table\">

                    <tr>
                        <th>File</th>
                        <th>Similarity Score</th>
                        <th>Conclusion</th>
                    </tr>
    """
    return html