t = [-pi:0.0001:pi];
f1 = square(t);
N = 10;
s1 = zeros(size(t));

for k=0:N-1
    subplot(1,2,1)
    s1 = s1 + (4/pi)/(2*k+1)*sin((2*k+1)*t);
    hold off
    plot(t/pi, f1)
    hold on
    plot(t/pi, s1)
    title(['Square Wave ', 'K = ', num2str(k+1)])
    subplot(1,2,2)
    hold on
    plot(t/pi, (4/pi)/(2*k+1)*sin((2*k+1)*t))
    pause(4/(k+1))
    drawnow limitrate
end
