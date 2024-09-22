


import csv
import logging


logging.basicConfig(level=logging.INFO, filename='question_master.log', 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Question:
    #Represents a single question with its number, text, options, and correct answer
    def __init__(self, num, question, options, correct_option):
        self.num = num
        self.question = question
        self.options = options
        self.correct_option = correct_option

class QuestionMaster:
    #To load questions from a CSV file when the class QuestionMaster is created
    def __init__(self):
        self.questions = self.load_questions()

    def load_questions(self):
        questions = []
        try:
            # Open the CSV file and read the questions
            with open('questions.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    num = int(row['num'])
                    question = row['question']
                    options = {
                        'A': row['A'].split('=')[1],
                        'B': row['B'].split('=')[1],
                        'C': row['C'].split('=')[1],
                        'D': row['D'].split('=')[1],
                    }
                    correct_option = row['correctoption']
                    questions.append(Question(num, question, options, correct_option))
            logging.info("Questions loaded successfully.")
        except FileNotFoundError:
            logging.error("questions.csv file not found.")
            print("Error: questions.csv file not found.")
        except Exception as e:
            logging.error("Error loading questions: " + str(e))
            print("Error loading questions:", e)
        return questions

    def add_question(self, question_text, options, correct_option):
        try:
            new_num = len(self.questions) + 1
            new_question = Question(new_num, question_text, options, correct_option)
            self.questions.append(new_question)
            logging.info(f"Added question: {new_question.question}")
        except Exception as e:
            logging.error("Error adding question: " + str(e))
            print("Error adding question:", e)

    def search_question(self, num):
        try:
            for question in self.questions:
                if question.num == num:
                    return question
            return None
        except Exception as e:
            logging.error("Error searching for question: " + str(e))
            print("Error searching for question:", e)
            return None

    def delete_question(self, num):
        try:
            for i, question in enumerate(self.questions):
                if question.num == num:
                    del self.questions[i]
                    logging.info(f"Deleted question number: {num}")
                    return True
            return False
        except Exception as e:
            logging.error("Error deleting question: " + str(e))
            print("Error deleting question:", e)
            return False

    def modify_question(self, num, new_question, new_options, new_correct_option):
        try:
            question = self.search_question(num)
            if question:
                question.question = new_question
                question.options = new_options
                question.correct_option = new_correct_option
                logging.info(f"Modified question number: {num}")
                return True
            return False
        except Exception as e:
            logging.error("Error modifying question: " + str(e))
            print("Error modifying question:", e)
            return False

    def display_questions(self):
        try:
            for question in self.questions:
                print(f"{question.num}. {question.question}")
                for key, value in question.options.items():
                    print(f"{key}) {value}")
                print()
        except Exception as e:
            logging.error("Error displaying questions: " + str(e))
            print("Error displaying questions:", e)

    def exit_menu(self):
        logging.info("Exiting the question master menu.")
        exit()

def main():
    qm = QuestionMaster()
    while True:
        print("1. Add a question")
        print("2. Search for a question")
        print("3. Delete a question")
        print("4. Modify a question")
        print("5. Display all questions")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                question_text = input("Enter the question: ")
                options = {
                    'A': input("Enter option 1: "),
                    'B': input("Enter option 2: "),
                    'C': input("Enter option 3: "),
                    'D': input("Enter option 4: "),
                }
                correct_option = input("Enter the correct option (A/B/C/D): ")
                qm.add_question(question_text, options, correct_option)
            except Exception as e:
                logging.error("Error adding question input: " + str(e))
                print("Error processing input for new question:", e)

        elif choice == '2':
            try:
                num = int(input("Enter question number to search: "))
                question = qm.search_question(num)
                if question:
                    print(f"Found: {question.question}")
                else:
                    print("Question not found.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            try:
                num = int(input("Enter question number to delete: "))
                if qm.delete_question(num):
                    print("Question deleted.")
                else:
                    print("Question not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            try:
                num = int(input("Enter question number to modify: "))
                question_text = input("Enter new question: ")
                options = {
                    'A': input("Enter new option 1: "),
                    'B': input("Enter new option 2: "),
                    'C': input("Enter new option 3: "),
                    'D': input("Enter new option 4: "),
                }
                correct_option = input("Enter the correct option (A/B/C/D): ")
                if qm.modify_question(num, question_text, options, correct_option):
                    print("Question modified.")
                else:
                    print("Question not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            qm.display_questions()

        elif choice == '6':
            qm.exit_menu()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
