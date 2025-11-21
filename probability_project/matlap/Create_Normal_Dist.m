clc; close all;

num_of_samples = 1e5;
x = -20:0.01:20;
required_mean = 0;
required_vaiance = 1; % sigma = 2
sigma = sqrt(required_vaiance);

FONTSIZE_LABEL = 14;
FONTSIZE_LEGEND = 12;

f = @(x) 1 / (sigma * sqrt(2*pi)) * exp(-(x-required_mean).^2/(2 * sigma^2));
F = @(x) 1 - qfunc((x-required_mean)/sigma);

z = randn(1, num_of_samples);
y = sigma*z + required_mean;
%y = y;

% Save the variable 'y' as a .mat file
save('Normal_dist_y.mat', 'y');

%%%%%%%%%%%%%%%%%%%%%%%%% PDF %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(1); subplot(1,2,1);
%%% generated PDF
histogram(y,200, 'Normalization','pdf');
hold on;
%%% theoretical PDF
plot(x, f(x), 'r-', 'LineWidth', 3);
legend('simulated', 'theoretical', 'Fontsize', FONTSIZE_LEGEND, 'Location', 'northeast');
xlabel('x', 'FontSize', FONTSIZE_LABEL);
ylabel('f_X(x)', 'FontSize', FONTSIZE_LABEL);
title('PFD', 'Interpreter', 'latex');
grid on; axis tight, grid minor, hold off;


%%%%%%%%%%%%%%%%%%%%%%%%% CDF %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(1); subplot(1,2,2);
%%% generated CDF
histogram(y,200, 'Normalization','cdf');
hold on;
%%% theoretical CDF
plot(x, F(x), 'r-', 'LineWidth', 3);
legend('simulated', 'theoretical', 'Fontsize', FONTSIZE_LEGEND, 'Location', 'northeast');
xlabel('x', 'FontSize', FONTSIZE_LABEL);
ylabel('F_X(x)', 'FontSize', FONTSIZE_LABEL);
title('CDF', 'Interpreter', 'latex');
grid on; axis tight, grid minor, hold off;



%%%%%%%%%%%%%%%%%%%%%%%%% MGF and Derivatives %%%%%%%%%%%%%%%%%%%%%%
t_values = 0:0.01:2;

% Calculate MGF
mgf_values = arrayfun(@(t) mean(exp(t*y)), t_values);

% Calculate the first derivative
mgf_derivative_1 = diff(mgf_values) ./ diff(t_values);

% Calculate the second derivative
mgf_derivative_2 = diff(mgf_derivative_1) ./ diff(t_values(1:end-1));

% Calculate the third derivative
mgf_derivative_3 = diff(mgf_derivative_2) ./ diff(t_values(1:end-2));

% Calculate the mean and variance
mean_from_mgf = mgf_derivative_1(1);
variance_from_mgf = mgf_derivative_2(1) - (mgf_derivative_1(1)*mgf_derivative_1(1));
third_moment = mgf_derivative_3(1);

% Plot MGF
figure;
subplot(1,3,1);
plot(t_values, mgf_values, 'b-', 'LineWidth', 2);
title('MGF', 'FontSize', FONTSIZE_LABEL);
xlabel('t', 'FontSize', FONTSIZE_LABEL);
ylabel('M(t)', 'FontSize', FONTSIZE_LABEL);
grid on;

% Plot first derivative
subplot(1,3,2);
plot(t_values(1:end-1), mgf_derivative_1, 'g-', 'LineWidth', 2);
title('First Derivative of MGF', 'FontSize', FONTSIZE_LABEL);
xlabel('t', 'FontSize', FONTSIZE_LABEL);
ylabel('dM(t)/dt', 'FontSize', FONTSIZE_LABEL);
grid on;

% Plot second derivative
subplot(1,3,3);
plot(t_values(1:end-2), mgf_derivative_2, 'r-', 'LineWidth', 2);
title('Second Derivative of MGF', 'FontSize', FONTSIZE_LABEL);
xlabel('t', 'FontSize', FONTSIZE_LABEL);
ylabel('d^2M(t)/dt^2', 'FontSize', FONTSIZE_LABEL);
grid on;

