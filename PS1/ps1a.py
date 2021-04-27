###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows ={}
    ooga = open(filename, "r")
    for boom in ooga:
        name, age = boom.split(",")
        cows[name] = int(age)
    return cows
        
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_list = sorted(cows.items(), key = lambda x: x[1], reverse = True)
    removed_cow=[]
    all_trips=[]
    for i in range(len(cows_list)):
        if len(cows_list) == len(removed_cow):
            break
        current_weight=0
        current_trip =[]
        if (current_weight + ((cows_list[i])[1])) <= limit:
            if (cows_list[i]) not in removed_cow:
              current_trip.append(cows_list[i])
              current_weight+=((cows_list[i])[1])
              removed_cow.append(cows_list[i])
        for cow in cows_list[i+1:]:
            if cow not in removed_cow:
                if current_weight+ cow[1] <= limit:
                    current_trip.append(cow)
                    current_weight += cow[1] 
                    removed_cow.append(cow)
        all_trips.append(current_trip)
    return all_trips
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_list = sorted(cows.items(), key = lambda x: x[1], reverse = True)
    best_choice = cows_list[:]
    for partition in get_partitions(cows_list):
        for trip in partition:
            trip_weight = 0
            for cow in trip:
                trip_weight+=cow[1]
            if trip_weight> limit:
               break
        if trip_weight<=limit:  
            if len(partition)<len(best_choice):
                best_choice = partition[:]
    return best_choice

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    a={"muscles":65,"moomoo":85,"clover":5,"louis":45,"polaris":20,"bella":15,"patches":60,"horns":50,"milkshake":75,"lotus":10,"butter":72,"rose":50}
    b={"butter":72,"lily":24,"dottie":85,"betsy":65,"willow":35,"daisy":50,"patches":12,"coco":10,"abby":38,"rose":50}
    start = time.time()
    print(greedy_cow_transport(a,100))
    end = time.time()
    print("The time for greedy is", (end - start))
    start = time.time()
    print(brute_force_cow_transport(a,100))
    end = time.time()
    print("The time for brute force is", (end - start))
    

# if __name__ == "main":
compare_cow_transport_algorithms()