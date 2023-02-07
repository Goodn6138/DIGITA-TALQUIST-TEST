from colorthief import ColorThief
import matplotlib.pyplot as plt

path = 'blood_drop.jpg'

ct = ColorThief(path)
dominant_color = ct.get_color(quality =1)

print(dominant_color)
plt.imshow([[dominant_color]])
palette = ct.get_palette(color_count = 5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()
