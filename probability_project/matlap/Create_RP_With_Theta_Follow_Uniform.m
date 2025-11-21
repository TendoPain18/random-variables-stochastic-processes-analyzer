clc;

num_of_samples = 1e2;

a = 0;
b = pi;

t = linspace(0, 2, 101);
%theta = a + (b - a) * rand(1, num_of_samples);

% Use element-wise multiplication to create a matrix Z
%Z = cos(4 * pi * t + theta');

f = @(t) cos(4* pi * t + theta');
d = @(t) theta' * t;

save('RP_Z(t).mat', 'Z', 't');

% Calculate the mean as a function of time
mean_Z = mean(f(t));


resultMatrix = zeros(length(t), length(t));

for i = 1:length(t)
    for j = 1:length(t)
        vector1 = f(t(i));
        vector2 = f(t(j));
        resultMatrix(i, j) = mean(dot(vector1, vector2));
    end
end







% Plot mean
figure;
subplot(2,1,1);
plot(t, mean_Z);
xlabel('Time (t)');
ylabel('Mean');
title('Mean as a function of time');


% Plot 3D representation of resultMatrix
figure;
subplot(2,1,2);
[X, Y] = meshgrid(t, t);
surf(X, Y, resultMatrix);
xlabel('t');
ylabel('t');
zlabel('Matrix Result');
title('3D Plot of Result Matrix');
colorbar;  % Display colorbar


fs = 1 / (t(2) - t(1));  % Sampling frequency
psd_Z = abs(fft(Z)).^2 / (length(Z) * fs);

% Plot PSD
figure;
subplot(2,1,2);
frequencies = linspace(0, fs/2, length(psd_Z));
plot(frequencies, 10*log10(psd_Z));
xlabel('Frequency (Hz)');
ylabel('PSD (dB/Hz)');
title('Power Spectral Density (PSD)');


