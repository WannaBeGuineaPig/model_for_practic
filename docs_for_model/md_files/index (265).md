---
search:
  boost: 2 
---
# Функции планировщика задач

<table border="1">
  <tr>
    <th width="200px">Название действия (задача)</th>
    <th width="width:auto;">Техническое название</th>
    <th width="width:auto;">Что она делает</th>
    <th width="200px">Где используется</th>
    <th width="180px">Рекомендуемая частота выполнения задачи</th>
  </tr>
  <tr>
    <td>Автоматическое обновление статуса обучение</td>
    <td>ecosoft-lexema8-scheduler-staff-training-functions.AutomaticUpdateStudyingCourseStatus</td>
    <td>Автоматически переводит просроченные <a href="../Программы обучения/">программы обучения</a> по дате обучения в статус "Не пройдено"</td>
    <td>В процедуре обучения</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Автоматическое создание заявок на обучение</td>
    <td>ecosoft-lexema8-scheduler-staff-training-functions.CreateUnitedStaffTrainingRequest</td>
</td>
    <td>Осуществляет автоматическое создание <a href="../Заявки на обучение/">заявки на обучение</a> из <a href="../План обучения/">плана обучения</a>.</td>
    <td>В процессе планирования обучения</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Автоматическое формирование протоколов обучения</td>
    <td>ecosoft-lexema8-scheduler-staff-training-functions.AutomaticCreateStaffTrainingJournalFromStatistic</td>
    <td>Автоматически формирует протоколы обучения согласно статистике обучения по сотрудникам</td>
    <td>В процедуре обучения</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Блокировка учетных записей пользователей, где дата увольнения меньше текущей</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.UserBloking</td>
    <td>Проставляет признак блокировки у пользователей, если у связанного сотрудника проставлена дата увольнения меньше текущей даты</td>
    <td>В процедуре блокировки пользователей</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Выгрузка документов из Лексемы в 1С</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.unLoadDocuments</td>
    <td>Осуществляет автоматическую выгрузку документов из Лексемы в 1С перечисленные на вкладке <a href="../Настройка для интеграции с 1С/Настройка интеграции справочников и документов/Вкладка Исходящие документы/">Исходящие документы</td>
    <td>В процедуре автоматической выгрузки данных в 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Выпуск новых сертификатов, когда истекают сроки</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.createCloudCertificateExpiring</td>
    <td>Осуществляет автоматическую заявку на выпуск <a href="../Выпуск ОНЭП/#Заявки-на-выпуск-ЭП"> сертификата</a> пользователям у которых закончился срок действия сертификата электронной подписи. В настройках учетной политики должна быть включена константа <b>"ЭЦП_количество_дней_за_сколько_отправтить_заявку_на_перевыпуск"</b>, где указывается значение количества дней по которому нужно проверять сертификаты. Если текущая дата меньше даты окончания действующего ЭП либо равна константе - то создается заявка на перевыпуск. Сертификаты создаются по всем филиалам организаций, на которых истекает срок действия. Также с помощью <a href="../Настройка констант/#система_электронного_и_кадрового_документооборота">константы</a> "количество_перевыпускаемых_сертификатов_ЭП_за_раз" возможно задать количество сертификатов которые будут выпущены за раз.</td>
    <td>В процедуре выпуска сертификатов пользователям</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Выпуск сертификатов новым сотрудникам</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.NewUsersCloudCertificateCreate</td>
    <td>Осуществляет автоматический выпуск сертификатов электронной подписи новым принятым сотрудникам. Функция работает по следующему принципу: в случае если используется положение о КЭДО, то кандидаты подбираются если текущая дата больше либо равна дата перехода на КЭДО и есть логин в системе. В случае если положение о КЭДО не используется то по наличию логина в системе у сотрудника.</td>
    <td>В процедуре выпуска сертификатов пользователям</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Добавление в список рассылки ЛНА с признаком "Ознакомлен ранее"</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.InsertReadListLNDReadEarlier</td>
    <td>В список рассылки автоматически добавляются сотрудники, которые подписали ознакомление с ЛНА на бумажном носителе при приеме на работу</td>
    <td>В процедуре создания ЛНА</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Договора в статусе черновик (не отправленные по маршруту)</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.sendingContractNotificationsExpired</td>
    <td>Удаляет договора, которым не назначен маршрут. На следующий день после создания договора. Все договора, которые остались без маршрута будут удалены</td>
    <td>В процедуре удаления договоров, которым не назначен маршрут</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Загрузка в Лексему документов на подписание из файлов (расчетные листы)</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.loadDocumentForSigningFromFile</td>
    <td>Осуществляет автоматическую загрузку файлов в Лексему из сетевого хранилища</td>
    <td>В процедуре автоматической загрузки данных из 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Загрузка в Лексему из 1С документов</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.loadDocumentForm</td>
    <td>Осуществляет автоматическую загрузку физических документов из 1С в Лексему перечисленные на вкладке <a href="../Настройка для интеграции с 1С/Настройка интеграции справочников и документов/Вкладка Входящие документы/">"Входящие документы"</a> с типом "Документ в Лексеме"</td>
    <td>В процедуре автоматической загрузки данных из 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Загрузка в Лексему из 1С произвольных выборок</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.loadFreeQuery</td>
    <td>Осуществляет автоматическую загрузку сущностей, не относящих к справочникам и документам, в произвольном виде в физическую таблицу СЭД. Например, управленческую структуру.</td>
    <td>В процедуре автоматической выгрузки произвольных выборок из 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Загрузка из 1С в Лексему документов на подписание</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.loadDocumentForSigningFromFile</td>
    <td>Осуществляет автоматическую загрузку документов на подписание из 1С в Лексему <a href="../Настройка для интеграции с 1С/Настройка интеграции справочников и документов/Вкладка Входящие документы/">"Входящие документы"</a> с типом "Документ в Лексеме". Также создает документы на подписание в документообороте</td>
    <td>В процедуре автоматической загрузки данных из 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Загрузка из 1С физ.лиц</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.loadDocumentForm</td>
    <td>Осуществляет автоматическую загрузку физических лиц из 1С</td>
    <td>В процедуре автоматической загрузки физических лиц из 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Загрузка пользователей из Active Directory в форму для сопоставления</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.loadADUsers</td>
    <td>Автоматически добавляет и сопоставляет доменные учетные записи из Active Directory со справочником физических лиц</td>
    <td>В процедуре создания нового пользователя. Если в системе Active Directory были изменения в данных пользователей, таких как ФИО или адрес электронной почты, то обновленная информация используется для обновления соответствующих таблиц.</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Загрузка справочников (должности,подразделения,физ.лица и сотрудники)</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.loadDictionary</td>
    <td>Осуществляет автоматическую загрузку справочников из 1С. Будут загружаться только те справочники, у которых в настройке стоит галка в поле "Загружать в пакете справочников" (должности,подразделения, ... физические лица при небольшом объеме можно загружать здесь же)</td>
    <td>В процедуре автоматической загрузки данных из 1С</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Напоминание о входе в систему неактивированным пользователям</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.SendAuthEmail</td>
    <td>Создает в системе информационное письмо, с помощью которого рассылается напоминание пользователям о входе в систему, которые не сделали этого ранее (в настройках учетной политики должна быть настроена константа "УпрП_напоминание_о_созданной_УЗ" со значением 1). Также задача направляет уведомление пользователям, которые дали согласие на кадровый электронный документооборот, но также не зарегистрировались в системе (в настройках учетной политики должна быть настроена константа "ПереходНаКЭДО_НапоминаниеОбОригинале" со значением 1).</td>
    <td>В процедуре активации учетной записи пользователями</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Напоминание о необходимости сдачи заявления на сертификат в отдел кадров</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.SendSertificationEmail</td>
    <td>Осуществляет автоматическую отправку письма пользователю, у которого был выпущен сертификат НЭП, но не были сданы оригиналы документов "Заявление на выдачу сертификата" и "Расписка в получении сертификата ключа проверки электронной подписи".</td>
    <td>В процедуре автоматической отправки писем</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Отзыв сертификатов при изменении должности</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.revokeCertificate</td>
    <td>Создает документ "Отзыв сертификата" при смене должности сотрудника. Проверяет должность в сертификате и текущую должность сотрудника на предприятии.</td>
    <td>В процессе смены должности сотрудником</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Проверка документов Лексемы на удаление в 1С</td>
    <td>ecosoft-lexema8-scheduler-odata-functions.unLoadDictionaryMaterials</td>
    <td>У заявлений проставляется признак "Удалено" у тех документов, которые были удалены в 1С. Также этот признак отображается в реестре обмена с 1С.</td>
    <td>В процедуре автоматической загрузки данных из 1С</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Просроченные документы</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.sendingNotificationsExpired</td>
    <td>Рассылает пользователям информацию о просроченных документах (нарушения сроков обработки).</td>
    <td>В процедуре рассылки просроченных документов</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Рассылка документов на этапе инициирования</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.sendingNotificationsFirstStage</td>
    <td>Осуществляет автоматическую отправку письма инициатору, в случае если он создал документ, но не запустил документ по маршруту.</td>
    <td>В процедуре автоматической отправки писем</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Рассылка просроченных документов руководителям</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.sendingNotificationsExpiredChief</td>
    <td>Создает автоматическую рассылку руководителю подразделения со списком подчиненных, у которых есть задолженности, с указанием количества просроченных документов и типов документов.</td>
    <td>В процедуре автоматической рассылки просроченных документов руководителям</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Рассылка сводки по просроченным документам их инициаторам</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.SendingNotificationsExpiredSummaryToInitiator</td>
    <td>Оповещения направляются инициатору с информацией по документам, действия по которым просрочил любой из маршрута.</td>
    <td>В процедуре автоматической отправки писем</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Рассылка уведомлений об ознакомлении ЛНА</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.longQuery</td>
    <td>В список рассылки автоматически добавляются вновь принятые сотрудники, которые работают в подразделения, на которые распространяется действие ЛНА. Также из списка рассылки автоматически удаляются уволенные сотрудники, которые не успели ознакомиться с данным ЛНА.</td>
    <td>В процедуре автоматической отправки писем</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Снятие с ознакомления ЛНА с истёкшим сроком действия</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.ClearReadListOfExpiredLND</td>
    <td>Отменяет факт отправки ЛНА на ознакомление пользователям, которые не ознакомились с ЛНА до истечения его срока действия. В списках рассылки таких ЛНА останутся только пользователи, которые ознакомились с ним до выполнения задачи.</td>
    <td>В процедуре рассылки ЛНА</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Создание новых пользователей</td>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.createNewUsers</td>
    <td>Создает новых пользователей, осуществляет их привязку к организации, формирует документы "настройка пользователей" на основании данных справочников "Физическое лицо" и "Сотрудник", а также данных, загруженных из Active Directory, при необходимости. Примечание: У физического лица должно быть заполнено поле "Адрес эл/почты".</td>
    <td>В процедуре создания новых пользователей</td>
    <td>Один раз в час</td>
  </tr>
  <tr>
    <td>Уведомления Lexema</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.SendingNotificationLexema</td>
    <td>Создает уведомления в системе, с помощью которых можно посылать по СЭД сообщения пользователям. Все уведомления будут находиться в окне "На обработку" как напоминание.</td>
    <td>В процедуре уведомления в системе</td>
    <td>Ежеминутно</td>
  </tr>
  <tr>
    <td>Уведомления о приближающейся просрочке документов</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.SendingNotificationsProcessing</td>
    <td>Создает в системе информационное письмо, с помощью которого пользователям направляется уведомление о необходимости обработки документов СЭД согласно срокам. Необходима настройка константы "Предупреждать об окончании норматива согласования за (дней)".</td>
    <td>В процедуре уведомления в системе</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Уведомления о приближающейся просрочке документов через СМС</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.SendingNotificationsSMS</td>
    <td>Пользователям направляется уведомление о необходимости обработки документов СЭД согласно срокам, а также о просроченных документов через SMS.</td>
    <td>В процедуре уведомления в системе</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Уведомления об окончании срока доверенностей</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.SendingEmpowermentNotificationExpired</td>
    <td>Автоматически рассылает уведомления об окончании срока действия доверенности.</td>
    <td>В процедуре рассылки</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Установка даты перехода на КЭДО принятым сотрудникам</th>
    <td>ecosoft-lexema8-scheduler-admin-console-functions.UpdateWorkerDateEDM</td>
    <td>Осуществляет автоматическое проставление вновь принятым сотрудникам даты перехода на кадровый электронный документооборот. Система проверяет на текущий день всех новых сотрудников, у которых присутствует логин, но отсутствует дата перехода на КЭДО. В настройках учетной политики должна быть настроена константа "Дата_принятия_положения_КЭДО" с заполненной датой в формате дд.мм.гггг (например 09.09.2022). По указанной дате система определяет сотрудников, у которых дата приема позже, чем дата из константы, и по таким сотрудникам устанавливает дату перехода на КЭДО, равную дате приема.</td>
    <td>В процедуре автоматического проставления даты перехода на КЭДО</td>
    <td>Один раз в день</td>
  </tr>
  <tr>
    <td>Формирование недостающих отчетов со штампом электронной подписи</td>
    <td>ecosoft-lexema8-scheduler-formation-mailing-list.loadWaterMarkReport</td>
    <td>Формирует автоматическое вложение отчета со штампом электронной подписи во вложении к заявлению, в случае если это не было сделано ранее по завершению маршрута заявления.</td>
    <td>В процедуре укомплектования документов</td>
    <td>Один раз в час</td>
  </tr>
</table>

**Способы и примеры настройки расписания задаются в формате crontab**  
Ознакомиться подробнее можно в разделе [Создание расписания в формате Crontab](../FAQ/#использование_crontab_для_сервиса_sheduler)

## Настройка заданий для планировщика

Также для планировщика возможно настроить иные задания с помощью справочника ["настройки заданий"](../Настройка%20внутрисистемных%20уведомлений/#настройка_заданий_для_планировщика), где во вкладке "Задача" указывается часть содержащая динамический запрос для выполнения задачи. Текст для таких задач возможно назначить с помощью ["Конструктора уведомлений"](../Конструктор%20уведомлений/#вид_уведомления_настройка_заданий_для_планировщика) Данные задачи отрабатывают при запуске задачи **"Уведомления Lexema"**. Далее представлены примеры запросов.

<!-- ### Документы, не пришедшие из 1с

??? Задача

    ```sql
    with "no1c"
    as
    (select r."COrgName" , 'таб.№ ' || r."NumTab"|| ' ' || r."Workers" as "Workers" ,r."PostWorkers" , 
    r."name1c"  || ' По заявлению № ' || r."DocumentNumber" || ' от ' || to_char( "DocumentDate"::date, 'DD.MM.YYYY')  as  "name1c" 
    , l."link_txt" || '#/view/'|| r."TypeName" ||'Form' ||'/' ||  r."VCode"  as "link"  
    from	odata."getExchange1CGuidsRegistry"(null, null, (now()::date+ '-45 day'::interval)::date , (now()::date+ '-3 day'::interval)::Date , null) r
        cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") l
      where 
    coalesce( "DeletionMark",'false') = 'false ' and 
    r."VCode" is not null and 
              r."DFS_VCode" is null and
            r."guid" is not null and
              r.name1c not ilike '%больнич%' 
            and
              r.name1c not ilike '%НДФЛ%' 
            and
              r.name1c not ilike '%вычет%' 
        and
              r.name1c not ilike '%мат%пом%'
        and
            r. "DocumentDate" >= now()::date+ '-45 day'::interval 
          and
            r. "DocumentDate" <= now()::date+ '-3 day'::interval 
        )
        
    insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")
    select distinct  'Personnel' as "DocflowUser" , 
    --rlU."DocflowUser" ,   
                  'Следующие документы не пришли на подписание из 1С :  <br/>' || 
    replace(
    replace(replace(
    '<table style = "border-collapse:collapse">
      <tr>
        <th style="text-align:center; border-left: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Организация</th>
        <th style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Работник</th>
      <th style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Должность</th>
        <th style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Документ</th>
      </tr>'||  
    (SELECT DISTINCT string_agg(x."Body", '') 
        FROM(select '<tr><td style="text-align:center; border-left: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black">'|| coalesce(p2."COrgName",'')||'</td>
          <td style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black;">'||coalesce(p2."Workers",'')||'</td>
            <td style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black;">'||coalesce(p2."PostWorkers",'')||'</td>
          
          <td style="text-align:center; border-left: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black">' ||
          '<a href="' || coalesce(p2."link",'') || '">' ||coalesce(p2."name1c",'')|| '</a>'::text || '</td>
          
        </tr>' as "Body" from "no1c" p2  
            order by  p2."COrgName", p2."Workers"  ) x)||'</table>'
    ,'&lt;','<'),'&gt;','>'),
    '&amp;','&')    as txt,
              null::bigint as "link", 'Первичный документ', 'Первичный документ',  
          'Информационное сообщение о документах, не пришедших из 1С', 
            null::bigint as "IdWorker"
    from  "no1c" dd
            /*join comdoc."ReadListGroup" rl on rl."Name" = 'Кадровики для рассылки документов, не пришедших из 1С' 
                                                                            and rl."DocTypes" ilike '%NotificationLexema%'
            join comdoc."ReadListGroupUsers" rlU on rl."VCode" = rlU."PCode"*/
    --group by 	rlU."DocflowUser" 
    ```

### Задача по изменению фамилии в карточке пользователя + склонение в карточке физического лица

??? Задача

    ```sql
    do $$
    begin
    IF NOT comdoc."isTableExists"('#fio', 'temp') THEN
      CREATE TEMP TABLE "#fio"("Id" bigint, "OldFam" text, "OldName" text, "OldOtch" text, 
                  "IdPerson" bigint, "NewFam" varchar(255), "NewName" varchar(255), "NewOtch" varchar(255), "UserName" varchar(255), "Code" varchar(2550)
      )  ON COMMIT DROP;
    END IF;
    insert into  "#fio"
    select m."Id",m."LastName", m."FirstName", m."MiddleName", per."VCode", per."Family", per."Name", per."Father",  m."UserName" , c."Code" 
    from lex."UserMeta" m 
    join rp."RP_PersonContact" c on c."IdTypeContact" = 6 and m."UserName" = c."Code"
    join rp."RP_Person" per on per."VCode" = c."Pcode"
    where (lower(coalesce(m."LastName",''))<> lower(coalesce(per."Family",'')) or lower(coalesce(m."FirstName",''))<> lower(coalesce(per."Name",'')) 
      or lower(coalesce(m."MiddleName",''))<>lower(coalesce(per."Father",'')))
    and (select count(a."Pc") from (select distinct c."Pcode" as "Pc" from rp."RP_PersonContact" c 
    join rp."RP_Person" per on per."VCode" = c."Pcode"
    where c."Code" =m."UserName")a) =1;
        
    update lex."UserMeta" m set "LastName" = q."NewFam", "FirstName" = q."NewName", "MiddleName" = q."NewOtch"
      from "#fio" q
      where q."Id" = m."Id";

    update rp."RP_Person" per set "Note" = case when per."Note" is not null then per."Note" ||'
    ' else '' end ||to_char(now(),'DD.MM.YYYY')
      || (select ' изменено ФИО с '||coalesce(f."OldFam",'')||' '||coalesce(f."OldName",'')||' '||coalesce(f."OldOtch",'')||' на '
        ||coalesce(f."NewFam",'')||' '||coalesce(f."NewName",'')||' '||coalesce(f."NewOtch",'')from "#fio" f where f."IdPerson" = per."VCode" limit 1),
      "FNFAccusative" = comdoc."Lexsklon"(per."Family", per."Name", per."Father", case when per."Sex" = 1 then 'Ж' else 'M' end, 1),
      "FNFDative" = comdoc."Lexsklon"(per."Family", per."Name", per."Father", case when per."Sex" = 1 then 'Ж' else 'M' end, 0),
      "FNFGenitive" = comdoc."Lexsklon"(per."Family", per."Name", per."Father", case when per."Sex" = 1 then 'Ж' else 'M' end, 2)
      from "#fio" q
      where per."VCode" = q."IdPerson";


    end;
    $$;
    ```

### Оповещение о необходимости замены паспорта

??? Задача

    ```sql
    insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")				  
    select distinct  pc."Code" ,  '<font size="3"> <b>Настоящим сообщаем, что приближается срок замены паспорта </b> <br/>' || '</font>' ,
              null::bigint as "link", '', '',  
          'Инф. сообщение о замене паспорта', 
              w."VCode" as "IdWorker"
    from rp."RP_Person" p
      join rp."RP_Worker" w on p."VCode" = w."IdPerson"
        left join rp."RP_WorkerMove" wm on w."VCode" = wm."IdWorker" and now() between coalesce(wm."DateBeg", '20010101') and coalesce(wm."DateEnd", '20700101')
      left join comdoc."Department" dep on wm."IdDepartment" = dep."VCode"
        left join rp."RP_Post" post on wm."IdPost" = post."VCode"
      left join rp."RP_PersonContact" pc on p."VCode" = pc."Pcode" and pc."IdTypeContact" = 6
      LEFT JOIN LATERAL comdoc."getAccountingConstantValues"(w."COrg", 'СЭД_Уведомления_Сообщения_о_замене_паспорта', NULL) cv on true
    where (
        now() between p."DateBirth" - (coalesce(cv."valueConst",30) || ' day')::interval + (date_part('year',age(p."DateBirth"))+1 || 'year')::interval and
                      p."DateBirth" + (date_part('year',age(p."DateBirth"))+1 || 'year')::interval and
        date_part('year',age(p."DateBirth" -  (coalesce(cv."valueConst",30) || ' day')::interval ))::int in (20,45)
    )  or w."VCode" = 53
    ```

### Оповещение о списке работников, которые не создали заявление об отпуске из уведомления

??? Задача

    ```sql
    with list as (
    select ud."VCode", ud."IdWorker", atr."Value" as "Vacation", to_char(atrD."DateValue",'DD.MM.YYYY') as "DateBeg" , f."Name" as "COrgName"
    from dfd."UniversalDocument" AS ud
          join dfd."DocumentConstructor" dc on ud."DocumentCategory" = dc."VCode"
        join dfd."DocumentSubtype" ds on dc."DocumentSubtype" = ds."VCode"
        join dfd."DocumentAdditionalAttribute" atr on ud."VCode" = atr."PCode"
        join dfd."DocumentCategoryAttributeType" atrtype on atr."CategoryAttributeType" = atrtype."VCode" and ud."DocumentCategory" = atrtype."PCode" and 
            atrtype."AttributeType" = 'string' and atrtype."ColumnName" = '#typeVacation#'
        join dfd."DocumentAdditionalAttribute" atrD on ud."VCode" = atrD."PCode"
        join dfd."DocumentCategoryAttributeType" atrtypeD on atrD."CategoryAttributeType" = atrtypeD."VCode" and ud."DocumentCategory" = atrtypeD."PCode" and 
            atrtypeD."AttributeType" = 'Date' and atrtypeD."ColumnName" = '#bdate#'
    join comdoc."VFilials" f on ud."COrg" = f."VCode"
    where ud."TypeName" = 'NotificationLexema' and
          ds."InternalName" = 'NotificationVacation' and
          not exists (select 1 
              from dfd."UniversalDocument" es
                      join comdoc."DocflowLink" dle on ud."VCode" = dle."DocCode2" and 
                ((dle."DocType2" =  ud."TypeName" and ud."VCode" = dle."DocCode2") or
                (dle."DocType1" =  ud."TypeName" and ud."VCode" = dle."DocCode1")
                )
                  where es."TypeName" = 'EmployeeStatement' ) and
        atrD."DateValue" > now()::date )

    insert into "#forInsNotification" ( "txt", "txtSMS", "txtTelegram")
    select null as "txt", null as "txtSMS", null as "txtTelegram"
    from (select ('<table><tr><th align="left">Организация</th><th align="left">Сотрудник</th><th align="left">Отпуск</th></tr>' ||
    (SELECT DISTINCT string_agg(x."link", '') 
        FROM ( SELECT '<tr><td>' || coalesce(l."COrgName",'') || '</td><td>' || coalesce(r."NameFull",'') || '</td>' || 
          '<td>' || coalesce(l."Vacation", '') || ' ' || l."DateBeg" || '</td>'
          ||'</tr>' as "link" 
              FROM list l
                    join rp."RP_Worker" r on l."IdWorker" = r."VCode") AS x) || '</table>' 
              ) ::text as "data") d
    ```

    таблица.столбец | описание | # для шаблона
    ----------------|----------|--------------
    d."data" | Список | #query_list#

### Отсутствие планового графика отпусков по подразделению

??? Задача

    ```sql
    with "chiefStruct" as
    (select * from vac."SendingLateApplicationNotice"())
    insert into "#forInsNotification" ("DocflowUser","CopyTo", "txt")	
    select  /*main."ChiefLogin"*/ 'Loginovasa@lexema.ru', (select  DISTINCT string_agg(coalesce(ch."ChiefLogin",''),', ') from "chiefStruct" ch
                  where ch."IdWorker" = main."Chief" and main."ChiefLogin"<>coalesce(ch."ChiefLogin",'')),  
    'Добрый день, ' || '<b>'||RTRIM(coalesce(du."FirstName",'') || ' ' || coalesce(du."MiddleName",''))||'</b>' ||
    '.   <br><br>' ||
    '<br> По следующим сотрудникам не сформированы заявки на отпуск на '||main."planYear"::text||' год:'||
    '<br><br>' ||
    replace(
    replace(replace(
    '<table style = "border-collapse:collapse">
      <tr>
      <th style="text-align:center; border-left: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Организация</th>
        <th style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Подразделение</th>
        <th style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Работник</th>
      <th style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black">Должность</th>
      </tr>'||  
    (SELECT DISTINCT string_agg(x."link", '') 
        FROM(select  '<tr><td style="text-align:center; border-left: 1px solid black; border-right: 1px solid black; border-bottom: 1px solid black">'||fil||'</td>
            <td style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black">'||dep||'</td>
          <td style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black;">'||fio||'</td>
            <td style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black;">'||post||'</td>
        </tr>' as "link" from (select distinct f."Name" as fil, coalesce(dep."Name",'') as "dep", coalesce(w."NameShort",w."NameFull",'') as fio , coalesce(rp."Name",'') as post
                from "chiefStruct" p2 
                  left join rp."RP_Worker" w on w."VCode" = p2."IdWorker"		  
                  left join comdoc."Department" dep on dep."VCode" = p2."IdDepartment"
                  left join rp."RP_Post" rp on rp."VCode" = p2."IdPost"
                  left join comdoc."VFilials" f on w."COrg" = f."VCode"
                  where coalesce(p2."ChiefLogin",'') = coalesce(main."ChiefLogin",'')) qw
                order by fil, "dep", fio ) as x)||'</table>'
    ,'&lt;','<'),'&gt;','>'),
    '&amp;','&') as "Body"
    from "chiefStruct" main
    inner join comdoc."DocflowUser" du on main."ChiefLogin" = du."UserName"
    group by  main."Chief", coalesce(du."FirstName",''), coalesce(du."MiddleName",''), main."ChiefLogin", main."planYear";
    ```



### Создание отзывов доверенностей МЧД по уволенным

??? Задача
    ```sql
    with res as (select * ,
                        '<tr>
          <td style="text-align:center; border-right: 1px solid black; border-bottom: 1px solid black;">'||
          '<a href="' || 
      (select "LocationProtocol" || '//' || "LocationHostName" || coalesce(':'||"LocationPort",'') from comdoc."DocflowSettings" order by "CDate" desc limit 1)
      || '/#/view/' || se."DocForm" || '/' || r."VCode"::text
      || '">' || case when r."TypeName" = 'EmpowermentRevocation' then 'Отзыв доверенности' else 'Доверенность' end || ' № ' ||coalesce(r."DocumentNumber",'') || ' от ' || to_char(r."DocumentDate",'DD.MM.YYYY')
            || '</a>'::text ||'</td> </tr>' as "ref_link"
                          from dfd."createEmpowermentRevocationUvol" () r 
                                    join comdoc."DocflowDocumentSettings" se on r."TypeName" = se."DocType"
                                    )

    insert into "#forInsNotification" ("DocflowUser", "txt")
    select d."DocflowUser", null as "txt"
    from (select distinct r."DocflowUser", (select string_agg(coalesce(r1."ref_link",''),'') 
              from res r1 where r."DocflowUser" = r1."DocflowUser") as list
              from res r
              ) d
    ```

    таблица.столбец | описание | # для шаблона
    ----------------|----------|--------------
    d.list | Список документов | #query_list#

### Перенос логов отправки почты и СМС в таблицу SendLog

??? Задача

    ```sql
      call comdoc."PostToSendLog"();
    ```

### Уведомление о просрочке предоставления ответа на входящие документы

??? Задача

    ```sql
      with param as (select COALESCE(comdoc."getFilial"(), 2) as "getFilial", 
      comdoc."fnDefineRegion"(null::bigint, comdoc."getFilial"()::bigint, now()::date) as "Region")	

      insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")
      select 	(SELECT DISTINCT string_agg(x."EMail", ',') 
            from (select distinct du."EMail"--,da."Name", da."InternalName" AS "DocumentAction" ,da.*
                    FROM comdoc."Route" AS a
                    JOIN comdoc."RouteStage" AS s ON s."PCode" = a."VCode"
                    join comdoc."StageItem" as i on i."PCode" = s."VCode"
                  LEFT JOIN comdoc."DocumentAction" AS da ON da."VCode" = i."DocumentAction"
                  LEFT JOIN comdoc."DocflowUser" AS du ON du."VCode" = i."StageUser"     
                        WHERE  s."IsMarked" IS NOT true      
                          and a."DocCode" = Incoming."VCode"
                          and a."DocType" = 'IncomingDocument'
                          and (da."InternalName" like 'Execute%' or da."InternalName" = 'Run') 
                      )x
              )as "DocflowUser",     
            '<tr><th align="left">По документу </th></tr>' ||
          '<tr><td>' ||
            '<a href="' ||ss."link_txt" || '/#/view/' || dds."DocForm"||'/'|| Incoming."VCode" ::text || '">'||'Входящий документ №'||coalesce(Incoming."DocumentNumber",'')||'</a>' || '</td>'
            ||'</tr>' ||'<tr><th>'||' не предоставлен ответ. Срок: '|| to_char("ResponseDatePlan"::date, 'DD.MM.YYYY')|| '</th></tr>'  as "txt",
      null::bigint as "Link", 
      null as "DocType",
        '' as "DocName", --это для физ уведомления
      'Входящие документы с истекающей датой предоставления ответа'::text  as "DocSubject",
      null::bigint as "IdWorker" --это для физ уведомления;
        
      from dfd."DocflowDocument" Incoming
        cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") ss
          left join  comdoc."DocflowDocumentSettings" AS dds ON dds."DocType" = Incoming."TypeName"
      where Incoming."TypeName"  = 'IncomingDocument'
      and "ResponseDatePlan" is not null
      --and comdoc."datediff"('day',"ResponseDatePlan",CURRENT_DATE)>3
      and "NeedResponse" =true
      and coalesce((select count(*)
            from comdoc."VDocflowCalendar" d
          cross join param p
          where ((d."RDate" between CURRENT_DATE and "ResponseDatePlan" and "ResponseDatePlan">CURRENT_DATE)  )
          and d."isDayOff" = false 
          and ((d."orgId" = p."getFilial" and coalesce(p."Region",0) =0 ) or d."Region" = p."Region")),0)<4
      and  not exists(select "DocCode1"
              from comdoc."DocflowLink" l
              where l."DocCode2" = Incoming."VCode"
                and "DocType2" = 'IncomingDocument'
              and "DocType1" = 'OutgoingDocument'
              )
    ```

### Уведомление HR о просрочке уведомлений об отпуске

Ищет все уведомления, в которых дата начала отпуска начинается с завтрашнего дня и сколько дней указано вперед, указывается в скобках (1, 10).

Находятся заявления с подтипом, который в операциях по этому типу отпуска можно создать и у которых нет завершенного маршрута, и нет отриц статуса
по ним формируется письмо.

таблица.столбец | описание | # для шаблона
----------------|----------|--------------
d."list" | Список | #query_list#

??? Задача

    ```sql
      insert into "#forInsNotification" ("txt",  "txtSMS", "txtTelegram", "DocSubject")
      select null as "txt", null as "txtSMS", null as "txtTelegram", 'Уведомление HR о просрочке уведомлений об отпуске'
      from dfd."SendingNotificationsExpiredNotificationVacation"( 1, 10)  d
      -- 
    ``` -->