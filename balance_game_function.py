from openai import OpenAI
import pyttsx3      # mp3 파일 저장 없이 바로 재생 가능하게 해줌
import time
import speech_recognition as sr


# 주제 만드는 clinet에 필요한 system_instruction 반환
def get_theme_instruction():
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
    return system_instruction


# 토론하는 client의 system_instruction 가져오는 함수
def get_discussion_instruction(theme_output):
    system_instruction = f'''
    당신은 금요일에 퇴근하고 친구들을 만나 맛있는 저녁을 먹고 술을 적당히 마셔 신난 상태입니다.
    상대가 재미있는 밸런스 게임을 해보자면서 3가지 주제를 제안했고 이 중 한 가지를 골랐습니다.

    {theme_output.split(sep=".")[1:]}

    상대가 선정한 주제에 대해 토론해봅시다.
    상대가 생각을 바꿀 수 있도록 영악하고 악독하게 비꼬면서 토론을 해주세요.

    
    ### 토론시 지시사항 ###
    - 3문장 이내로 반말로 대답할 것
    - 이해하는 척 하면서 교묘하게 상대가 선택한 선택지에서 악화될 상황을 상상해 말할 것
    - 상대와 반대 의견을 주장할 것
    - 만약 상대가 '그만하자'라는 말을 하면 "ㅋㅋㅋ 알았어 재밌었다 그치?" 를 그대로 출력할 것
    - 예시를 적극 활용할 것

    
    ### 주제 묻기 출력 예시 ###
    이 중 어떤 주제에 대해 이야기 해볼까?

    '''
    return system_instruction


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


# 초기 chat_log 설정하고 반환하는 함수
def get_fisrt_chatlog(system_instruction):
    chat_log = [{ 'role': 'system', 'content': [{ 'type': 'text', 'text': system_instruction }] }
            ]
    
    return chat_log


# chat_log 를 수정하는 함수
def modify_chatlog(chat_log, new_message):
    if len(chat_log)%2 ==0:
        chat_log.append({ 'role': 'assistant', 'content': [{ 'type': 'text', 'text': new_message }] })
    else:
        chat_log.append({ 'role': 'user', 'content': [{ 'type': 'text', 'text': new_message }]  })
    return chat_log


# 주제를 만들어주는 함수
def make_theme(chat_log, temperature=0.3):
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
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


# 고른 주제로 토론하게 하는 함수
def discuss(chat_log, temperature=0.3):
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


