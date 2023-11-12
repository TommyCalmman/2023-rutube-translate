| Организатор  | Кейсодержатель |
| ------------- | ------------- |
| <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/cplogo.jpg">  | <img width="600" height="300" alt="image" src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/rutube-logo.jpg">  |

# Распознавание именованных сущностей в названиях и описаниях к видео

## Оглавление
1. [Задание](#zadanie)
2. [Описание решения](#solution)
3. [Запуск](#startup)
4. [Стек](#stack)
5. [Команда](#team)
6. [Ссылки](#urls)

## <a name="zadanie"> Задание </a>

Большинство видео на платформе RUTUBE содержат русскую речь. Однако русскоязычный контент также может быть интересен не русскоговорящим пользователям, поэтому внедрение инструмента автоматического дубляжа контента для блогеров поможет им нарастить аудиторию. Также автоматический дубляж может помочь пользователям в изучении иностранного языка.

Участникам предлагается решить задачу автоматического дублирования видео на иностранный язык. Необходимо реализовать одну или несколько моделей машинного обучения, способных перевести речь на видео в речь на иностранном языке.

## <a name="solution">Решение </a>
Наше решение имеет два метода, из которых первый хорош в видео с несколькими голосами, а 2 подходит больше для 1 говорящего:
1) Разбиваем видео на суббтитры, по суббтитрам получаем отдельные видео ряды, аудиоряды и текст, текст переводим, затем используя xtts создаём аудио на переведенном языке с обученным на этой части аудидорожки записью и после чего через wav2lip создаём синхронизированный видеоряд с переведенным текстом.
2) Разбиваем видео на суббтитры, суббтитры переводим, через xtts создаём отдельные аудиодорожки и накладываем их на полный переведенный аудиоряд с той же длиной, что и оригинальное видео. Затем Используя wav2lip совмещаем аудиоряд с видеоизображением.

### Функциональная модель решения 1
<img width="600" height="1200" alt="func_scheme" src="https://github.com/TommyCalmman/2023-rutube-translate/blob/main/method1.png"> 

### Функциональная модель решения 2
<img width="600" height="1200" alt="func_scheme" src="https://github.com/TommyCalmman/2023-rutube-translate/blob/main/method2.png"> 

<br>
<p>Пример обработки </p>

| Суббитры ru  | Суббтитры latn |
| ------------- | ------------- |
| 0.0, 10.76,  И так следующая категория. А давайте-ка пойдем ва-банк. Это как? Я выбираю
10.76, 18.240000000000002,  категорию технические вопросы за 500 за 600 и за 700. Странное решение, но тем не менее. Что делать,
18.240000000000002, 23.04,  если письмо с подтверждением не пришло на почту? Что делать, если у меня уже нет доступа
23.04, 30.68,  по крайне указанному имейлу и почему я не могу войти на сайт? Собака. Собака? Ну, собака, если
30.68, 39.879999999999995,  полностью, help собака root you broo. В любой непонятной ситуации подобной тем, что вы описали, необходимо
39.879999999999995, 46.96,  обращаться в службу поддержки по этому адресу, ибо вам все равно не поможет ничего из того,
47.2, 53.2,  что может оказаться в карманах ваших жилетов. Ну что же, до скорой встречи, Анатолий. Это были все
53.2, 54.72,  технические вопросы на сегодня.  | 0.0, 10.76, Y así la siguiente categoría. A vamos a ir al banco. Eso es como? 10.76, 18.240000000000002, ¿Qué hacer, por ejemplo, si se trata de un problema de seguridad? 18.240000000000002, 23.04, ¿Qué hacer si ya no tengo acceso? 23.04, 30.68, ¿Por qué no puedo entrar en el sitio? 30.68, 39.879999999999995, En cualquier situación incomprensible como la que has descrito, es necesario. 39.879999999999995, 46.96, En cualquier caso, no hay nada que pueda ayudarle. 47.2, 53.2, Bueno, hasta pronto, Anatoli, eso fue todo. 53.2, 54.72, Las preguntas técnicas de hoy.  |


## <a name="startup">Запуск</a>

### Последовательные шаги для запуска кода:
1. Склонируйте гит репозиторий;    
```Bash
git clone https://github.com/TommyCalmman/2023-rutube-translate.git
```

2. перейдите в каталог;    
```Bash
pip install jupyter-notebook
```

3. Запустите ноутбук;    
```Bash
jupyter-notebook
```    

## <a name="stack">Стек </a>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/scikit.jpg" title="scikit" alt="scikit" width="60" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/spacy.jpg" title="spacy" alt="spacy" width="50" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/torch.jpg" title="torch" alt="torch" width="50" height="40"/>&nbsp;
  <img src="https://github.com/ViktoriaMityaeva/2023-10-hackaton-rutube/blob/main/static-all/transformers.jpg" title="transformers" alt="transformers" width="60" height="40"/>&nbsp;

## <a name="team">Команда </a>

*Состав команды "RGB"*    
*Артем Франчук    
*Виктория Митяева    
*София Филина    
*Михаил Нуридинов    

## <a name="urls">Ссылки </a>
 
- [ссылка на весы модели 1]()    
- [ссылка на гугл 2](https://drive.google.com/drive/folders/1DeyO53LnkqDt6IY__3LsW0aSBtJSK3bx?usp=drive_link)    
