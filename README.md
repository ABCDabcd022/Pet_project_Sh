# Pet_project_Sh
Пет-проект по курсу Инструменты анализа данных.           
Цель: получить модель, которая сможет кратко, в нескольких абзацах, пересказать книгу. 
## План реализации:
### I. Source
#### 1. Собрать и подготовить датаеты для тренировки моделей
https://github.com/salesforce/booksum             
https://github.com/abisee/cnn-dailymail/tree/master?tab=readme-ov-file       
https://github.com/becxer/cnn-dailymail/      
#### 2. Посмотреть готовые модели для этой задачи
##### 1). bart-large-cnn       
https://huggingface.co/facebook/bart-large-cnn          
Не поддерживает русский язык.    
Модель facebook/bart-large-cnn — это версия BART, которая была дообучена для задачи новостной суммаризации на датасете CNN/DailyMail. Вот основные этапы её обучения:

Предобучение (Pre-training):

BART изначально обучалась на большом корпусе текстов, включая книги, статьи и другие данные. Это обучение было "самообучением" (self-supervised), где модель училась восстанавливать искаженные тексты.

Дообучение (Fine-tuning):

После предобучения модель была дообучена на датасете CNN/DailyMail, который содержит новостные статьи и их summaries (краткие описания). Это supervised learning, где модель училась генерировать summaries на основе полного текста.

### II. Мои действия
#### 1. Скачать датасет cnn-dailymail    
Скачайте файлы cnn_stories.tgz и dailymail_stories.tgz здесь:      
https://cs.nyu.edu/~kcho/DMQA/          
Распакуйте их.        
Скачайте Stanford CoreNLP с официального сайта:       
https://stanfordnlp.github.io/CoreNLP/            
Распакуйте архив.       
Добавьте путь к CoreNLP в переменную окружения CLASSPATH.    
В cmd:      
CLASSPATH=C:\00Projects\Pet_project_A_Sh\stanford-corenlp-4.5.8\stanford-corenlp-4.5.8.jar             
Проверим: echo %CLASSPATH%        
Вывод: C:\00Projects\Pet_project_A_Sh\stanford-corenlp-4.5.8\stanford-corenlp-4.5.8.jar
Проверьте, что CoreNLP работает:
echo "Please tokenize this text." | java edu.stanford.nlp.process.PTBTokenizer         
Вывод:        
  "        
  Please      
  tokenize        
  this       
  text        
  .      
  "       
  PTBTokenizer tokenized 7 tokens at 115,97 tokens per second.

Токенизация датасета      
Скачиваем репозиторий с датасетом:       
git clone https://github.com/becxer/cnn-dailymail/        
Перейдите в директорию, куда вы скачали репозиторий с датасетом       
python make_datafiles.py C:\00Projects\Pet_project_A_Sh\cnn\stories C:\00Projects\Pet_project_A_Sh\dailymail\stories       
Перед эти в файле make_datafiles.py настроить путь:       
```python
command = [
    'java',
    '-cp', 'C:/00Projects/Pet_project_A_Sh/stanford-corenlp-4.5.8/*',  # Укажи путь к JAR-файлам
    'edu.stanford.nlp.process.PTBTokenizer',
    '-ioFileList',
    '-preserveLines',
    'mapping.txt'
]
```

#### 2. Перевести его на русский язык 
#### 3. Дообучить модель bart-large-cnn, чтобы она работала с русским языком

### III. Бейзлайн   
