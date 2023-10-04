# UsumTestTask
test tasks which left after interview

Howto:
1. Simple path (not sure that really simple)
_NB:docker exec only from terminal, needs extended tty
   docker-build -t usumtesttask in directory with Dockerfile
   docker exec -d usumtesttask python3 your_host -- Task.py 
  //https://code.visualstudio.com/docs/containers/quickstart-python#_build-run-and-debug-the-container
  
3. Oldschool path
  Just create new venv 3.11, install requirements, run via terminal like 'python Task.py', that's all

Known issues:
1. Do not press Cancel
2. May be (definitely) some other bugs (almost no try catches)
3. Idk about windows environment running
