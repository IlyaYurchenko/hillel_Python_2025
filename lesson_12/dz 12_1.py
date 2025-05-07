import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    is_tag = False
    cleaned_html = ''

    for char in html:
        if char == '<':
            is_tag = True
        elif char == '>':
            is_tag = False
            continue

        if not is_tag:
            cleaned_html += char

    with open('cleaned.txt', 'w+', encoding='utf-8') as file_cleaned:
        file_cleaned.write(cleaned_html)

delete_html_tags('draft.html', result_file='cleaned.txt')
