

# Do imports
from fpdf import FPDF


def main():

    # Define key variables
    i_width = 216
    i_length = 279
    s_pdf_file = 'output.pdf'

    # Initialize fpdf object
    o_pdf = FPDF(format='Letter')

    # Add page #0
    o_pdf.add_page()

    #	    Add letterhead
    o_pdf.image('fig_template_NEW/Letterhead_CROPPED.png', y=0, x=0, w=i_width)

    #	    Add document title
    o_pdf.ln(70)
    o_pdf.set_font('Helvetica', '', 24)
    o_pdf.cell(w=0, h=0, align='L', txt='Document Title')
    o_pdf.ln(8)
    o_pdf.set_font('Helvetica', '', 14)
    o_pdf.cell(w=0, h=0, align='L', txt='Document Subtitle')

    # Add page #1
    o_pdf.add_page()

    #	    Add section title
    o_pdf.ln(10)
    o_pdf.set_font('Helvetica', 'U', 14)
    o_pdf.cell(w=0, h=0, align='C', txt='Section Title')
    o_pdf.ln(10)
    o_pdf.set_font('Helvetica', '', 8)
    o_pdf.cell(w=0, h=0, align='L', txt='Description providing more information about the section.')

    #	    Add one centered image
    o_pdf.image('images/puppy_0.jpg', y=40, x=73, w=i_width-146)

    #	    Add two centered images in same row
    o_pdf.image('images/bunny_0.jpg', y=120, x=33, w=i_width-146)
    o_pdf.image('images/chipmunk_0.jpg', y=120, x=113, w=i_width-146)

    #	    Add two centered images in same row
    o_pdf.image('images/raccoon_0.jpg', y=200, x=33, w=i_width-146)
    o_pdf.image('images/squirrel_0.jpg', y=200, x=113, w=i_width-146)

    # Save report
    o_pdf.output(s_pdf_file)


if __name__ == '__main__':
    main()

    