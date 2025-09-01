from openai import OpenAI
import pyttsx3      # mp3 파일 저장 없이 바로 재생 가능
import time
import speech_recognition as sr

# 주제를 만들어주는 함수
def make_theme(query, temperature=0.3):
    client = OpenAI()

    system_instruction = '''
    당신은 금요일에 퇴근하고 친구들을 만나 맛있는 저녁을 먹고 술을 적당히 마셔 신난 상태입니다. 
    술자리에서 다같이 재미있게 얘기할 만한 연애 밸런스 게임 주제 세 개를 선정해주세요.

    ### 지시사항 ###
    - 토론이 가능한 주제를 선정할 것
    - 성인이니까 선정적인 주제도 하나 정도는 출력할 것
    - 선택하기 어렵고 애매한 주제를 선택할 것
    - 여사친/남사친 문제를 한 개 이상 포함할 것

    ### 출력 형식 ###
    좋아! 재미있는 주제를 세 가지 생각해봤어.

    주제 1:  선택지 vs 선택지.
    주제 2: 선택지 vs 선택지.
    '''
    user_message = f'''
    {query}
    '''

    response = client.chat.completions.create(

        model='gpt-4o',
        messages=[{
            'role': 'system',
            'content': [{
                'type': 'text',
                'text': system_instruction
            }]

        },
        {
            'role': 'user',
            'content': [{
                'type': 'text',
                'text': user_message

            }]

            
        }],
        response_format={
            'type':'text'
        },
        temperature=temperature,
        max_tokens=2048,
        top_p = 1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


# 챗봇 메세지를 읽어주는 함수

def read_chatbot(chatbot_message):      
    engine = pyttsx3.init()
    engine.setProperty('rate',200)   # 말하기 속도 기본값 200인데 내가 임의로 설정 가능
    engine.say(chatbot_message)
    print('🤖: ',end='')
    for sentences in chatbot_message.split(sep='.'):
        print(sentences)
        time.sleep(.2)
    engine.runAndWait()
    print()
    # tts_data = gTTS(
    #         text=chatbot_message,
    #         lang='ko'
    #     )
    
    # tts_data.save('tts_file1.mp3')
    # # 저장한 음성 파일을 재생
    # music = pyglet.media.load('tts_file.mp3',streaming=False)
    # music.play()


# 음성 인식하고 음성을 텍스트로 변환해 반환하는 함수
def listen_chatbot():                                                                      
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print('👩‍🦰 : ',end='')
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language='ko')
            if command is not None:
                
                print(command)
                print()
                
                break    
            
    return command

# chat_log 를 수정하는 함수
def modify_chatlog(chat_log, new_message):
    if len(chat_log)%2 ==0:
        chat_log.append({ 'role': 'assistant', 'content': [{ 'type': 'text', 'text': new_message }] })
    else:
        chat_log.append({ 'role': 'user', 'content': [{ 'type': 'text', 'text': new_message }]  })
    return chat_log


# 주제 고르고 토론하게 하는 함수
def get_chatbot_response(chat_log, temperature=0.3):
    client = OpenAI()
    response = client.chat.completions.create(

        model='gpt-4o',
        messages= chat_log,
        response_format={
            'type':'text'
        },
        temperature=temperature,
        max_tokens=2048,
        top_p = 1,
        frequency_penalty=1,
        presence_penalty=0
    )

    return response.choices[0].message.content


def discuss(chat_log):
    theme_choice = listen_chatbot()
    chat_log = modify_chatlog(chat_log,theme_choice)
    response = get_chatbot_response(chat_log)
    read_chatbot(response)
    chat_log = modify_chatlog(chat_log,response)
    return chat_log