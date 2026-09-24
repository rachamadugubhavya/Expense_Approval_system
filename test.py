# test.py

from prompt import prompt
from parser import parser
from model import get_model
from config import TEST_CASES
from langfuse.langchain import CallbackHandler

langchain_handler = CallbackHandler()
python 

def run_single_test(expense_description):

    try:
        model = get_model()

        chain = prompt | model | parser

        result = chain.invoke({
            "expense_description": expense_description
        },
        config={
            'callbacks': [langchain_handler],
            'tags': ["expense-categorizer"],
            'metadata': {
                'project': "Expense Categorizer"
            }
        })

        return result

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def run_all_tests():

    print("=" * 80)
    print("EXPENSE CATEGORIZER TESTS")
    print("=" * 80)

    for test_name, test_data in TEST_CASES.items():

        print(f"\nTest Case: {test_name}")
        print("-" * 80)

        result = run_single_test(
            test_data["expense_description"]
        )

        if result:
            print("Output:")
            print(result.model_dump())
        else:
            print("Test Failed")


if __name__ == "__main__":
    run_all_tests()