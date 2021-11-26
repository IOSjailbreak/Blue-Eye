#!/bin/sh

git filter-branch -f --env-filter '

    OLD_EMAIL="adool.ali.naim@hotmail.com"
    CORRECT_NAME="Adel Naim"
    CORRECT_EMAIL="Private@Private"
    if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
    then
        export GIT_COMMITTER_NAME="$CORRECT_NAME"
        export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
    fi
    if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
    then
        export GIT_AUTHOR_NAME="$CORRECT_NAME"
        export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
    fi
    ' --tag-name-filter cat -- --exclude="refs/original"
    # originally this had `-- --branches --tags`, but has been revised as
    # per the answer below, and a -f also added.
