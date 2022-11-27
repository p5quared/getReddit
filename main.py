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
    if use_case == 2:  # Test Run
        for filename in os.listdir("./test_resources/sample_objects/"):
            with open(filename, "r") as json_file:
                reddit_obj = json.load(json_file)
                # problem : this does not return a reddit_obj, just a json_obj.
                # will need to create a constructor to use this with...
    print("Let's setup your sample...")
    post_num = 1
    comm_num = 5
    content = getReddit('askreddit', post_num, comm_num)
    if use_case == 3:  # Gather Objects
        for post in content:  # Post Object
            all_post_content = {"head": post.head.__dict__,
                                "comments": [comment.__dict__ for comment in post.comments]}
            with open("./test_resources/sample_objects/"+str(post.head.body), 'w') as f:
                json.dump(all_post_content, f, indent=2)
    if use_case == 1:
        for post in content:
            post.write_movie()
    elif use_case == 3:
        # Saving new json object
        for i, post in enumerate(content):
            post.write_test_object(i)
        print("Objects written!")
    else:
        print("Input not understood.")
