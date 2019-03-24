from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def myinit ():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 50)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)


def road ():
    glLoadIdentity()
    glColor(0.4,0.4,0.4)
    glRotate(90,0,1,0)
    glBegin(GL_POLYGON)
    glVertex(50, 0, -3)
    glVertex(50, 0, 4)
    glVertex(-20, 0, 4)
    glVertex(-20, 0, -3)
    glEnd()


    glLoadIdentity()
    glColor(0.4,0.5,0.1)
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(50, 0, -4.5)
    glVertex(50, 0, -50)
    glVertex(-20, 0, -50)
    glVertex(-20, 0, -4.5)
    glEnd()

    glLoadIdentity()
    glColor(0.4,0.5,0.1)
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(50, 0, 4.5)
    glVertex(50, 0, 50)
    glVertex(-20, 0, 50)
    glVertex(-20, 0, 4.5)
    glEnd()



    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(30, 0, 0)
    glVertex(30, 0, 1)
    glVertex(37, 0, 1)
    glVertex(37, 0, 0)
    glEnd()

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(20, 0, 0)
    glVertex(20, 0, 1)
    glVertex(27, 0, 1)
    glVertex(27, 0, 0)
    glEnd()

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(10, 0, 0)
    glVertex(10, 0, 1)
    glVertex(17, 0, 1)
    glVertex(17, 0, 0)
    glEnd()


    glLoadIdentity()
    glColor(1,1,1)
    glRotate(90,0,1,0)
    glBegin(GL_POLYGON)
    glVertex(0,0,0)
    glVertex(0,0,1)
    glVertex(7,0,1)
    glVertex(7,0,0)
    glEnd()

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(-11, 0, 0)
    glVertex(-11, 0, 1)
    glVertex(-4, 0, 1)
    glVertex(-4, 0, 0)
    glEnd()



def trees ():
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(0,-1,0)
    glColor3f(0, 0.4, 0.8)
    glBegin(GL_POLYGON)
    glVertex(35, 3.5, 0)
    glVertex(35, 10, 0)
    glVertex(-25, 10, 0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor(0.5, 0.2, 0)
    glTranslate(0, 0, -8)
    glBegin(GL_POLYGON)
    glVertex(-3, 0, 0)
    glVertex(-3.5, 0, 0)
    glVertex(-3.5, 3, 0)
    glVertex(-3, 3, 0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-3.5, 3, -8)
    glColor3f(0.2, 0.8, 0.1)
    glutSolidSphere(1, 200, 200)


    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor(0.5, 0.2, 0)
    glTranslate(0, 0, -8)
    glBegin(GL_POLYGON)
    glVertex(1, 0, 0)
    glVertex(1.5, 0, 0)
    glVertex(1.5, 3, 0)
    glVertex(1, 3, 0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(1, 3, -8)
    glColor3f(0.2, 0.8, 0.1)
    glutSolidSphere(1, 200, 200)

    glLoadIdentity()
    glColor(0.5, 0.2, 0)
    glRotate(90,0,1,0)
    glTranslate(0,0,-8)
    glBegin(GL_POLYGON)
    glVertex(6,0,0)
    glVertex(6.5,0,0)
    glVertex(6.5,3,0)
    glVertex(6,3,0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(6, 3, -8)
    glColor3f(0.2, 0.8, 0.1)
    glutSolidSphere(1, 200, 200)

    glLoadIdentity()
    glColor(0.5, 0.2, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(0, 0, -8)
    glBegin(GL_POLYGON)
    glVertex(11, 0, 0)
    glVertex(11.5, 0, 0)
    glVertex(11.5, 3, 0)
    glVertex(11, 3, 0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(11, 3, -8)
    glColor3f(0.2, 0.8, 0.1)
    glutSolidSphere(1, 200, 200)

    glLoadIdentity()
    glColor(0.5, 0.2, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(0, 0, -8)
    glBegin(GL_POLYGON)
    glVertex(16, 0, 0)
    glVertex(16.5, 0, 0)
    glVertex(16.5, 3, 0)
    glVertex(16, 3, 0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(16, 3, -8)
    glColor3f(0.2, 0.8, 0.1)
    glutSolidSphere(1, 200, 200)

    glLoadIdentity()
    glColor(0.5, 0.2, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(0, 0, -8)
    glBegin(GL_POLYGON)
    glVertex(21, 0, 0)
    glVertex(21.5, 0, 0)
    glVertex(21.5, 3, 0)
    glVertex(21, 3, 0)
    glEnd()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(21, 3, -8)
    glColor3f(0.2, 0.8, 0.1)
    glutSolidSphere(1, 200, 200)




def axis ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()

angle = 0
x = 0
forward = True
trn = 0

def arrow_keys(key, x, y):
    global trn
    if key == GLUT_KEY_LEFT:
        trn += 3
    elif key == GLUT_KEY_RIGHT:
        trn -= 3


    display()

def display ():
    global angle
    global x
    global forward
    global trn
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)


    glLoadIdentity()
    glRotate(90,0,1,0)
    glColor(0,0,0)
    glTranslate(-24, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-22, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-20, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-18, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-16, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-14, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-12, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-10, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-6, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-2, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(0, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(2, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(4, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(6, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(8, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(10, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(12, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(14, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(16, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(18, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(20, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(22, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(24, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0,0,0)
    glRotate(90, 0, 1, 0)
    glTranslate(26, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(28, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(30, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1,1,1)
    glRotate(90, 0, 1, 0)
    glTranslate(32, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(34, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(36, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(38, 0, -3)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    #############################

    #Right blocks

    ###############################

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor(0, 0, 0)
    glTranslate(-24, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-22, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-20, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-18, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-16, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-14, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-12, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-10, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-6, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-2, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(0, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(2, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(4, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(6, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(8, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(10, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(12, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(14, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(16, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(18, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(20, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(22, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(24, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(26, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(28, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(30, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(32, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(34, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(1, 1, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(36, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    glLoadIdentity()
    glColor(0, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(38, 0, 4)
    glScale(2, 0.5, 1)
    glutSolidCube(2)

    ##########################



    #############################

    glLoadIdentity()
    road()

    glLoadIdentity()
    trees()

    #glLoadIdentity()
    #axis()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x,0,0 + trn)
    glColor3f(0.1,0,0.2)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor(0.1,0,0.4)
    glRotate(90, 0, 1, 0)
    glTranslate(x,5*0.25,0 + trn)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)


    glColor3f(0,0,0)
    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(2.5 + x ,-2.5*0.25,2.5*0.5 + trn)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2,0.5,12,8)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.5 + x , -2.5 * 0.25, 2.5 * 0.5 + trn )
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 12, 8)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(2.5 + x , -2.5 * 0.25, -2.5 * 0.5 +trn)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 12, 8)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.5 + x , -2.5 * 0.25, -2.5 * 0.5 + trn)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(0.2, 0.5, 12, 8)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.8 + x ,0,-0.5 + trn)
    glColor3f(1,1,0)
    glutWireSphere(0.2,100,100)

    glLoadIdentity()
    glRotate(90,0,1,0)
    glTranslate(-2.8 + x , 0, 0.5 + trn)
    glColor3f(1, 1, 0)
    glutWireSphere(0.2, 100, 100)


    if forward:
        angle -= 0.9
        x += 0.05
        if x > 20:
            forward = False
    else :
        x -= 0.05
        angle += 0.9
        if x < -7 :
            forward = True



    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
glutDisplayFunc(display)
glutIdleFunc(display)
glutSpecialFunc(arrow_keys)
myinit()
glutMainLoop()