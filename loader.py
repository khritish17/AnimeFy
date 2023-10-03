import animefy as anfy
import hierarchy_builder as hb
import color_assigner as ca

def loader(image = ""):
    ANFY = anfy.Animefy()
    image_matrix = ANFY.load_image(image)
    contours, hierarchy = ANFY.getContours() 
    print(hierarchy)
    H_BUILDER = hb.hierarchy_Tree(hierarchy)
    root_nodes = H_BUILDER.retrieve_root()
    ca.Assigner(contours, root_nodes, image_matrix)
    # print(image.shape)
    for root in root_nodes:
        print("ID:{}, pixels:{}".format(root.id, root.pixels))

loader("6.png")