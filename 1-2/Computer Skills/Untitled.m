clear all;clc
x=linespace(-5,5,50);
y= @(x) (x*1.5+3).*(x>-2 & x< 0)+(x*(-1.5)+3).*(x>0 & x<2);
figure
plot(x,y(x))
grid