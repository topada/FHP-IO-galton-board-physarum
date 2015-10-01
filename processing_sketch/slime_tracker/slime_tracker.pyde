#libs
add_library('video')
add_library('opencv_processing')


#globals
video = None
opencv = None
font = None

connect = []
contours = []
c_oat = []

a = 0
c = 0


#vid size
w = 500
h = 500

def setup():
    #ref globals
    global video
    global opencv
    global font
    
    #misc
    smooth()
    
    #font
    font = createFont("Arial", 12)
    textFont(font)
    textAlign(LEFT)
    
    #sketch
    size(int(1.5*w), h)
    
    #vid/opencv setup
    video = Movie(this, "slimelapse_extended.mov")
    opencv = OpenCV(this, w,h)
    
    #Background Substraction
    opencv.startBackgroundSubtraction(20, 10, 0.7)
    
    #start
    frameRate(50);
    video.loop()
    video.play()

def draw():
    global a
    global c
    global c_oat
    
    # counter
    c = c + 1
    
    fill(255)
    
    ### (1)
    ## Capture
    opencv.useColor(RGB)
    opencv.loadImage(video)
    
    ## Filter
    ## Analyse
    
    ## Display
    snap1 = opencv.getSnapshot()
    image(snap1, 0, 0, snap1.width, snap1.height)
    text("composite video", 10, 15)
    
    ### (2)
    ## Capture
    opencv.useColor(HSB)
    opencv.loadImage(video)
    
    ## Filter
    opencv.contrast(2)
    opencv.setGray(opencv.getH().clone())
    opencv.inRange(24,30) #(24,30)
    opencv.erode()
    opencv.dilate()
    snap2 = opencv.getSnapshot()
    
    ## Analyse
    contours = opencv.findContours(False, True)
    noFill()
    stroke(230,230,20)
    strokeWeight(1)
    smooth()
    for contour in contours:
        r = contour.getBoundingBox()
        if r.width > 30:
            contour.draw()
    
    
    ## Display
    #snap2 = opencv.getSnapshot() #above
    image(snap2, snap2.width, 0, snap2.width/2, snap2.height/2)
    text("snap2: physarum detection", snap1.width+10, 15)
    
    
    ### (3)
    ## Capture
    opencv.useColor(HSB)
    opencv.loadImage(video)
    
    
    ## Filter
    opencv.setGray(opencv.getB().clone())
    opencv.brightness(-10)
    opencv.threshold(160)
    opencv.erode()
    opencv.dilate()
    opencv.dilate()

    ## Analyse
    if(c < 2):        
        c_oat = opencv.findContours(False, True)

    snap3 = opencv.getSnapshot()
    smooth()
        
    i = 0
    a = 0
    
    for oat in c_oat:
        i = i + 1

        if(i < 18):
            r = oat.getBoundingBox()
            if r.width > 12 and r.width < 50:
                noFill()
                stroke(255,0,0)
                strokeWeight(2)
                oat.draw()
                        
                stroke(255,80)
                strokeWeight(1)
                ellipse(r.x+(r.width/2), r.y+(r.height/2), r.height+5, r.height+5);
                
                fill(255)
                text(i,r.x,r.y)
                
                fill(255,0,0)
                ellipse(r.x+(r.width/2), r.y+(r.height/2), 5, 5);
                
        
      
    ## Display
    fill(255)
    image(snap3, snap3.width, snap3.height/2, snap3.width/2, snap3.height/2)
    text("snap3: oat detection", snap3.width+10, snap3.height/2+15)
    
    
    #### DETECT eating?

    for contour in contours:
        r = contour.getBoundingBox()
        if r.width > 30:
            for oat in c_oat:
                r_oat = oat.getBoundingBox()
                if r_oat.width > 12 and r_oat.width < 50:
                    if contour.containsPoint(r_oat.x,r_oat.y):
                        if r_oat not in connect:
                            connect.append(r_oat)
   
    for el in connect:
        stroke(0,0,255)
        fill(80,80,255,80)
        ellipse(el.x+(el.width/2), el.y+(el.height/2), el.width+5, el.height+5);                    
            
    
        

def movieEvent(m):
    m.read()
    
