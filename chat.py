import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['Hola|Hola!|Hola ¿qué tal?', ['Hola, ¿cómo estás?', '¡Hola!']],
    ['¿Cómo estás?|¿Cómo te sientes?', ['Estoy bien, gracias. ¿Y tú?', 'Me siento muy bien, gracias']],
    ['¿Cuál es tu nombre?|¿Cómo te llamas?|Hola', ['Me llamo Chatbot, ¿y tú?', 'Mi nombre es Chatbot']],
    ['Adiós|Hasta luego|Chao|Hasta pronto', ['Adiós, ¡que tengas un buen día!', 'Hasta luego']],

]
chatbot = Chat(pairs, reflections)
chatbot.converse()
