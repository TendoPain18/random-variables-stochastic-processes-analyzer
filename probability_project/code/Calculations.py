import random
import numpy
import numpy as np


class Calculations:
    def __init__(self):
        self.random_variable_time_vector = np.arange(0, 2.1, 0.01)
        self.random_variable_len = None
        self.random_variable_mean = None
        self.random_variable_variance = None
        self.random_variable_third_moment = None
        self.mgf_values = []
        self.first_derivative = []
        self.second_derivative = []

        self.random_process_time_vector = None
        self.mean_of_RP = []
        self.ACF = None

    def get_random_variable_mean(self, data):
        self.random_variable_len = len(data[0])
        self.random_variable_mean = sum(data[0]) / self.random_variable_len
        return self.random_variable_mean

    def get_random_variable_variance(self, data):
        self.random_variable_variance = sum(
            (x - self.random_variable_mean) ** 2 for x in data[0]) / self.random_variable_len
        return self.random_variable_variance

    def mgf(self, t, data):
        return sum(np.exp(t * x) for x in data) / self.random_variable_len

    def get_random_variable_mgf(self, data):
        self.mgf_values = numpy.array([self.mgf(t, data[0]) for t in self.random_variable_time_vector])
        x_values = self.random_variable_time_vector
        y_values = self.mgf_values
        labels = ['Moment Generating Function(t)', 'time(s)', 'M(t)']
        return labels, x_values, y_values

    def get_random_variable_first_derivative_mgf(self):
        self.first_derivative = np.diff(self.mgf_values) / np.diff(self.random_variable_time_vector)
        x_values = self.random_variable_time_vector[:-1]
        y_values = self.first_derivative
        labels = ['1st Derivative(t)', 'time(s)', 'Derivative Values(t)']
        return labels, x_values, y_values

    def get_random_variable_second_derivative_mgf(self):
        self.second_derivative = np.diff(self.first_derivative) / np.diff(self.random_variable_time_vector[:-1])
        x_values = self.random_variable_time_vector[:-2]
        y_values = self.second_derivative
        labels = ['2nd Derivative(t)', 'time(s)', 'Derivative Values(t)']
        return labels, x_values, y_values

    def get_random_third_moment(self):
        self.random_variable_third_moment = \
            (np.diff(self.second_derivative) / np.diff(self.random_variable_time_vector[:-2]))[0]
        return self.random_variable_third_moment

    def get_random_variable_first_derivative_mgf_at_0(self):
        return self.first_derivative[0]

    def get_random_variable_second_derivative_mgf_at_0(self):
        return self.second_derivative[0]

    def calculate_random_variable(self, data):
        x1 = self.get_random_variable_mean(data)
        x2 = self.get_random_variable_variance(data)
        x4, x5, x6 = self.get_random_variable_mgf(data)
        x7, x8, x9 = self.get_random_variable_first_derivative_mgf()
        x10, x11, x12 = self.get_random_variable_second_derivative_mgf()
        x3 = self.get_random_third_moment()
        x13 = self.get_random_variable_first_derivative_mgf_at_0()
        x14 = self.get_random_variable_second_derivative_mgf_at_0()
        list_ = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14]
        return list_

    ##################################################################################################################
    ##################################################################################################################
    ##################################################################################################################
    ##################################################################################################################
    def get_random_m_sample_functions(self, time, data, m):
        self.random_process_time_vector = time[0]
        random_numbers = []
        for i in range(m):
            r = random.randint(0, len(data) - 1)
            while r in random_numbers:
                r = random.randint(0, len(data) - 1)
            random_numbers.append(r)
        x_values = self.random_process_time_vector
        y_values = []
        for i in random_numbers:
            y_values.append(data[i])
        labels = ["Random_M_Sample_Functions(t)", "time(s)", "sample functions(t)"]
        return labels, x_values, y_values

    def get_random_process_ensemble_mean_plot(self, data):
        lists = []
        for i in range(len(data[0])):
            val = []
            for j in range(len(data)):
                val.append(data[j][i])
            lists.append(val)
        self.mean_of_RP = []
        for i in lists:
            mean_value = sum(i) / len(i)
            self.mean_of_RP.append(mean_value)

        x_values = self.random_process_time_vector
        y_values = self.mean_of_RP
        print(self.mean_of_RP)
        labels = ["Mean(t)", "time(s)", "mean(t)"]
        return labels, x_values, y_values

    def get_random_process_statistical_auto_correlation_plot(self, data):
        ti = self.random_process_time_vector
        tj = self.random_process_time_vector
        t_i, t_j = np.meshgrid(ti, tj)

        lists = []
        for i in range(len(data[0])):
            val = []
            for j in range(len(data)):
                val.append(data[j][i])
            lists.append(val)

        result_matrix = np.zeros((len(self.random_process_time_vector), len(self.random_process_time_vector)))

        for i in range(len(self.random_process_time_vector)):
            for j in range(len(self.random_process_time_vector)):
                result_matrix[i, j] = np.mean(np.multiply(lists[i], lists[j]))

        self.ACF = result_matrix

        x_values = t_i
        y_values = t_j
        z_values = result_matrix
        labels = ["acf(ti,tj)", "t_i", "t_j", "ACF(ti,tj)"]

        return labels, x_values, y_values, z_values

    @staticmethod
    def get_time_mean_of_the_nth_sample_function(time, data, n_th):
        # Calculate the range of time values (denominator)
        den = np.max(time[0]) - np.min(time[0])

        total_sum = sum(data[n_th - 1]) / den

        return total_sum

    @staticmethod
    def time_auto_correlation_function_of_the_nth_sample_function(time, data, n_th):
        # Calculate the range of time values (denominator)
        den = np.max(time[0]) - np.min(time[0])
        time_acf = 0
        for i in range(len(data[0])):
            for j in range(i, len(data[0])):
                temp = data[n_th][i] * data[n_th][j]
                time_acf = time_acf + temp
        time_acf = time_acf / den
        return time_acf

    def get_the_power_spectral_density_of_the_process_plot(self, data):
        N = len(data)
        K = len(data[0])
        dt = 0.02

        total_Ft_per_realization = np.zeros(K, dtype=complex)

        for i in range(N):
            X_Ft = np.fft.fft(data[i])
            total_Ft_per_realization += X_Ft

        avg_Ft_per_realization = total_Ft_per_realization / N

        # Square the result
        power_spectral_density = np.abs(avg_Ft_per_realization) ** 2

        # Frequency values corresponding to the Fourier transform
        freq = np.fft.fftfreq(K, dt)

        labels = ["PSD(f)", "F(Hz)", "psd(f)"]

        return labels, freq, power_spectral_density

    def get_total_average_power_of_the_process(self, data):
        lists = []
        for i in range(len(data[0])):
            val = []
            for j in range(len(data)):
                val.append(data[j][i])
            lists.append(val)

        result_matrix = []

        for i in range(len(self.random_process_time_vector)):
            result_matrix.append(sum(x * x for x in lists[i]) / len(lists[i]))

        mean = sum(result_matrix) / len(result_matrix)

        return mean

    def calculate_random_process(self, time, data, m, n_th):
        x1, x2, x3 = self.get_random_m_sample_functions(time, data, m)
        x4, x5, x6 = self.get_random_process_ensemble_mean_plot(data)
        x7, x8, x9, x10 = self.get_random_process_statistical_auto_correlation_plot(data)
        x11 = self.get_time_mean_of_the_nth_sample_function(time, data, n_th)
        x12 = self.time_auto_correlation_function_of_the_nth_sample_function(time, data, n_th)
        x13, x14, x15 = self.get_the_power_spectral_density_of_the_process_plot(data)
        x16 = self.get_total_average_power_of_the_process(data)
        list_ = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16]
        return list_
