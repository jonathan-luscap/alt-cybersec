# itération 1 failles de sécurité

## 1.2 — Un exemple de problème de sécurité
- all extensions run with the privileges of the user that has opened the VSCode without any sandbox 
-> This means that the extension can install any program on your computer including ransomwares, wipers, and more. In fact, it can access and even alter all the code that you have locally and even use your SSH key to change the code in all your organization’s repositories in GitHub.
- typosquatting = A small variation in the URL, such as omitting a letter ‘t’ or transforming ‘b’ to ‘p. 
-> Other registries have fought against this technique and typically don’t allow users to create new packages with such similarities.
- we were able to create a name which is an exact replica of a highly popular extension. These names do not need to be unique and, thus, anyone can enter almost any value desired under these names.
-> anyone can masquerade as almost any extension.
- information about the extension in the GitHub repository : anyone can enter whatever value he wants without validation or confirmation of whether this extension is actually linked to the registry.

## 1.4 — Accéder à la base de données des vulnérabilités
```bash
#!/usr/bin/env bash

echo "