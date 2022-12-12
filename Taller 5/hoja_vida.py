import pdfkit
import jinja2
from datetime import datetime
import wkhtmltopdf

data = {}
data['nombre'] = 'Anthony Emiliano'
data['hora'] = '60'
data['fecha'] = datetime.now().strftime("%m %b %Y")


content = {'data': data}

template_loader = jinja2.FileSystemLoader('D:/Anthony/tecnicas_programcionA1/hoja de vida')
template_env = jinja2.Environment(loader=template_loader)

template_html = 'index.html'
template = template_env.get_template(template_html)
output_text = template.render(content)
path_wkhtmltopdf = b"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
output_pdf = 'certificado.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config)