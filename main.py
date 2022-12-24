from tkinter import *

'''

Grade Points
S 10
A9
B8
C7
D6
E4
U0
W,I 0
H,L 0
'''
root = Tk(className=" MARKSHEET")
root.geometry("+750+500")
root.geometry("1000x300")
root.configure(bg="light grey")


def grading(grade):
    if grade == 'S':
        return 10
    if grade == 'A':
        return 9
    if grade == 'B':
        return 8
    if grade == 'C':
        return 7
    if grade == 'D':
        return 6
    if grade == 'E':
        return 4
    else:
        return 0


def cgpa():
    c1 = (Sub_1.get())
    c2 = (Sub_2.get())
    c3 = (Sub_3.get())
    c4 = (Sub_4.get())
    g1 = grading(c1)
    g2 = grading(c2)
    g3 = grading(c3)
    g4 = grading(c4)
    sum = ((g1 * 4) + (g2 * 4) + (g3 * 3) + (g4 * 4))
    sgpaa = sum / 15
    total_credit = 0

    if g1 != 0:
        crd_1.config(text="4")
        total_credit += 4
    else:
        crd_1.config(text="0")
    if g2 != 0:
        crd_2.config(text="4")
        total_credit += 4
    else:
        crd_2.config(text="0")
    if g3 != 0:
        crd_3.config(text="3")
        total_credit += 3
    else:
        crd_3.config(text="0")
    if g4 != 0:
        crd_4.config(text="4")
        total_credit += 4
    else:
        crd_4.config(text="0")

    tot_cred_out.config(text=str(total_credit))
    sgpa_out.config(text=str(round(sgpaa, 2)))


# column 1 :
name_label = Label(root, text="Name", bg="light grey")
name_label.grid(row=1, column=1)

roll_no = Label(root, text="Roll.No.", bg="light grey")
roll_no.grid(row=2, column=1)

srl_no = Label(root, text="Srl.No", bg="light grey")
srl_no.grid(row=3, column=1)

no_1 = Label(root, text="1", bg="light grey")
no_1.grid(row=4, column=1)

no_2 = Label(root, text="2", bg="light grey")
no_2.grid(row=5, column=1)

no_3 = Label(root, text="3", bg="light grey")
no_3.grid(row=6, column=1)

no_4 = Label(root, text="4", bg="light grey")
no_4.grid(row=7, column=1)

# column 2:
Name_entry = Entry(root, width=20)
Name_entry.get()
Name_entry.grid(row=1, column=2)

Roll_entry = Entry(root, width=20)
Roll_entry.get()
Roll_entry.grid(row=2, column=2)

Subj_lbl = Label(root, text="Subject", bg="light grey")
Subj_lbl.grid(row=3, column=2)

sub_1 = Label(root, text="CS 201", bg="light grey")
sub_1.grid(row=4, column=2)

sub_2 = Label(root, text="CS 202", bg="light grey")
sub_2.grid(row=5, column=2)

sub_3 = Label(root, text="MA 201", bg="light grey")
sub_3.grid(row=6, column=2)

sub_4 = Label(root, text="EC 201", bg="light grey")
sub_4.grid(row=7, column=2)

submit = Button(root, text="submit", fg="black", bg="green", command=cgpa)
submit.grid(row=9, column=2)

# column 3
grade = Label(root, text="Grade", bg="light grey")
grade.grid(row=3, column=3)

Sub_1 = Entry(root, width=20)
Sub_1.grid(row=4, column=3)

Sub_2 = Entry(root, width=20)
Sub_2.grid(row=5, column=3)

Sub_3 = Entry(root, width=20)
Sub_3.grid(row=6, column=3)

Sub_4 = Entry(root, width=20)
Sub_4.grid(row=7, column=3)

tot_cred_out = Label(root, text="", bg="light grey")
tot_cred_out.grid(row=8, column=3)

sgpa_out = Label(root, text="", bg="light grey")
sgpa_out.grid(row=9, column=3)

# column 4
reg = Label(root, text="Reg.No", bg="light grey")
reg.grid(row=1, column=4)

Sub_credit = Label(root, text="Sub Credit", bg="light grey")
Sub_credit.grid(row=3, column=4)

cr_1 = Label(root, text="4", bg="light grey")
cr_1.grid(row=4, column=4)

cr_2 = Label(root, text="4", bg="light grey")
cr_2.grid(row=5, column=4)

cr_3 = Label(root, text="3", bg="light grey")
cr_3.grid(row=6, column=4)

cr_4 = Label(root, text="4", bg="light grey")
cr_4.grid(row=7, column=4)

tot = Label(root, text="Total credit", bg="light grey")
tot.grid(row=8, column=4)

scgpa = Label(root, text="SGPA", bg="light grey")
scgpa.grid(row=9, column=4)

# column 5
reg_entry = Entry(root, width=20)
reg_entry.grid(row=1, column=5)

crdt_ob = Label(root, text="Credit obtained", bg="light grey")
crdt_ob.grid(row=3, column=5)

crd_1 = Label(root, text="", bg="light grey")
crd_1.grid(row=4, column=5)

crd_2 = Label(root, text="", bg="light grey")
crd_2.grid(row=5, column=5)

crd_3 = Label(root, text="", bg="light grey")
crd_3.grid(row=6, column=5)

crd_4 = Label(root, text="", bg="light grey")
crd_4.grid(row=7, column=5)
root.mainloop()
