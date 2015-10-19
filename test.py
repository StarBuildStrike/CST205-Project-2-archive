folder = "C:/Users/Ulysses/Documents/CST205/Project 1/Images/" #specify the path of your folder 



pictures = [] # make a list of the images 

image1 = makePicture(folder + "1.png") # load the path of the image and open the first picture
pictures.append(image1)
image2 = makePicture(folder + "2.png")  # load the path of the image and open the second picture
pictures.append(image2)
image3 = makePicture(folder + "3.png")   # load the path of the image and open the third picture
pictures.append(image3)
image4 = makePicture(folder + "4.png")   # load the path of the image and open the fourth picture
pictures.append(image4)
image5 = makePicture(folder + "5.png")   # load the path of the image and open the fifth picture
pictures.append(image5)
image6 = makePicture(folder + "6.png")   # load the path of the image and open the sixth picture
pictures.append(image6)
image7 = makePicture(folder + "7.png")   # load the path of the image and open the seventh picture
pictures.append(image7)
image8 = makePicture(folder + "8.png")   # load the path of the image and open the eight picture
pictures.append(image8)
image9 = makePicture(folder + "9.png")   # load the path of the image and open the ninth picture
pictures.append(image9)

imageWidth = getWidth(image1)  #specify the width of the image
imageHeight = getHeight(image1)  #specify the height of the image




emptyImage = makeEmptyPicture(imageWidth,imageHeight) #make a new image then specify its width and height

#then create an empty list for a three RGB pixels

redPixelList = [] # create an empty list for red pixel
greenPixelList = [] # create an empty list for green pixel
bluePixelList = [] # create an empty list for blue pixel

def findMedian(pictures): # declare a function for the median where it make the calculations for all nine images

      listLength = len(pictures) #use the len (method to get all of the pictures in the list)
      sortedValues = sorted(pictures)#after getting the images sort all the pictures
      middleIndex = (listLength/2) + 1 #use the median formula to get the median of all the nine images
      return sortedValues[middleIndex] #return the value of the median
     
      
      
    
for x in range(0, imageWidth / 2): #the loop for x which is the width of the image
  for y in range(0,imageHeight): #the loop for x which is the height of the image
    for image in range(0,9):   #the loop for all nine images 
      
    
      pixel = getPixel(pictures[image], x, y)#get the pixels for all the nine images along with the height and the width
      imgRed = getRed(pixel) #get the pixel for the red color
      imgGreen = getGreen(pixel) #get the pixel for the green color
      imgBlue = getBlue(pixel) #get the pixel for the blue color
    
      redPixelList.append(imgRed) #add the red pixels to the list
      greenPixelList.append(imgGreen) #add the green pixels to the list
      bluePixelList.append(imgBlue)  #add the blue pixels to the list
      
    newPixel = makeColor(findMedian(redPixelList),findMedian(greenPixelList),findMedian(bluePixelList)) #set the red, green and blue pixel values on to the new image
    getPixel(emptyImage,x,y).setColor(newPixel) #get the pixel for the new image and fill it with RGB colors
    color= getColor(getPixel(image1, x, y))
    setColor(getPixel(emptyImage, x, y), color)
    setColor(getPixel(emptyImage,imageWidth-x-1, y),color)
    
    redPixelList = [] #temporary list for red pixels which is now being deleted
    greenPixelList = [] #temporary list for green pixels which is now being deleted
    bluePixelList = [] #temporary list for blue pixels which is now being deleted
show(emptyImage) #finally, show the new image produced. 
   


  



  

  
  
  
  


