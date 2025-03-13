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
#### 2. Перевести его на русский язык 
#### 3. Дообучить модель bart-large-cnn, чтобы она работала с русским языком

### III. Бейзлайн   
