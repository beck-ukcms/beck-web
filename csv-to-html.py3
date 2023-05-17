#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import csv
import os

with open("input.csv", "r") as csv_f:
    reader=csv.reader(csv_f)
    data=list(reader)

os.system('cp header.html output.html')
html_footer='        </div> <!--End all topics-->\n'
'    </div> <!--End container holding collapsible topics-->\n'
'</body>\n'
'</html>'

with open("output.html","a") as html_f:
    counta=0
    countb=1
    for row in data:
        if row[1]=="" and row[0]!="":
            if counta!=0:
                html_f.write('</div></div>\n')
            html_f.write('<!--Topic '+str(counta+1)+'-->\n'
            '<input id="'+str(counta+1)+'" class="toggle" type="checkbox">\n'
            '  <label for="'+str(counta+1)+'" class="lbl-toggle lbl-toggle-bold">'+row[0]+'</label>\n'
            '    <div class="collapsible-content"> <div class="content-inner">\n'
            '      <!-- Begin topic '+str(counta+1)+' sub-topics -->\n'
            '      <div class="wrap-collabsible">\n')
            countb=1
            counta=counta+1
        elif row[1]!="":
            html_f.write('<input id="')
            html_f.write(str(counta)+'.'+str(countb))
            html_f.write('" class="toggle" type="checkbox">\n'
            '<label for="')
            html_f.write(str(counta)+'.'+str(countb))
            html_f.write('" class="lbl-toggle">'+row[0]+'</label>\n'
            '<div class="collapsible-content">\n'
            '<div class="content-inner">\n<p>'+row[1]+'</p>\n'
            '</div>\n'
            '</div>\n')
            countb=countb+1
        else:
            countb=countb
    html_f.write(html_footer)

