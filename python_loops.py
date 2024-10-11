import random
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["happy", "sad", "energetic", "calm",
         "lazy", "excited", "hopeful", "angry", "relaxed"]

#1. Range Riddle
for i in range(len(days)):
    mood = random.choice(moods)
    print("On " + days[i] + ", I felt " + mood)

#2. double scoop with nested loops
times = ["morning", "afternoon", "evening"]
for i in range(len(days)):
    for j in range(len(times)):
        mood = random.choice(moods)
        print("On " + days[i] + " " +  times[j] + ", I felt " + mood)