# Настройка внутрисистемных уведомлений

На проекте есть возможность настроить уведомления для пользователей. Для этого необходимо произвести настройку (сделаем на примере оповещения о начале отпуска по основному месту работы). Пользователь должен обладать правами Администратора.

## Конструктор документов

* Для открытия документа необходимо в Меню в поисковой строке ввести - "Конструктор документов"_

В открывшемся реестре проверьте, не присутствует ли уже добавленный ранее шаблон "Уведомления Lexema". Если присутствует, то пропустите шаг по по созданию конструктора документов и перейдите в раздел [Справочник рассылок для документа Уведомление Lexema](#настройка_заданий_для_планировщика). Данный шаблон конструктора должен быть в единичном экземпляре. Если он отсутствует, то его необходимо создать. Для этого в реестре шаблонов нажмите **Создать**. Подробнее про конструктор документов можно узнать в статье [Конструктор документов](../Конструктор документов).

В поле **Группа** выберите **Уведомления Lexema**. Если она отсутствует, то ее необходимо создать в [Настройках документов](../Настройка документов/index.md)

В поле **Служебное наименование** введите **NotificationLexema**.

В поле **Подтип документа** выберите **Уведомления Lexema**. Если такого подтипа нет, его необходимо [создать](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Подтипы%20документов/). Настройка документов относится к полю Группа (см. комм. выше).

<!-- Поставьте галочку напротив **Автоматически формировать маршрут**. -->

Нажмите сохранить и закрыть.

![Заполненный конструктор](media/constructor.png)

## Настройка заданий для планировщика

Данный документ предназначен для формирования рассылки уведомлений для действующего/применяемого для определённого набора сотрудников. С помощью данного справочника в системе электронного документооборота можно направлять пользователям уведомления, и они будут находиться у них в панели документооборота как напоминание. В справочнике содержатся преднастроенные задачи, которые можно по необходимости включать и выключать на проекте. При необходимости появления новой задачи для рассылки её вносят в  справочник рассылок. 

Для создания рассылки, необходимо перейти _Администрирование - Рассылка электронных писем - Настройка заданий для планировщика_

В открывшемся реестре нажмите кнопку **"Создать"**.

Откроется новая форма.

![alt text](media/image-3.png)

### Вкладка "Настройки"

В открывшейся вкладке необходимо заполнить следующие поля:

**Подтип документов** - из выпадающего списка выбирается подтип документа, по которому будет действовать планировщик.

**Наименование задачи**, которое будет отображаться в качестве названия задачи.

Состояние **"Включено"** данного реквизита означает выполнение задачи в планировщике, если галочка не стоит, значит задача выполняться не будет.

**Не создавать документ Уведомление** при включенной функции уведомление будет направлено только на почту пользователю, без создания документа "Уведомления".

**Исключить уволенных сотрудников** при включенной функции не будут учитываться уволенные сотрудники, а также из списков рассылки будут автоматически удаляться уволенные сотрудники.

**Проверять отправку уведомления в течение дней:** проверяет в течение определенного количества дней ушло ли уведомление пользователю. Проверка осуществляется с помощью таблицы уведомлений. Она находится в процедуре, которая вызывается при отработке ее в планировщике задач.

**Не запускать по расписанию. Техническая задача** при включенной функции данная задача не будет выполняться не при каких условиях. Это нужно когда необходимо запускать задачу по определенным условиям, например, при нажатии на кнопку в форме документа или аналитической формы.

В блоке **Настройка расписания рассылки** выбирается, в какой день недели какого месяца и т.д. будет выполняться рассылка. Если ничего не заполнено, то задание будет запускаться по расписанию, указанному в [планировщике](#настройка_расписания_задачи_в_планировщике).

В блоке **Исключить пользователей из рассылки** выбираются пользователи, которые не должны получать уведомление по данной задаче.

![Настройка рассылки](media/nastroikaRass.png)

В блоке **Настройка рассылки почты** заполняется информация для рассылки по почте:

**Email получателей** - указывается электронная почта по которой необходимо направить уведомление. Чтобы добавить несколько получателей необходимо нажать кнопку "+ Получателя". Во всплывающем окне выбрать дополнительных получателей и нажать "Добавить".

![Получатель](media/addPoluch.png)

**Email копия** - указывается электронная почта кому необходимо дополнительно направить уведомление. Добавление несколько получателей производится аналогично как добавление основных получателей.

**Email скрытая копия** - указывается электронная почта кому необходимо дополнительно направить скрытое уведомление. Получателе не будет видно в письмо в спике адресатов. Добавление несколько получателей производится аналогично как добавление основных получателей.

**По вопросу** - указывается тема уведомления.

**Документ** - указывается наименование документа для отображения в системе.

**Добавить ссылку на документ** - при включенной галочке в текст уведомления добавляется гиперссылка на документ.

<!-- **Текст для ссылки** - в данном поле можно задавать свой текст для гиперссылки. -->

В блоке **Настройка списка рассылки** - при необходимости дополнительно указывается получатели через [группу рассылки](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Группы%20рассылки/), либо по [сервисной функции](../Настройка шаблонов маршрутов/index.md#сервисные_функции), которые используются в шаблоне маршрута, либо указывается конкретный логин получателя.

Пример заполненной вкладки предоставлен ниже:

![alt text](media/image-4.png)

Поле "Комментарий" - текстовое для ведения каких-либо комментариев, записей по задаче.

### Вкладка "Задача"

В поле указывается часть с динамическим запросом, содержащим непосредственно текст для генерации документа.

<!-- Пример: 

```SQL
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker", "DateBeg", "Days", "TypeVacation", "Vacation", "DateEnd", "CopyTo", "txtSMS", "txtTelegram")
select pc_ch."Code" as "User", null as "txt", 
p."VCode" as "link",p."TypeName", null /*case when "TypeName" = 'Base.RP_DocVacationChanges' then 'Переносы отпусков' else 'График отпусков' end*/,
 null, /*'Уведомление работника о времени начала отпуска',*/
m."IdWorker", coalesce(m."DateBegPer",m."DateBeg")::date, coalesce(m."DaysPer",m."Days"), m."HolidayTypeGuid", coalesce(tw."Name",ex.name1c), coalesce(m."DateEndPer",m."DateEnd") , null, null as "txtSMS", null as "txtTelegram"
from  aw."RP_DocVacation" p
      join aw."RP_WorkerVacation" m on p."VCode" = m."Pcode"
      cross join (select  (now() + '1 day'::interval)::date as bd,   (now() + '8 day'::interval)::date as ed  ) dt 
      cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") l
      join rp."RP_Worker" w_ch on w_ch."VCode" = m."IdWorker"
      join rp."RP_Person" p_ch on w_ch."IdPerson" = p_ch."VCode"
      join rp."RP_PersonContact" pc_ch on p_ch."VCode" = pc_ch."Pcode" and pc_ch."IdTypeContact" = 6
      left join odata.exchange1cguids ex on m."HolidayTypeGuid" = ex.guid and ex.atype = 'TypeVacation' and ex.corg= p."COrg"
     left join aw."VTypeTimeWork" tw on m."TypeVacation" = tw."VCode"
where p."COrg" <> 4 and 
        coalesce(m."DateBegPer",m."DateBeg")>= dt.bd and coalesce(m."DateBegPer",m."DateBeg") <=dt.ed and
             not exists (select 1 
 			   from "dfd"."UniversalDocument" AS "ud"
 			         join comdoc."ReadListItem" "rl" on "ud"."VCode" = "rl"."DocCode"
 			         join comdoc."DocflowLink" "dl" on "dl"."DocCode2" = p."VCode" and "dl"."DocCode1" = "ud"."VCode"
                     join dfd."DocumentAdditionalAttribute" atr on "ud"."VCode" = atr."PCode"
					 join dfd."DocumentCategoryAttributeType" atrtype on "atr"."CategoryAttributeType" = atrtype."VCode" and "ud"."DocumentCategory" = atrtype."PCode" and atrtype."AttributeType" = 'Date' and atrtype."ColumnName" = '#bdate#'
 			   where "rl"."DocflowUser" = pc_ch."Code" and 			        
					 "ud"."TypeName" = 'NotificationLexema' and 
                      atr."DateValue" = coalesce(m."DateBegPer",m."DateBeg") 
						 --"ud"."Text" like '%'|| to_char(coalesce(m."DateBegPer",m."DateBeg")::date, 'DD.MM.YYYY') ||'%'
						)   and
           w_ch."DateEDM" is not null and
           w_ch."DateEnd" is null and

--проверка на созданное заявление с завершенным маршрутом, на отпуск или на перенос
           not exists (select 1 
			   from "dfd"."UniversalDocument" AS "ud" 
                                      join dfd."DocumentAdditionalAttribute" atr on "ud"."VCode" = atr."PCode"
				      join dfd."DocumentCategoryAttributeType" atrtype on "atr"."CategoryAttributeType" = atrtype."VCode" and "ud"."DocumentCategory" = atrtype."PCode" and atrtype."AttributeType" = 'Date' and atrtype."ColumnName" = '#bdate#'
                                     join dfd."DocumentConstructor" dc on "ud"."DocumentCategory" = dc."VCode"
                                     join dfd."DocumentSubtype" ds on dc."DocumentSubtype" = ds."VCode"
                                    join comdoc."Route" r on ud."VCode" = r."DocCode" and ud."TypeName" = r."DocType" and r."RouteStatus" = 3
			   where "ud"."TypeName" = 'EmployeeStatement'  and
                                        "ud"."IdWorker" = m."IdWorker" and
                                         atr."DateValue" = coalesce(m."DateBegPer",m."DateBeg") and
                                         ds."InternalName" in ('EmployeeStatementVacation','EmployeeStatementTransperVacation') and
                                         ud."Removed" is not true and 
                                        not exists (select 1 from dfd."CancellationAct" a where a."DocCode" = ud."VCode" and a."DocType" = ud."TypeName") and
not exists (select 1  
from comdoc."Route" r
	join comdoc."RouteStage" rs on r."VCode" = rs."PCode"
	join comdoc."StageItem" si on rs."VCode" = si."PCode"
	inner join comdoc."DocflowDocumentSettings" as sts on sts."DocType" = r."DocType"
	inner join comdoc."DocflowDocumentSettingsDetail" as dfs on dfs."PCode" = sts."VCode" and 
																dfs."DocumentAction" = si."DocumentAction" and 
																dfs."DocumentStatus" = si."DocumentStatus"
where r."DocCode" =  "ud"."VCode" and 
      r."DocType" = p."TypeName" and
	  dfs."NegativeStatus" is true)
	  )
		
```

!!! warning
	Важным условием является наличие `null as "txt",` в динамическом запросе. В процессе запроса `null as "txt",` заменяется на текст из конструктора уведомлений. Если в запросе отсутствует `null as "txt",` , то система не сможет корректно обработать запрос и уведомление не будет отправлено пользователю.

	![Текст](../Конструктор уведомлений/media/null.png) -->

В динамическом запросе прописывается вычисление, т.е. правило, по которому рассчитываются получатели уведомления, документы и другая необходимая информация. Данное вычисление на выходе имеет определенную структуру - перечень колонок (столбцов) для дальнейших настроек.

Эти столбцы описаны в таблице справа  - 

В **таблица.столбец** - указывается столбец с вычисленной информацией.

В **описание** - задается пользовательское описание и назначение по каждой строке из столбца 1.

В **# для шаблона** - задаются служебное наименования, заключенные с обеих сторон в #. Наименование может называться как угодно, главное чтобы оно было уникальным, на латинице и было оформлено с обеих сторон решеткой.

<!-- В примере указано: из столбца **p_ch."Name"** с помощью запроса указанного в задаче считывается хранимая в данном столбце информация, после чего система сохраняет ее в виде служебного наименования **#query_Name#**, у которого в конструкторе уведомлений будет описание что в данном служебном наименовании хранится **имя сотрудника**. -->

![Таблица](media/table.png)

![Конструктор уведомлений](media/constructor2.png)

Для дополнении новых служебных наименований необходимо обратиться в техническую поддержку.

<!-- В примере заполненной вкладки предоставлен ниже:

![Задача](media/task.png) -->

После заполнения всех полей нажмите Сохранить и закрыть.

## Настройка расписания задачи в планировщике

Далее необходимо настроить [задачу](../Функции планировщика задач/index.md) **Уведомления Lexema** c помощью [планировщика](../Планировщик задач/index.md) если не было настроенно ранее.

![Задача в шедулере](media/sheduler.png)

Задача отслеживает дату начала отпуска при заданных конфигурационных параметрах, и за указанное ранее количество дней  отправляет  пользователю уведомление. Оно появляется в панели документооборота.

![Уведомление](media/push.png)

Внутри документа будет уведомление о приближающейся дате начала отпуска. В документ можно перейти по ссылке, или по вложенным документам.

![Информационное письмо](media/vacation.png)

Внутри документа можно сразу создать заявление на отпуск. Для этого нажмите на кнопку "Операции" и выберите "Создать заявление от сотрудника". Автоматически откроется документ ["Заявления от сотрудника"](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Заявления%20от%20сотрудников/)

![Операция создания заявления из уведомления](media/createStatement.png)

<!-- ## Ручное создание уведомления

Для ручного создания уведомления, перейдите в Меню - Кадровый документооборот. Реестры - Уведомления. В открывшемся реестре необходимо нажать кнопку "Создать".

![Реестр](media/reestr.png)

В блоке "Основной текст" заполните необходимый текст уведомления.

![Текст уведомления](media/pushText.png)

В меню "Рассылка" добавьте и выберите пользователей, которым необходимо отправить уведомление, после чего нажмите кнопку "Отправить"

![Список рассылки](media/mailingList.png)

В документообороте у пользователя, которому было направлено уведомление, появится соответствующий документ на обработку.

![Уведомление](media/document.png) -->

<!-- Для ознакомления с данным документом нажмите на кнопку "Рассылка" после этого внутри всплывающего окна кнопку"Подтвердить ознакомление"

![Ознакомление](media/familiarization.png) -->

## Настройка уведомлений из личного кабинета HR и личного кабинета руководителя

В личных кабинета [HR](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Личный%20кабинет%20HR/) можно направлять пользователям сообщение, и они будут находиться у них в панели документооборота как напоминание.

Для отправки сообщений должны быть настроены [конструкторы документов](#конструктор_документов), в котором необходимо выбрать подтип **"Сообщение от службы HR"** (если такой подтип отсутствует, то необходимо его создать) и указать служебное наименование **HRNote** для личного кабинета HR:

![HR](media/HR.png)

Для личного кабинета руководителя: подтип "Сообщение от руководителя" и служебное наименование **ManagersNote**:

![Руководители](media/rukovoditeli.png)

<!-- ## Примеры рассылок

### Уведомления об отпуске на основании Графика отпусков по внешним совместителям

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker", "DateBeg", "Days", "TypeVacation", "Vacation", "DateEnd", "CopyTo")
select "User", "txt", "link", "TypeName", "DocName", "DocSubject"
, "IdWorker"
, "DateBeg", "Days", "TypeVacation", "Vacation", "DateEnd", "CopyTo"
from (
	select distinct pc_ch."Code" as "User", '<font size="4"> </font><p style="text-align: center;">' || p_ch."Name" || ' ' || coalesce(p_ch."Father", '') || ', добрый день!</p><p style="text-align: center;"><br></p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;На основании
статьи 123 Трудового кодекса Российской Федерации и согласно утвержденному&nbsp;графику отпусков на ' || p."Year"::text ||' год информируем о дате начала Вашего оплачиваемого отпуска (<b>' ||  coalesce(tw."Name",ex.name1c,'')||') </b> с <strong>' || to_char(coalesce(m."DateBegPer",m."DateBeg")::date, 'DD.MM.YYYY') ||  '</strong> сроком на <strong>' || coalesce(m."DaysPer",m."Days")::text
|| '</strong> календарных
дня(ей). Дата выхода на работу <strong>' ||to_char((coalesce(m."DateEndPer",m."DateEnd") +  '1 day'::interval)::date, 'DD.MM.YYYY')  
|| '</strong>. В случае, если дата выхода на
работу приходится на выходной день, она переносится на ближайший рабочий день.</p>

<p>&nbsp;</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ВАЖНО! </p>

<p><em>В связи с
вышеизложенным Вам следует подать заявление о предоставлении отпуска для
своевременного проведения расчетов и подготовки соответствующих документов. </em></p>

<p><em>Если Вы не
планируете использовать отпуск в указанные даты, обязательно сформируйте
заявление о переносе отпуска. </em></p>

<p><strong>&nbsp;</strong></p>

<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Заявление на
отпуск или перенос отпуска необходимо сформировать в системе КЭДО Lexema при 
помощи кнопки «Операции» на панели инструментов данного
уведомления.</strong></p>

<p><strong>&nbsp;</strong></p>

<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Уведомление
можно закрыть только после выполнения одного из действий.</strong></p>

<p><br>
Приятного отдыха! </p>
<font size="4"></font>'   as txt,
	p."VCode" as "link",p."TypeName", 
null as "DocName" /*case when "TypeName" = 'Base.RP_DocVacationChanges' then 'Переносы отпусков' else 'График отпусков' end*/,
 null as "DocSubject", /*'Уведомление работника о времени начала отпуска',*/
 m."IdWorker",  coalesce(m."DateBegPer",m."DateBeg")::date as "DateBeg", coalesce(m."DaysPer",m."Days") as "Days", 
	m."HolidayTypeGuid" as "TypeVacation", coalesce(tw."Name",ex.name1c) as "Vacation", 
	coalesce(m."DateEndPer",m."DateEnd") as "DateEnd", null as "CopyTo", "IdTypeBusy", "IdPerson"
	from  aw."RP_DocVacation" p
		  join aw."RP_WorkerVacation" m on p."VCode" = m."Pcode"
		  cross join (select  (now() + '1 day'::interval)::date as bd,   (now() + '6 day'::interval)::date as ed  ) dt 
		  cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") l
		  join rp."RP_Worker" w_ch on w_ch."VCode" = m."IdWorker"
		  join rp."RP_WorkerMove" rpwm on rpwm."IdWorker" = w_ch."VCode"
		  join rp."RP_Person" p_ch on w_ch."IdPerson" = p_ch."VCode"
		  join rp."RP_PersonContact" pc_ch on p_ch."VCode" = pc_ch."Pcode" and pc_ch."IdTypeContact" = 6
		  left join odata.exchange1cguids ex on m."HolidayTypeGuid" = ex.guid and ex.atype = 'TypeVacation' and ex.corg= p."COrg"
		 left join aw."VTypeTimeWork" tw on m."TypeVacation" = tw."VCode"
	where coalesce(m."DateBegPer",m."DateBeg")>= dt.bd and coalesce(m."DateBegPer",m."DateBeg") <=dt.ed and
				not exists (select 1 
				   from "dfd"."UniversalDocument" AS "ud"
						 join comdoc."ReadListItem" "rl" on "ud"."VCode" = "rl"."DocCode"
						 join comdoc."DocflowLink" "dl" on "dl"."DocCode2" = p."VCode" and "dl"."DocCode1" = "ud"."VCode"
				   where "rl"."DocflowUser" = pc_ch."Code" and
						 "ud"."TypeName" = 'NotificationLexema' and 
						 "ud"."Text" like '%'|| to_char(coalesce(m."DateBegPer",m."DateBeg")::date, 'DD.MM.YYYY') ||'%') 
				 and (rpwm."DateEnd" is null 
					  OR (now()::date <= coalesce(rpwm."DateEnd", '2100-01-01'::date)))
				 and coalesce(rpwm."IdTypeBusy",1) = 3
		) as v
		where not exists(select 1 
							from aw."RP_WorkerVacation" t_wv
								join rp."RP_Worker" t_w on t_w."VCode" = t_wv."IdWorker"
		  						join rp."RP_WorkerMove" t_rpwm on t_rpwm."IdWorker" = t_w."VCode"
		  						join rp."RP_Person" t_p on t_p."VCode" = t_w."IdPerson"
							where t_p."VCode" = v."IdPerson"
								and (t_rpwm."DateEnd" is null 
								  	OR (now()::date <= coalesce(t_rpwm."DateEnd", '2100-01-01'::date)))
								and v."DateBeg" = coalesce(t_wv."DateBegPer",t_wv."DateBeg")
								and v."Days" = coalesce(t_wv."DaysPer",t_wv."Days")
						 		and coalesce(t_rpwm."IdTypeBusy",1) in (1,2)
					 	)
```

### Оповещение о списке работников, которые не создали заявление об отпуске

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

### Уведомления об отпуске на основании Графика отпусков по внутренним совместителям

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker", "DateBeg", "Days", "TypeVacation", "Vacation", "DateEnd", "CopyTo")
select pc_ch."Code" as "User", '<font size="4"> </font><p style="text-align: center;">' || p_ch."Name" || ' ' || coalesce(p_ch."Father", '') || ', добрый день!</p><p style="text-align: center;"><br></p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;На основании
статьи 123 Трудового кодекса Российской Федерации и согласно утвержденному&nbsp;графику отпусков на ' || p."Year"::text ||' год информируем о дате начала Вашего оплачиваемого отпуска (<b>' ||  coalesce(tw."Name",ex.name1c,'')||') </b> с <strong>' || to_char(coalesce(m."DateBegPer",m."DateBeg")::date, 'DD.MM.YYYY') ||  '</strong> сроком на <strong>' || coalesce(m."DaysPer",m."Days")::text
|| '</strong> календарных
дня(ей). Дата выхода на работу <strong>' ||to_char((coalesce(m."DateEndPer",m."DateEnd") +  '1 day'::interval)::date, 'DD.MM.YYYY')  
|| '</strong>. В случае, если дата выхода на
работу приходится на выходной день, она переносится на ближайший рабочий день.</p>

<p>&nbsp;</p>

<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ВАЖНО! </p>

<p><em>В связи с
вышеизложенным Вам следует подать заявление о предоставлении отпуска для
своевременного проведения расчетов и подготовки соответствующих документов. </em></p>

<p><em>Если Вы не
планируете использовать отпуск в указанные даты, обязательно сформируйте
заявление о переносе отпуска. </em></p>

<p><strong>&nbsp;</strong></p>

<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Заявление на
отпуск или перенос отпуска необходимо сформировать в системе КЭДО Lexema по
соответствующей операции через кнопку «Операции» на панели инструментов данного
уведомления.</strong></p>

<p><strong>&nbsp;</strong></p>

<p><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Уведомление
можно закрыть только после выполнения одного из действий.</strong></p>

<p><br>
Приятного отдыха! </p>
<font size="4"></font>'   as txt,
p."VCode" as "link",p."TypeName", 
null /*case when "TypeName" = 'Base.RP_DocVacationChanges' then 'Переносы отпусков' else 'График отпусков' end*/,
 null, /*'Уведомление работника о времени начала отпуска',*/
 m."IdWorker", 
coalesce(m."DateBegPer",m."DateBeg")::date as "DateBeg", coalesce(m."DaysPer",m."Days") as "Days", 
m."HolidayTypeGuid", coalesce(tw."Name",ex.name1c), coalesce(m."DateEndPer",m."DateEnd") as "DateEnd", null as "CopyTo"
from  aw."RP_DocVacation" p
      join aw."RP_WorkerVacation" m on p."VCode" = m."Pcode"
      cross join (select  (now() + '1 day'::interval)::date as bd,   (now() + '6 day'::interval)::date as ed  ) dt 
      cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") l
      join rp."RP_Worker" w_ch on w_ch."VCode" = m."IdWorker"
      join rp."RP_Person" p_ch on w_ch."IdPerson" = p_ch."VCode"
      join rp."RP_PersonContact" pc_ch on p_ch."VCode" = pc_ch."Pcode" and pc_ch."IdTypeContact" = 6
      left join odata.exchange1cguids ex on m."HolidayTypeGuid" = ex.guid and ex.atype = 'TypeVacation' and ex.corg= p."COrg"
     left join aw."VTypeTimeWork" tw on m."TypeVacation" = tw."VCode"
where coalesce(m."DateBegPer",m."DateBeg")>= dt.bd and coalesce(m."DateBegPer",m."DateBeg") <=dt.ed and
            not exists (select 1 
			   from "dfd"."UniversalDocument" AS "ud"
			         join comdoc."ReadListItem" "rl" on "ud"."VCode" = "rl"."DocCode"
			         join comdoc."DocflowLink" "dl" on "dl"."DocCode2" = p."VCode" and "dl"."DocCode1" = "ud"."VCode"
			   where "rl"."DocflowUser" = pc_ch."Code" and
			         "ud"."TypeName" = 'NotificationLexema' and 
                     "ud"."Text" like '%'|| to_char(coalesce(m."DateBegPer",m."DateBeg")::date, 'DD.MM.YYYY') ||'%') 
			 and 2 = coalesce((select "IdTypeBusy"
								from rp."RP_WorkerMove" rpwm 
								where rpwm."IdWorker" = w_ch."VCode"
									 and (rpwm."DateEnd" is null 
										  OR (now()::date <= coalesce(rpwm."DateEnd", '2100-01-01'::date)))
								limit 1)
							  , 1)
```

### Отмена признака Ознакомлен, если заявление удалили или сделали акт об аннулировании

```sql
with forupd as (
select uved."VCode"
from dfd."UniversalDocument" uved 
     join comdoc."DocflowLink" dl on dl."DocType2" in ('Base.RP_DocVacation','Base.RP_DocVacationChanges') and dl."DocType1" = uved."TypeName" and dl."DocCode1" = uved."VCode"
	 join comdoc."ReadListItem" r on uved."VCode" = r."DocCode" and uved."TypeName" = r."DocType"
where uved."TypeName" = 'NotificationLexema' and
      coalesce(r."ReadCount",0) <> 0 and
            exists (select 1 
			   from dfd."UniversalDocument" AS ud
			    join comdoc."DocflowLink" dle on  ud."VCode" = dle."DocCode2" and 
						dle."DocType2" =  ud."TypeName" and
						dle."DocType1" = 'NotificationLexema' and dle."DocCode1" = uved."VCode"
			   where ud."TypeName" = 'EmployeeStatement'  and 
                ( (coalesce(ud."Removed", false) = false  and exists (select 1 from dfd."CancellationAct" a where a."DocCode" = ud."VCode" and a."DocType" = ud."TypeName")) 
					or coalesce(ud."Removed", false) = true
				    or not exists (select 1 from comdoc."Route" rt where rt."DocCode" = ud."VCode" and rt."DocType" = ud."TypeName") )
)
	)
	
update comdoc."ReadListItem" r 
set "ReadCount" = 0
where r."DocCode" in (select "VCode" from forupd) 
      and 'NotificationLexema' = r."DocType"
```

### Документы не пришедшие на подписание в систему из 1С

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")
select distinct  rlU."DocflowUser" ,  'Следующие документы не пришли на подписание из 1С: :  <br/>' || 
         string_agg(dd."txt", ',  <br/>') ,
          null::bigint as "link", 'Первичный документ', 'Первичный документ',  
		  'Информационное сообщение о документах, не пришедших из 1С', 
         (select w."VCode" 
			from rp."RP_Worker" w
				   join rp."RP_PersonContact" pc on w."IdPerson" = pc."Pcode" and pc."IdTypeContact" = 6 and pc."Code" = rlU."DocflowUser"
			order by w."DateBeg" desc
			limit 1
			) as "IdWorker"
from (
	select r."name1c" || ' ' || "Workers" || ' (' || to_char(r."WDate"::date, 'DD.MM.YYYY')   || ')' || '<a href=' || l."link_txt" || '#/view/'|| r."TypeName" ||'Form' ||'/' ||  r."VCode" ||  '> перейти ' || l."link_txt" || '#/view/'|| r."TypeName" ||'Form' ||'/' ||  r."VCode" || '</a>' as txt
	from odata."getExchange1CGuidsRegistry"(null, null, null, null, null, null, null, null, null, null) r
		cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") l
	where r."VCode" is not null and 
          r."DFS_VCode" is null and
	  r."guid" is not null and
          r.name1c not ilike '%больнич%' and
	      r. "DocumentDate" >= '20221001')
dd
         join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу' and rl."DocTypes" ilike '%NotificationLexema%'
         join comdoc."ReadListGroupUsers" rlU on rl."VCode" = rlU."PCode"
group by 	rlU."DocflowUser" 	
```
!!! Примечание
      В строке `join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу'` указывается наименование [группы рассылки](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Группы%20рассылки/)

![1С](media/1C.png)

### Документы не ушедщие в систему  1С

```sql
insert into "#forInsNotification" ( "txt")
select '<table><tr><th align="left">Организация</th><th align="left">Сотрудник</th><th align="left">Документ</th><th align="left">Ссылка на документ</th></tr>' ||
(SELECT DISTINCT string_agg(x."link", '') 
     FROM ( SELECT '<tr><td>' || coalesce(l."COrgName",'') || '</td><td>' || coalesce(L."Workers",'') || '</td>' || 
		   '<td>' || coalesce(l."DocumentSubtypeName", "DocumentCategoryName") || ' ' || l."DocumentNumber" || ' от ' || to_char("DocumentDate",'DD.MM.YYYY')||'</td>' || '<td>' ||ss."link_txt" || '/#/view/' || dds."DocForm"||'/'|| l."VCode"::text || '</td>'
		   ||'</tr>' as "link" 
		   		FROM  odata."getExchange1CGuidsCheckExport"(30::integer) l
		            cross join (select "LocationProtocol" || '//' || "LocationHostName" as "link_txt" from comdoc."DocflowSettings") ss
                            left join  comdoc."DocflowDocumentSettings" AS dds ON dds."DocType" = l."TypeName"
) AS x) || '</table>' 
```

### Напоминание об обработке документа руководителю на этапе "Согласование"

```sql
with "approve" as
( select distinct   r."Initiator", i."StageUser",  r."DocName",  i."BeginDate",
	i."ActionDate", i."DaysForAction", r."DocType", 
	(select "LocationProtocol" || '//' || "LocationHostName" || coalesce(':'||"LocationPort",'') from comdoc."DocflowSettings" order by "CDate" desc limit 1)
	|| '/#/view/' || se."DocForm" || '/' || r."DocCode" as "ref",
	r."DocCode",
	false as "Terminal", coalesce(dd."COrg", comdoc."getFilial"()) as "Org"
from comdoc."StageItem" i 
	join comdoc."RouteStage" st on st."VCode" = i."PCode"
	join comdoc."Route" r on r."VCode" = st."PCode"
	join dfd."UniversalDocument" dd on r."DocCode" = dd."VCode" AND r."DocType" = dd."TypeName"
	join comdoc."DocflowUser" du on i."StageUser" = du."UserName"
	join comdoc."DocflowUser" dui on r."Initiator" = dui."UserName"
	join comdoc."DocflowDocumentSettings" se on r."DocType" = se."DocType"
	left join dfd."DocumentConstructor" cons on dd."DocumentCategory" = cons."VCode"
    
where   (coalesce(st."IsMarked",false)!=true)
	AND r."RouteStatus" = 2
	AND i."StageItemStatus" = 2
	AND st."Status" = 2
	and "DocumentAction"= 1
	and st."StageName"='Согласование руководителем'
 )
 
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")
 
 select a."StageUser"   as "DocflowUser",
 
 'Добрый день, ' || '<b> '|| du."SmallName" ||' </b>' ||'.   <br>' || 

 '<br>  Вам поступил документ на обработку.'||
'<br> Организация: ' || f."Name" ||
'<br> Задача: Согласовать' ||
'<br> Документ: ' || a."ref" ||
'<br> Предыдущий этап маршрута: Инициатор ' 
'<br>' || dui."SmallName" || '- Подписан ЭП ' 
  as "txt",
 null as "Link", null as "DocType", a."DocName" as "DocName", --это для физ уведомления
 'Lexema. ' || f."Name" || 'Согласовать. ' || a."DocName"  as "DocSubject",
	 
 (select w."VCode" 
      from rp."RP_Worker" w
           join rp."RP_PersonContact" pc on w."IdPerson" = pc."Pcode" and pc."IdTypeContact" = 6 and pc."Code" = a."StageUser"
      order by w."DateBeg" desc
      limit 1
      ) as "IdWorker"
from "approve" a
 	join comdoc."DocflowUser" du  on a."StageUser" = du."UserName"
	join comdoc."DocflowUser" dui on a."Initiator" = dui."UserName"
	join comdoc."VFilials" f on a."Org" = f."VCode"
where  now() > a."BeginDate" + '2 hour'::interval 
and  a."StageUser" = 'HRDirector'
;
```
!!! Примечание
      В строке `and st."StageName"='Согласование руководителем'` - указывается название этапа в [шаблоне маршруте](../Настройка шаблонов маршрутов/index.md).

      В строке `and  a."StageUser" = 'HRDirector'` - указывается логин пользователя руководителя


![Обработка документа](media/docObrabotka.png)

### Об окончании испытательного срока

В настройках учетной политики необходимо указать константу **СЭД_Уведомления_Предупреждение_об_окончании_испытательного_срока** и заполнить значение в календарных дней.

![Константа](media/constantSrok.png)

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")
select distinct  rlU."DocflowUser" ,  '<font size="3"> <b>Уведомляем об окончании испытательного срока сотрудников :  </b> <br/>' || 
         string_agg(dd."txt", ',  <br/>') || '</font>' ,
          null::bigint as "link", 'Первичный документ', 'Первичный документ',  
		  'Инф. сообщение об окончании испыт. срока', 
         (select w."VCode" 
			from rp."RP_Worker" w
				   join rp."RP_PersonContact" pc on w."IdPerson" = pc."Pcode" and pc."IdTypeContact" = 6 and pc."Code" = rlU."DocflowUser"
			order by w."DateBeg" desc
			limit 1
			) as "IdWorker"
from (select  w."NameFull" || ' ' || coalesce(w."NumTab", '')  || ' (' || coalesce(dep."Name", '') || case when coalesce(wm."IdPost",0) <>0 then ', '  else '' end || coalesce(post."Name", '')  || case when coalesce(wm."IdPost",0) <>0 or coalesce(wm."IdDepartment",0) > 0 then ', '  else '' end || ' Испыт.срок: ' || wm."Probation"::text || 'мес. Дата приема: '||to_char(w."DateBeg", 'DD.MM.YYYY') || ')' as txt
from rp."RP_Worker" w
	 join rp."RP_WorkerMove" wm on w."VCode" = wm."IdWorker" and now() between coalesce(wm."DateBeg", '20010101') and coalesce(wm."DateEnd", '20700101')
        left join comdoc."Department" dep on wm."IdDepartment" = dep."VCode"
left join rp."RP_Post" post on wm."IdPost" = post."VCode"
     LEFT JOIN LATERAL comdoc."getAccountingConstantValues"(w."COrg", 'СЭД_Уведомления_Предупреждение_об_окончании_испытательного_срока', NULL) cv on true
where now() between  (w."DateBeg" + (wm."Probation"::text || ' month')::interval) -  (coalesce(cv."valueConst",14)||' day')::interval   and   (w."DateBeg" + (wm."Probation"::text || ' month')::interval) and
	  w."DateEnd" is null and 
          coalesce(wm."Probation",0) > 0
	)
dd
         join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу' and rl."DocTypes" ilike '%NotificationLexema%'
         join comdoc."ReadListGroupUsers" rlU on rl."VCode" = rlU."PCode"
group by 	rlU."DocflowUser"

```
!!! Примечание
      В строке `join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу'` указывается наименование [группы рассылки](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Группы%20рассылки/)

![Испытательный срок](media/ИспытательныйСрок.png)

### Отсутствие планового графика отпусков по подразделению

В настройках учетной политики необходимо указать константу **срок подготовки планового графика отпусков** и заполнить значение в календарных дней за сколько дней направлять руководителю уведомление.

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

![Отсутствие отпуска](media/otsutstviePlanOtpusk.png)

### Оповещение о необходимости замены паспорта

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")				  
select distinct  pc."Code" ,  '<font size="3"> <b>Настоящим сообщаем, что приближается срок замены паспорта </b> <br/>' || '</font>' ,
          null::bigint as "link", '', '',  
		  'Инф. сообщение о замене паспорта', 
           w."VCode" as "IdWorker"
from rp."RP_Person" p
	 join rp."RP_Worker" w on p."VCode" = w."IdPerson"
     join rp."RP_WorkerMove" wm on w."VCode" = wm."IdWorker" and now() between coalesce(wm."DateBeg", '20010101') and coalesce(wm."DateEnd", '20700101')
	 left join comdoc."Department" dep on wm."IdDepartment" = dep."VCode"
     left join rp."RP_Post" post on wm."IdPost" = post."VCode"
	 left join rp."RP_PersonContact" pc on p."VCode" = pc."Pcode" and pc."IdTypeContact" = 6
	 LEFT JOIN LATERAL comdoc."getAccountingConstantValues"(w."COrg", 'СЭД_Уведомления_Сообщения_о_замене_паспорта', NULL) cv on true
where 
 	  now() between p."DateBirth" - (coalesce(cv."valueConst",30) || ' day')::interval + (date_part('year',age(p."DateBirth"))+1 || 'year')::interval and
 	                p."DateBirth" + (date_part('year',age(p."DateBirth"))+1 || 'year')::interval and
	  date_part('year',age(p."DateBirth" -  (coalesce(cv."valueConst",30) || ' day')::interval ))::int in (20,45)

```
![Паспорт](../Рассылки системы/media/passport.png)

### Сообщения о приближающемся юбилее работы в компании

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")				  
select distinct  rlU."DocflowUser" ,  '<font size="3"> <b>Список юбиляров :  </b> <br/>' || 
         string_agg(dd."txt", ',  <br/>') || '</font>' ,
          null::bigint as "link", '', '',  
		  'Инф. сообщение о юбилее работы в компании', 
         (select w."VCode" 
			from rp."RP_Worker" w
				   join rp."RP_PersonContact" pc on w."IdPerson" = pc."Pcode" and pc."IdTypeContact" = 6 and pc."Code" = rlU."DocflowUser"
			order by w."DateBeg" desc
			limit 1
			) as "IdWorker"
from (select  w."NameFull" || ' ' || coalesce(w."NumTab", '')  || ' (' || coalesce(dep."Name", '') 
	         || case when coalesce(wm."IdPost",0) <>0 then ', '  else '' end || coalesce(post."Name", '') 
	         || ' Дата приема: '||to_char(w."DateBeg", 'DD.MM.YYYY') || ')' as txt
from rp."RP_Worker" w 
     join rp."RP_WorkerMove" wm on w."VCode" = wm."IdWorker" and now() between coalesce(wm."DateBeg", '20010101') and coalesce(wm."DateEnd", '20700101')
	 left join comdoc."Department" dep on wm."IdDepartment" = dep."VCode"
     left join rp."RP_Post" post on wm."IdPost" = post."VCode"
	 LEFT JOIN LATERAL comdoc."getAccountingConstantValues"(w."COrg", 'СЭД_Уведомления_Сообщения_о_юбилее_работы_в_компании', NULL) cv on true
where 
 	 w."DateEnd" is null  and
	  date_part('year',age(w."DateBeg"- (coalesce(cv."valueConst",30) || ' day')::interval))::int >1 and
          date_part('year',age(w."DateBeg" - (coalesce(cv."valueConst",30) || ' day')::interval))::int % 5 = 0 and
now() between w."DateBeg" - (coalesce(cv."valueConst",30) || ' day')::interval + (date_part('year',age(w."DateBeg"))+1 || 'year')::interval and
 	                w."DateBeg" + (date_part('year',age(w."DateBeg"))+1 || 'year')::interval) dd
         join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу' and rl."DocTypes" ilike '%NotificationLexema%'
         join comdoc."ReadListGroupUsers" rlU on rl."VCode" = rlU."PCode"
group by 	rlU."DocflowUser" 					 					
```

!!! Примечание
      В строке `join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу'` указывается наименование [группы рассылки](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Группы%20рассылки/)

![Юбилей в компании](media/yubileyCompan.png)

### Сообщение о приближающихся юбилеях

```sql
insert into "#forInsNotification" ("DocflowUser", "txt", "Link", "DocType", "DocName", "DocSubject", "IdWorker")				  
select distinct  rlU."DocflowUser" ,  '<font size="3"> <b>Список юбиляров :  </b> <br/>' || 
         string_agg(dd."txt", ',  <br/>') || '</font>' ,
          null::bigint as "link", '', '',  
		  'Инф. сообщение о юбилярах', 
         (select w."VCode" 
			from rp."RP_Worker" w
				   join rp."RP_PersonContact" pc on w."IdPerson" = pc."Pcode" and pc."IdTypeContact" = 6 and pc."Code" = rlU."DocflowUser"
			order by w."DateBeg" desc
			limit 1
			) as "IdWorker"
from (select  w."NameFull" || ' ' || coalesce(w."NumTab", '')  || ' (' || coalesce(dep."Name", '') 
	         || case when coalesce(wm."IdPost",0) <>0 then ', '  else '' end || coalesce(post."Name", '') 
	         || ' Дата рождения: '||to_char(p."DateBirth", 'DD.MM.YYYY') || ')' as txt
from rp."RP_Person" p
	 join rp."RP_Worker" w on p."VCode" = w."IdPerson"
     join rp."RP_WorkerMove" wm on w."VCode" = wm."IdWorker" and now() between coalesce(wm."DateBeg", '20010101') and coalesce(wm."DateEnd", '20700101')
	 left join comdoc."Department" dep on wm."IdDepartment" = dep."VCode"
     left join rp."RP_Post" post on wm."IdPost" = post."VCode"
	 LEFT JOIN LATERAL comdoc."getAccountingConstantValues"(w."COrg", 'СЭД_Уведомления_Сообщения_о_юбилярах', NULL) cv on true
where 
 	  now() between p."DateBirth" - (coalesce(cv."valueConst",30) || ' day')::interval + (date_part('year',age(p."DateBirth"))+1 || 'year')::interval and
 	                p."DateBirth" + (date_part('year',age(p."DateBirth"))+1 || 'year')::interval and
	  date_part('year',age(p."DateBirth" -  (coalesce(cv."valueConst",30) || ' day')::interval ))::int % 5 = 0
	 	) dd
         join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу' and rl."DocTypes" ilike '%NotificationLexema%'
         join comdoc."ReadListGroupUsers" rlU on rl."VCode" = rlU."PCode"
group by 	rlU."DocflowUser" 					
```

!!! Примечание
      В строке `join comdoc."ReadListGroup" rl on rl."Name" = 'Рассылка для менеджера по персоналу'` указывается наименование [группы рассылки](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Группы%20рассылки/)

![Юбилей](media/yubiley.png)

### Уведомление о перевыпуске сертификата в связи с изменением ФИО

```sql
with list_persons as
   ( select distinct case when coalesce(sert."LastName",'') <> coalesce(pers."Family",'') then 'фамилия, ' else '' end ||
       case when coalesce(sert."FirstName",'') <> coalesce(pers."Name",'') then 'имя, ' else '' end ||
	   case when coalesce(sert."MiddleName",'') <> coalesce(pers."Father",'') then 'отчество' else '' end as "Changed",
	   sert."FullName", 
	   coalesce(pers."Family",'') || ' ' || coalesce(pers."Name",'')|| ' ' ||coalesce(pers."Father",'') as "PersonFIO"
      
from comdoc."ECPCertificateApplication" sert
     join rp."RP_PersonContact" pc on sert."DocflowUser" = pc."Code" and pc."IdTypeContact" = 6
	 join rp."RP_Person" pers on pc."Pcode" = pers."VCode"
where now()::date between sert."BeginDate" and sert."EndDate" and
            (coalesce(sert."LastName",'') <> coalesce(pers."Family",'') or
      coalesce(sert."FirstName",'') <> coalesce(pers."Name",'') or
	  coalesce(sert."MiddleName",'') <> coalesce(pers."Father",'')))

insert into "#forInsNotification" ( "txt", "txtSMS", "txtTelegram")
select  null as "txt", null as "txtSMS", null as "txtTelegram"
from (select ('<table><tr><th align="left">Изменение</th><th align="left">ФИО в сертификате</th><th align="left">ФИО в Физ.лице</th></tr>' ||
(SELECT DISTINCT string_agg(x."link", '') 
     FROM ( SELECT '<tr><td>' || coalesce(l."Changed",'') || '</td><td>' || coalesce(l."FullName",'') || '</td>' || 
		   '<td>' || coalesce(l."PersonFIO", '') || '</td>'
		   ||'</tr>' as "link" 
		   		FROM list_persons l ) AS x) || '</table>' 
					) ::text as "data") d
```

![Уведомление](media/certs.png)

!!! note
	Для отображения в табличной части необходимо в настройке задаче заполнить табличную часть "Сопоставление данных":

 <table>
  <tr>
    <th>столбец</th>
    <th>описание</th>
    <th># для шаблона</th>
  </tr>
  <tr>
    <td>d."data"</td>
    <td>список</td>
    <td>#query_list#</td>
  </tr>
 </table>

 ![Таблица](media/table3.png)

### Уведомление HR о необходимости обработки заявления на увольнение

!!! note
	Уведомление по умолчанию направляется за три дня от текущей даты

```sql
insert into "#forInsNotification" ( "txt", "txtSMS", "txtTelegram", "DocflowUser")

select  null as "txt", null as "txtSMS", null as "txtTelegram", d."StageUser"
from dfd."SendingNotificationsHRAgreedUvol"() d
```

!!! note
	Для отображения в табличной части необходимо в настройке задаче заполнить табличную часть "Сопоставление данных":

таблица.столбец | описание | # для шаблона
----------------|----------|--------------
d."data" | Список | #query_list#
d."FirstName" | Имя | #query_Name#
d."MiddleName" | Отчество | #query_Father#

![Alt text](media/image.png)


<!-- ### Создание заявки на проверку контрагента при достижении суммы

```sql
call dfd."CreateCheckContractor"()
```--> 