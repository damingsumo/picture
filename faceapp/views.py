from django.shortcuts import render
import numpy as np
import cv2 as cv
# Create your views here.

from django.http import HttpResponse


def index(request):
    img = cv.imread('D:/face.jpg')

    return HttpResponse(img)

    # height, width,channel = img.shape
    # HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # lower_black = np.array([0,0,0])
    # upper_black = np.array([180, 40, 46])
    # mask = cv.inRange(HSV,lower_black,upper_black)
    #
    # cv.imwrite('out.jpg', mask)

    # HSV1 = cv.merge([b, g, r])
    # MergedImg1 = cv.cvtColor(HSV1, cv.COLOR_HSV2BGR)
    # cv.imwrite('out.jpg', HSV1)

    # for i in range(0,img.height):
    #     for j in range(0, img.width):
    #
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # height,width,channel = img.shape
    # for i in range(0, height):
    #     for j in range(0, width):
    #         for k in range(0, channel):
    #             t = img[i, j, k]
    #
    #
    #
    #
    #             # t = t+50 if t>150 else t
    #
    #             img[i, j, k] = t
    # return HttpResponse(img)
    # img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
    # cv2.imwrite('out.jpg', img)
