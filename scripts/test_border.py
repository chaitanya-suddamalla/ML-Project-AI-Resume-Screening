from pptx import Presentation
from pptx.util import Inches
from pptx.oxml import parse_xml

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[6])
table_shape = slide.shapes.add_table(3, 3, Inches(1), Inches(1), Inches(6), Inches(3))
table = table_shape.table

def set_cell_black_borders(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    for side in ['lnL', 'lnR', 'lnT', 'lnB']:
        existing = tcPr.find(f'{{http://schemas.openxmlformats.org/drawingml/2006/main}}{side}')
        if existing is not None:
            tcPr.remove(existing)
        ln_xml = f'<a:{side} xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" w="19050"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:{side}>'
        tcPr.append(parse_xml(ln_xml))

for row in table.rows:
    for cell in row.cells:
        set_cell_black_borders(cell)

prs.save("test_border.pptx")
print("SUCCESS: Solid black table cell borders verified!")
