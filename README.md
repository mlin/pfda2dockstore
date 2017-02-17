# pfda2dockstore

Export precisionFDA apps to Dockstore

## GitHub Repo Creation

This script (`createrepo.py`) takes your Github token and an organization name and creates a repository in it with a given CWL and Dockerfile.

    pip install PyGithub
    python createrepo.py --token $GITHUB_TOKEN --org pfda2dockstore --tool test5

This will create a test5 repo in Github under the pfda2dockstore organization.

Actions:

* I left off with a problem tagging... see https://github.com/PyGithub/PyGithub/issues/488

## Quay.io Repo Creation

Actions:

  * Given a Quay token, and Github token, and github repo:
     * Initialize a quay repo with the same name from a Dockerfile in the github repo
     * Setup auto build on any new tag or branch update

----

Inputs: Github Token, Quay.io token, reponame, list of files
