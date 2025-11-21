clc;

num_of_samples = 1e2;
required_mean = -5;
required_vaiance = 5; % sigma = 2
sigma = sqrt(required_vaiance);

z = randn(1, num_of_samples);
A = sigma*z + required_mean;

t = linspace(0, 2, 101);

% Use element-wise multiplication to create a matrix Z
%W = A' * cos(4 * pi * t);

f = @(t) A' * cos(4 * pi * t);

save('RP_W(t).mat', 'W', 't');

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
