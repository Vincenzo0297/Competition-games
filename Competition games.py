import random

class Country:
    # Constructor to initialize name, player, and age
    def __init__(self, name, player, age):
        self.name = name
        self.player = player
        self.age = age
    
    # Accessor methods
    def get_name(self):
        return self.name
    
    def get_player(self):
        return self.player
    
    def get_age(self):
        return self.age
    
    # Mutator method
    def set_info(self, name, player, age):
        self.name = name
        self.player = player
        self.age = age

class Diving:
    SIZE = 7  # No. of judges: 7

    def __init__(self, country, scores, difficulty, cf):
        self.country = country
        self.scores = scores
        self.difficulty = difficulty
        self.cf = cf
    
    # Accessor methods
    def get_country(self):
        return self.country
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_carried_forward(self):
        return self.cf
    
    def get_final_score(self):
        return self.calculate_final_score()
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    # Get sorted list of scores
    def get_sorted_list(self):
        return sorted(self.scores)
    
    def highest(self):
        return self.get_sorted_list()[-1]
    
    def second_highest(self):
        return self.get_sorted_list()[-2]
    
    def lowest(self):
        return self.get_sorted_list()[0]
    
    def second_lowest(self):
        return self.get_sorted_list()[1]
    
    # Calculate final score
    def calculate_final_score(self):
        total = sum(self.scores)
        return (total - self.highest() - self.second_highest() - self.lowest() - self.second_lowest()) * self.difficulty
    
    # Get total score (final score + carried forward)
    def get_total_score(self):
        return self.calculate_final_score() + self.cf
    
    # Print information
    def print_info(self):
        print(f"{self.country.get_name():<12}", end="")
        for score in self.scores:
            print(f"{score:6.1f}", end="")
        print(f"{self.difficulty:12.1f}{self.cf:9.2f}{self.calculate_final_score():9.2f}{self.get_total_score():9.2f}")
    

    
# Main function to simulate the diving competition
def main():
    countries = ["China 2", "Thailand", "China 1", "South Korea", "Japan", "USA", "Australia", "Malaysia", "Russia", "Brazil"]
    
    carryforward = [0.00 for _ in countries]  # Carryforward array initialized to 0.00
    country_list = [Country(name, f"Name {i+1}", get_age()) for i, name in enumerate(countries)]
    difficulty = [get_difficulty() for _ in countries]  # Generate random difficulty values
    
    for round_num in range(1, 6):
        diving_list = []
        print(f"Round: {round_num}")
        print("Starting position\n")
        display_game_info(country_list, difficulty)
        
        for i in range(len(countries)):
            scores = get_scores()
            diving_list.append(Diving(country_list[i], scores, difficulty[i], carryforward[i]))
        
        print("\nResults:\n")
        display_result_info(diving_list)
        
        # Update carryforward scores
        update_carryforward(diving_list, carryforward)
        
        # Sort and display results
        sorted_diving_list = sorted(diving_list, key=lambda d: d.get_total_score(), reverse=True)
        display_sorted_list(sorted_diving_list)

# Generate random score values between 0 and 10, rounded to 1 decimal place
def get_scores():
    return [round(random.uniform(0, 10), 1) for _ in range(Diving.SIZE)]

# Generate random difficulty value between 2 and 5
def get_difficulty():
    return round(random.uniform(2, 5), 1)

# Generate random age between 15 and 30
def get_age():
    return random.randint(15, 30)

# Display game info (country names, divers, ages, difficulty)
def display_game_info(country_list, difficulty):
    print(f"{'Country':<15}{'Diver':<10}{'Age':<10}{'Difficulty'}")
    for i, country in enumerate(country_list):
        print(f"{country.get_name():<15}{country.get_player():<10}{country.get_age():<10}{difficulty[i]:<10.1f}")

# Display results for each country (judges' scores, difficulty, carried forward, final score, total score)
def display_result_info(diving_list):
    print(f"{'Country':<15}{'J1':<6}{'J2':<6}{'J3':<6}{'J4':<6}{'J5':<6}{'J6':<6}{'J7':<7}{'Difficulty':<13}{'c/f':<9}{'Current':<9}{'Total':<7}")
    for diving in diving_list:
        diving.print_info()

# Update carryforward scores after each round
def update_carryforward(diving_list, carryforward):
    for i, diving in enumerate(diving_list):
        carryforward[i] = diving.get_total_score()

# Display sorted list of results by total score
def display_sorted_list(sorted_diving_list):
    print("The result is:")
    for rank, diving in enumerate(sorted_diving_list, start=1):
        print(f"{rank:<4}{diving.get_country().get_name():<15}{diving.get_total_score():.2f}")

# Run the main function
if __name__ == "__main__":
    main()
