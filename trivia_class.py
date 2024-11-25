import requests
from random import shuffle


class Questions:
    # def __init__(self):
    #     self.my_api = "https://opentdb.com/api.php"

    # def define_category(self, chosen_category):
    #     if chosen_category == "Animals":
    #         number = 27
    #     elif chosen_category == "Films":
    #         number = 11
    #     elif chosen_category == "Music":
    #         number = 12
    #     else:
    #         number = 23
    #     return number

    QUESTION_1 = {
        'type': 'multiple', 
        'difficulty': 'easy', 
        'category': 'Harry', 
        'question': 'Ile razy Harry złapał znicz?', 
        'correct_answer': '7', 
        'incorrect_answers': ['2', '4', '0']
    }

    QUESTION_2 = {
        'type': 'multiple', 
        'difficulty': 'easy', 
        'category': 'Harry', 
        'question': 'W które urodziny otrzymuje się pierwszy list z Hogwartu?', 
        'correct_answer': '11', 
        'incorrect_answers': ['5', '8', '18']
    }

    QUESTION_3 = {
        'type': 'multiple', 
        'difficulty': 'easy', 
        'category': 'Harry', 
        'question': 'W której części Ron i Hermiona się pocałowali?', 
        'correct_answer': 'Insygnia śmierci cz.2', 
        'incorrect_answers': ['Komnata Tajemnic', 'Zakon Feniksa', 'Książe Półkrwi']
    }

    def get_questions(self):
        # my_params = {
        #     "amount": amount,
        #     "category": self.define_category(chosen_category=category),
        #     "difficulty": "easy",
        #     "type": quiz_type.lower()
        # }
        # respond = requests.get(url=self.my_api, params=my_params)
        # data = respond.json()["results"]
        data = [self.QUESTION_1, self.QUESTION_2, self.QUESTION_3]
        final_result = []
        """
        # data
        [
            {
            'type': 'multiple', 
            'difficulty': 'easy', 
            'category': 'Animals', 
            'question': 'Hippocampus is the Latin name for which marine creature?', 
            'correct_answer': 'Seahorse', 
            'incorrect_answers': ['Dolphin', 'Whale', 'Octopus']
            }, 
            {'type': 'multiple', 'difficulty': 'easy', 'category': 'Animals', 'question': 'What is the fastest  land animal?', 'correct_answer': 'Cheetah', 'incorrect_answers': ['Lion', 'Thomson&rsquo;s Gazelle', 'Pronghorn Antelope']}, {'type': 'multiple', 'difficulty': 'easy', 'category': 'Animals', 'question': 'By definition, where does an abyssopelagic animal live?', 'correct_answer': 'At the bottom of the ocean', 'incorrect_answers': ['In the desert', 'On top of a mountain', 'Inside a tree']}
        ]
        """
        for item in data:
            answers = item["incorrect_answers"]
            answers.append(item["correct_answer"])
            shuffle(answers)
            variable = {
                "category": item["category"],
                "question": item["question"],
                "correct": item["correct_answer"],
                "wrong": answers
            }
            final_result.append(variable)
        """
        # final_result
        [
            {
            'category': 'Animals', 
            'question': 'By definition, where does an abyssopelagic animal live?', 
            'correct': 'At the bottom of the ocean', 
            'wrong': ['On top of a mountain', 'At the bottom of the ocean', 'Inside a tree', 'In the desert']
            }, 
            
            {'category': 'Animals', 'question': 'What do you call a baby bat?', 'correct': 'Pup', 'wrong': ['Cub', 'Kid', 'Pup', 'Chick']}, {'category': 'Animals', 'question': 'What colour is the female blackbird?', 'correct': 'Brown', 'wrong': ['Brown', 'White', 'Black', 'Yellow']}
        ]
        """
        return final_result
