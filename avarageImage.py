# 参考サイト
# https://www.it-swarm-ja.tech/ja/python/opencv%e3%81%a7python%e3%81%a7%e7%94%bb%e5%83%8f%e3%81%ae%e5%b9%b3%e5%9d%87%e8%89%b2%e3%82%92%e8%a6%8b%e3%81%a4%e3%81%91%e3%82%8b%e6%96%b9%e6%b3%95%e3%81%af%ef%bc%9f/831361145/
# http://pineplanter.moo.jp/non-it-salaryman/2019/03/24/post-7337

import os
import cv2
import glob
import numpy as np
from skimage import io
import collections

path = 'data/subAccount/tweet_media'
count = 0

from sklearn.cluster import KMeans
for filename in glob.glob(os.path.join(path, '*.jpg')):
  img = cv2.imread(filename)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  flatten = img.reshape(-1,3)
  pred = KMeans(n_clusters=5).fit(flatten)

  key1 = collections.Counter(pred.labels_).most_common()[0][0]
  key2 = collections.Counter(pred.labels_).most_common()[1][0]
  key3 = collections.Counter(pred.labels_).most_common()[2][0]
  key4 = collections.Counter(pred.labels_).most_common()[3][0]
  key5 = collections.Counter(pred.labels_).most_common()[4][0]

  color1 = pred.cluster_centers_[key1]
  color1_size = collections.Counter(pred.labels_)[key1]

  color2 = pred.cluster_centers_[key2]
  color2_size = collections.Counter(pred.labels_)[key2]

  color3 = pred.cluster_centers_[key3]
  color3_size = collections.Counter(pred.labels_)[key3]

  color4 = pred.cluster_centers_[key4]
  color4_size = collections.Counter(pred.labels_)[key4]
  
  color5 = pred.cluster_centers_[key5]
  color5_size = collections.Counter(pred.labels_)[key5]

  total_size = color1_size + color2_size + color3_size + color4_size + color5_size

  color1_per = int( color1_size / total_size * 100 )
  color2_per = int( color2_size / total_size * 100 )
  color3_per = int( color3_size / total_size * 100 )
  color4_per = int( color4_size / total_size * 100 )
  color5_per = int( color5_size / total_size * 100 )
  # #画像生成 二次元配列 宣言
  blank = np.zeros((100,100,3))
  c = 0
  for i in range(len(blank)):
    if c < color1_per:
      blank[i] = color1
    elif c < color1_per + color2_per:
      blank[i] = color2
    elif c < color1_per + color2_per + color3_per:
      blank[i] = color3
    elif c < color1_per + color2_per + color3_per + color4_per:
      blank[i] = color4
    else:
      blank[i] = color5
    c += 1

  blank = blank[:, :, [2, 1, 0]]

  cv2.imwrite(str(path)+'/cv2_3/'+str(count)+'.png',blank)
  count += 1
  print(filename + '  finishied!')