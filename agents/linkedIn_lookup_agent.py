from langchain import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    template = """
        Given a name {nameis} find the linkedIn url for that person. Given only the url as answer.
    """
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn Profile",
            func=get_profile_url,
            description="Used to find linkedIn url from a name",
        )
    ]
    prompt_template = PromptTemplate(input_variables=["nameis"], template=template)
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    linkedin_profile_url = agent.run(prompt_template.format_prompt(nameis=name))

    return linkedin_profile_url
