# Spellcheck
Add containerized spellcheck functionality to your Asciidoc repo.

# Installation

1. Clone this repo.
2. Copy all files in the `spellcheck` repo to the asciidoc repo you want to spellcheck. This includes:
* `.github/workflows` - contains the `spellcheck.yaml` GitHub action.
* `bin` contains the spellchecker `spellcheck-ci.py` 
* `aspell.dict` - the dictionary the spellchecker uses. Modify the dictionary to add exceptions for your individual project. 
* `Dockerfile` - builds a base container and tooling. 
3. Push these changes to the repo will cause the GitHub action to run. A successful run of Spellcheck will still show an Action failure if you have spelling errors. 
4. Subsequent pushes will run the Spellchecker.

## Modify Dictionary

To modify the dictionary, open `aspell.dict` and add your specialized nomenclature to the list. Remember to commit the changed `aspell.dict` to your repo.

## Troubleshooting

If you get an Action error like this on `push`:

```
docker: Error response from daemon: failed to create shim: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: “./bin/spellcheck-ci.py”: permission denied: unknown.
```

Change directory to your asciidoc repo and run `chmod +x bin/*` to mark the spellcheck scripts as executable. 

## Credits

This is bradfordcp's work, I'm just distributing it to the team.  
