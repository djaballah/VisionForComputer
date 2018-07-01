import cv2
import numpy as np
from matplotlib import pyplot as plt

def average_filter(img, kernel_size):
    '''
    Apply the average filter on img

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :param kernel_size: dimension of the kernel matrix
    :type: int
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    '''

    assert isinstance(img, np.ndarray)
    kernel_size = (kernel_size, kernel_size)
    filtered_img = cv2.blur(src= img, ksize= kernel_size)
    return filtered_img

def median_filter(img, kernel_dimension):
    """
    Apply the median filter on img

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :param kernel_size: dimension of the kernel matrix
    :type: int
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    """

    assert isinstance(img, np.ndarray)
    filtered_image = cv2.medianBlur(img, kernel_dimension)
    return filtered_image

def erosion_filter(img, kernel_size):
    """
    Apply the erosion filter on img

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :param kernel_size: dimension of the kernel matrix
    :type: int
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    """
    assert isinstance(img, np.ndarray)
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    filtered_image = cv2.erode(img, kernel)
    return filtered_image

def dilation_filter(img, kernel_size):
    """
    Apply the dilation filter on img

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :param kernel_size: dimension of the kernel matrix
    :type: int
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    """
    assert isinstance(img, np.ndarray)
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    filtered_image = cv2.dilate(img, kernel)
    return filtered_image



def morphological_filter(img, filter, kernel_size):
    """
    Apply the dilation filter on img

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :param kernel_size: dimension of the kernel matrix
    :type: int
    :filter: Type of morphological filter
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    """
    assert isinstance(img, np.ndarray)
    kernel = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    filtered_image = cv2.morphologyEx(img, filter , kernel)
    return filtered_image

def laplacian_gradient(img):
    """
    Calculate the laplacian of the image

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    """
    assert isinstance(img, np.ndarray)
    #laplacian = cv2.Laplacian(src=img, ddepth=cv2.CV_64F)
    #laplacian = cv2.pencilSketch(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    img_blend = cv2.divide(img_gray, img_blur, scale=256)
    img_bg = cv2.imread("gray_bg.jpg", cv2.CV_8UC1)
    img_bg = cv2.resize(img_bg, (400, 400))
    img_blend = cv2.multiply(img_blend, img_bg, scale=1. / 256)
    img_blend = cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)
    cv2.imwrite("result.jpg", img_blend)
    return img_blend

def edge_detector(img):
    """
    Detecte Edges of img

    :param img: a multidimensional array representing the image
    :type: np.ndarray
    :return: a multidimensional array representing the filtered image
    :type: np.ndaaray
    """
    assert isinstance(img, np.ndarray)
    filtered_image = cv2.Canny(img, 100, 200)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_GRAY2RGB)
    return filtered_image

def track_object(img):
    """
    Track object within an image
    :param img: A Two dimension image
    :type: np.ndarray
    :return:
    """
    assert isinstance(img, np.ndarray)
    filtered_image = median_filter(img, 3)
    upper_black = np.array([0, 0, 0])
    lower_black = np.array([57, 36, 48])
    black_mask = cv2.inRange(filtered_image, upper_black, lower_black)
    upper_red = np.array([0, 0, 150])
    lower_red = np.array([143, 115, 234])
    red_mask = cv2.inRange(filtered_image, upper_red, lower_red)
    filtered_image = black_mask + red_mask

    #filtered_image = cv2.bitwise_and(filtered_image, filtered_image, mask)
    #filtered_image = cv2.inRange(img, upper_red, lower_red)
    filtered_image = erosion_filter(filtered_image, 3)
    filtered_image = dilation_filter(filtered_image, 3)
    filtered_image = dilation_filter(filtered_image, 3)
    filtered_image = erosion_filter(filtered_image, 3)
    try:
        image, contours, hierarchy = cv2.findContours(filtered_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        #big = 0
        #big_cnt = 0
        #for cnt in contours:
            #if len(cnt) > big:
                #big = len(cnt)
                #big_cnt = cnt
        contours = sorted(contours, key= cv2.contourArea, reverse=True)
        for cnt in contours[:2]:
            m = cv2.moments(cnt)
            area = m['m00']
            if area > 40:
                cx = int(m['m10'] / m['m00'])
                cy = int(m['m01'] / m['m00'])
                cv2.circle(img, (cx, cy), 20, (0, 255, 0), -1)
    except ZeroDivisionError:
        pass
    return img


def comp(kernel):
    center = kernel[1][1]
    l = []
    for i, line in enumerate(kernel):
        for j,col in enumerate(line):
            if (j == 1 and i == 1):
                l.append(-1)
                continue
            if center >= col:
                l.append(1)
            else:
                l.append(0)
    l = np.array(l)
    l = l.reshape((3, 3))
    """
    binary_vector = []
    binary_vector.append(l[0][1])
    binary_vector.append(l[0][0])
    binary_vector.append(l[1][0])
    binary_vector.append(l[2][0])
    binary_vector.append(l[2][1])
    binary_vector.append(l[2][2])
    binary_vector.append(l[2][1])
    binary_vector.append(l[2][0])
    binary_vector = list(reversed(binary_vector))
    """
    binary_vector = []
    binary_vector.append(l[0][0])
    binary_vector.append(l[0][1])
    binary_vector.append(l[0][2])
    binary_vector.append(l[1][2])
    binary_vector.append(l[2][2])
    binary_vector.append(l[2][1])
    binary_vector.append(l[2][0])
    binary_vector.append(l[1][0])
    #binary_vector = list(reversed(binary_vector))
    sum_ = 0
    for i, val in enumerate(binary_vector):
        sum_ += pow(2, i) * val
    return sum_


def lbp(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height = img.shape[0]
    width = img.shape[1]
    lbp_img = np.zeros((height -2, width - 2), np.uint8)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            l = []
            for ind in range(i-1, i + 2):
                for jnd in range(j-1, j + 2):
                    l.append(img[ind][jnd])
            kernel = np.array(l)
            kernel = kernel.reshape((3, 3))
            val = comp(kernel)
            lbp_img[i-1][j-1] = val
    lbp_img = cv2.cvtColor(lbp_img, cv2.COLOR_GRAY2RGB)
    return lbp_img

def normalize_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    max_ = np.max(img)
    min_ = np.min(img)
    height = img.shape[0]
    width = img.shape[1]
    for i in range(height):
        for j in range(width):
            val = img[i][j]
            val = 255 * (val - min_)
            val = val // (max_ - min_)
            img[i][j] = val
    return img

def make_histogram(img, hist_name):
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    # plt.legend(('cdf', 'histogram'), loc='upper left')
    # plt.show()
    plt.savefig(hist_name)
    plt.clf()
    plt.cla()
    plt.close()
    hist = cv2.imread(hist_name)
    return hist

def compare_img_hist(img1, img2):
    lbp_hist1 = cv2.calcHist([img1.flatten()], [0], None, [5], [0, 256])
    lbp_hist2 = cv2.calcHist([img2.flatten()], [0], None, [5], [0, 256])
    res = cv2.compareHist(lbp_hist1, lbp_hist2, cv2.HISTCMP_CHISQR)
    return res

