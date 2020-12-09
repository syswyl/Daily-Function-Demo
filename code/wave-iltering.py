import cv2 as cv
import numpy as np
import math

def getClosenessWeight(sigma_g, H, W):
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    closeWeight = np.exp(-0.5*np.power(r, 2) + np.power(c, 2) / math.pow(sigma_g, 2))
    return closeWeight

def bfltGray(I, H, W, sigma_g, sigma_d):
    # 构建空间距离权重模板
    closenessWeight = getClosenessWeight(sigma_g, H, W)
    # 模板的中心点位置
    cH = (H - 1) // 2
    cW = (W - 1) // 2
    # 图像矩阵的行数和列数
    rows, cols = I.shape
    # 双边滤波后的结果
    bflGrayImage = np.zeros(I.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = I[r][c]
            # 判断边界
            rTop = 0 if r - cH < 0 else r - cH
            rBottom = rows - 1 if r + cH > rows - 1 else r + cH
            cLeft = 0 if c - cW < 0 else c - cW
            cRight = cols - 1 if c + cW > cols - 1 else c + cW
            # 权重模板作用的区域
            region = I[rTop:rBottom+1, cLeft:cRight+1]
            # 构建灰度值相似性的权重因子
            similarityWeightTemp = np.exp(-0.5*np.power(region-pixel, 2.0) / math.pow(sigma_d, 2))
            closenessWeightTemp = closenessWeight[rTop-r+cH:rBottom-r+cH+1, cLeft-c+cW:cRight-c+cW+1]
            # 两个权重模板相乘
            weightTemp= similarityWeightTemp * closenessWeightTemp
            # 归一化权重模板
            weightTemp = weightTemp / np.sum(weightTemp)
            # 权重模板和对应的邻域值相乘求和
            bflGrayImage[r][c] = np.sum(region * weightTemp)
    return bflGrayImage


if __name__ == '__main__':
    image = cv.imread('./JPEGImages/100194.jpg', 0)
    print(image.shape)
    # 显示原图
    cv.imshow("image", image)
    # 将灰度值归一化
    image = image / 255
    # 双边滤波
    bfltImage = bfltGray(image, 30, 30, 150, 0.1)
    # 显示双边滤波的结果
    cv.imshow("bflt", bfltImage)

    # gauImage = cv.GaussianBlur(image, (51, 51), 5)
    # cv.imshow("gaussian", gauImage)
    # blurImage = cv.blur(image, (51, 51))
    # cv.imshow("blur", blurImage)
    cv.waitKey(0)
    cv.destroyAllWindows()
