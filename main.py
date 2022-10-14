import json
import os

from getReddit import getReddit

if __name__ == '__main__':
    use_case = int(input("Please select desired use:\n"
                         "1. Full-Simulation\n"
                         "2. Run with pre-gathered objects.\n"
                         "3. Gather new objects.\n"
                         ">> "))
    print("GETTING TEST POSTS:")
    if use_case == 2:  # run with gathered objects... parse from text files
        for filename in os.listdir("./test_resources/sample_objects/"):
            with open(filename, "r") as json_file:
                reddit_obj = json.load(json_file)
                # problem : this does not return a reddit_obj, just a json_obj.
                # will need to create a constructor to use this with...
    else:
        print("Let's setup your sample...")
        post_num = int(input("How many posts to grab?\n>> "))
        comm_num = int(input("How many comments to grab?\n>> "))
        content = getReddit('askreddit', post_num, comm_num)
        if use_case == 1:
            for post in content:
                post.write_movie()
        elif use_case == 3:
            for i, post in enumerate(content):
                post.write_test_object(i)
            print("Objects written!")
        else:
            print("Input not understood.")
