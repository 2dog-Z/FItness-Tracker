class User:
    def __init__(self,username):
        #Define all the self variables
        self.username=username
        self.exercises=[]
        
    def get_username(self):
        return self.username
    
    def get_exercises(self):
        return self.exercises

    def read_data(self):
        try:
            with open(f"{self.username}.txt",'r') as file:  #Try to open a file
                lines=file.readlines()  #have all the lines
                for line in lines:  #loop
                    if line.strip():  # ignore the empty lines
                        data=line.strip().split(',')    #divide the data, and ignore the space and the empty
                        exercise=Exercise(data[0], data[1], data[2], data[3])
                        self.exercises.append(exercise) #add into the list
                return True
        except:
            print(f"{self.username} has no available data.")    #Error
            return False
        
    def calculate_distance(self,exercise_name,month):
        total_distance=0
        for exercise in self.exercises: #loop
            if exercise.get_name()==exercise_name:  #If the same
                if month is None or exercise.get_date().strip()==month: #month, string or None, the month the exercises took place (mm/yyyy) format
                    total_distance+=exercise.get_distance() #Calculate
        return total_distance

    #the below have the same idea
    
    def calculate_duration(self,exercise_name,month):
        total_duration=0
        for exercise in self.exercises:
            if exercise.get_name()==exercise_name:
                if month is None or exercise.get_date().strip()==month:
                    total_duration+=exercise.get_duration()
        return total_duration

    def calculate_max_distance(self,exercise_name):
        max_distance=0
        for exercise in self.exercises:
            if exercise.get_name()==exercise_name:
                max_distance=max(max_distance,exercise.get_distance())
        return max_distance
    
    def calculate_max_duration(self,exercise_name):
        max_duration=0
        for exercise in self.exercises:
            if exercise.get_name()==exercise_name:
                max_duration=max(max_duration,exercise.get_duration())
        return max_duration


class Exercise:
    def __init__(self, name, disStr, duratStr, date):
        #Define all the self variables
        self.name=name
        self.distance=float(disStr) #Convert into float
        self.duration=int(duratStr) #Convert into int
        self.date=date
        
    #All the below use return to finish
    
    def get_name(self):
        return self.name

    def get_distance(self):
        return self.distance

    def get_date(self):
        return self.date

    def get_duration(self):
        return self.duration


def welcome_screen():
    #Re-use your "Display the welcome screen" code!
    line="*-"*13+'*'    #Get the repeat line in one variable
    print(line)
    print("| WELCOME TO USYD FITNESS |")
    print(line)
    print("*    LOGS YOUR WORKOUT    *")
    print("*   TRACKS YOUR FITNESS   *")
    print("*    GET FIT & HEALTHY    *")
    print(line)


def login():
    #Re-use your "Create a login screen" code!
    #Remember to update so that it:
        #Returns the username OR
        #Returns None
    inStr=input("Login with your username: ")
    if len(inStr)<=20:
        line='~'*27 #Get the repeat line in one variable
        print(line)
        print(f"| Hi {inStr}{' '*(21-len(inStr))}|")    #Calculate how many spaces
        print(line)
        print("| [1] Log an activity     |")
        print("| [2] Track your fitness  |")
        print("| [3] Plan your health    |")
        print(line)
        return inStr
    else:
        print("Your username is too long.") #Error message
        return None


def is_valid_date(date: str):
    #write your function code here
    if not '/' in date: #Find if there a /
        print("Please use '/' as a separator")
        return False
    else:
        try:
            month=date[:2]  #suppose the input is right, like MM/YYYY. So month is before the 2nd character
            year=date[3:] #Same as before
            if not month.isdigit() or not 1 <= int(month) <= 12:    #Justice if this is number, and if the number is valid
                print("Please enter a valid month.")
                return False
            if not year.isdigit() or not 2000 <= int(year) <= 2025:
                print("Please enter a valid year.")
                return False
        except:
            print("Please enter a valid month.")    #Error message
            return False
        return True


def log_workout(username: str):
    #write your function code here
    exercise=input("What exercise would you like to log? ")
    suExercise=['swim', 'run', 'cycle'] #Define the valid list
    if exercise.lower() not in suExercise:  #Use lower to justify
        print(f"Sorry, {exercise} is not supported.")
        return False
    inDate=input(f"What month did you {exercise} (mm/yyyy)? ")
    if not is_valid_date(inDate):   #Justify if the date valid
        return False
    disStr=input(f"What distance did you {exercise} (km or miles)? ")
    if 'miles' in disStr:   #Convert miles into km
        distance=float(disStr.replace('miles',''))
        distance=round(distance*1.6,1)
    else:
        distance=float(disStr.replace('km','')) #Convert into number
        distance=round(distance,1)
    time=int(input(f"How long did you {exercise} (minutes)? "))
    filename=f"{username}.txt"  #Open the file
    try:
        file=open(filename,'a')
        file.write(f"{exercise.lower()},{distance},{time},{inDate}\n")
        file.close()
    except:
        file=open(filename,'w')
        file.write(f"{exercise.lower()},{distance},{time},{inDate}\n")
        file.close()
    return True


def track_activity(username):
    user=User(username)
    if not user.read_data():
        return False
    #Get tracking exercise
    exercise=input("What exercise would you like to track? ")
    #su means Suitable
    suExercise=['swim', 'run', 'cycle'] #Define the valid list
    if exercise.lower() not in suExercise:  #Use lower to justify
        print(f"Sorry, {exercise} is not supported.")
        return False
    #Get tracking month
    month=input("What month would you like to track (mm/yyyy)? ")
    if month.lower()!="all":
        if not is_valid_date(month):
            return False
    else:
        month=None
    #Calculate
    total_distance=user.calculate_distance(exercise.lower(),month)
    total_duration=user.calculate_duration(exercise.lower(),month)
    exercise_count=0
    for exerc in user.get_exercises():
        if exerc.get_name()==exercise.lower():    #Only Calculate Currente Exercise
            if month is None or exerc.get_date().strip()==month:
                exercise_count+=1
    if exercise_count==0:
        return False
    #Calculate the average
    avg_distance=total_distance/exercise_count
    avg_duration=total_duration/exercise_count
    avg_speed=total_distance/(total_duration/60)
    #Print out
    print(f"Total distance: {total_distance:.1f}km")
    print(f"Average distance: {avg_distance:.1f}km")
    print(f"Total duration: {total_duration} mins")
    print(f"Average duration: {avg_duration:.0f} mins")
    print(f"Average speed (km/h): {avg_speed:.2f}km/h")
    return True


def plan_health(username):
    user=User(username)
    if not user.read_data():
        return False
    goal=input("What goal would you like to achieve? ")
    suGoal=['marathon run', 'marathon swim', 'century', 'ironman', '5 minute mile'] #Define the valid list
    if goal.lower() not in suGoal:  #Use lower to justify
        print(f"Sorry, that goal is not supported.")
        return False
    weeks=int(input("How many weeks do you have to achieve it? "))

    if goal.lower()=='marathon run':
        max_run=user.calculate_max_distance('run')
        if max_run<42:
            left_distance=(42-max_run)/weeks    #Calculate the left distance
        else:
            left_distance=0.0   #No need to increase
        print(f"To achieve the {goal} challenge you need to:")
        print(f"    Increase your max run by {left_distance:.1f}km per week.")

    elif goal.lower()=='marathon swim':
        max_swim=user.calculate_max_distance('swim')
        if max_swim<10:
            left_distance=(10-max_swim)/weeks
        else:
            left_distance=0.0
        print(f"To achieve the {goal} challenge you need to:")
        print(f"    Increase your max swim by {left_distance:.1f}km per week.")

    elif goal.lower()=='century':
        max_cycle=user.calculate_max_distance('cycle')
        if max_cycle<100:
            left_distance=(100-max_cycle)/weeks
        else:
            left_distance=0.0
        print(f"To achieve the {goal} challenge you need to:")
        print(f"    Increase your max cycle by {left_distance:.1f}km per week.")     

    elif goal.lower()=='ironman':
        max_swim=user.calculate_max_distance('swim')
        max_cycle=user.calculate_max_distance('cycle')
        max_run=user.calculate_max_distance('run')
        if max_swim<4:  #If the max is less than the goal
            swim_increase=(4-max_swim)/weeks
        else:
            swim_increase=0.0
        if max_cycle<180:
            cycle_increase=(180-max_cycle)/weeks
        else:
            cycle_increase=0.0
        if max_run<42:
            run_increase=(42-max_run)/weeks
        else:
            run_increase=0.0
        print(f"To achieve the {goal} challenge you need to:")
        print(f"    Increase your max swim by {swim_increase:.1f}km per week.")
        print(f"    Increase your max cycle by {cycle_increase:.1f}km per week.")
        print(f"    Increase your max run by {run_increase:.1f}km per week.")     

    else:  # 5 minute mile
        max_speed=0
        for exercise in user.get_exercises():   #loop
            if exercise.get_name()=="run":
                speed=exercise.get_distance()/exercise.get_duration()*60  #Calculate the speed
                if speed>max_speed:
                    max_speed=speed #Update the max speed
        target_speed=19.2    #The target speed
        if max_speed<target_speed:
            speed_increase=(target_speed-max_speed)/weeks   #Calculate the increase
        else:
            speed_increase=0.0
        print(f"To achieve the {goal} challenge you need to:")
        print(f"    Increase your max speed by {speed_increase:.2f}km/h per week.")
    return True


def main():
    #print the welcome screen
    welcome_screen()
    username=None
    while username is None:
        username=login()    #Login menu
    option=input("Choose an option: ")
    if option=="1":
        log_workout(username)
    elif option=="2":
        track_activity(username)
    elif option=="3":
        plan_health(username)
    return


if __name__ == '__main__':
    main()
