import animefy as anfy

def loader(image = ""):
    ANFY = anfy.Animefy()
    ANFY.load_image(image)
    # thresh = ANFY.threshold()
    # anfy.display(thresh)
    print(len(ANFY.getContours()))

loader("3.jpg")