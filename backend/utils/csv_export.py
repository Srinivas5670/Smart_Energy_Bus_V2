import csv
import io


def generate_csv(history):

    output = io.StringIO()

    if not history:
        return output.getvalue()

    writer = csv.DictWriter(
        output,
        fieldnames=history[0].keys()
    )

    writer.writeheader()

    for row in history:
        writer.writerow(row)

    return output.getvalue()