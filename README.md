# mvv.auth.django


# How to build and upload

To upload a built package to our local pip store, we need the file 
[.pypirc](.pypirc).

1. Create a personal access token with the permission "package: Read and Write": [Link](https://dschroeck.ddns.net/gitea/user/settings/applications)
2. Copy the .pypirc file to your HOME: ``cp .pypirc ~/ ``
3. Adapt username and password (password = Personal access token)

Steps 1 and 3 need only be made once.

Now to the actual upload of a version:
4. Increase version number in (version.py)[version.py]
5. ``python setup.py bdist_wheel sdist``
6. ``python3 -m twine upload --repository gitea dist/*``

