# Working-with-pdf-and-images using CV2 and pypdf2
task3a
I first converted the PDF doc into jpg just to work with CV2 library
. In that case, one easily finds out the coordinates and apply gaussian blur or fill the dark
image.
task3b:
The keywords were not enough to classify reports, As i scanned
through the documents there were keywords there but it has prefix like NO and sufic like
found which can make our code obsolete. Hence I added this feature into my code to take
care of that. Other stuff were basic pattern matching to the text which made easier by the
library PyPDF2 pdfreader
