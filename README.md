1. Make sure you type the correct config locally

# Pushing with different account

```
git config --local user.name <username>
git config --local user.email <emailAddress>
```

2. Reset the git credential locally

```
git config --local credential.helper ""
```

3. Commit and push any changes and git will prompt login upon you push

```
git push
```

# Utils

Any script i developed that helps boost efficiency of doing certain action will also be put here

# health-checks

Scripts that check the health of my computers

This repo will be populated with lots of fancy checks.

We have checks to system cpu, network connectivity and disk space
