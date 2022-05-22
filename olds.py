

def extract_year(line):
    """Extract the year in a bibtex line."""
    start = line.find("{") + 1
    end = line.find("}")
    return line[start:end]


def get_bibtex_year(bibtex_lies, label):
    """Return the year given in the bibtex file."""
    lines = get_bibtex_lines(bibtex_lines, label)
    for line in lines:
        if "year" in line:
            year = extract_year(line)
            return year
    return None

new_json = []
for label in labels:
    small_json = get_json(json_bib, label)
    year = get_bibtex_year(bibtex_lines, label)
    if year:
        print("fix date for", label)
        small_json["date"] = year
    new_json.append(small_json)

write_json_file(new_json, "new_mazhe.json", pretty=True)
