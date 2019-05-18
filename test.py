import matplotlib.pyplot as plt
fig = plt.figure()
#plot sth
plt.savefig('test.png')

html = 'Some html head' + '<img src=\'test.png\'>' + 'Some more html'

with open('test.html','w') as f:
    f.write(html)
