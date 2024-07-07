#! Problem1
# print("""
#     Twinkle, twinkle, little star,
#     How I wonder what you are!
#     Up above the world so high,
#     Like a diamond in the sky.

#     When the blazing sun is gone,
#     When he nothing shines upon,
#     Then you show your little light,
#     Twinkle, twinkle, all the night.

#     Then the trav'ller in the dark,
#     Thanks you for your tiny spark,
#     He could not see which way to go,
#     If you did not twinkle so.

#     In the dark blue sky you keep,
#     And often thro' my curtains peep,
#     For you never shut your eye,
#     Till the sun is in the sky.

#     'Tis your bright and tiny spark,
#     Lights the trav'ller in the dark:
#     Tho' I know not what you are,
#     Twinkle, twinkle, little star.""")

#! Problem3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

#! Problem4
# import os

# def list_directory_contents(directory):
#     try:
#         # List all files and directories in the specified directory
#         with os.scandir(directory) as entries:
#             for entry in entries:
#                 print(entry.name)
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{directory}'.")

# # Specify the directory you want to list
# directory_to_list = '/'
# list_directory_contents(directory_to_list)
