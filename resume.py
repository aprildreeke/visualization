import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Communicator', 'Collaborator', 'Systems thinker', 'Organized',  'Creative', 
                'Funny', 'Adapts')
y_pos = np.arange(len(objects))
performance = [5,5,5,5,5,5,5]
 
plt.bar(y_pos, performance, align='center', alpha=0.3, color='g')
plt.yticks([1, 2, 3, 4], ['Familiar', 'Good', 'Great', 'Excellent'])
plt.xticks(y_pos, objects, rotation = 50)
plt.tick_params(axis='y', which='major', labelsize=8, length = 1/500)
plt.tick_params(axis='x', which='major', labelsize=11)
plt.title('Off the Chart Characteristics')
 
plt.show()
