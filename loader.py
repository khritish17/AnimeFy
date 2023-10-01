import animefy as anfy
import hierarchy_builder as hb

def loader(image = ""):
    ANFY = anfy.Animefy()
    ANFY.load_image(image)
    contours, hierarchy = ANFY.getContours() 
    H_BUILDER = hb.hierarchy_Tree(hierarchy)
    root_node = H_BUILDER.retrieve_root()
    

loader("2.jpg")