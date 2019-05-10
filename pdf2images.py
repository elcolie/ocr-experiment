import fitz


def main():
    """
    Get then PNG pictures from the Dr. Bradley scanned by Google Inc.
    :return:
    """
    doc = fitz.open("thailaw-by-dr-bradley.pdf")
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:  # this is GRAY or RGB
                pix.writePNG("p%s-%s.png" % (i, xref))
            else:  # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG("p%s-%s.png" % (i, xref))
                pix1 = None
            pix = None


if __name__ == '__main__':
    main()
