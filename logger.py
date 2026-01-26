import pandas as pd
import random

class LogData:
    def __init__(self, path="recordings.csv"):
        self.path = path
        self.lt_label = "lap_time"
        self.read = True 

    # Gets the data from the csv provided into a format we can easily work with
    #
    def get_data(self):
        data = pd.read_csv(self.path)
        if len(data.values) == 0:
            self.read = False
            print("The file is empty!")
            return None
        
        return data
    
    # We get the data (target speed, brake threshold ect) associated with the row with the best lap time
    #
    def get_best_lap(self):
        data = self.get_data()

        if self.read:
            best_row = self.find_row(data)
            x = data.iloc[best_row].tolist()

            return x[:-1] # We exclude the lap time from the array - we have no need for it
        
        return None

    # Finds the index/ row number with the best lap time
    #
    def find_row(self, data):
        if self.read:
            fastest_lap = min(data[self.lt_label]) # Finds the lowest lap time in the data 
            row_index = (data.index[data[self.lt_label] == fastest_lap])[-1]
            
            return row_index
        
        return None
    
    # Gets a random value within the specified range for the parameter
    #
    def deviate_value(self, index):
        DECIMAL_PLACES = 3
        return_value = -1

        if index == 0: # Target speed (75-300)
            return_value = random.uniform(75, 300)
        elif index == 1: # Steer gain (1-100)
            return_value = random.uniform(1, 100)
        elif index == 2: # Centering gain (0-2)
            return_value = random.uniform(0, 2)
        elif index == 3: # Brake threshold (0-1.5)
            return_value = random.uniform(0, 1.5)
        elif index == 4: # Gentle speed (85-160)
            return_value = random.uniform(85, 160)
        elif index == 5: # Sharp speed (50-75)
            return_value = random.uniform(1, 75)
        elif index == 6: # Straight speed (75-300)
            return_value = random.uniform(75, 300) 

        return round(return_value, DECIMAL_PLACES)  

    # Cleans up the data - makes no sense for our target speed to be greater than the straight speed
    # or gentle corner speed to be less than sharp corner speed
    #
    def clean_data(self, data):
        if data[5] > data[4]:
            data[4] = data[5]

        if data[5] > data[0]:
            data[0] = data[5]

        if data[0] > data[6]:
            data[6] = data[0]

        return data

    # Gets the best lap data and changes a single parameter
    #
    def mix_values(self):
        best_lap_data = self.get_best_lap()
        if best_lap_data != None:
            random_index = random.randint(0, len(best_lap_data) - 1)

            best_lap_data[random_index] = self.deviate_value(random_index)
            best_lap_data = self.clean_data(best_lap_data)
            return best_lap_data
        
        else:
            print("No data avaliable")
            return None

    # Formats the statistics of the lap run so that we can easily write it to the csv file
    #
    def format_data(self, lap_run_data):
        text = ""

        for i in range(len(lap_run_data) - 1):
            text += str(lap_run_data[i]) + ","

        text += str(lap_run_data[i+1])

        return text

    # Writes the statistics of the lap run to the csv file
    #
    def log_data(self, lap_run_data):
        with open(self.path, "a") as file:
            file.write("\n")
            text_to_write = self.format_data(lap_run_data)
            file.write(text_to_write)
