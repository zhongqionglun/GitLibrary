# -*-coding:UTF-8-*-

import pickle, json

d = dict(name='Bob', age=20, score=80)
d['name'] = 'Bill'
print(pickle.dumps(d))

f = open('dump.txt', 'w')
print(pickle.dump(d, f))
f.close()
f = open('dump.txt', 'r')
d = pickle.load(f)
f.close()
print(d)
