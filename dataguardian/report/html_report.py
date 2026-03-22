import os


def generate_html_report(results, filename="report.html"):
    """
    Generate HTML report from diagnosis results
    """
    html = f"""
    <html>
    <head>
        <title>DataGuardian Report</title>
        <style>
            body {{ font-family: Arial; padding: 20px; }}
            h1 {{ color: #2c3e50; }}
            .warning {{ color: red; }}
            .good {{ color: green; }}
        </style>
    </head>
    <body>

    <h1>📊 DataGuardian Report</h1>

    <h2>Dataset Info</h2>
    <p><b>Shape:</b> {results['shape']}</p>
    <p><b>Columns:</b> {results['columns']}</p>

    <h2>Score</h2>
    <p><b>Data Health Score:</b> {results['score']}</p>

    <h2>Warnings</h2>
    """

    for w in results["warnings"]:
        html += f"<p class='warning'>⚠ {w}</p>"

    html += """
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"📄 HTML report saved as {filename}")