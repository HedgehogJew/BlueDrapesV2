from first import news
from second import articles
import numpy

print("Выберите необходимый тип генерации 1)новости   2)сочинение")
generation_type = int(input())

if (generation_type == 1):
    print("Первый тип новости")
    #news.py
    model.eval1()

    print(evaluate(
        model,
        char_to_idx,
        idx_to_char,
        temp=0.3,
        prediction_len=1000,
        start_text='Жизнь '
    )
    )
  #do // отпралвяем на обученную модель 1
elif (generation_type == 2):
    print("Второй тип сочинение")
    model.eval2()

    print(evaluate(
        model,
        char_to_idx,
        idx_to_char,
        temp=0.3,
        prediction_len=1000,
        start_text='Смерть '
    )
    )
    #do ///отпралвяем на обученную модель 2
    #articles.py
    # do ///отпралвяем на обученную модель 2
'''
elif (generation_type == 3):
    print("Третий тип статья")
  #do ///отпралвяем на обученную модель 3
'''
