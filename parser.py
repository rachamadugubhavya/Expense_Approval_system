# parser.py

from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class ExpenseCategorizer(BaseModel):

    expense_category: str = Field(
        description="Category like Food, Transport, Utilities, Shopping, Entertainment, etc."
    )

    expense_type: str = Field(
        description="Essential or Non-Essential"
    )

    confidence_note: str = Field(
        description="Short explanation for the classification"
    )


parser = PydanticOutputParser(
    pydantic_object=ExpenseCategorizer
)