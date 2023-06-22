from typing import Tuple

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from third_parties.linkedIn import scrape_linkedin_profile
from agents.linkedIn_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser, PersonIntel


def ice_break(name: str) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    print(linkedin_profile_url)

    linkedIn_data = scrape_linkedin_profile(linkedIn_profile_url=linkedin_profile_url)

    summary_template = """

       given the information {information} about a person I want you to create
       1. A short summary.
       2. Two interesting facts.
       3. A topic that may interest them.
       4. Two creative ice breakers to open a conversation with them.
        \n {format}
       """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={"format": person_intel_parser.get_format_instructions()},
    )
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result = chain.run(information=linkedIn_data)

    return person_intel_parser.parse(result), linkedIn_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Hello LangChain")
    res,siuu = ice_break("Harrison Chase")
    print(siuu)
    print(res)


#
#    info = """
#    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business magnate and investor. He is the founder, CEO and chief engineer of SpaceX; angel investor, CEO and product architect of Tesla, Inc.; owner, CTO and chairman of Twitter; founder of the Boring Company and X Corp.; co-founder of Neuralink and OpenAI; and president of the philanthropic Musk Foundation. Musk is the wealthiest person in the world according to the Bloomberg Billionaires Index and Forbes's Real Time Billionaires list as of June 2023, primarily from his ownership stakes in Tesla and SpaceX, with an estimated net worth of around $225 billion according to Bloomberg and $235 billion according to Forbes.[4][5][6]
#
# """
#
#    summary_prompt_template = PromptTemplate(
#        input_variables=["information"], template=summary_template
#    )
#    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
#    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
#
#    print(chain.run(information=info))
