from source.model.chunks.Chunk import Chunk
import numpy as np
import math


def apply_hough_filter(chunk, d_rau=1, d_theta=math.pi / 180):
    # binarize chunk
    bin_chunk = __threshold_binarize_filter(chunk, 0)

    # for each not null pixel, evaluate in 0 - PI range with d_theta step the rau value rounded with the d_rau step.
    acc_mat = __get_accumulation_matrix(bin_chunk, d_rau, d_theta)

    # find the theta,rau configurations for which the length of the vector points is the max to create the hough_chunk
    return __hough_chunk_filter(chunk, acc_mat)


def __hough_chunk_filter(chunk, acc_mat):
    # initialize the hough chunk
    hough_chunk = Chunk(chunk.coords, chunk.size)

    # iterate the acc_mat
    for key in acc_mat:
        if len(acc_mat[key]) > 50: # TODO random value
            for coord in acc_mat[key]:
                hough_chunk.chunk[coord[0]][coord[1]] = 1

    return hough_chunk


def __get_accumulation_matrix(bin_chunk, d_rau, d_theta):
    # init accumulation matrix
    acc_mat = {}

    # iterate the binarized chunk
    for i in range(bin_chunk.size):
        for j in range(bin_chunk.size):
            # if a pixel is found
            if bin_chunk.chunk[i][j] == 1:
                for k in np.arange(0, math.pi + d_theta, d_theta):
                    # "exact" rau value
                    rau = i * math.cos(k) + j * math.sin(k)

                    # rau value rounded with the d_rau step
                    rau = round(rau / d_rau) * d_rau

                    # check if key exists
                    if (rau, k) in acc_mat.keys():
                        # append the pixel coordinates for this key configuration
                        acc_mat[(rau, k)].append((i, j))
                    else:
                        acc_mat[(rau, k)] = [(i, j)]
    return acc_mat


def __threshold_binarize_filter(chunk, threshold):
    bin_chunk = Chunk(chunk.coords, chunk.size)
    for i in range(chunk.size):
        for j in range(chunk.size):
            if chunk.chunk[i][j] > threshold:
                bin_chunk.chunk[i][j] = 1
    return bin_chunk
