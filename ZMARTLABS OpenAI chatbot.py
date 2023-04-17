copyrightNotice = '''

___  _  _ ____ ____ ___ _    ____ ___  ____    ____ ___  ____ _  _ ____ _    ____ _  _ ____ ___ ___  ____ ___
  /  |\/| |__| |__/  |  |    |__| |__] [__     |  | |__] |___ |\ | |__| |    |    |__| |__|  |  |__] |  |  |
 /__ |  | |  | |  \  |  |___ |  | |__] ___]    |__| |    |___ | \| |  | |    |___ |  | |  |  |  |__] |__|  |


'''
print(copyrightNotice)


import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI and Research Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="ZMARTLABS OpenAI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)