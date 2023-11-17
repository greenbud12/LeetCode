word = 'Engineer'
wordLen = len(word)

width = 0.05 # 
height = 0.1 # ~0.08-0.2

areaX = int((1 - width) * 32)
areaY = int((1 - height) * 17)
print(areaX, areaY)

print('\n'.join([
  ''.join([
    (word[(x-y)%wordLen] if((x*width)**2+(y*height)**2-1)**3-(x*width)**2*(y*height)**3<=0 else' ') 
    for x in range(-areaX,areaX)
  ]) 
  for y in range(areaY,-areaY,-1)
]))
