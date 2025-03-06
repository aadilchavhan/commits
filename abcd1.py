import os
from datetime import datetime

def make_commits(num_commits: int):
    # Get the current date and time
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    for i in range(num_commits):
        # Append some text to the file
        with open('data.txt', 'a') as file:
            file.write(f'Commit {i + 1} on {current_date}\n')
        
        # Add the file to the staging area
        os.system('git add data.txt')
        
        # Commit with a unique message for each commit
        os.system(f'git commit --date="{current_date}" -m "Commit {i + 1} on {current_date}"')

    # Push all commits after loop
    os.system('git push')

# Call the function with the desired number of commits
make_commits(100)