import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def celanDataset(arr):
    c = 0
    lst = []
    k = 25
    z = len(arr)
    for i in range(len(arr)):
        if(i >= len(arr)):
            break

        if(c == k and arr[i] == 0):
            arr = np.delete(arr,lst)
            lst = []
            c = 0
            i -= k + 1
            continue

        elif(arr[i] <= 0.001):
            c += 1
            lst.append(i)
        else:
            lst = []
            c = 0
    return  arr

def heatMap(arr):
    sns.color_palette("rocket", as_cmap=True)
    fig, ax = plt.subplots(figsize=(20, 150))

    arr = np.array(arr)
    arr = celanDataset(arr)

    print(arr.shape)

    df = pd.DataFrame({"Phrases": arr}, )

    sns.heatmap(df, fmt="g", vmin=0, vmax=1,ax = ax,xticklabels=False)

    plt.show()