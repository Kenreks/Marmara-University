w0=6000;
x=[0:400];
E=200000;
L=2;
b=200;
h=500;
I=b*(h^3)/12;
y=-(10.*(L.^3)-10.*(L.^2)*x+5.*L.*(x.^2)-(x.^3)).*w0.*(x.^2)/(120.*E.*I);
plot(x,y,'--*g','LineWidth',2.25,'MarkerSize',5)
legend('x=beam station')
xlabel("beam length")
ylabel("beam deflection")
m=polyder(y);
fprintf('%f is coefficient of rotation angle of the beam \n',m)