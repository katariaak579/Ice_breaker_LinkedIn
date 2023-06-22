from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(description="Return the summary of the person")
    facts: List[str] = Field(
        description="Returns the list of interesting facts about the person"
    )
    topic_of_interest: List[str] = Field(
        description="Returns the list of topics of interest"
    )
    ice_breakers: List[str] = Field(
        description="Returns the list of ice breakers of the person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topic_of_interest": self.topic_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser = PydanticOutputParser(pydantic_object=PersonIntel)
