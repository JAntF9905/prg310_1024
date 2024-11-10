import matplotlib.pyplot as plt
import numpy as np
import os
import imageio


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr


def save_frames(frames, path='frames', prefix='frame'):
    if not os.path.exists(path):
        os.makedirs(path)
    for i, frame in enumerate(frames):
        plt.figure()
        plt.bar(range(len(frame)), frame, color='blue')
        plt.title(f'Step {i+1}')
        plt.savefig(f'{path}/{prefix}{i}.png')
        plt.close()

    images = [imageio.imread(f'{path}/{prefix}{i}.png') for i in range(len(frames))]
    imageio.mimsave(f'{path}/{prefix}.gif', images, 'GIF', duration=0.5)


if __name__ == "__main__":
    arr = np.random.randint(1, 50, size=10)
    frames = list(bubble_sort(arr.copy()))
    save_frames(frames)
