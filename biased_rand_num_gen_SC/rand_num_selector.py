import random


class RandomNumberSelector():
    """Class for creating an instance which facilitates methods for selecting a number from a list based on provided probability weights.
    """

    def __init__(self, population : list, probabilities : list):
        """[summary]

        Args:
            population (list): List of possible numbers from which you want to pick one.
            probabilities (list):
            A list that defines the probabilities for each element being selected.
            The indexes of both population and probabilities correspond to each other.
            This list must be the same length as the population and total of all probabilities
            must add to 1.
        """

        #Verification
        if len(probabilities) != len(population):
            raise ValueError("Both list probabilities & population should have the same number of elements")

        if all([isinstance(item, float) | isinstance(item, int) for item in population]) == False:
            raise TypeError("List population can only contain elements of type int or float.")

        if all([isinstance(item, float) for item in probabilities]) == False:
            raise TypeError("List probabilities can only contain elements of type float.")

        if all([(item < 1 and item >= 0) for item in probabilities]) == False:
            raise ValueError("List probabilities can only contain elements X that are: 0 <= X < 1.")

        if round(sum(probabilities),2) != 1:
            raise ValueError("List probabilities' elements must sum up to 1.00 (to 2dp).")

        self._population = population

        self._probabilities = probabilities



    def next_num(self):


        #in an elimnation manner, the more indexes that get eliminated in the list, the larger the share of the next index in the list of being larger then RAND as its chance of occuring now is an accumulation of the probabilities of the previous indexes, in this manner i can maintain propotionality.

        rand_n = random.random() #Whichever number's chance is greater then this, gets returned.

        tot_chance_of_this_index = 0

        for index, prob in enumerate(self._probabilities):
            tot_chance_of_this_index+=prob

            if  tot_chance_of_this_index >= rand_n:
                return self._population[index]


    def next_num_tracker(self, k: int):
        """
        Generates a number from the population
        using next_num 'k' number of times and in the end
        prints out how many times each number was selected.

        When this method is called multiple times
        over a long period, it should return the numbers roughly with the initialized probabilities.

        Args:
            k (int): Amount of times next_num should be called. k should be > 1.
        """

        #verify
        if isinstance(k, int) == False:
            raise TypeError("k should be of type int")
        if k < 1 == True:
            raise ValueError("k should be atleast >= 1")

        population_selection_dict = dict.fromkeys(self._population, 0) #convert list into dict, with default vals 0

        for i in range(k):

            num = self.next_num()

            population_selection_dict[num] += 1

        for key, value in population_selection_dict.items():
            print(f'{key}: {value} times')





if __name__ == "__main__":


    randomGen = RandomNumberSelector([-1, 0, 1, 2, 3],  [0.01, 0.3, 0.58, 0.1, 0.01])

    randomGen.next_num_tracker(10000)


