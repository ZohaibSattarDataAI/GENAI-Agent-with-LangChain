from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# LLM
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
Translate the following text into {language}.

Only return the translated text.

Text:
{text}
""")

parser = StrOutputParser()


def translator(language):
    return prompt.partial(language=language) | model | parser


parallel_translator = RunnableParallel(
    Urdu=translator("Urdu"),
    Hindi=translator("Hindi"),
    Arabic=translator("Arabic"),
    French=translator("French"),
    German=translator("German"),
    Spanish=translator("Spanish"),
    Chinese=translator("Chinese"),
    Japanese=translator("Japanese")
)

result = parallel_translator.invoke({
    "text": "Artificial Intelligence is changing the future of technology."
})

for language, translation in result.items():
    print("=" * 60)
    print(language)
    print("=" * 60)
    print(translation)