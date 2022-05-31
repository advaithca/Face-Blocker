from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle



def draw_image_after_blurring(filename):
    data =  plt.imread(filename)
    detector = MTCNN()
    result_list = detector.detect_faces(data)
    plt.imshow(data)
    ax = plt.gca()
    for result in result_list:
        x, y, width, height = result['box']
        rect = Rectangle((x, y), width, height, fill=True, color='white')
        ax.add_patch(rect)

    plt.savefig('output.jpg',dpi=90,bbox_inches='tight')
    plt.show()

filename = 'test.jpg'

draw_image_after_blurring(filename=filename)