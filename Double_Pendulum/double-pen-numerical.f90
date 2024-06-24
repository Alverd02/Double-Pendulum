PROGRAM DPENDULUM

IMPLICIT NONE

DOUBLE PRECISION :: x1,x2,y1,y2,vy1,vy2,t0,tf,theta1_0,theta2_0,vtheta1_0,vtheta2_0
DOUBLE PRECISION :: g,l,m,t
DOUBLE PRECISION,ALLOCATABLE :: funcina(:),phi1(:),vphi1(:),phi2(:),vphi2(:)
integer :: n,nequs,i
COMMON/CONSTANTS/g,l,m

n = 800
nequs = 4

allocate(funcina(nequs),phi1(n),vphi1(n),phi2(n),vphi2(n))


g = 9.81d0
l = 1d0
m = 5.d0

t0 = 0.d0
tf = 20.d0

theta1_0 = 3.1415926535898/2
vtheta1_0 = 0.d0
theta2_0 = 0.d0
vtheta2_0 = 0.d0


funcina = [theta1_0,vtheta1_0,theta2_0,vtheta2_0]

OPEN(11,file="double_data.dat")

CALL integralRK4(t0,tf,n,nequs,funcina,phi1,vphi1,phi2,vphi2)
DO i=1,n

X1 = l*dsin(phi1(i))
y1 = -l*dcos(phi1(i))

x2 = x1 + l*dsin(phi2(i))
y2 = y1 -l*dcos(phi2(i))

WRITE(11,*) x1,y1,x2,y2

END DO

CLOSE(11)

OPEN(12,file="double_time.dat")

CALL integralRK4(t0,tf,n,nequs,funcina,phi1,vphi1,phi2,vphi2)
DO i=1,n

t = t0 + i*tf/n

WRITE(12,*) phi1(i),vphi1(i),phi2(i),vphi2(i),t

END DO

CLOSE(12)

END PROGRAM

SUBROUTINE RungeKutta4(t0,dt,funcin,dfuncout,nequs,EDO)
IMPLICIT NONE
DOUBLE PRECISION :: dt,t,t0
DOUBLE PRECISION,DIMENSION(nequs) :: funcin, dfuncout, y, k1, k2, k3, k4
INTEGER :: nequs
CALL EDO(nequs, t0, funcin, k1) !
y = funcin + 0.5d0 * k1 * dt 
t = t0 + 0.5d0*dt 
CALL EDO(nequs, t, y, k2)
y = funcin + 0.5d0 * k2 * dt
t = t0 +  0.5d0*dt
CALL EDO(nequs, t, y, k3)
y = funcin + k3 * dt 
t = t0 + dt 
CALL EDO(nequs, t, y, k4)
dfuncout = funcin + dt/6.d0*(k1+2.d0*k2+2.d0*k3+k4)

END

SUBROUTINE EDO(nequs, t, funcin, dyoutput)
IMPLICIT NONE

DOUBLE PRECISION :: t,g,l,m
DOUBLE PRECISION ,DIMENSION(nequs)::funcin,dyoutput
INTEGER :: nequs
COMMON/CONSTANTS/g,l,m 

dyoutput(1) = funcin(2)
dyoutput(3) = funcin(4)
dyoutput(2) = (-2*dsin(funcin(1)-funcin(3)) - dcos(funcin(1)-funcin(3))*dsin(funcin(1)-funcin(3))*funcin(2)**2 +&
dcos(funcin(1)-funcin(3))*(g/l)*dsin(funcin(3)) -(2*g/l)*dsin(funcin(1)))/(2.d0-dcos(funcin(1)-funcin(3))**2)
dyoutput(4) = dsin(funcin(1)-funcin(3))*funcin(2)**2 -(g/l)*dsin(funcin(3)) + (-2*dsin(funcin(1)-funcin(3)) - &
dcos(funcin(1)-funcin(3))*dsin(funcin(1)-funcin(3))*funcin(2)**2 + dcos(funcin(1)-funcin(3))*(g/l)*dsin(funcin(3))&
-(2*g/l)*dsin(funcin(1)))/(2.d0-dcos(funcin(1)-funcin(3))**2)
END

SUBROUTINE integralRK4(t0,tf, N,nequs,funcin, phi1,vphi1,phi2,vphi2)
IMPLICIT NONE
DOUBLE PRECISION :: t0,tf,dt,t
DOUBLE PRECISION,DIMENSION(nequs) :: funcin,phiRK
DOUBLE PRECISION,DIMENSION(N) :: phi1,vphi1,phi2,vphi2
INTEGER :: N, nequs, i
EXTERNAL EDO
dt = (tf-t0)/dble(N) 

DO i =1,n
t = t0 + dt*i
phi1(i) = funcin(1)
vphi1(i) = funcin(2)
phi2(i) = funcin(3)
vphi2(i) = funcin(4)
call RungeKutta4(t,dt,funcin,phiRK,nequs,EDO)
funcin = phiRK
END DO
END