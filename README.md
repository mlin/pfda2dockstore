# pfda2dockstore

Export precisionFDA apps to Dockstore

## GitHub Repo Creation

This script (`createrepo.py`) takes your Github token and an organization name and creates a repository in it with a given CWL and Dockerfile.  I had to use two libraries here because PyGithub has a bug when creating a release.

    pip install PyGithub agithub

    python createrepo.py --token $GITHUB_TOKEN --org pfda2dockstore --tool test5 --tag 1.0.0

This will create a test5 repo in Github under the pfda2dockstore organization.

## TODO

* working through tagging, I need to merge with Mike's script

## Quay.io Repo Creation

Actions:

  * Given a Quay token, and Github token, and github repo:
     * Initialize a quay repo with the same name from a Dockerfile in the github repo
     * Setup auto build on any new tag or branch update

## Dockstore Registration

Need to add this code, Ola is working on this.

----

Inputs: Github Token, Quay.io token, reponame, list of files
