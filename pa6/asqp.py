"""
CAPP 30121: Airline Service Quality Performance (ASQP) data

YOUR NAME HERE

Answer questions about airline performance data.
"""
import numpy as np

DATA_LEN = 36

############## TASK1 1 ##############

def average_delay(arrival_time):
    """
    Given ASQP data, determine the average flight delay 

    Args:
        arrival_time (NumPy array): flight arrival times (negative
            if the flight is early, positive if the flight is late)

    Returns (float): the average delay of non-early flights
    """
    ### YOUR CODE HERE ###
    return


def delay_and_cancel_fractions(arrival_time, cancellation_code):
    """
    Given ASQP data, compute the fraction of delayed and cancelled flights

    Args:
        arrivals_time (NumPy array): flight arrival times
        cancellation_code (NumPy array): flight cancellation codes

    Returns (tuple of floats): fraction of flights that were delayed, 
        fraction of flights that were cancelled
    """
    ### YOUR CODE HERE ###
    return


def per_carrier_cancels(cancellation_code_by_carriers):
    """
    Given ASQP data, determine how many of each carrier's flights were
        cancelled, and which carrier cancelled the most flights

    Input:
        cancellation_code_by_carriers (dictionary): a dictionary mapping a 
            carrier to a NumPy array of that carrier's flight cancellation codes

    Returns (dictionary, string): a dictionary mapping a carrier to the number of
        cancelled flights, and the carrier with the most cancellations
    """
    ### YOUR CODE HERE ###
    return


def underperforming_carriers(arrivals_by_carrier):
    """
    Given ASQP data, determine which carriers have a worse than average delay 

    Input:
        arrivals_by_carrier (dictionary): a dictionary mapping a carrier to a 
            NumPy array of that carrier's arrival times

    Returns (list): carriers whose average delay is worse than the overall
        average delay
    """
    ### YOUR CODE HERE ###
    return


############## TASK 2 ##############

def read_and_process_npy(filename):
    """
    Read in and process time series ASQP data

    Input:
        filename (string): name of the NPY file

    Returns (NumPy array): a time series NumPy array
    """
    ### YOUR CODE HERE ###
    return


############## PART 2 HELPER FUNCTION ##############

def perform_least_squares(y):
    """
    Given a data set, finds the line best fit perform least squares

    Input:
        y (array): data

    Returns (tuple of floats): the slope and y-intercept of the
        line fitted to y
    """

    x = np.arange(len(y))
    A = np.vstack([x, np.ones(len(y))]).T
    m, b = np.linalg.lstsq(A, y, rcond=None)[0]

    return m, b


############## TASK 3 ##############

def remove_irregularities(ts, width):
    """ 
    Apply a smoothing technique to remove irregularities from the 
        times series ASQP data

    Input:
        ts (NumPy array): the time series
        width (int): the width over which to smoothe

    Returns (NumPy array): smoothed time series data
    """
    ### YOUR CODE HERE ###
    return


def remove_trend(ts, width):
    """ 
    Remove overall trend from time series ASQP data

    Input:
        ts (NumPy array): the time series
        width (int): the width over which to smoothe

    Returns (NumPy array): detrended time series data
    """
    ### YOUR CODE HERE ###
    return


def is_seasonal(ts, width):
    """ 
    Bucket late flights, determine the bucket with the most 
        late flights

    Input:
        ts (NumPy array): the time series
        width (int): the width over which to smoothe

    Returns (NumPy array, int): number of delays in each month,
        the index of the month with the most delays (January = 0, etc.)
    """
    ### YOUR CODE HERE ###
    return