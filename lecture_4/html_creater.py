from cgitb import html
from user_interface import temper_view
from user_interface import press_view

def create(device = 1):
#     t, p = data ver 2
    style = 'style="font-size:22px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '   <p {}>Temperature: {}  C</p>\n'\
        .format(style, temper_view(device)) ## t = temper_view(device)
    html += '   <p {}>Pressure: {}  mmHg</p>\n'\
        .format(style, press_view(device)) ## p = press_view(device)
    html += '   </body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)

    return html

