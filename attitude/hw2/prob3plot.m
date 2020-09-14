psi = load('psi.mat').psi;
psi_dot = load('psi_dot.mat').psi_dot;
plot(psi(1,:), psi(2, :))
xlabel('Time')
ylabel('Magnitude')
title('Psi')
figure
plot(psi_dot(1,:), psi_dot(2, :))
xlabel('Time')
ylabel('Magnitude')
title('Psi Dot')