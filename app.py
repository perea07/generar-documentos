import pandas as pd
from docxtpl import DocxTemplate

doc = DocxTemplate('template.docx')
df = pd.read_excel('names.xlsx')
names = df['names']

for name in names:
    constants = {'name': name}
    doc.render(constants)
    doc.save(f'users/{name}.docx')

print('finished work ✅.')
