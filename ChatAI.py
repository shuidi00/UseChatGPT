"""
此程序用于调用ChatGPT接口
"""
import openai
import logging

# 创建一个日志记录器
logger = logging.getLogger('my_logger')
# 设置日志级别
logger.setLevel(logging.INFO)
# 创建一个FileHandler，将日志写入文件中
file_handler = logging.FileHandler('ai.log', encoding='utf-8')
# 创建一个Formatter，用于指定日志输出格式
formatter = logging.Formatter('%(message)s')
# 将Formatter添加到FileHandler中
file_handler.setFormatter(formatter)
# 将FileHandler添加到日志记录器
logger.addHandler(file_handler)


openai.api_key = "sk-UCozFNIh9x79kkU0IuMVT3BlbkFJiaXa2E6rmbSpszrvgHF"
last_question = ''
last_answer = ''


def request_ai(this_q, last_q, last_a):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个人。"},
            {"role": "user", "content": last_q},
            {"role": "assistant", "content": last_a},
            {"role": "user", "content": this_q}
        ],
        timeout=60
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return result


def ask():
    while True:
        try:
            global last_question
            global last_answer
            question = input('问：')
            logger.info('问：')
            logger.info(question)
            answer = request_ai(question, last_question, last_answer)
            print('答：', end='')
            print(answer)
            logger.info('答：')
            logger.info(answer)
            last_question, last_answer = question, answer
            if '谢谢' in question or '谢谢' in answer or '感谢' in answer:
                print('如果有帮到您，可访问以下地址给予支持，谢谢。')
                print('https://www.kdocs.cn/l/cpLMSSf0lXD5')
                logger.info('如果有帮到您，可访问以下地址给予支持，谢谢。')
                logger.info('https://www.kdocs.cn/l/cpLMSSf0lXD5')
        except Exception as e:
            logger.debug(e)
            print('答：', end='')
            print('网络不稳定，请再试一次')
            logger.info('答：')
            logger.info('网络不稳定，请再试一次')
        finally:
            print('-' * 60)
            logger.info('-' * 60)


if __name__ == '__main__':
    ask()
