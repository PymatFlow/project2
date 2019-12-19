
from annoy import AnnoyIndex
 
file = "glove.6B.50d.txt"
content = []

with open(file) as f:
    content = f.readlines()
 
content2 = [x.split(" ") for x in content]
 
t = AnnoyIndex(50,'angular') 
idx = 0
terms = [i[0] for i in content2]
for i in content2:
  vec = [float(a) for a in i[1:]]
  #print(len(vec))
  t.add_item(idx, vec)
  idx = idx + 1
 
t.build(10) # 10 trees

near = t.get_nns_by_item(0, 10) # nearest 10 terms
nearWords = [terms[i] for i in near]
print(nearWords)