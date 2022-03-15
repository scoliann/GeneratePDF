This script demonstrates how to programatically generate a pdf.

## Inspiration

I can imagine many future projects that have a report component where data is visualized in an easily accessible format.  To facilitate development of these projects, I created the `example.py` script to serve as a reference demonstrating basic pdf generation functionality.

## Setup

The steps to setup generation of a pdf file are as follows:
1.  Create conda environment with `conda env create -f environment.yml`
2.  Create letterhead
    - Log into [Adobe Creative Cloud Express](https://express.adobe.com/sp/projects)
    - Design letterhead
    - Download letterhead as image file
    - Crop relevant section of letterhead and save as separate file

## Running the Code

To run the code do the following:
1.  `python example.py`

## Notes

All images in the `image` directory have the same length and height.  This simplifies the calculations for how they should be placed in the report.  For more complex pdfs, it might be advantageous to make all image files have the same length and/or height.

## Resources

[This YouTube video](https://www.youtube.com/watch?v=UmN2_R4KEg8) served as my initial reference explaining how to use the `fpdf2` python package to create pdf files.