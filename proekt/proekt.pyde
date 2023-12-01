# x=100
# z=30
# c=1
m=255
def setup():
    size (1000 ,1000)
    frameRate(10)
    background (100,100,100)
def draw():
    global m
    textSize (30)
    fill (m,m,m)
    text ('You are an idoit!!!',370,300)
    ellipseMode (CENTER)
    ellipse (500,600,150,150)
    ellipse (470,570,30,30)
    ellipse (530,570,30,30)
    stroke (100,100,100)
    rect (440,540,120,100)
    stroke (0,0,0)
    ellipse (500,600,150,150)
    ellipse (500,600,120,120)
    ellipse (470,570,30,30)
    ellipse (530,570,30,30)
    noFill ()
    # x=x+1
    # z=z+1
    # c=c+1
    m=m-250
    # if x > 250:
    #     x=x-250
    # if c > 250:
    #     c=c-250
    # if z > 250:
    #     z=z-250
    if m < 10:
        m=m+250
