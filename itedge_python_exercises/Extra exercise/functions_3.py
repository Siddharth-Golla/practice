"""
Create a function that will show us profile information for a user.
We'll pass parameters to it in the form of username (intended as a string), and followers (intended as an integer).
"""

def profile(username:str, folllowers:int):
    result_str = f"Username : {username.ljust(20)} Followers : {folllowers}"
    return result_str


if __name__ == '__main__':
    print(profile("xyz_itedge", 150))
    print(profile("officallyitedge", 3264))
    print(profile("itedge.in", 351))