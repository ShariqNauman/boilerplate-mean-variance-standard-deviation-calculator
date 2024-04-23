import numpy as np

def calculate(digits):
    if len(digits) < 9:
        raise ValueError("List must contain nine numbers.")

    digits_array = np.array(digits, dtype=np.int64).reshape(3, 3)


    calculations = {
        'mean': [list(np.mean(digits_array, axis=0)), list(np.mean(digits_array, axis=1)), np.mean(digits_array)],
        'variance': [list(np.var(digits_array, axis=0)), list(np.var(digits_array, axis=1)), np.var(digits_array)],
        'standard deviation': [list(np.std(digits_array, axis=0)), list(np.std(digits_array, axis=1)), np.std(digits_array)],
        'max': [list(np.max(digits_array, axis=0)), list(np.max(digits_array, axis=1)), np.max(digits_array)],
        'min': [list(np.min(digits_array, axis=0)), list(np.min(digits_array, axis=1)), np.min(digits_array)],
        'sum': [list(np.sum(digits_array, axis=0)), list(np.sum(digits_array, axis=1)), np.sum(digits_array)]
                                                                                                              
    }



    return calculations