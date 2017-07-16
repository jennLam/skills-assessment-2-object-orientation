"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""

class Student(object):
    """A student."""

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A question."""

    def __init__(self, question, correct_answer):
        """Initialize question attributes."""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Asks the users a question and evaluates the user's input."""
        #display question and store input in variable, answer
        answer = raw_input(self.question + " > ")
        #if answer is equal to the correct answer, return True
        #otherwise return False
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """An exam."""

    def __init__(self, name):
        """Initialize exam attributes."""
        self.name = name
        self.questions = []

    def add_question(self, qs):
        """Adds questions to exam."""
        #append question to questions list
        self.questions.append(qs)

    def administer(self):
        """Administer exam."""
        #create variables num_of_correct and total
        num_of_correct = 0.0

        #loop through questions in the questions list
        for q in self.questions:
            #set a variable equal to the answer validation
            result = q.ask_and_evaluate()
            #if True, the num_of_correct will increment
            if result:
                num_of_correct += 1
            #increment total to get total number of questions
        #return the float of num_of_correct/total number of questions
        return float(num_of_correct/len(self.questions))


class Quiz(Exam):
    """A quiz. Subclass of Exam."""

    def administer(self):
        """Administer quiz."""
        #check if result of super administer method is greater than 0.5
        if super(Quiz, self).administer() >= 0.5:
            #if it is, return 1
            #otherwise, return 0
            return 1
        else:
            return 0


class StudentExam(object):
    """A student exam."""

    def __init__(self, student, exam):
        """Initialize student exam attributes."""
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        """Administer test and print score."""
        #print score taken from administer
        self.score = self.exam.administer()
        print self.score
        

def example():
    """An example of an exam with various questions. A student and student
    exam is also created."""

    #create exam and create various questions
    the_exam = Exam("Final")
    q1 = Question("What color is the sun?", "yellow")
    q2 = Question("What color is the grass?", "green")
    q3 = Question("What color is the sky?", "blue")
    q4 = Question("What color is the dirt?", "brown")

    #add question to exam
    the_exam.add_question(q1)
    the_exam.add_question(q2)
    the_exam.add_question(q3)
    the_exam.add_question(q4)

    #create student
    the_student = Student("Jenny", "Lam", "12 Blue St")

    #create student exam using the_student and the_exam
    student_exam = StudentExam(the_student, the_exam)
    #have student take test
    student_exam.take_test()

if __name__ == "__main__":
    example()