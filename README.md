# OCR-EXPERIMENT
My first time serious hobby on OCR. Inspired by Mark Hollow

# Dataset
https://books.google.co.th/books?id=BrcTAAAAQAAJ&pg=PP7#v=onepage&q&f=false

# Strategies
1. Text detection use `CTPN`. https://github.com/eragonruan/text-detection-ctpn
1. Train the `model`
1. Post processing by using `language modeling`

# Steps to get the stripe
It is consist of multiple projects read carefully.

1. Get the `pngs` individual page by running `python pdf2images.py`
1. Go back to `text-detection-ctpn`. Then get the `detected coordinates` of each pages
1. Run `tear_down_page('p23-181.png', 'res/p23-181.txt', 'cropped_sentences')`


# Thanks
- https://github.com/KMKnation/Four-Point-Invoice-Transform-with-OpenCV

# Future Improvements
- [x] cropped image must has offset to cover puncture and tone sign
- [x] remove black horizontal edge. The consequence of adding offset cover tone sign
