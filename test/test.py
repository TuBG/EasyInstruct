from easyinstruct import BasePrompt
from easyinstruct.utils.api import set_openai_key, set_anthropic_key, set_proxy

set_openai_key("")
set_anthropic_key("")
set_proxy("http://127.0.0.1:7890")

prompts = BasePrompt()
prompts.build_prompt("Give me three names of cats.")
# print(prompts.get_openai_result(engine = "gpt-3.5-turbo-0301"))
print(prompts.get_anthropic_result(engine="claude-v1.2"))