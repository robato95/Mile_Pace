import tkinter as tk
import pandas as pd
import datetime



class Mile_Backend():
    def __init__(self):
        self._age = 16
        self._gender = 'male'
        self._fitness = 'average'
        self._time = ''
        self._df_male = pd.read_excel(r"/Users/robertvargas/Documents/Projects/Python/Mile Time/Mile_Information.xlsx", sheet_name = 'Male')
        self._df_female = pd.read_excel(r"/Users/robertvargas/Documents/Projects/Python/Mile Time/Mile_Information.xlsx", sheet_name = 'Female')
        ##the data frames are based off data obtained from
        ##https://www.healthline.com/health/average-mile-time#by-age

class Mile_GUI():
    def __init__(self, root):
        root.title("Mile Time App")
        root['background'] = 'purple'
        root.geometry("500x200")
        self._backend = Mile_Backend()
        ##age items
        age_label = tk.Label(text = "Age:", bg = 'purple', fg = 'white')
        age_label.grid(row = 0, column = 0)
        self._age_entry = tk.Entry()
        self._age_entry.grid(row = 0, column = 1)
        ##gender items
        gender_label = tk.Label (text = "Gender", bg = 'purple', fg = 'white')
        gender_label.grid(row = 1, column =0)
        self._gender_var = tk.StringVar()
        gender_male = tk.Radiobutton(text = 'male', value = "male", 
                                     variable = self._gender_var, command = self.gender_selection)
        gender_male.grid(row = 1, column = 1)
        gender_female = tk.Radiobutton(text = 'female', value = "female",  
                                       variable = self._gender_var, command = self.gender_selection)
        gender_female.grid(row = 1, column = 2)
        ##fitness items
        fitness_label = tk.Label (text = 'Fitness Level:', bg = 'purple', fg = 'white')
        fitness_label.grid(row = 3, column = 0)
        fitness_levels = ['Active', 'Average', 'Below Average']
        self._fitnesslevel = tk.StringVar()
        self._fitnesslevel.set(fitness_levels[0])
        fitness_option = tk.OptionMenu(root, self._fitnesslevel,*fitness_levels)
        fitness_option.grid(row = 3, column = 1)
        ##blank row
        blank_label = tk.Label (text = "", bg = 'purple', fg = 'white')
        blank_label.grid(row = 4, column = 1)
        ##retrieve button
        calculate_button= tk.Button(text = "Retrieve", fg = "purple", command = self.mile_output)
        calculate_button.grid(row = 5, column = 1)
        ##blank row
        blank_label = tk.Label (text = "", bg = 'purple', fg = 'white')
        blank_label.grid(row = 6, column = 1)
        ##output items
        output_label = tk.Label (text = "Mile Time:", bg = 'purple', fg = 'white')
        output_label.grid( row = 7, column = 0)
        self._output_entry = tk.Entry ( fg = "black", bg = "white")
        self._output_entry.grid(row = 7, column = 1)
        
    def gender_selection(self):
        self._backend._gender = str(self._gender_var.get())
    
    def conversion(self, n):
        return str(datetime.timedelta(seconds=int(n)))
    
    def retrieve_mile_info(self):
        self._backend._age = int(self._age_entry.get())
        self._backend._fitness = self._fitnesslevel.get()
        if self._backend._gender == 'male':
            if self._backend._fitness == "Average":
                return(self._backend._df_male.iloc[self._backend._age - 16]['Average'])
            elif self._backend._fitness == "Active":
                return(self._backend._df_male.iloc[self._backend._age - 16]['Active'])
            elif self._backend._fitness == 'Below Average':
                return(self._backend._df_male.iloc[self._backend._age-16]['Below Average'])
        elif self._backend._gender  == 'female':
            if self._backend._fitness == "Average":
                return(self._backend._df_female.iloc[self._backend._age - 16]['Average'])
            elif self._backend._fitness == "Active":
                return(self._backend._df_female.iloc[self._backend._age - 16]['Active'])
            elif self._backend._fitness == 'Below Average':
                return(self._backend._df_female.iloc[self._backend._age-16]['Below Average']) 
    
    def mile_output(self):
        self._backend._time = self.retrieve_mile_info()
        self._backend._time = self.conversion(self._backend._time)
        self._output_entry.delete(0, tk.END)
        self._output_entry.insert(0, self._backend._time)
        
if __name__ == "__main__":  
    root= tk.Tk()
    app = Mile_GUI(root)
    root.mainloop()
