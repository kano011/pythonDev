# 参考サイト
# https://www.it-swarm-ja.tech/ja/python/opencv%e3%81%a7python%e3%81%a7%e7%94%bb%e5%83%8f%e3%81%ae%e5%b9%b3%e5%9d%87%e8%89%b2%e3%82%92%e8%a6%8b%e3%81%a4%e3%81%91%e3%82%8b%e6%96%b9%e6%b3%95%e3%81%af%ef%bc%9f/831361145/
# http://pineplanter.moo.jp/non-it-salaryman/2019/03/24/post-7337

import cv2
import numpy as np
from skimage import io
import collections


img =cv2.imread('data/SoySyoy/image/1070341900639469569-DtqeRy0VsAALaqL.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


flatten = img.reshape(-1,3)

from sklearn.cluster import KMeans
pred = KMeans(n_clusters=10).fit(flatten)


key1 = collections.Counter(pred.labels_).most_common()[0][0]
key2 = collections.Counter(pred.labels_).most_common()[1][0]
key3 = collections.Counter(pred.labels_).most_common()[2][0]

color1 = pred.cluster_centers_[key1]
color1_size = collections.Counter(pred.labels_)[key1]

color2 = pred.cluster_centers_[key2]
color2_size = collections.Counter(pred.labels_)[key2]

color3 = pred.cluster_centers_[key3]
color3_size = collections.Counter(pred.labels_)[key3]

total_size = color1_size + color2_size + color3_size

color1_per = int( color1_size / total_size * 100 )
color2_per = int( color2_size / total_size * 100 )
color3_per = int( color3_size / total_size * 100 )

# #画像生成 二次元配列 宣言
blank = np.zeros((100,100,3))
c = 0
for i in range(len(blank)):
  if c < color1_per:
    blank[i] = color1
  elif c < color1_per + color2_per:
    blank[i] = color2
  else:
    blank[i] = color3
  c += 1

cv2.imwrite('test.png',blank)
print('finish')