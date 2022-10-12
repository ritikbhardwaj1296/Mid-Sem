%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

path = 'D:\Semester\Intelligent Robotics\Image1.jpeg'


img = mpimg.imread(path)
imgplot = plt.imshow(img)
plt.show()


