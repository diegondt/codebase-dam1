flowchart TD

start["git init"]
add["git add archivo"]
commit["git commit -m 'mensaje con los cambios'"]

start --> add --> commit

commit -- es un repo de github --> push["git push"]
commit -- es un repo local --> create["gh repo create"]