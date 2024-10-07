# Workflow
## Branches
- master: do not change here; use this to copy changes from Consortium to own repository
    - update using github webpage: https://github.com/SteffenBrinckmann/TheELNFileFormat
    - pull those changes down and merge them into other branches
- new_pastaELN: use this to stage changes that become a pull-request in the consortium repo
    - only create / copy changes in once you are sure everything is fine (all tests successful)
    - use "git checkout playground FILE-NAME" to copy changes (filenames: PASTA.eln, README.md)
    - the branch name can differ
- playground: your local copy to test and develop things
    - can be pushed to own repository
    - can have nice .gitignore and all zip-extracted examples; you can delete non-working .elns
    - use to develop the tests
## Commands
Steps:
- go to playground
- create readme file and check
- commit and github-action test the new file
- go to new_version_branch
- copy content and commit and push

``` bash
git checkout playground
cp /tmp/PASTA.eln examples/PASTA/PASTA.eln
python tools/eln2md.py -d examples/PASTA/
tail examples/PASTA/README.md
git commit -a -m 'updated eln export of pasta-eln'
git push
# wait for tests to run
git checkout new_PastaELN
git checkout playground examples/PASTA/PASTA.eln
git checkout playground examples/PASTA/README.md
git commit -m 'updated eln export of pasta-eln'
git push
```

- wait for test, which might fail because the test scripts are not as awesome
- go to https://github.com/TheELNConsortium/TheELNFileFormat
