import aspose.slides as slides
import aspose.words as aw
import io

# The path to source files directory
filepath = r"C:\Users\wouth\OneDrive - Hogeschool VIVES\Bureaublad\prutsen\ "
filepath = filepath[-1:]
# Load the Aspose.Slides license in your application
pptxLicense = slides.License()
pptxLicense.set_license(filepath + "Aspose.Total.lic")
    
# Load the Aspose.Words license in your application
wordsLicense = aw.License()
wordsLicense.set_license(filepath + "Aspose.Total.lic")

# Create the Presentation object to load the source presentation file
srcPresentation = slides.Presentation(filepath + "Fiche 8 Wat is uw adres.pptx")
    
# Create stream object to hold intermediate HTML
doc_stream = io.BytesIO()
    
# Convert the PPTX to HTML and save in stream
srcPresentation.save(doc_stream, slides.export.SaveFormat.HTML)   

# Set the stream position to 0
doc_stream.seek(0)
    
# Load the HTML from stream
wordDocument = aw.Document(doc_stream)

# Close the stream now as it is no longer needed because the document is in memory
doc_stream.close()
    
# Save the document with comments
wordDocument.save("PptxToWord.docx")
   
print ("PPTX is converted to DOCX")