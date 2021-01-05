# https://www.it-swarm-ja.tech/ja/python/%e3%83%95%e3%82%a9%e3%83%ab%e3%83%80%e5%86%85%e3%81%ae%e3%81%99%e3%81%b9%e3%81%a6%e3%81%ae%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e3%82%92%e9%96%8b%e3%81%8f%e6%96%b9%e6%b3%95/1040341273/
# https://pypi.org/project/subprocess.run/
# https://www.it-swarm-ja.tech/ja/python/opencv%e3%81%a7python%e3%81%a7%e7%94%bb%e5%83%8f%e3%81%ae%e5%b9%b3%e5%9d%87%e8%89%b2%e3%82%92%e8%a6%8b%e3%81%a4%e3%81%91%e3%82%8b%e6%96%b9%e6%b3%95%e3%81%af%ef%bc%9f/831361145/
# https://aiqlab.com/tech_blog?id=204

import os
import glob
import cv2
import numpy as np
import collections
from skimage import io


path = 'data/lab'
count = 0


for filename in glob.glob(os.path.join(path, '*.jpg')):
  img =cv2.imread(filename)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  flatten = img.reshape(-1,3)

  from sklearn.cluster import KMeans
  pred = KMeans(n_clusters=4).fit(flatten)

  out = zip(pred.labels_, flatten)
  clu0 = np.array([data.tolist() for label, data in zip(pred.labels_,flatten) if label==0])
  clu1 = np.array([data.tolist() for label, data in zip(pred.labels_,flatten) if label==1])
  clu2 = np.array([data.tolist() for label, data in zip(pred.labels_,flatten) if label==2])
  clu3 = np.array([data.tolist() for label, data in zip(pred.labels_,flatten) if label==3])


  print(collections.Counter(pred.labels_))
  key = collections.Counter(pred.labels_).most_common()[0][0]
  print(str(key) + ":" + str(pred.cluster_centers_[key]))


  #画像生成
  blank = np.zeros((100,100,3))
  blank += pred.cluster_centers_[key]
  blank = blank[:, :, [2, 1, 0]]
  name = str(path)+'/cv2/'+str(count)+'.png'
  cv2.imwrite(name,blank)
  print("finish: " + filename + name)
  count += 1