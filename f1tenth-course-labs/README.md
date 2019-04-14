# f1tenth-course-labs
Lab Exercises and Practice Code Repo for F1/10 Autonomous Racing Course at the University of Virginia

This git repo contains the code for ROS packages that you will need through this course. 

## Instructions for how to use the code in this repo

**Step 1)**

Make sure to create a ROS workspace on your machine. Usually this can be done in the home directory.
You would have already doen this in a previous lab session but here we recap all the steps.
You can do this by tying the following coommands in the terminal, one at a time.
If you already have a ROS workspace on your machine, you can skip directly to Step 2, and use your ROS workspace name instead of the name catkin_ws.

~~~bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ..
catkin_make
source ~/catkin_ws/devel/setup.bash
~~~

**Step 2)**

Next create a new directory in your home folder to clone this git repository.

~~~bash
mkdir ~/github
cd ~/github
git clone https://github.com/linklab-uva/f1tenth-course-labs.git
~~~

This will create a `f1tenth-course-labs` folder inside the `github` directory you just created. 

The git repository, will usually contain a folder with the same name as the lab handout issued. 
For example, the repository contains a folder 'beginner_tutorials', which we will use for illustrating the next step. But you may want to replace the folder name with the appropriate name as indicated by the lab handout. 

**Step 3)** 

Create a symbolic link between the folder of interest, e.g. `beginner_tutorials` and the src folder in your catkin workspace.
Note that you may already have a `beginner_tutorials` package that you may have created in a previous lab. We will remove that folder and symbolically link our git repo with the workspace. 

Depending on your ROS workspace. First remove the beginner_tutorials directory and its contents. 

~~~bash
madhur@ubuntu:~$ cd ~/catkin_ws/src/
madhur@ubuntu:~/catkin_ws/src$ rm -rf beginner_tutorials/
~~~

In this example we assume that the root folder for the workspace source does not contain a `beginner_tutorials` directory.
We will make sure all the python scripts are executable:
Run:

~~~bash
ln -s ~/github/f1tenth-course-labs/beginner_tutorials ~/catkin_ws/src/
cd ~/catkin_ws
find . -name “*.py” -exec chmod +x {} \;
catkin_make
source ~/catkin/devel/setup.bash
~~~

Thats it !, you should now be able to run any ROS command that interacts with packages.



