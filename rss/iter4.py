# pdf = FPDF()
# pdf.add_page()

# def toPdf(item, pdf_path, media):

#     pdf.set_font('Arial', 'B', 16)
#     title = item.title
#     print(title)
#     pdf.cell(40, 10, ln=1, txt=title)
#     pdf.set_font('Arial', size=14)
#     published = item.published
#     pdf.cell(10, 10, ln=2, txt=published)
#     description = getDescription(item.description)
#     pdf.cell(10, 10, ln=3, txt=description)

#     rand = random.randint(1, 120)
#     if not os.path.exists('images/'):
#         os.makedirs('images/')
#     filename_ = 'images/' + str(rand) + '.jpg'
#     urllib.request.urlretrieve(media, filename_)
    
#     pdf.image(filename_)

#     # name_ = item.title.split()[1]
#     if not os.path.exists(pdf_path):
#         os.makedirs(pdf_path)
#     outfile = pdf_path + 'news' + '.pdf'
#     pdf.output(r'outfile', 'F')
# import dominate
# from dominate.tags import *


# doc = dominate.document(title='HTML document')

# with doc:
#     with div():
#         h2("A Louisiana woman has been arrested for selling $20 fake doctor&amp;#39;s notes to students trying to skip class")
#         p("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
#         # img(src=os.path.abspath(filename_))
        
    
# with open('test.html', 'w') as f:
#             f.write(str(doc))

import os

print(os.getcwd())