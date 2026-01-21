# Importing necessary libraries
import json
import os

class StudyDataManager:
    """
    class that controls the program data (matrix of hours, names of activities, 
    survey results (this last one could be modified soon))
    """
    def __init__(self):
        self.weekly_log = [ # Matrix (rows=days, columns=activities)
            [1.0, 1.0, 0.5, 0.5],
            [0.8, 1.2, 0.7, 0.4],
            [0.6, 1.4, 0.8, 0.5],
            [0.5, 1.0, 1.2, 0.3],
            [0.9, 1.3, 0.7, 0.6],
            [0.7, 1.1, 0.9, 0.4],
            [0.6, 1.0, 1.1, 0.5]
        ]
        
        self.activities = ["Reading/Theory", "Exercises/Practice", # Names of the activities
                    "Project/Programming", "Review/Assessment"]
        
        self.survey_data = { # Results of the survey
            "question1":0.0,
            "question2":0,
            "question3":0,
            "question4":0,
            "question5":0.0,
            "question6":0.0
        }
        
    def update_matrix(self, row, column, value):
        """
        Method to update a specific value in the matrix, using the row, column, 
        and new value as parameters
        """
        self.row = row
        self.column = column
        self.value = float(value)
        if 0<=self.row<=6 and 0<=self.column<len(self.weekly_log[0]):
            self.weekly_log[row][column] = self.value
        else:
            return False
            
    def update_activities(self, index, text):
        """
        Method to change the name of a specific activity, using its index and the new name 
        of the chosen activity as parameters
        """
        self.index = index
        self.text = text
        if 0<=index<len(self.activities):
            self.activities[index] = self.text
        else:
            return False
            
    def add_activities(self, new_activitie):
        """
        Method to add a new activity (column), using the name of the new activitie as a parameter
        """
        self.new_activitie = new_activitie
        self.activities.append(self.new_activitie)
        
    def remove_activities(self, delete_activitie):
        """
        Method to remove a specific activity (column), using the name of the selected 
        activity as a parameter.
        """
        self.delete_activitie = delete_activitie
        self.activities.remove(self.delete_activitie)
        
    def save_to_file(self, filename="study_data.json"):
        """
        Method to save the changed data to a .json file
        """
        data = {
            "matrix": self.weekly_log,
            "activities": self.activities,
            "survey": self.survey_data
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return filename

    def load_from_file(self, filename="study_data.json"):
        """
        Method to load that previously saved data using the generated .json file
        """
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.weekly_log = data.get("matrix", self.weekly_log)
                self.activities = data.get("activities", self.activities)
                self.survey_data = data.get("survey", self.survey_data)
            return True
        return False

data_manager = StudyDataManager()

