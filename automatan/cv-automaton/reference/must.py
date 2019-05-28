from SimpleCV import *
cam = Camera()
display = Display()
# load the cascades
stache = Image("mustache.png", sample=True) # load the stache
mask = stache.createAlphaMask().invert() # load the stache mask
while display.isNotDone():
    img = cam.getImage()
    faces = img.findHaarFeatures("face.xml") #find faces
    if faces: # if we have a face
        faces.sortArea() #get the biggest one
        face = faces[-1] #last element
        myFace = face.crop() # get the face image
        noses = myFace.findHaarFeatures("nose.xml") #find the nose
        if noses:# if we have a nose
          noses.sortArea()
          nose = noses[-1] # get the biggest
          # these get the upper left corner of the face/nose with respect to original image
          xf = face.x -(face.width()/2)
          yf = face.y -(face.height()/2)
          xm = nose.x -(nose.width()/2)
          ym = nose.y -(nose.height()/2)
          #calculate the mustache position
          xmust = xf+xm-(stache.width/2)+(nose.width()/2)
          ymust = yf+ym+(2*nose.height()/3)
          #blit the stache/mask onto the image
          img = img.blit(stache, pos=(xmust,ymust), mask = mask)

img.save(display) #display