# 2025-ITELEC2-S03-E01
Session 03 - Exercise 01 - Working with Variables, Arithmetic and Assignment Operators

---

### **Step 1: Accept the Assignment**

1. Click on the assignment link provided by your instructor.
2. GitHub Classroom will create a **private repository** under your GitHub account.
3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 2: Clone the Repository to Your Local Machine**

1. On your repository page, click the green **"Code"** button.
2. Copy the repository URL (choose HTTPS for simplicity).
3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:

```bash
git clone https://github.com/PLMUN-CITCS/itelec2-s03-e01-[your username].git
```

4. Navigate into the cloned folder:

```bash
cd itelec2-s03-e01-[your username]
```

### **Step 3: Complete the Assignment**

# **Problem Set 01 - Problem 01**
Simple Calculator Program
A. Write a Simple Calculator Program

1. Open `problem_01.py` in your text editor or IDE (Python)
```python
# YOUR NAME
# ITELEC2
# Problem Set 01 - Problem 01
# Simple Calculator Program

def main():
    pass # replace this line with all of your code

if __name__ == "__main__":
    main()
```

2. Replace Line 7 from `problem_01.py`, and start introducing the program
```python
print("Simple Calculator Program")
```

3. Get two numbers from the user
```python
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
```

4. Return the sum of the two numbers
```python
print(f"The sum is {num1 + num2}")
```

5. Return the difference of the two numbers
```python
print(f"The difference is {num1 - num2}")
```

6. Return the product of the two numbers
```python
print(f"The product is {num1 * num2}")
```

7. Return the quotient of the two numbers
```python
print(f"The quotient is {(num1 / num2):.2f}")
```

8. Save `problem_01.py` and verify your work by typing this command in the terminal
```bash
python problem_01.py
```

# **Problem Set 01 - Problem 02**
Square the Number Program
B. Square the Number Program

1. Open `problem_02.py` in your text editor or IDE (Python)
```python
# YOUR NAME
# ITELEC2
# Problem Set 01 - Problem 02
# Square the Number Program

def main():
    pass # replace this line with all of your code

if __name__ == "__main__":
    main()
```

2. Replace Line 7 from `problem_02.py`, and start introducing the program
```python
print("Square the Number Program")
```

3. Get a number from the user
```python
number = int(input("Enter a number: "))
```

4. Return the square of the number
```python
print(f"The square of {number} is {(number*number):.2f}")
```

5. Save `problem_02.py` and verify your work by typing this command in the terminal
```bash
python problem_02.py
```

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
Open the terminal and run:

```bash
git status
```
This command shows any modified or new files.

2. Stage the changes:
Add all modified files to staging:

```bash
git add .
```

3. Commit your changes:
Write a meaningful commit message:

```bash
git commit -m "Submitting Python Session 03 - Exercise 01"
```

4. Push your changes to GitHub:
Upload your changes to your remote repository:

```bash
git push origin main
```

### **Step 5: Submit Your Repository Link**
Once your changes have been pushed:
1. Visit your GitHub repository online.
2. Copy the repository URL from your browser (e.g., https://github.com/PLMUN-CITCS/itelec2-s03-e01-[your username] ).
3. Submit the repository link to your instructor via the classroom portal or as instructed.

