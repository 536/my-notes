# git commit template

```bash
touch ~/.git_commit_template.txt
```

```txt
# ~/.git_commit_template.txt
TAG: summarize what is changed

# Why is this change happening, e.g. goals, issues etc.
# Why:
# - The reason why this change is made.
# - List each reason in one bullet item.
# - Max 72 characters each line.

# How is this change happening, e.g. implementations, algorithms, etc.
# How:
# Detailed description about what is changed.

# List all relative web pages, issue trackers, co-authors etc.
# See: http://example.com
# See: [Example Page](http://example.com)
# Co-authored-by: Name <name@example.com>
# Co-authored-by: Name <name@example.com>

# ## Help ##
# Summary line TAGs:
#
#   Add = Add new features/tests...
#   Drop = Drop old features/tests...
#   Fix = Fix an issue(bug/typo...)
#   Make = Change build process/tools...
#   Optimize = A change MUST just about performance.
#   Document = A change MUST be only in documentation.
#   Refactor = A change that MUST be just refactoring.
#   Reformat = A change that MUST be just format.
#
```

```bash
git config --global commit.template ~/.git_commit_template.txt
```
