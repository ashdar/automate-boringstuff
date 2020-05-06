# .SYNOPSIS
# A 'practice project' exercise from the end of Chapter 4.

import random


def toss_coin():
    """'flip a coin' and return Heads or Tails
    Returns string"""
    if (random.randint(0, 1) == 0):
        return 'T'
    else:
        return 'H'


### Main begins here #########
verbose = False
debug = False
count_of_streaks_total = 0
count_of_streaks_by_type = {"H": 0, "T": 0}

# experiment size in 'tosses'
trial_size = 100

# X tosses in a row means a 'streak'
required_streak_length = 6

# how many trials do we make?
experiment_size = 10000
# Requirement #1: Generate a string of random Heads and Tails values.

for trial_id in range(1, experiment_size + 1):
    trial_result = ''
    for i in range(trial_size):
        toss_result = str(toss_coin())
        trial_result += toss_result

    # print(len(trial_results))
    if debug:
        print('Debug: Trial Result: ' + trial_result)

    # Requirement #2: Look for a streak of N Heads or N Tails
    count_of_streaks_for_experiment = 0
    for j in range(trial_size):
        streak_types = ['H', 'T']
        for streak_type in streak_types:
            if streak_type * required_streak_length == trial_result[j:(j + required_streak_length)]:
                if debug:
                    print("Debug: ExperimentID {0} hit a streak of '{1}' at position {2}".format(
                        str(trial_id), streak_type, str(j)))
                count_of_streaks_total += 1
                count_of_streaks_for_experiment += 1
                count_of_streaks_by_type[streak_type] += 1

    if verbose:
        print('Count of streaks for Experiment #' + str(trial_id) +
              ' was ' + str(count_of_streaks_for_experiment))

print('Count of trial(s) is {0}. Size of each trial is {1} tosses. Count of tosses, total, is {2}. '.format(
    experiment_size, trial_size, (experiment_size * trial_size)))

# FIXME: I am unsure tht this 'chance of streak' calculation is providing a good value, but it matches the book.
print('Count of streaks, total, is {0}. Chance of streak: {1:.2%}'.format(
    count_of_streaks_total, (count_of_streaks_total / (experiment_size * trial_size))))

print(count_of_streaks_by_type)
