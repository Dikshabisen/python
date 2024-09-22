import datetime
import logging
from question_master import QuestionMaster

# Set up logging to keep track of what happens during the exam and to record any mistakes.
logging.basicConfig(level=logging.INFO, filename='exam_client.log', 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class ExamClient:
    def __init__(self):
        self.qm = QuestionMaster()
        self.score = 0
        self.total_questions = len(self.qm.questions)

    def start_exam(self):
        try:
            #to display current date and time
            print(f"Today's date and time: {datetime.datetime.now().strftime('%d/%b/%Y %H.%M.%S')}")
            student_name = input("Enter student name: ")
            university = input("Enter university: ")
            logging.info(f"Exam started for {student_name} from {university}")

            # iterate through each question in the question set

            for question in self.qm.questions:
                print(f"{question.num}) {question.question}")
                for key, value in question.options.items():
                    print(f"{key}) {value}")

                try:
                    answer = input("Enter your choice: ")
                    if answer == question.correct_option:
                        self.score += 1
                except Exception as e:
                    logging.error("Error processing answer input: " + str(e))
                    print("Error processing answer. Please try again.")
        
            print(f"Student name = {student_name}")
            print(f"University = {university}")
            print(f"Marks scored = {self.score} out of {self.total_questions}")

        except Exception as e:
            logging.error("Error starting exam: " + str(e))
            print("An error occurred while starting the exam. Please try again.")

def main():
    #create an object of class ExamClient and start the exam
    exam = ExamClient() 
    exam.start_exam()

if __name__ == "__main__":
    main()
