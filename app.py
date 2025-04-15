from openai import OpenAI
import telebot


TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🤖 سلام انسان هوشمند!\n\n"
        "به دنیای هوش مصنوعی خوش اومدی...\n"
        "اینجا با یک *چت‌بات قدرتمند بر پایه ChatGPT* در ارتباطی — جایی که مکالمات ساده به تجربه‌ای هوشمند و دقیق تبدیل می‌شن!\n\n"
        "این سیستم توسط *محمد تقی‌زاده* طراحی و توسعه داده شده؛ با بهره‌گیری از تکنولوژی‌های نوین *هوش مصنوعی* و زبان برنامه‌نویسی *پایتون*.\n"
        "مغز این بات، از دل الگوریتم‌های پردازش زبان طبیعی بیرون اومده تا بتونه به شکلی هوشمند، سریع و دقیق پاسخ‌گوی سوالاتت باشه.\n\n"
        "🎯 فقط کافیه سوالت رو تایپ کنی…\n"
        "و بقیه‌ش رو بسپار به من!"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')


client = OpenAI(api_key='YOUR_API_KEY')
def chatgpt(question):
    qa_messages = [
        {
            'role': 'system',
            'content': 'Answer this question'
        },
        {
            'role': 'user',
            'content': question,
        }
    ]

    qa_response_completion = client.chat.completions.create(
        model='gpt-4o-mini', # just for openai
        messages=qa_messages,
        max_tokens=150  # محدودیت تعداد کلمات خلاصه
    )

    qa_response_text = qa_response_completion.choices[0].message.content.strip()
    return qa_response_text


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_text = message.text
    response = chatgpt(user_text)
    bot.send_message(message.chat.id, response, parse_mode='Markdown')
    

bot.polling()