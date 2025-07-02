# <p align="center"> Проект по автоматизированному тестированию ресурса Swagger Petstore </p>
> <a target="_blank" href="https://petstore.swagger.io/">Swagger Petstore</a>
<p align="center">
<img title="Swagger Petstore Main Page" src="images/screenshots/swagger_petstore_screenshot.png">
</p>

<!-- Технологии -->

## Используемые технологии

<p  align="center">
<a href="https://www.python.com/"><img src="images/logos/python.png" width="50" height="50"  alt="Python"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="images/logos/pycharm.png" width="50" height="50"  alt="PyCharm"/></a>
<a href="https://github.com/"><img src="images/logos/github-mark.png" width="50" height="50"  alt="GitHub"/></a>
<a href="https://docs.pytest.org/"><img src="images/logos/pytest.png" width="50" height="50"  alt="Pytest 5"/></a>
<a href="https://docs.pydantic.dev/"><img src="images/logos/pydantic.png" width="50" height="50"  alt="Selenium"/></a>
<a href="https://github.com/psf/requests"><img src="images/logos/requests.png" width="50" height="50"  alt="Selenium"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="images/logos/allure_report.png" width="50" height="50"  alt="Allure"/></a>
<a href="https://qameta.io/"><img src="images/logos/allure_testops.png" width="50" height="50"  alt="Allure TestOps"/></a>  
<a href="https://www.jenkins.io/"><img src="images/logos/jenkins.png" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://www.atlassian.com/ru/software/jira/"><img src="images/logos/jira.png" width="50" height="50"  alt="Jira"/></a> 
<a href="https://web.telegram.org/k/"><img src="images/logos/tg.png" width="50" height="50"  alt="Jira"/></a>  
</p>



<!-- Тестовые сценарии -->
## Реализованные тестовые сценарии:

 #### Создание сущности
 >* ✅ Создание питомца со статусом "availabe"
 >* ✅ Создание питомца со статусом "pending"
 >* ✅ Создание питомца со статусом "sold"
 
 #### Изменение сущности 
>* ✅ Изменение информации о питомце
 
 #### Получение сущности
>* ✅ Поиск питомцев по статусу "sold"
>* ✅ Поиск питомцев по статусу "availabe"
>* ✅ Поиск питомцев по статусу "pending"
>* ✅ Поиск питомца по id
 
 #### Удаление сущности
>* ✅ Удаление питомца

<!-- Jenkins -->

## <img width="3%" title="Jenkins" src="images/logos/jenkins.png"> Запуск проекта в Jenkins

##### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_api_project_ash/">Проект в Jenkins</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке ENVIRONMENT
4. Нажать кнопку `Build`
5. Результат прохождения тестов можно увидеть в Allure отчете или в Allure Testops

<img alt="This is an image" src="images/screenshots/jenkins_screenshot.png" width="900"/>

<!-- Allure report -->

## <img width="3%" title="Allure Report" src="images/logos/allure_report.png"> Allure report

>#### Результаты выполнения тестов можно посмотреть в Allure-отчете.
![This is an image](images/screenshots/allure_report_screenshot.png)

>#### Сформированный сьют с тест-кейсами из тестового прогона отображается в вкладке "Suites".
![This is an image](images/screenshots/allure_report_testcases.png)


<!-- Allure TestOps -->

## <img width="3%" title="Allure TestOps" src="images/logos/allure_testops.png"> Интеграция с Allure TestOps

>#### Ссылка на <a target="_blank" href="https://allure.autotests.cloud/project/4810/dashboards">Dashboard</a>

![This is an image](images/screenshots/allure_testops_dashboard.png)

>#### Тест-кейсы, сформированные в рамках прохождения тестового прогона

![This is an image](images/screenshots/allure_testops_test_cases.png)


<!-- Jira -->

## <img width="3%" title="Jira" src="images/logos/jira.png"> Интеграция с Jira

>#### Реализована интеграция Allure TestOps с Jira. В задачу из Jira можно добавить список тест-кейсов и результат тестового прогона по ним.

![This is an image](images/screenshots/jira_screenshot.png)


<!-- Telegram -->

## <img width="3%" title="Telegram" src="images/logos/tg.png"> Оповещения в Telegram
>#### После завершения джобы в Telegram bot приходит уведомление с графиком и информацией о тестовом прогоне.

<img alt="This is an image" src="images/screenshots/telegram_bot_screenshot.png" width="900"/>