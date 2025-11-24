import numpy as np

def calculate_statistics(data):
    """
    Calculate basic statistics: mean, median, and standard deviation.

    Parameters:
    data (list or np.ndarray): Input numerical data.

    Returns:
    dict: A dictionary containing mean, median, and standard deviation.
    """
    data_array = np.array(data)
    
    mean = np.mean(data_array)
    median = np.median(data_array)
    std_dev = np.std(data_array)
    
    return {
        'mean': mean,
        'median': median,
        'std_dev': std_dev
    }