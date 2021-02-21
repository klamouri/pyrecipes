def format_measurements(text, measurements):
    for m in measurements:
        if m in text:
            return text[: text.find(m) + len(m)] + " " + text[text.find(m) + len(m) :]
    return text

def format_nutrition(line):
    if (len(line) == 2) :
        return line.contents[0].text + " " + line.contents[1].text
    else:
        return line.text