- Prune local branches: `git fetch -p`
- start maintenance: `git maintenance start`
- 'real blame': `git blame -w -C -C -C`

equivalent in intellij (not really sure it's completely equivalent, maybe it's just -C -C)
<img width="546" alt="image" src="https://github.com/shautvast/notes/assets/3645743/ea6a901a-2d4d-42ea-9858-594827ae66ea">

MAN:
In addition to -M, detect lines moved or copied from other files that were modified in the same commit. This is useful when you reorganize your program and move code around across files. When this option is given twice, the command
           additionally looks for copies from other files in the commit that creates the file. When this option is given three times, the command additionally looks for copies from other files in any commit.
