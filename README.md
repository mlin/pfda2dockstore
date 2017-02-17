# pfda2dockstore
Export precisionFDA apps to Dockstore

## GitHub Repo Creation

This script (`createrepo.py`) takes your Github token and an organization name and creates a repository in it with a given CWL and Dockerfile.

    pip install PyGithub
    python createrepo.py --token $GITHUB_TOKEN --org pfda2dockstore --tool test5

This will create a test5 repo in Github under the pfda2dockstore organization.
