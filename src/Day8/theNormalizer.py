import numpy as np

student_list= np.random.randint(50,101,size=(5,3))
subject_mean= np.mean(student_list, axis=0)
centered= (student_list - subject_mean)
print("Original Scores:\n",student_list)
print("Centered Scores:\n",centered)