import io
import sys
from docx import Document


chars = ['.', ',', '!', '?', ';', ':', '\'', '"', '(', ')', '…', '—', '–']
output_file_name = 'output.txt'


def get_paragraphs_text(document):
    text = ''
    for paragraph in document.paragraphs:
        text += paragraph.text
    return text


def main(input_file_name):
    document = Document(input_file_name)
    text = get_paragraphs_text(document)

    with io.open(output_file_name, 'w', encoding='utf8') as output_file:
        for char in chars:
            output_file.write('Символ \'%c\' встречается в тексте %d раз\n' % (char, text.count(char)))
        output_file.close()


if len(sys.argv) != 2:
    print('Invalid arguments. Please enter: <script name> <input file>')
else:
    main(sys.argv[1])
