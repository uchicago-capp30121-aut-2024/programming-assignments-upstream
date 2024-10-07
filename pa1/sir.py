"""
Modeling Epidemics

YOUR NAME HERE

Functions for running a simple SIR epidemiological simulation
"""

import random
import sys
import click


# This seed should be used for debugging purposes only!  Do not refer
# to this variable in your code.
TEST_SEED = 20170217


def has_an_infected_neighbor(city, location):
    """
    Determine whether or not a person at a location has an infected
    neighbor in a city modelled as a ring.

    Args:
        city (list of tuples): the state of all people in the simulation at the
            start of the day
        location (int): the location of the person to check

    Returns (boolean): True if the person has an infected neighbor, 
        False otherwise.
    """

    # The location needs to be a valid index for the city list.
    assert 0 <= location < len(city)

    # This function should only be called when the person at location
    # is susceptible to infection.
    disease_state, _ = city[location]
    assert disease_state == "S"

    # YOUR CODE HERE

    # REPLACE False WITH AN APPROPRIATE RETURN VALUE
    return False


def advance_person_at_location(city, location, days_contagious, 
                               days_immune, infection_probability):
    """
    Compute the next state for the person at the specified location.

    Args:
        city (list of tuples): the state of all people in the simulation at the
            start of the day
        location (int): the location of the person to check
        days_contagious (int): the number of days a person is infected
        days_immune (int): the number of days a person is recovered before
            the become susceptible
        infection_probability (float): the probability that a vaccinated person 
            will become infected

    Returns (string, int): Disease state and number of days in that state
        of the person after one day.
    """

    assert 0 <= location < len(city)

    # YOUR CODE HERE

    # REPLACE ("R", 0) WITH AN APPROPRIATE RETURN VALUE
    return ("R", 0)


def simulate_one_day(starting_city, days_contagious, 
                     days_immune, infection_probability):
    """
    Move the simulation forward a single day.

    Args:
        starting_city (list of tuples): the state of all people in the 
            simulation at the start of the day
        days_contagious (int): the number of a days a person is infected
        days_immune (int): the number of days a person is recovered before
            the become susceptible
        infection_probability (float): the probability that a vaccinated person  
            will become infected

    Returns (list of tuples): The state of the city after one day. 
    """

    # YOUR CODE HERE

    # REPLACE [] WITH AN APPROPRIATE RETURN VALUE
    return []


def is_transmission_possible(city):
    """
    Is there at least one susceptible person who has an infected neighbor for 
        some number of days?

    Args:
        city (list of tuples): the current state of the city

    Returns (boolean): True if the city has at least one susceptible person
        with an infected neighbor, False otherwise.
    """

    # YOUR CODE HERE

    # REPLACE False WITH AN APPROPRIATE RETURN VALUE
    return False


def run_simulation(starting_city, days_contagious, days_immune, 
                   infection_probability, max_days):
    """
    Run the entire simulation. 

    Args:
        starting_city (list of tuples): the state of all people in the city at
            the start of the simulation
        days_contagious (int): the number of a days a person is infected
        days_immune (int): the number of days a person is recovered before
            the become susceptible
        infection_probability (float): the probability that a vaccinated person  
            will become infected
        max_days (int): the maximum number of days to run the simulation

    Returns (list of tuples, int): The final state of the city
        and the number of days actually simulated.
    """

    # YOUR CODE HERE

    # REPLACE ([], 0) WITH AN APPROPRIATE RETURN VALUE
    return ([], 0)


################ Do not change the code below this line #######################

def run_trials(city, days_contagious, days_immune, infection_probability, 
               max_days, random_seed, num_trials):
    """
    Run multiple trials of vaccinate_and_simulate and compute the median
    result for the number of days until infection transmission stops.

    Args:
        city (list of tuples): the current state of the city
        days_contagious (int): the number of days a person is infected
        days_immune (int): the number of days a person is recovered before
            the become susceptible
        infection_probability (float): the probability that a vaccinated person  
            will become infected
        max_days (int): the maximum number of days to run the simulation
        random_seed (int): the seed for the random number generator
        num_trials (int): the number of trial simulations to run
        
    Returns (int): The median number of days until infection transmission stops.
    """

    days = []
    for i in range(num_trials):
        if random_seed:
            random.seed(random_seed+i)

        _, num_days_simulated = run_simulation(city, 
                                               days_contagious, 
                                               days_immune, 
                                               infection_probability, 
                                               max_days)

        days.append(num_days_simulated)

    # quick way to compute the median
    return sorted(days)[num_trials // 2]


def parse_city_file(filename):
    """
    Read a city represented as person tuples from a file.

    Args:
        filename (string): the name of the file

    Returns (list of tuples or None): City, or None if the file does not exist
        or cannot be parsed.
    """

    try:
        with open(filename) as f:
            residents = [line.split() for line in f]
    except IOError:
        print("Could not open:", filename, file=sys.stderr)
        return None

    ds_types = ('S', 'I', 'R', 'V')

    rv = []
    try:
        for i, res in enumerate(residents):
            ds, nd = res
            num_days = int(nd)
            if ds not in ds_types or num_days < 0:
                raise ValueError()
            rv.append((ds, num_days))
    except ValueError:
        emsg = ("Error in line {}: person tuples are represented "
                "with a disease state {} and a non-negative integer.")
        print(emsg.format(i, ds_types), file=sys.stderr)
        return None
    return rv


@click.command()
@click.argument("filename", type=str)
@click.option("--days-contagious", default=2, type=int)
@click.option("--days-immune", default=4, type=int)
@click.option("--infection-probability", default=0.2, type=float)
@click.option("--random-seed", default=None, type=int)
@click.option("--num-trials", default=1, type=int)
@click.option("--max-days", default=1, type=int)
def cmd(filename, days_contagious, days_immune, infection_probability, 
        random_seed, num_trials, max_days):
    """
    Process the command-line arguments and do the work.
    """
    city = parse_city_file(filename)
    if not city:
        return -1

    print("Running trials of the simulation ...")
    median_num_days = run_trials(city, 
                                days_contagious, 
                                days_immune, 
                                infection_probability, 
                                max_days, 
                                random_seed, 
                                num_trials)
    print("Median number of days until infection transmission stops:", median_num_days)
    return 0
         

if __name__ == "__main__":
    cmd()  # pylint: disable=no-value-for-parameter