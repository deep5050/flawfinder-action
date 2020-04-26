import os
import subprocess as sp


GITHUB_EVENT_NAME = os.environ['GITHUB_EVENT_NAME']

# Set repository
CURRENT_REPOSITORY = os.environ['GITHUB_REPOSITORY']
# TODO: How about PRs from forks?
TARGET_REPOSITORY = os.environ['INPUT_TARGET_REPOSITORY'] or CURRENT_REPOSITORY
PULL_REQUEST_REPOSITORY = os.environ['INPUT_PULL_REQUEST_REPOSITORY'] or TARGET_REPOSITORY
REPOSITORY = PULL_REQUEST_REPOSITORY if GITHUB_EVENT_NAME == 'pull_request' else TARGET_REPOSITORY

# Set branches
GITHUB_REF = os.environ['GITHUB_REF']
GITHUB_HEAD_REF = os.environ['GITHUB_HEAD_REF']
GITHUB_BASE_REF = os.environ['GITHUB_BASE_REF']
CURRENT_BRANCH = GITHUB_HEAD_REF or GITHUB_REF.rsplit('/', 1)[-1]
TARGET_BRANCH = os.environ['INPUT_TARGET_BRANCH'] or CURRENT_BRANCH
PULL_REQUEST_BRANCH = os.environ['INPUT_PULL_REQUEST_BRANCH'] or GITHUB_BASE_REF
BRANCH = PULL_REQUEST_BRANCH if GITHUB_EVENT_NAME == 'pull_request' else TARGET_BRANCH

GITHUB_ACTOR = os.environ['GITHUB_ACTOR']
GITHUB_REPOSITORY_OWNER = os.environ['GITHUB_REPOSITORY_OWNER']
GITHUB_TOKEN = os.environ['INPUT_GITHUB_TOKEN']

# command related inputs

REPORT_TYPE = os.environ['INPUT_REPORT_TYPE'] or 'html'
DATA_ONLY = os.environ['INPUT_DATA_ONLY'] or 'disable'
NEVER_IGNORE = os.environ['INPUT_NEVER_IGNORE'] or 'disable'
FALSE_POSITIVE = os.environ['INPUT_FALSE_POSITIVE'] or 'disable'
INPUT_FLAGS = os.environ['INPUT_INPUT_FLAGS'] or 'disable'
DOT_DIR = os.environ['INPUT_DOT_DIRECTORIES'] or 'disable'
ALLOW_LINK = os.environ['INPUT_ALLOW_LINK'] or 'disable'


command = ""
out_file = ""


def prepare_command():
    global command
    global out_file
    command = command + "flawfinder "
    # check every flags
    if REPORT_TYPE == 'html':
        out_file = "flawfinder_report.html"
        command = command + " --html"

    elif REPORT_TYPE == "text":
        out_file = "flawfinder_report.txt"

    if DATA_ONLY == 'enable':
        command = command + " --dataonly"

    if NEVER_IGNORE == "enable":
        command = command + " --neverignore"

    if FALSE_POSITIVE == "enable":
        command = command + " --falsepositive"

    if INPUT_FLAGS == "enable":
        command = command + " --inputs"

    if DOT_DIR == "enable":
        command = command + " --followdotdir"

    if ALLOW_LINK == "enable":
        command = command + " --allowlink"


def run_flawfinder():
    global command
    command = command + f" --columns --context --singleline . >{out_file}"
    sp.call(command, shell=True)


def commit_changes():
    """Commits changes.
    """
    set_email = 'git config --local user.email "flawfinder-action@master"'
    set_user = 'git config --local user.name "flawfinder-action"'

    sp.call(set_email, shell=True)
    sp.call(set_user, shell=True)

    git_checkout = f'git checkout {TARGET_BRANCH}'
    git_add = f'git add {out_file}'
    git_commit = 'git commit -m "flawfinder report added"'
    print(f'Committing {out_file}')

    sp.call(git_checkout, shell=True)
    sp.call(git_add, shell=True)
    sp.call(git_commit, shell=True)


def push_changes():
    """Pushes commit.
    """
    set_url = f'git remote set-url origin https://x-access-token:{GITHUB_TOKEN}@github.com/{TARGET_REPOSITORY}'
    git_push = f'git push origin {TARGET_BRANCH}'
    sp.call(set_url, shell=True)
    sp.call(git_push, shell=True)


def main():

    if (GITHUB_EVENT_NAME == 'pull_request') and (GITHUB_ACTOR != GITHUB_REPOSITORY_OWNER):
        return

    prepare_command()
    run_flawfinder()
    commit_changes()
    push_changes()


if __name__ == '__main__':
    main()
