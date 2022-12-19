# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(4)) 

from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()